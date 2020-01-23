<h1 align="center">
    Microblog
</h1>

<p align="center">
  <strong>A web app written using Flask:</strong><br>
</p>

## Contents
- [Installing Application](#installing-application)
- [Starting Application](#starting-application)
    - [Reindexing Models](#reindexing-models)
- [Unit Tests](#unit-tests)

## Installing Application
To ensure all the configuration is passed as an environment variables to the application, we will create a local 
`.env.dev` file which gets passed to the container as a env_file. Copying the content of `.dev.dev-sample` and make 
changes as required according to your local machine.
  
Once we've made the environment file, we need to install [docker](https://www.docker.com/) in your local machine to 
create containers which hosts the application and all the dependencies. Once docker is installed, go the project root 
directory and run:  

    docker-compose build
    
This command will download all dependencies and will install the application in docker container.


## Starting Application
Once we've installed the application using `docker-compose build`, we can easily start the application by:
    
    docker-compose up -d

This will start the application, database and elasticsearch in detached mode

### Reindexing Models
After the application is installed and running, we need to update the indexes for [searching](#-searching) to work. 
For this let's `reindex` all the models used for searching

Currently we support searching in 
- Posts

Since the application is running in a container we created, we first need to connect to the `microblog_flask_app` 
container which host our application. Ensure the application is running, go to the
project root directory and execute:
    
    docker exec -it microblog_flask_app bash
    
This connects to the `microblog_flask_app` container in interactive mode so that we can run/check the application. In 
order to reindex the POST, we'll use `flask shell` command from the container:
```shell script
$ flask shell
Python 3.8.0 (default, Nov 15 2019, 02:22:06)
[GCC 8.3.0] on linux
App: app [development]
Instance: /home/microblog/instance
>>> Post.reindex()
>>> 
```
    
## Unit Tests
The unit tests are written in the `tests.py` using python's unittest module and can by connecting to the container and 
executing:

    python tests.py