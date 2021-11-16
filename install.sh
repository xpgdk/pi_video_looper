#!/bin/sh

# Error out if anything fails.
set -e

# Make sure script is NOT run as root.
if [ "$(id -u)" = "0" ]; then
  echo "Must NOT be run as root with sudo!"
  exit 1
fi


echo "Installing dependencies..."
echo "=========================="
sudo apt update && sudo apt -y install python3 python3-vlc python3-pip python3-pygame supervisor omxplayer ntfs-3g exfat-fuse

echo "Installing video_looper program..."
echo "=================================="

# change the directoy to the script location
cd "$(dirname "$0")"

#pip3 install setuptools
sudo python3 setup.py install --force

sudo cp ./assets/video_looper.ini /boot/video_looper.ini

echo "Configuring video_looper to run on start..."
echo "==========================================="

mkdir -p $HOME/.config/systemd
cp assets/video-looper.service $HOME/.config/systemd

echo "Finished!"
