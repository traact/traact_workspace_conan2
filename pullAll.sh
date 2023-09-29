#! /bin/bash
find . -name .git -type d -execdir git pull -v ';'