<h1 align="center">
    Microblog
</h1>

<p align="center">
  <strong>A web app written using Flask:</strong><br>
</p>

## Contents
- [Installing](#-installing)
- [Unit Tests](#-unit-tests)
- [Searching](#-searching)



## Installing
All the dependencies are listed in the requirements.txt file. The application is written in Python 3, in order to 
install the dependencies, execute:

    pip install -r requirements.txt
    
After the application is installed, we need to update the indexes for [searching](#-searching) to work, for this reindex 
the models which will be used for searching

Currently we support searching in 
- Posts

In order to reindex the POST, we'll use `flask shell` command from the project root directory:
```shell script
$ flask shell
Python 3.7.4 (default, Oct 22 2019, 11:44:14)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
App: app [development]
Instance: /Users/user/PythonWorkspace/microblog/instance
>>> Post.reindex()
>>> 
```
    
## Unit Tests
The unit tests are written in the `tests.py` using python's unittest module and can be run as:

    python tests.py
    
## Searching
The application uses `elasticsearch` for searching the posts. Ensure it is installed and running in order for it to 
work correctly.