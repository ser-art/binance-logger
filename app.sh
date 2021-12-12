#!/bin/sh

set -o errexit
set -o nounset
set -o pipefail

mkdir -p logs/

export $(grep -v '^#' config/.env | xargs)

python app.py
