from github import Github

# using username and password
def app():
	repoName = input('Specify your repo, for example (testuser/reponame):')
	if repoName == "":
		print("Enter a username")
		app()

	g = Github()
	repo = g.get_repo(repoName)
	issues = repo.get_issues()
	csvOutput = ""
	for issue in issues:
		csvOutput += '"{}";"{}";\n'.format(issue.title, issue.body)

	f = open('output.csv', 'w')
	f.write(csvOutput)
	print("Done")
	
app()