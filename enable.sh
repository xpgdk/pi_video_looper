#!/bin/sh

# Make sure script is NOT run as root.
if [ "$(id -u)" = "0" ]; then
  echo "Must NOT be run as root!"
  exit 1
fi

systemctl --user enable video-looper.service
