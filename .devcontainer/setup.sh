#!/bin/bash

echo "Setting up environment python..."
dir="/workspaces/NoiseID/server"
echo "Workspace: $dir"
python3 -m venv $dir/.venv
$dir/.venv/bin/pip install --upgrade pip
$dir/.venv/bin/pip install -r $dir/requirements.txt
exit 0
