#!/bin/bash

echo ">>> Make Python Virtual Env..."
python3 -m venv .venv
source .venv/bin/activate
echo ">>> Done 1/3"

echo ">>> Install Python Package..."
python_packages=(pydantic pydantic_settings python-dotenv moviepy)
echo ">>> Done 2/3"

for package in "${python_packages[@]}"
do
    if pip show "${package[@]}" &> /dev/null
    then
        :
    else
        pip install "${package[@]}"
    fi
done

echo ">>> Install Brew Package..."
brew_packages=(ffmpeg imagemagick)
for package in "${brew_packages[@]}"
do
    if brew list | grep "${package[@]}" &> /dev/null
    then
        :
    else
        brew install "${package[@]}"
    fi
done
echo ">>> Done 3/3"
