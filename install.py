#!/usr/bin/env python3
"""
SKILLS4VIBE Easy Install Script
=============================

This script simplifies installing SKILLS4VIBE skills for Mistral Vibe CLI.
Instead of manually cloning, copying, and reloading, just run this script.

Usage:
    python install.py                    # Install or update skills
    python install.py --uninstall        # Remove installed skills
    python install.py --repo /path/to/repo  # Use a specific local repo
    python install.py --no-symlinks      # Copy files instead of symlinking

The script will:
1. Clone SKILLS4VIBE repo (or use existing one)
2. Create symlinks from repo to ~/.vibe/skills/ (default)
3. Tell you to reload Vibe

With symlinks (default):
    - Skills update automatically when you `git pull` in the repo
    - No duplication of files

Without symlinks (--no-symlinks):
    - Files are copied instead
    - Useful if symlinks don't work on your system
"""

import argparse
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path


REPO_URL = "https://github.com/tzuV/SKILLS4VIBE.git"
DEFAULT_REPO_DIR = os.path.join(os.path.expanduser("~"), "SKILLS4VIBE")


def get_vibe_home():
    """Get the Vibe configuration directory."""
    vibe_home = os.environ.get("VIBE_HOME")
    if vibe_home:
        return Path(vibe_home)
    
    if sys.platform == "win32":
        return Path(os.environ.get("USERPROFILE", "~")).expanduser() / ".vibe"
    else:
        return Path("~").expanduser() / ".vibe"


def get_skills_dir():
    """Get the Vibe skills directory."""
    return get_vibe_home() / "skills"


def repo_exists(repo_path):
    """Check if a git repo exists at the given path."""
    return (Path(repo_path) / ".git").exists()


def clone_or_update_repo(repo_path, repo_url):
    """Clone the repo or update if it already exists."""
    repo_path = Path(repo_path)
    
    if repo_exists(repo_path):
        print(f"  Repository already exists at {repo_path}")
        print("  Updating...")
        
        # Stash any local changes
        try:
            subprocess.run(["git", "stash"], cwd=repo_path, check=False, capture_output=True)
        except FileNotFoundError:
            pass
        
        # Pull latest changes
        result = subprocess.run(
            ["git", "pull", "origin", "main"],
            cwd=repo_path,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"  Warning: Git pull failed: {result.stderr.strip()}")
            # Try fetching first
            subprocess.run(["git", "fetch", "origin"], cwd=repo_path, check=False, capture_output=True)
            subprocess.run(["git", "reset", "--hard", "origin/main"], cwd=repo_path, check=False, capture_output=True)
        else:
            print(f"  Updated to latest version")
        
        # Pop stashed changes back
        try:
            subprocess.run(["git", "stash", "pop"], cwd=repo_path, check=False, capture_output=True)
        except FileNotFoundError:
            pass
    else:
        print(f"  Cloning repository to {repo_path}")
        result = subprocess.run(
            ["git", "clone", repo_url, str(repo_path)],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"  Error cloning repository: {result.stderr.strip()}")
            sys.exit(1)
        
        print(f"  Repository cloned successfully")
    
    return repo_path


def get_repo_skills_dir(repo_path):
    """Get the skills directory from the repo."""
    skills_dir = Path(repo_path) / ".vibe" / "skills"
    if not skills_dir.exists():
        print(f"  Error: Skills directory not found at {skills_dir}")
        sys.exit(1)
    return skills_dir


def create_symlink(src, dst):
    """Create a symlink, handling existing files."""
    dst = Path(dst)
    src = Path(src)
    
    # Remove existing file/directory if it exists
    if dst.exists():
        if dst.is_symlink():
            dst.unlink()
        else:
            print(f"  Warning: {dst} exists and is not a symlink. Skipping.")
            return False
    
    # Create parent directories if needed
    dst.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        dst.symlink_to(src, target_is_directory=True)
        return True
    except OSError as e:
        # On Windows, symlinks often require admin privileges
        if sys.platform == "win32" and "privilege" in str(e).lower():
            print(f"  Warning: Creating symlinks on Windows requires Administrator privileges.")
            print(f"  Try running this script as Administrator, or use --no-symlinks to copy files instead.")
        else:
            print(f"  Warning: Could not create symlink {dst} -> {src}: {e}")
        return False


def copy_directory(src, dst):
    """Copy a directory, handling existing files."""
    src = Path(src)
    dst = Path(dst)
    
    # Remove existing directory if it exists
    if dst.exists():
        shutil.rmtree(dst)
    
    # Create parent directories
    dst.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        shutil.copytree(src, dst, dirs_exist_ok=True)
        return True
    except Exception as e:
        print(f"  Warning: Could not copy {src} to {dst}: {e}")
        return False


def install_skills(repo_path, use_symlinks=True):
    """Install skills from repo to Vibe skills directory."""
    repo_skills_dir = get_repo_skills_dir(repo_path)
    target_skills_dir = get_skills_dir()
    
    print(f"\n  Installing skills to: {target_skills_dir}")
    
    if not repo_skills_dir.exists():
        print(f"  Error: Source skills directory not found: {repo_skills_dir}")
        sys.exit(1)
    
    # Get all skill directories
    skill_dirs = [d for d in repo_skills_dir.iterdir() if d.is_dir()]
    
    if not skill_dirs:
        print(f"  Warning: No skill directories found in {repo_skills_dir}")
        return
    
    installed_count = 0
    skipped_count = 0
    
    for skill_dir in skill_dirs:
        skill_name = skill_dir.name
        target_path = target_skills_dir / skill_name
        
        if use_symlinks:
            success = create_symlink(skill_dir, target_path)
        else:
            success = copy_directory(skill_dir, target_path)
        
        if success:
            print(f"  ✓ Installed: {skill_name}")
            installed_count += 1
        else:
            print(f"  ✗ Skipped: {skill_name}")
            skipped_count += 1
    
    print(f"\n  Installed {installed_count} skills")
    if skipped_count > 0:
        print(f"  Skipped {skipped_count} skills")


def uninstall_skills(repo_path):
    """Remove skills that came from this repo."""
    repo_skills_dir = get_repo_skills_dir(repo_path)
    target_skills_dir = get_skills_dir()
    
    print(f"\n  Uninstalling skills from: {target_skills_dir}")
    
    if not target_skills_dir.exists():
        print(f"  No skills directory found at {target_skills_dir}")
        return
    
    # Get skill names from repo
    repo_skill_names = {d.name for d in repo_skills_dir.iterdir() if d.is_dir()}
    
    uninstalled_count = 0
    
    for skill_name in repo_skill_names:
        target_path = target_skills_dir / skill_name
        
        if target_path.exists():
            # Check if it's a symlink pointing to our repo
            if target_path.is_symlink():
                target_path.unlink()
                print(f"  ✓ Removed symlink: {skill_name}")
                uninstalled_count += 1
            else:
                # It's a real directory, ask for confirmation
                print(f"  Found non-symlink directory: {skill_name}")
                print(f"  This might contain user modifications.")
                response = input(f"  Delete {skill_name}? [y/N]: ").strip().lower()
                if response == 'y':
                    shutil.rmtree(target_path)
                    print(f"  ✓ Removed directory: {skill_name}")
                    uninstalled_count += 1
                else:
                    print(f"  ✗ Skipped: {skill_name}")
    
    print(f"\n  Uninstalled {uninstalled_count} skills")


def main():
    parser = argparse.ArgumentParser(
        description="Install or update SKILLS4VIBE for Mistral Vibe CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "--repo",
        default=DEFAULT_REPO_DIR,
        help=f"Path to SKILLS4VIBE repository (default: {DEFAULT_REPO_DIR})"
    )
    
    parser.add_argument(
        "--no-symlinks",
        action="store_true",
        help="Copy files instead of creating symlinks"
    )
    
    parser.add_argument(
        "--uninstall",
        action="store_true",
        help="Remove installed skills"
    )
    
    parser.add_argument(
        "--repo-url",
        default=REPO_URL,
        help=f"Repository URL (default: {REPO_URL})"
    )
    
    args = parser.parse_args()
    
    # Check if git is available
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Error: Git is not installed or not in PATH")
        print("Please install Git first: https://git-scm.com/downloads")
        sys.exit(1)
    
    vibe_home = get_vibe_home()
    vibe_skills_dir = get_skills_dir()
    
    print(f"\nVibe configuration directory: {vibe_home}")
    print(f"Skills will be installed to: {vibe_skills_dir}")
    
    if args.uninstall:
        uninstall_skills(args.repo)
        print("\n✅ Uninstall complete!")
        print("\nTo use the changes, reload Vibe or start a new session.")
        return
    
    # Clone or update the repository
    repo_path = clone_or_update_repo(args.repo, args.repo_url)
    
    # Install skills
    use_symlinks = not args.no_symlinks
    install_skills(repo_path, use_symlinks=use_symlinks)
    
    print("\n✅ Installation complete!")
    
    if use_symlinks:
        print("\nSkills are symlinked from the repository.")
        print("To update skills in the future:")
        print(f"  1. cd {repo_path}")
        print("  2. git pull origin main")
        print("  3. (No need to re-run this script!)")
    else:
        print("\nSkills were copied to your Vibe directory.")
        print("To update, run this script again or manually copy new skills.")
    
    print("\nTo use the new skills:")
    print("  1. Restart Vibe or use /reload command")
    print("  2. Try: /caveman or /diagnosis or /plan")
    
    # Show which skills were installed
    repo_skills_dir = get_repo_skills_dir(repo_path)
    skill_dirs = [d.name for d in repo_skills_dir.iterdir() if d.is_dir()]
    print(f"\nAvailable skills: {', '.join(sorted(skill_dirs))}")


if __name__ == "__main__":
    main()
