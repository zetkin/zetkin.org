# Database developer utilities

## What are seeds?
Seeds are database dumps of setups which developers can use to avoid having to
first create a bunch of dummy data. There is a seed file stored in the git
repo, but you can create new ones yourself.

This is also useful if you want to back up data before making any schema
changes or running new migrations.

## Starting from dev seed
There is a development seed in this folder containing dummy data for
development. Before building and starting anything, copy it as `seed.sql.gz` to
use it as dummy data when starting.

```
$ cp db/dev.sql.gz db/seed.sql.gz
$ docker-compose up --build
```

If you had already started the system before doing this, see below for how to
reset from a seed by first deleting the existing data.

## Resetting from seed
To reset the database using a new seed, stop docker, remove the container and
data volume, and rebuild. When the data volume is empty, the initial launch of
the database container will load the data from seed.sql.gz.

```
$ docker-compose rm
...
$ docker volume rm zetkinorg_dbdata
...
$ docker-compose up --build
```

## Generate seed
To generate a new seed, run `mkseed.sh` in this folder, while the website is
running (having used `docker-compose up` to start it).

```
$ ./db/mkseed.sh
Generating seed ./db/seed-20190928_105307.sql
Generating ./db/seed.sql.gz
```

## Should seeds be commited to source control?
In general, no. The seed.sql.gz file should never be commited (and is ignored
by Git). But when significant changes have been made and it makes sense to add
new dummy data for developers, the dev.sql.gz file could be updated.
