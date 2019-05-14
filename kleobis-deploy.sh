#!/bin/bash

git fetch origin
git reset --hard origin/master

make clean
make all -j 2
