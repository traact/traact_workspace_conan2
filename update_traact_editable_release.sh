#!/bin/bash
# This script loops through all files in a directory and prints the filename
# and the extracted part between {} if it matches the pattern: traact_{.*}-debug-x86_64-data.cmake

# Get the directory name as an argument or use the current directory
dir="./build/Release/generators"
cwd=$(pwd)
# Loop through all files in the directory
for file in "$dir"/*; do
# Get the filename without the path
filename="${file##*/}"
# Check if the filename matches the pattern using a regular expression
if [[ $filename =~ ^traact_(.*)-release-x86_64-data.cmake$ ]]; then
# Print the filename
echo "$filename"
# Extract the part between {} using parameter expansion
extracted="${filename#traact_}"
extracted="${extracted%-release-x86_64-data.cmake}"
# Print the extracted part
echo "$extracted"
search_line="set(traact_${extracted}_LIB_DIRS_RELEASE \"\${traact_${extracted}_PACKAGE_FOLDER_RELEASE}/build/Release/.\")"
replace_line="set(traact_${extracted}_LIB_DIRS_RELEASE \"${cwd}/build/Release/traact_${extracted}/.\")"
sed -i --expression "s@$search_line@$replace_line@" "$dir/$filename"


fi
done

sed -i --expression 's|\$script_folder/\.\./\.\./\.\./\([^/]*\)/build/Release/\.|$script_folder/../\1/.|g' "./build/Release/generators/conanrunenv-release-x86_64.sh"
sed -i --expression 's|\$script_folder/\.\./\.\./\.\./\([^/]*\)/build/Release|$script_folder/../\1|g' "./build/Release/generators/conanrunenv-release-x86_64.sh"
