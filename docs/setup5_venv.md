# Task 5: Setting up a virtual environment for our class

When you installed Python on your computer (see setup2_python) you installed it globally on your computer. But, working in a global environment can be tricky because different versions of python packages may not play nicely together. To avoid any conflicts, developers usually create a virtual environment for each project and then install the packages they need in that virtual environment. When you then run a Python program within that environment, you know that it's running against only those specific packages. 

## Setting up a virtual environment in our be433-spring-2023 folder

We are going to create a virtual environment in VS Code for our class. We will install several python packages that will help us to test, debug and format our code in this virtual environment. 

### Step 1: Connect VS Code and Github

Before we set up your virtual environment in VS Code we need to connect VS Code and GitHub so we can create a virtual environment in your BE434/534 workspace (your be433-spring-2023 folder). 

* To connect VS Code and GitHub you will need to have your BE434-spring-2023 open in GitHib Desktop
* Click on "Open VS Code" from the main page of your Github Desktop. This will open VS Code and take you to the BE434-spring-2023 directory.

### Step 2: Create a virtual environment in the BE434-spring-2023 workspace (directory)

Next, we will create a virtual environment (venv) in VS Code to install all of the Python packages we will need for our class. 
venv allows you to manage separate package installations for different projects and is installed with Python 3 by default.

From within VS Code, you can create non-global environments, using virtual environments by opening the Command Palette (⇧⌘P), start typing "Python: Create Environment command" to search, and then select the command.

The command presents a list of environment types: Venv or Conda. Select Venv.
![venv](./images/1_venv_select_env_type.png "Selecting a venv type")

For a Mac, you will need to follow the folowing steps:

For a PC, you will need to follow the following steps:

* Jump over to VS code from the Github Desktop by clicking on "Open VS Code" from the main page of your Github Desktop.
* In VS Code, navigate to the 01_salutations directory and create a new file called "hello.py" in the directory called 01_salutations (hint, you can do this from the )
* Try to "commit" this new file from Github Desktop. 
* It is good practice to add a detailed "commit message" in the description box that details your changes. If this is the first time you are "committing" aka saving a file you might want to add a meaage like this "Initial commit hello.py. This program says hello to a name the user provides". Once you have "commited" you then have to "push" to send the code to your GitHub repository using the "push to origin" command at the top right. This all sounds complicated! But, fear not, we will do this over and over during the semester and you will quickly get the hang of it.