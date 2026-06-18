#!/bin/bash
# SKILLS4VIBE Easy Install Script for Unix-like systems
# =====================================================
#
# This script simplifies installing SKILLS4VIBE skills for Mistral Vibe CLI.
#
# Usage:
#   ./install.sh                    - Install or update skills
#   ./install.sh --uninstall        - Remove installed skills
#   ./install.sh --no-symlinks      - Copy files instead of symlinking
#
# Requires: Python 3 and Git

python3 "$(dirname "$0")/install.py" "$@"
