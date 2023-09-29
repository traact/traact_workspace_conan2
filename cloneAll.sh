#!/bin/bash

while IFS= read -r repo 
do
echo "clone $repo ..."
git clone "git@github.com:traact/${repo}.git"
cd ..
done < repos.txt
