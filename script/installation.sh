#!/usr/bin/env bash

sudo apt update -y

sudo apt install python3 -y

sudo apt install python3-pip -y

sudo apt install python3-venv -y

python3 -m venv venv

pwd 

ls

pip3 install -r requirements.txt

source ~/.bashrc

source /var/lib/jenkins/workspace/example_freestyle/venv/bin/activate

python3 /var/lib/jenkins/workspace/example_freestyle/app.py


