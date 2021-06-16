#!/bin/bash

print_usage() {
  echo "On first usage:"
  echo ""
  echo "$ sudo cwtlbot-discord --init"
  echo ""
  echo "Thereafter:"
  echo "- $ sudo cwtlbot-discord"
  echo "- $ cwtlbot-discord --version"
}

if [[ $# -ge 2 ]]; then
  print_usage
  exit 1
fi

if [[ $# -eq 0 ]]; then
  if [[ "$(whoami)" != root ]]; then
    echo "Fatal error: cwtlbot-discord must be run as root when no option is specified"
    exit 1
  fi
  cd $SNAP/lib/node_modules/cwtlbot-discord
  CONFIG_PATH=$SNAP_DATA/config npm start
  exit
fi

if [[ "$1" = --init ]]; then
  if [[ "$(whoami)" != root ]]; then
    echo "Fatal error: cwtlbot-discord must be run as root when the --init option is specified"
    exit 1
  fi
  mkdir -p $SNAP_DATA/config
  echo -n "Enter the login token for your Discord bot: "
  IFS= read -rs token
  echo "$token" > $SNAP_DATA/config/token
  chmod 600 $SNAP_DATA/config/token
  echo ""
  echo -n "Enter the username for your Discord bot: "
  IFS= read -r username
  echo "$username" > $SNAP_DATA/config/username
  exit
fi

if [[ "$1" = --version ]]; then
  echo "0.1.1"
  exit
fi

print_usage
exit 1
