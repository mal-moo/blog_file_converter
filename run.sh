#!/bin/bash

packages=(pydantic python-dotenv moviepy)

for package in "${packages[@]}"
do
    if pip show "${package[@]}" &> /dev/null
    then
        :
    else
        pip install "${package[@]}"
    fi
done

python src/main.py