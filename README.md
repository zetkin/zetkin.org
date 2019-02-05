# Zetkin Foundation website (zetkin.org) using Django CMS

## Running the project
To run the project in development mode, simply use Docker Compose. You'll need
to install the [Docker Engine](https://www.docker.com/products/docker-engine)
and [Docker Compose](https://docs.docker.com/compose/) for your platform.

You also need to make sure that port 80 is not bound on your system, e.g. stop
any HTTP servers you may have running on that port (like Apache).

Once Docker and Docker Compose are installed, simply run:

```
docker-compose up --build
```

Add the `-d` flag if you want to return to your shell and not display any log
output while you're developing (not recommended).

### First run
The first time you start the project, you will need to create a database and a
superuser to log into Django. Without stopping the docker-compose process, e.g.
in a new shell, run this to create the database:

```
docker-compose exec www python3 manage.py migrate
```

Once the migrations have executed and all tables have been created in the
database, create a new superuser using the following command.

```
docker-compose exec www python3 manage.py createsuperuser
```

Follow the guide to create a user. This will only be used in your development
environment, so don't be too concerned with selecting a great password et c.

At this point, it should be possible to browse to
[http://localhost](http://localhost) and find the (empty) Django setup there.

## Repository structure

### Backend code
The `backend` directory contains code for the back-end portions of this website,
including application logic and templates. The directory is a Django project,
which means that it contains project configuration (in the `zf` folder) and an
application (`zf_plugins`). The entire Django project is run using Docker.

### Front-end code
The `frontend` directory contains source code for the front-end, including JS
and SASS. It contains configuration to build the code using gulp, which will
normally be run inside a Docker container

### Docker configuration
The `docker-compose.yml` file contains a configuration to run the entire project
using Docker Compose. It will run the following containers:

* `db` which is a Postgresql database used by Django
* `www` which is the Django project running the Django development server
* `builder` which is a utility container that listens for changes to the
  front-end source code and rebuilds it
