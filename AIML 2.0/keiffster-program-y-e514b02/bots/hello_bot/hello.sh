#! /bin/sh

clear

export PYTHONPATH=../../src/

python3 aiml/form_weather.py
python3 ../../src/programy/clients/console.py --config ./config.yaml --cformat yaml --logging ./logging.yaml --debug

