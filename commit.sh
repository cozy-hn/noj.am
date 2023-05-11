git add .
printf "Enter the commit message: "
read -r commit_message
git commit -m "$commit_message"
git push