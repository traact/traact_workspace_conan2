#!/bin/bash

while IFS= read -r repo 
do
echo "exporting $repo ..."
cd $repo
conan remove "$repo*" -c
conan export . --user traact --channel latest
cd ..
done < repos.txt
