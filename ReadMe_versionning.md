#collaborative repo management procedure 

##A - set up your local and remote own feature branch : 
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
#### a - ALWAYS update your local feature branch with the main branch (this is to prevent future potential conflict) : 
- get in your local main branch : git checkout main
- update your local main branch : git pull (remote main : this is optional)
- get into your feature branch git checkout maarten // git checkout mahak
- to be on the safe side  commit any change that you may have done on your feature branch (git add . and thet git commit -m 'safety commit') 
- merge the local "uptodate" main branch with your local feature branch : git merge main 
- push your updated local feature branch to the remote repo : git push origin mahak (or maarten)
- on github get in your your own remote feature branch that should now be on par with the main : "This branch is up to date with main"
			
	### b - ALWAYS ALWAYS  check that your are in your on feature branch (git branch) before working and if not go into it . you are ready to code

### 2 - when you want to commit some work, from your branch :  
- git add .  
- git commit -m "explanatory message of the commit content"
- git push remote mahak (or maarten)
- get in github and go to your own remote feature branch you should see : "This branch is 1 commit ahead of main"
- click on compare & pull request or on contribute and open pull request (same)
- make a bigger description of the change requested
- IMPORTANT : at the top of the pull request change the base : main to base : dev  to allow the pull request to be done towards the dev branch and not in the main directly 
- send your pull request.

Nota Bene 1 : once the pull request towards the dev branch is validated (see below) then the dev branch will show as 1 commit ahead of the main and it will stay like this until we pull request from dev branch to the main one  

Nota Bene 2 : So will be your own remote feature branch on github 

### 3 - once the PR code review is done and PR is validated (see question below)
- then pull request can be made from the dev to the main on github 
- once the pull request is validated and the main updated, then we should reproduce (B-1-a)  process to put our local branches (main, dev &  feature branch) and remote feature branch in full sync and avoid future conflict
- the person that will have validated the dev branch PR update is responsible to sync it (through git -  (process B-1-a))
		

## To Be Discussed :
### do we really need a dev environment (i think it is a great practice indeed)
### what control/protection do we put in place for the dev and for the main 
- 1 reviewer/validator , if review not satisfactory > reject the request + message
- loop validation on the dev : Sylvain pull request validated by Mahak, Mahak by Marteen, Maarteen by Sylvain ? Or all on maarteen but what about maarten PR then ? 
- who pull request from the dev to the main ? who validated and with what action on that validation exactly
- the person that validate a PR should warn the others so that they can do B-3-b on their local  own local branch (comment valid for dev and main branch) . i think there should be email but to be on the safe side

	


