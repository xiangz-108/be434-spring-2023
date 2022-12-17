# Setting Up a Development Environment

## Downloading and building Python from source

To get started, we need to install the most recent version of Python on your laptop. The most recent stable version of Python is 3.11 from December 6, 2022. You can download the appropriate installer for your laptop (Mac or PC) from the [Python website](https://www.python.org/downloads/release/python-3111/).


## Downloading and installing the VS Code editor

Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. We will write and edit python code using the Visual Studio code editor. Follow the directions on the VS Code website to install the version of [VS Code](https://code.visualstudio.com/) that is appropriate for your laptop.

Once VS Code is installed you will also need to install an extension for Python. You can learn more about extensions [here] (https://code.visualstudio.com/docs/introvideos/extend). Go the the VS Code menu, Select View -> Extensions, to pull up the "Extensions Market Place" on the left-hand panel. Search for and install "Python" by IntelliSense. This extension works alongside Python in Visual Studio Code to provide performant language support, linters, and debuggers for Python. You will learn about each of these in the days to come. They will be useful in formatting your code to make it beautiful, while also checking for mistakes and errors.

Next, we need to tell VS Code which version of Python you want to use. And of course, we want to use the one we just installed! To do this, you can go to View -> Command Palette. Then in the search box look for Python: Select Interpreter. Choose the most recent version of python that you just installed 3.11.1

Now you are all set to start writing Python code in VS Code!

But, how do you get started? Fear not! We have created a Github repository with all of the assignments for the class that you will need to complete with input files and instructions for each, and a test that shows you if you have completed the coding assignment correctly. Also, we included a script to get you started with writing scripts called new.py. All of these goodies are in Github. So, now you just need to make a copy of that repository in your own Github account. Check out how to do that below...  

## GitHub

The following will help you create a GitHub account and copy the course repository into your own account.
This will allow you to have your own copy of the assignments, a place to write programs, and a repository in Github that you can submit your assignments to.  

First, create your free [GitHub](http://github.com) account 

* Go to [GitHub](http://github.com)
* Create a (free) user account

Next, go to the [course repository](https://github.com/bhurwitz33/be434-spring-2023) and click the "Fork" button so as to make a copy of the code into your own Github account. 

* Go to [the course repo](https://github.com/bhurwitz33/be434-spring-2023)
* Click the "Fork" button (upper-right)

This will create a new repository in your Github account. All your assignments will be pushed to GitHub where I will pull the code to my machine for checking. Add my GitHub username "bhurwitz33" as a Collaborator on your repo so that I can push and pull code, and then email me your GitHub username and the URL for your repo (bhurwitz@arizona.edu). At the end of the semester, you will have a public repository of code you can share to show proficiency in Python coding and testing. 

* Go to the "Settings" for your repo called "be434-spring-2023"
* Choose "Manage Access" from the left panel
* Click the green "Invite a collaborator" button
* Add "bhurwitz33" and send

Next, you will need to create a copy of this repository on your laptop so you can work on python code locally, and then turn it in by pushing the code back to Github (more on this next). I recommend using [the Github Desktop](https://desktop.github.com/)

* Download [the Github Desktop](https://desktop.github.com/) for your laptop
* From the top menu bar, select Github Desktop, then select Preferences, go to Accounts, and login to Github
* From the top menu bar, select Github Desktop, then select Preferences, go to Integrations, select Visual Studio Code as the "External Editor"
* Be sure to "save" your Preferences

With that, you now should be able _clone_ or copy down the contents of the repo onto your local machine (e.g., your laptop). 

* Using GitHub desktop, Go to File in the top menu, and select "Clone Repository"
* Use the "Filter your repositories" box to find "be434-spring-2023" in your GitHub Account
* Select the "be434-spring-2023" and click the "Clone" button to copy the repository to your local directory

Once you have downloaded the repository, and set up your preferences for VS code, you can now edit your python code in VS code. To jump over to VS code from the Github Desktop you can click on "Open VS Code" from the main page of your Github Desktop. 

And you can pop back to Github Desktop after you made any changes to "commit" the code, and push to your GitHob repository. Github tracks all of your changes, and it is good practice to add a detailed "commit message" in the description box that details your changes. If this is the first time you are "committing" aka saving a file you might want to add a meaage like this "Initial commit hello.py. This program says hello to a name the user provides". Once you have "commited" you then have to "push" to send the code to your GitHub repository using the "push to origin" command at the top right. This all sounds   

## Authors

Bonnie Hurwitz <bhurwitz@arizona.edu> and Ken Youens-Clark <kyclark@gmail.com>

