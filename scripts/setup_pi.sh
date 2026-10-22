#!/usr/bin/env bash
set -euo pipefail

# Raspberry Pi OS package setup for a Python kiosk app.
sudo apt-get update
sudo apt-get install -y \
  python3 \
  python3-venv \
  python3-pip \
  python3-tk \
  xserver-xorg \
  x11-xserver-utils \
  openbox \
  lightdm \
  unclutter

echo "Base Pi packages installed."
echo "Next: run scripts/setup_env.sh"
