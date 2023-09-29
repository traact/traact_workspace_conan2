@echo off
rem This script assumes that git is installed and available in the PATH
rem This script also assumes that the .txt file with the repositories is named repos.txt and is in the same folder as this script
rem This script will create a folder named cloned_repos and clone all the repositories from the .txt file into it

set CLONE_DIR=cloned_repos
mkdir %CLONE_DIR%

for /f "delims=" %%a in (repos.txt) do (
echo Cloning %%a ...
git clone %%a %CLONE_DIR%\%%~na
)

echo Done.