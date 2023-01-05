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
![1venv](./images/1_venv_select_env_type.png "Selecting a venv type")

The the command presents a list of interpreters that can be used as a base Python for the new virtual environment. Select Python Version 3.11.1 that we just installed.
![2venv](./images/2_venv_select_python_version.png "Selecting a venv python version")


### Step 3: Install the Python packages we need for this class.

Once you have created your vitual environment, you can install Python packages in that environment. In Python, packages are how you obtain any number of useful code libraries. For example, in this class we will use several packages that will help us to test, debug and format code. These are all contained in the requirement.txt file in the docs directory in the Github repository.  

First we need to open a terminal window:
![3venv](./images/vscode_open_terminal.png "Opening a terminal in VS Code")

For a Mac, you will need to enter the following commands in the terminal:
'''
source .venv/bin/activate
python3 -m pip install pytest
python3 -m pip install pylint
python3 -m pip install flake8
python3 -m pip install yapf
python3 -m pip install black
python3 -m pip install mypy
python3 -m pip install pytest-flake8
python3 -m pip install pytest-mypy
python3 -m pip install pytest-pylint
'''

For a PC, you will need to enter the following commands:
'''
.venv\scripts\activate
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
python -m pip install pytest
python -m pip install pylint
python -m pip install flake8
python -m pip install yapf
python -m pip install black
python -m pip install mypy
python -m pip install pytest-flake8
python -m pip install pytest-mypy
python -m pip install pytest-pylint
'''