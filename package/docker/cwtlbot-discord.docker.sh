#!/bin/bash

cd /app
echo "$LOGIN_TOKEN" > config/token
echo "$USERNAME" > config/username
npm start
