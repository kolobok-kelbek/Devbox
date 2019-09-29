#!/usr/bin/env bash

mkdir -p ~/.devbox
cp main.py ~/.devbox/main.py
cp req.txt ~/.devbox/req.txt
chmod +x ~/.devbox/main.py
cd ~/.devbox && pip3 install -r req.txt
sudo ln -s ~/.devbox/main.py /usr/bin/dev