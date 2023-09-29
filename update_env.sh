sed -i --expression 's|\$script_folder/\.\./\.\./\.\./\([^/]*\)/build/Debug/\.|$script_folder/../\1/.|g' "./build/Debug/generators/conanrunenv-debug-x86_64.sh"
sed -i --expression 's|\$script_folder/\.\./\.\./\.\./\([^/]*\)/build/Debug|$script_folder/../\1|g' "./build/Debug/generators/conanrunenv-debug-x86_64.sh"
