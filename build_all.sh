#!/bin/bash

while IFS= read -r repo 
do
echo "building $repo ..."
cd $repo
mkdir build
cd build
conan build ..
cd ../..
done < repos.txt
