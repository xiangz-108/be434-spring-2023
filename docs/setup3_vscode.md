# Getting started with a Python Code Editor

Code editors are fantastic resources that make it easy to write and edit code on your laptop. As part of this class, we will be using the VS Code editor to write and edit our Python programs. 

## Downloading and installing the VS Code editor

Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. We will write and edit python code using the Visual Studio code editor. Follow the directions on the VS Code website to install the version of [VS Code](https://code.visualstudio.com/) that is appropriate for your laptop.

## Installing the Python extensions for VS Code

Once VS Code is installed you will also need to install an extension for Python. VS Code can be used for programming in many different programming languages, so we will need to tell VSCode that we want to use Python. You can learn more about extensions [here] (https://code.visualstudio.com/docs/introvideos/extend). Go the the VS Code menu, Select View -> Extensions, to pull up the "Extensions Market Place" on the left-hand panel. Search for and install "Python" by IntelliSense. This extension works alongside Python in Visual Studio Code to provide performant language support, linters, and debuggers for Python. You will learn about each of these in the days to come. They will be useful in formatting your code to make it beautiful, while also checking for mistakes and errors.

## Specifying the version of Python to use

As we discussed in setup2_python, there are many versions of python. For this class, we are going to use the same version of python to make troubleshooting easy, and ensure that you can easily use all of the Python modules that we will use in this class. Python modules are bits of code, written by other programmers, that we can use in our own programs (more on that to come!). But, before we can use these modules, we need to tell our laptop which version of python to use, and where to install the modules. We will also need tell VScode to use this same version.

### Step 1: Telling our laptop which version of Python to use.

First make sure you have Python installed (via the setup2_python document), and that it is installed where we think it is. To do this, we will need to open a terminal window in VSCode and use the following Unix commands to "list" the contents of the directory where Python should be installed. In VSCode, select "View" from the menu bar and "Terminal" to open a Unix terminal. You should see a prompt like this "(base) bhurwitz@bonnies-mbp ~ %" in the box at the bottom. To keep things simple, I will replace this prompt with "$" below, please copy paste everything after the "$" and hit return to execute these commands.  

```
$ ls /usr/local/bin
```
Do you see python3.11 and pip3.11 listed in this directory? Great! Glad they are there, if not return to the setup2_python doc.

Next, we will need to make sure that we are pointing your laptop to this version of python. To do this, you will need to ensure that this version of python is included in your `$PATH`. Watch this week's video on PATH to learn more about `$PATH` and why it is important for finding things! But, before we can update our `$PATH`, we need to find out which version of Unix our system is using. To do this we will type the following command in the terminal box in VSCode. 

```
$ echo $SHELL
```

If are using the `bash` shell, you will need to edit _~/.bashrc_. If are using the `zsh` shell, you can edit _~/.zshrc_. We will need to edit this file to point to the correct version of Python. You can do this quickly using the Unix program nano from the VSCode terminal. 

If you are using `bash` shell, you will edit the .bashrc file as shown below, if you are using the `zsh` shell edit the .zshrc file.

```
$ nano ~/.bashrc
```

Add these lines into the .bashrc file
```
alias python=/usr/local/bin/python3.11
alias python3=/usr/local/bin/python3.11
alias pip=/usr/local/bin/pip3.11
alias pip3=/usr/local/bin/pip3.11
```

And save the file by using "^X", and "Y" to save and "return" to exit.

To make these changes take effect you need to "source" the .bashrc file like so:
```
$ source ~/.bashrc
```

Let's check if it worked
```
$ which python
```
You should see "python: aliased to /usr/local/bin/python3.11"

### Step 2: Telling VS Code which version of Python to use

Next, we need to tell VS Code which version of Python you want to use. And of course, we want to use the one we just installed! To do this, you can go to View -> Command Palette. Then in the search box look for Python: Select Interpreter. Choose the most recent version of python that you just installed 3.11.1

Now you are all set to start writing Python code in VS Code!


## Authors

Bonnie Hurwitz <bhurwitz@arizona.edu> 

