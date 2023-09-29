#!/bin/bash

while IFS= read -r repo 
do
echo "removing editable $repo ..."
cd $repo
conan editable remove . 
cd ..
done < repos.txt
