#!/bin/sh

#Remote and local branch commits
REMOTE="$(git rev-parse --verify origin/feature/akamalpuram)"
LOCAL="$(git rev-parse --verify HEAD)"

#Checks if the latest commits are same
if [[ "$REMOTE" == "$LOCAL" ]]
then echo "Remote and Local branches are in sync"
else 
      git pull
      git status -uno
      echo
      echo "Remote and Local branches are now in sync"
fi
