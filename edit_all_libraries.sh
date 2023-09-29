#!/bin/bash

while IFS= read -r repo 
do
echo "add editable $repo ..."
cd $repo
conan editable add . --user traact --channel latest
cd ..
done < repos.txt
