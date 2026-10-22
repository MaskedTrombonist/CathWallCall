#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is not installed."
  exit 1
fi

if ! python3 -m venv .venv; then
  PY_VER="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
  echo "Failed to create virtual environment."
  echo "Install venv support package and retry:"
  echo "  sudo apt-get install -y python${PY_VER}-venv"
  exit 1
fi

source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Environment ready."
echo "Run: ./run_kiosk.sh"
