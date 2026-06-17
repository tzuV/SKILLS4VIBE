#!/usr/bin/env python3
"""
Vibe Web UI - Display Mistral Vibe CLI conversations in a web browser
====================================================================

This skill provides a simple web interface that mirrors your current Vibe CLI
conversation in a browser window with better readability.

Just run the skill and it will:
1. Start a web server on localhost:5000
2. Automatically open your browser
3. Stream your current terminal conversation in real-time

Features:
- Live updates as you chat in the terminal
- Beautiful markdown rendering
- Dark/light theme toggle
- Session browser
- Responsive design
"""

import os
import sys
import json
import argparse
import threading
import time
import webbrowser
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Default configuration
DEFAULT_PORT = 5000
DEFAULT_HOST = "127.0.0.1"

# Paths
VIBE_DIR = os.path.expanduser("~/.vibe")
SESSIONS_DIR = os.path.join(VIBE_DIR, "logs", "session")


class VibeSession:
    """Represents a Vibe CLI conversation session"""
    
    def __init__(self, session_id, session_path):
        self.id = session_id
        self.path = session_path
        self.meta = self._load_meta()
        self.messages = self._load_messages()
    
    def _load_meta(self):
        """Load session metadata"""
        meta_path = os.path.join(self.path, "meta.json")
        if os.path.exists(meta_path):
            try:
                with open(meta_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass
        return {}
    
    def _load_messages(self):
        """Load all messages from messages.jsonl"""
        messages_path = os.path.join(self.path, "messages.jsonl")
        messages = []
        
        if os.path.exists(messages_path):
            try:
                with open(messages_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            try:
                                msg = json.loads(line)
                                messages.append(msg)
                            except json.JSONDecodeError:
                                pass
            except Exception:
                pass
        
        return messages
    
    def get_formatted_messages(self):
        """Get messages formatted for display"""
        formatted = []
        for msg in self.messages:
            formatted_msg = {
                'role': msg.get('role', 'unknown'),
                'content': msg.get('content', ''),
                'message_id': msg.get('message_id', ''),
                'timestamp': msg.get('timestamp', ''),
                'injected': msg.get('injected', False)
            }
            formatted.append(formatted_msg)
        return formatted


class SessionManager:
    """Manages Vibe CLI sessions"""
    
    def __init__(self):
        self.sessions = {}
        self.current_session_id = self._get_current_session()
    
    def _get_current_session(self):
        """Get the current active session ID"""
        last_session_path = os.path.join(SESSIONS_DIR, ".last_session")
        if os.path.exists(last_session_path):
            try:
                # Read the session ID from the last_session file
                for root, dirs, files in os.walk(last_session_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                session_id = f.read().strip()
                                if session_id:
                                    return session_id
                        except Exception:
                            pass
            except Exception:
                pass
        
        # Fallback: get the most recent session
        return self._get_most_recent_session()
    
    def _get_most_recent_session(self):
        """Get the most recently modified session"""
        if not os.path.exists(SESSIONS_DIR):
            return None
        
        sessions = []
        for item in os.listdir(SESSIONS_DIR):
            item_path = os.path.join(SESSIONS_DIR, item)
            if os.path.isdir(item_path) and not item.startswith('.'):
                sessions.append(item)
        
        if sessions:
            # Sort by modification time, newest first
            sessions.sort(key=lambda s: os.path.getmtime(os.path.join(SESSIONS_DIR, s)), reverse=True)
            return sessions[0]
        return None
    
    def list_sessions(self):
        """List all available sessions"""
        sessions = []
        if os.path.exists(SESSIONS_DIR):
            for item in os.listdir(SESSIONS_DIR):
                item_path = os.path.join(SESSIONS_DIR, item)
                if os.path.isdir(item_path) and not item.startswith('.'):
                    session = VibeSession(item, item_path)
                    sessions.append({
                        'id': item,
                        'meta': session.meta,
                        'message_count': len(session.messages),
                        'modified': os.path.getmtime(item_path)
                    })
        # Sort by modification time, newest first
        sessions.sort(key=lambda s: s['modified'], reverse=True)
        return sessions
    
    def get_session(self, session_id=None):
        """Get a specific session"""
        if session_id is None:
            session_id = self.current_session_id
        
        if session_id in self.sessions:
            return self.sessions[session_id]
        
        session_path = os.path.join(SESSIONS_DIR, session_id)
        if os.path.exists(session_path):
            session = VibeSession(session_id, session_path)
            self.sessions[session_id] = session
            return session
        
        return None


class VibeHandler(SimpleHTTPRequestHandler):
    """HTTP request handler for the web viewer"""
    
    # Class-level storage for session manager
    session_manager = None
    
    def log_message(self, format, *args):
        """Suppress default logging to keep terminal clean"""
        pass
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/' or self.path == '/index.html':
            self._serve_index()
        elif self.path.startswith('/api/'):
            self._handle_api()
        else:
            self.send_error(404)
    
    def _serve_index(self):
        """Serve the main HTML page"""
        # Get the absolute path to the template
        script_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(script_dir, '..', '..', 'templates', 'index.html')
        
        if os.path.exists(html_path):
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', len(content.encode('utf-8')))
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        else:
            # Fallback: serve a minimal HTML if template not found
            fallback_html = """
            <!DOCTYPE html>
            <html>
            <head><title>Vibe Web UI</title></head>
            <body>
                <h1>Vibe Web UI</h1>
                <p>Template not found. Please check the installation.</p>
            </body>
            </html>
            """
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', len(fallback_html.encode('utf-8')))
            self.end_headers()
            self.wfile.write(fallback_html.encode('utf-8'))
    
    def _handle_api(self):
        """Handle API requests"""
        if self.path == '/api/sessions':
            self._api_sessions()
        elif self.path == '/api/messages':
            self._api_messages()
        elif self.path.startswith('/api/session/'):
            self._api_session_messages()
        else:
            self.send_error(404)
    
    def _api_sessions(self):
        """Return list of all sessions"""
        sessions = self.session_manager.list_sessions()
        response = json.dumps({
            'sessions': sessions,
            'current_session': self.session_manager.current_session_id
        })
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(response.encode('utf-8')))
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
    
    def _api_messages(self):
        """Return messages from current session"""
        session = self.session_manager.get_session()
        if session:
            messages = session.get_formatted_messages()
            response = json.dumps({
                'session_id': session.id,
                'messages': messages
            })
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', len(response.encode('utf-8')))
            self.end_headers()
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_error(404, "Session not found")
    
    def _api_session_messages(self):
        """Return messages from a specific session"""
        # Extract session ID from path: /api/session/{session_id}
        parts = self.path.split('/')
        if len(parts) >= 4:
            session_id = parts[3]
            session = self.session_manager.get_session(session_id)
            if session:
                messages = session.get_formatted_messages()
                response = json.dumps({
                    'session_id': session.id,
                    'messages': messages
                })
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(response.encode('utf-8')))
                self.end_headers()
                self.wfile.write(response.encode('utf-8'))
            else:
                self.send_error(404, "Session not found")
        else:
            self.send_error(400, "Invalid request")


class FileWatchThread(threading.Thread):
    """Watches session files for changes and reloads data"""
    
    def __init__(self, session_manager):
        super().__init__()
        self.session_manager = session_manager
        self.running = True
        self.daemon = True
    
    def run(self):
        """Watch for file changes"""
        while self.running:
            # Check current session for updates
            if self.session_manager.current_session_id:
                session = self.session_manager.get_session()
                if session:
                    # Reload messages
                    session.messages = session._load_messages()
            time.sleep(0.5)  # Check every half second for responsiveness
    
    def stop(self):
        """Stop the watch thread"""
        self.running = False


def open_browser(port):
    """Open browser automatically"""
    url = f"http://localhost:{port}"
    try:
        # Try to open in default browser
        webbrowser.open(url)
        print(f"Opened: {url}")
    except Exception as e:
        print(f"Could not open browser: {e}")
        print(f"Please open: {url}")


def main():
    parser = argparse.ArgumentParser(
        description='Vibe Web UI - Stream CLI conversation in browser'
    )
    
    parser.add_argument(
        '--port', '-p',
        type=int,
        default=DEFAULT_PORT,
        help='Port to serve on (default: 5000)'
    )
    
    parser.add_argument(
        '--host', '-H',
        type=str,
        default=DEFAULT_HOST,
        help='Host to bind to (default: 127.0.0.1)'
    )
    
    parser.add_argument(
        '--session', '-s',
        type=str,
        default=None,
        help='Specific session ID to view'
    )
    
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List all sessions and exit'
    )
    
    parser.add_argument(
        '--no-browser',
        action='store_true',
        help='Do not open browser automatically'
    )
    
    args = parser.parse_args()
    
    # Initialize session manager
    session_manager = SessionManager()
    
    if args.list:
        # Just list sessions and exit
        sessions = session_manager.list_sessions()
        print(f"\nAvailable Sessions ({len(sessions)}):")
        print("=" * 60)
        for session in sessions:
            print(f"  {session['id']} ({session['message_count']} messages)")
        print("=" * 60)
        print(f"\nCurrent: {session_manager.current_session_id}\n")
        return
    
    # Override current session if specified
    if args.session:
        session_manager.current_session_id = args.session
    
    # Set up the handler
    VibeHandler.session_manager = session_manager
    
    # Start file watcher
    watcher = FileWatchThread(session_manager)
    watcher.start()
    
    # Get current session info
    current_session = session_manager.get_session()
    message_count = len(current_session.messages) if current_session else 0
    
    print(f"Starting Vibe Web UI on http://{args.host}:{args.port}")
    
    # Open browser if not disabled
    if not args.no_browser:
        # Small delay to ensure server is ready
        time.sleep(0.5)
        open_browser(args.port)
    
    try:
        # Start the server
        with HTTPServer((args.host, args.port), VibeHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping...")
        watcher.stop()
        watcher.join(timeout=2)
    except Exception as e:
        print(f"\nError: {e}")
        watcher.stop()
        sys.exit(1)


if __name__ == '__main__':
    main()
