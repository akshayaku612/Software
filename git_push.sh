#!/bin/sh

#Changes head of the local branch to the branch you want to track
#But pushes the commits to your original tracked remote branch

git_push () {
	echo "Enter Local branch name:"
	read local
        echo "Enter Remote target branch name:"
        read target
        target="origin/${target}"
	git branch -u "$target"
        git pull
        git push origin "$local"
        local="origin/${local}"
        git branch -u "$local"
}

git_push

