#!/bin/bash

while IFS= read -r repo 
do
echo "building $repo ..."
cd $repo
conan build . -pr release
cd ..
done < repos.txt
