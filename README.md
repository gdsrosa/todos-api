# TODOs API

[![Maintainability](https://api.codeclimate.com/v1/badges/1959979cca5a5c98bd26/maintainability)](https://codeclimate.com/github/gdsrosa/todos-api/maintainability)
[![Build Status](https://travis-ci.org/gdsrosa/todos-api.svg?branch=master)](https://travis-ci.org/gdsrosa/todos-api)


The goal of this repository is to show how to implement a simple RESTful using [Django](https://www.djangoproject.com/).


## Endpoints

Below you'll find a table with the current endpoints implemented:


Endpoint | Supported methods | Description
-------- | ----------------- | ------------ 
`/todos`   | GET             | Get list of ToDo items



## Contributing

### Getting started

* Fork this repository to your GitHub account by clicking the Fork button.
* [Clone](https://help.github.com/en/articles/fork-a-repo#step-2-create-a-local-clone-of-your-fork) the main repository locally:

```shell
$ git clone https://github.com/gdsrosa/todos-api
```
* Add your fork as a remote to push your work to. Replace {username} with your username. This names the remote "fork", the default remote is "origin".

```shell
$ git remote add fork https://github.com/<username>/todos-api
```

* Create a virtualenv.

```shell
$ python3 -m venv env/
```

* Install the development dependencies

```shell
$ pip install -r requirements.txt
```

### Start coding

Create a branch for what you would like to work on. Always branch off master to get the latest changes.

```
$ git fetch origin
$ git checkout -b your-branch-name origin/master
```

Using your favorite editor, make your changes, committing as you go.

Make sure to include tests that cover any code changes you make. Run the tests as described below.

Push your commits to your fork on GitHub and create a pull request.

```
$ git push --set-upstream fork your-branch-name
```


#### Running tests

```
$ python manage.py test todos
```

Happy coding!
