#!/bin/sh
# Virutal Environment
python -m venv bible

. bible/bin/activate

pip install requests beautifulsoup4
pip freeze > requirements.txt
