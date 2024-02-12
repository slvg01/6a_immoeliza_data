# Collaborative Repository : Branching/Versioning management process

## A - set up your local and remote own feature branch : 
- get in your local working folder  : cd XXXXX
- clone the repo in your local working folder  : git clone https://github.com/slvg01/immo-eliza-scraping-Qbicle.git
- get into the repo : cd immo-eliza-scraping-Qbicle
- list the the branches (you should see, main , dev and sylvain)
- ensure you are in main (should be) if not get into the main git checkout main 
- create and go into your own feature branch :  git checkout -b maarten // git checkout -b mahak
- directly push your feature branch to the remote :  git push -u origin mahak  // git push -u origin maarten
- got to git hub you should see your feature branch and that it is uptodate with main all good. 

## B - daily working process 
### 1 - before ANY work locally : 
#### a - ALWAYS update your local feature branch with the dev branch (this is to prevent future potential conflict) : 
- get in your local dev branch : git checkout dev
- update your local dev branch : git pull (remote dev : this is optional)
- get into your feature branch git checkout maarten // git checkout mahak
- to be on the safe side  commit any change that you may have done on your feature branch (git add . and thet git commit -m 'safety commit') 
- merge the local "uptodate" dev branch with your local feature branch : git merge dev 
- push your updated local feature branch to the remote repo : git push (optional origin mahak (or maarten))
- note that on github get your your own remote feature branch will not show it is in sync with main but this is normal as you have just sync with dev and not main
			
	### b - ALWAYS ALWAYS  check that your are in your on feature branch (git branch) before working and if not go into it . you are ready to code

### 2 - when you want to commit some work, from your branch :  
- git add .  
- git commit -m "explanatory message of the commit content"
- git push remote mahak (or maarten)
- get in github and go to your own remote feature branch you should see that some commit are there waiting to be PR
- click on compare & pull request or on contribute and open pull request (same)
- IMPORTANT : at the top of the pull request change the base : main to base : dev  to allow the pull request to be done towards the dev branch and not in the main directly 
- make a more precise description of the change requested
- send your pull request and inform team in discord for review process (we will be notified by email anyway)

Nota Bene 1 : once the pull request towards the dev branch is validated (see below) then the dev branch will show as 1 commit ahead of the main and it will stay like this until we pull request from dev branch to the main one  

Nota Bene 2 : So will be your own remote feature branch on github 

Nota Bene 3 : for the review process : got into the PR, then go in commit, review and choose relevant action if approve then go back to thye discussion table to approve the merge, will work only if enough validation are there 

### 3 - once the code is tested in dev 
- then pull request can be made from the dev to the main on github (marteen)
- 2 validations needed by mahak and sylvain and then merge  the PR 
- once the pull request is validated and the main updated, then we should reproduce (B-1-a)  process to put our local branches (main, dev &  feature branch) in sync with main  as well as pushing this latest sync to the and remote branches (local feature branch , local dev )  to avoid future conflict
		

	


