#!/bin/bash

git fetch origin
git reset --hard master

make clean
make all
