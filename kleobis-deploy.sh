#!/bin/bash

git fetch origin
git reset --hard master

source ksi-py3-venv/bin/activate
make clean
make all
