#!/bin/bash

REPOSITORIES=("zathura" "girara" "jumanji")
CWD=`pwd`
REPOSITORY_PATH="`pwd`/repositories/"
BRANCH="develop"

for repo in "${REPOSITORIES[@]}"; do
  path=$REPOSITORY_PATH$repo

  # Clone or pull latest changes from repository
  if [ ! -d $path ]; then
    git clone git://pwmt.org/$repo.git $path
    cd $path && git checkout --track -b $BRANCH origin/$BRANCH
  else
    cd $path && git pull origin
  fi

  # Generate documentation
  make doc || continue

  # Copy documentation to website
  mkdir -p $CWD/projects/$repo/doxygen
  cp -r $path/doc/html/* $CWD/projects/$repo/doxygen
done
