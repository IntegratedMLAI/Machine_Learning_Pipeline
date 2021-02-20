# Managing Virtual Environments in Windows

## Prerequisites
IF you have not yet installed python, go to python.org and install the latest stable python version of your OS.

## Multiple Python Versions On Windows
1. You will find all your installed python versions in C:\Users\YourUserName\AppData\Local\Programs\Python
2. The way python versions appear on Thom's windows machine are show below ...

![Python Versions On Thom's Machine](Python_Versions.png)

## How To Install Virtual Environment Wrapper For A Specific Version Of Python
1. Each python install has it's own version of pip.
2. They are stored in C:\Users\YourUserName\AppData\Local\Programs\Python\Python3x\Scripts
3. In each python x version scripts directory, you will find pip3.x.exe
4. From a terminal window (I recommend installing ConEmu), run pip3.x install virtualenvwrapper-win
5. Once the pip install is done, you will see some new files in C:\Users\YourUserName\AppData\Local\Programs\Python\Python37\Scripts
    * rmvirtualenv.bat
    * virtualenv.exe
    * virtualenvwrapper.bat
    * vwenv.bat
    * whereis.bat
    * workon.bat

## Default Location Of Virtual Environments
1. If you have existing python virtual environments, they are likely here C:\Users\YourUserName\Envs
2. The image below shows the ones on my windows machine

![Thom's Virtual Environments](Windows_Python_VENVs.png)

## Activating Existing Virtual Environments
1. Let's open and command terminal and run ```$ workon command```

(workon_command.png)

$ workon

Pass a name to activate one of the following virtualenvs:
==============================================================================
py37std
py37web
py38std
sfb_env


$ workon py39std

    virtualenv "py39std" does not exist.
    Create it with "mkvirtualenv "

$ deactivate
