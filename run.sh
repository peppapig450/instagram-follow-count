#!/bin/bash
set -Eeuo pipefail

# get path of bash script
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# source virtual environment
source "${SCRIPT_DIR}/venv/bin/activate"

arg="$1"

function run() {
    python3.9 scraper.py "$arg"
}
typeset -fx run

declare -i oldfoll newfoll

oldfoll=$(run) \
&& sleep 70
newfoll=$(run)

echo "$((newfoll - oldfoll)) is the followers gained in one minute"
