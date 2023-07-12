#!/bin/bash

echo "What should your commit message be?"
read msg
echo "$msg"

git add .
git commit -m  "$msg"
git push
