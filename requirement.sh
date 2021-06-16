#!/bin/sh
cd
echo "Installing Dependence"
echo "upgrading pip"
pip install --upgrade pip
echo "Installing bs4"
pip install bs4
echo "Installing selenium"
pip install selenium
echo "Downloading chromiumdriver"
sudo apt-get install -y chromium-chromedriver
sudo chmod +777 /usr/lib/chromium-browser/chromedriver
echo "Installing mpv player"
sudo apt install mpv


