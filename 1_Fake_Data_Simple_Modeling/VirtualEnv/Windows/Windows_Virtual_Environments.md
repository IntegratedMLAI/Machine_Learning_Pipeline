# Managing Virtual Environments in Windows

## Prerequisites
IF you have not yet installed python, go to python.org and install the latest stable python version of your OS.

## Multiple Python Versions on Windows
You will find all your installed python versions in C:\Users\YourUserName\AppData\Local\Programs\Python
![Python Versions On Thom's Machine](Python_Versions.png)

C:\Users\YourUserName\AppData\Local\Programs\Python\Python3x\Scripts
pip3.x.exe

pip3.x install virtualenvwrapper-win

C:\Users\YourUserName\AppData\Local\Programs\Python\Python37\Scripts
rmvirtualenv.bat
virtualenv.exe
virtualenvwrapper.bat
vwenv.bat
whereis.bat
workon.bat

C:\Users\YourUserName\Envs
See Windows_Python_VENVs.png

$ workon command
See workon_command.png

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
