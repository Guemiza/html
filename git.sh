#! /bin/bash 
Username=Guemiza
password =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 
git add .
git commit -m "update code source"
git branch 
GIT_ASKPASS="./git-askpass.sh" GIT_USERNAME="$Username" GIT_PASSWORD="$password" git push -u origin dockerfile
