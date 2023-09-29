Scripts to create a workspace like environment in conan2 to edit multiple libraries simultaneously until conan2 supports it.
The idea is to create a meta project that includes all dependencies and projects to be able to use Clion with all projects.
All libraries are in conan editable mode to find the packages in their folders.
As the projects depend on each other using CMake find_library, conan tries to find the .so files in the local package folder.
But since all projects are part of the meta project, the .so files are build in the meta project build folder 
We have to edit the generated .cmake files to point to the meta project build folder as well as the conan run env file.


# Installation

```
git clone https://github.com/traact/traact_workspace_conan2.git my_workspace
cd my_workspace
```

## edit workspace
Add all traact repositories you want to edit to repos.txt

Add all dependencies to conanfile.py as this is the only conan file used

Add all libraries directories you want to edit to CMakeLists.txt

## create workspace

```
./cloneAll.sh
./edit_all_libraries.sh
./build_all.sh
mkdir build
cd build
conan install ..
```

Open folder in Clion and run CMake

```
./update_env.sh
./update_traact_edtiable.sh
```

Run CMake again