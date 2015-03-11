# Zetkin.org Jekyll site
This repository contains the source for the zetkin.org website, 
built using [Jekyll](http://jekyllrb.com).

The contained `Dockerfile` defines a [Docker](http://docker.com) image
which contains all prerequisites to build the source to a static
website, to preview the site as you're working on it. 

Provided that you have docker installed, you just need to build the
image and then use it to run jekyll. Make sure that you are in the
root folder of the repository and then run these two commands:

```
$ docker build -t gh-pages .
$ docker run --rm -p 4000:4000 -v $PWD:/page gh-pages
```

This will build the image, calling it `gh-pages`, and then run the 
default command of that image, which is `jekyll serve`, exposing the
default port to the host system. The current working directory on the
host is mounted on the container and used as the source folder.
