git pull
git add .
git status
printf "Enter the commit message: "
read -r commit_message
git commit -m "$commit_message"
git push
