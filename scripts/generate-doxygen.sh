#!/bin/bash

REPOSITORIES=("zathura" "girara" "jumanji")
CWD=`pwd`
REPOSITORY_PATH="`pwd`/repositories/"
echo $REPOSITORY_PATH

for repo in "${REPOSITORIES[@]}"; do
  path=$REPOSITORY_PATH$repo

  # Clone or pull latest changes from repository
  if [ ! -d $path ]; then
    git clone git@pwmt.org:$repo.git $path
    cd $path
  else
    cd $path
    git pull
  fi

  # Generate documentation
  make doc || continue

  # Copy documentation to website
  mkdir -p $CWD/_site/projects/$repo/doxygen
  cp -r $path/doc/html/* $CWD/_site/projects/$repo/doxygen
done
