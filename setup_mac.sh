#!/usr/bin/env bash
# 1) ensure system deps are present
brew install pkg-config cairo ffmpeg

# 2) create & activate venv
python3 -m venv venv
source venv/bin/activate

# 3) upgrade pip & install Python deps
pip install --upgrade pip
pip install -r requirements.txt