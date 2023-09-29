#!/bin/bash

while IFS= read -r repo 
do
echo "delete build folder $repo ..."
cd $repo
rm -rf ./build
cd ..
done < repos.txt
