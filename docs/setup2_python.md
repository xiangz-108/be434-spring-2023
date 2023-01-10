# Task 2: Installing Python on your Computer

In this class, we will be teaching you Python programming from the ground up! The best way to learn Python is by practicing as often as you can. By installing python directly on your laptop, you can practice anywhere and anytime you like, with or without an internet connection.   

## Downloading and building Python from source (the quick overview)

Python might already be installed natively on your laptop (if you are a mac user) or can be installed using many applications (e.g. Anaconda, a package for data science and Bioinformatics). These applications may have different versions of Python. To simplify installation and make trouble shooting in the class easy, we will all be using the same version of Python and installing it from source on your laptop. The most recent stable version of Python is 3.11 from December 6, 2022. To get started, download the appropriate installer for your laptop (Mac or PC) from the [Python website](https://www.python.org/downloads/release/python-3111/). Then, follow the steps for the installation to your laptop.

## Detailed instructions by Operating System

### Install Python on Windows

Windows computers don't usually come with Python preinstalled. You can check by opening a command prompt and running:

```
python --version
```

If you do have it, great! But, we will want to make sure we are all using the same version of Python in this class (version 3.11.1) We can download the installable package from the [official website](https://www.python.org/downloads/release/python-3111/). On this page, you will download the executable installer for Python-3 64-bit architecture. Most computers today have a 64-bit architecture installations, so if in doubt, use that one unless you know your computer is running a 32-bit installation.

Once the executable installer has downloaded, you will need to run it and may need to enter the system password. This will install Python on your machine. Before clicking install now, make sure you click on the add Python 3.11.1 to Path box. The $PATH tells the operating system where to look for executables. This will make this verison of Python your default version. Great! You should have Python installed now.

Quick note that you can install Python through package managers like Chocolately, but for consistency we are installing right from the source!

### Installing Python on macOS

macOS ships with an older version of Python, and we need Python Version 3.11.1. Let's install it. We can download the installable package from the [official website](https://www.python.org/downloads/release/python-3111/). The website should automatically offer us a link to install Python 3 for macOS. Click on the executable installer and follow the steps to install it on your machine (which includes the license and entering your system password). Great, now we have a new and improved version of Python on our macOS. You can check the version by pulling up a terminal window (under the Utils folder in Applications) and running:

```
python3 --version
```

Quick note that you can install Python through package managers like Homebrew or anaconda, but for consistency we are installing right from the source!

### Installing on Linux

Chances are if you are running Linux, you already ahve Python installed. You can pull up a terminal window and check the version. If you need to update the version to 3.11.1, you'll need to use the package management system. The package management system depends on the distribution that you're using. It's called App on Debian Ubuntu and Linux Mint, yum on Red Hat or CentOS, and DNF on Fedora.

## Author

Bonnie Hurwitz <bhurwitz@arizona.edu>

