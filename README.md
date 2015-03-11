# Zetkin.org Jekyll site
This repository containsis the source for the zetkin.org website, 
built using Jekyll.

The contained `Dockerfile` defines a [Docker](http://docker.com) image
which contains all prerequisites to build the source to a static
website, to preview the site as you're working on it. 

Provided that you have docker install, you just need to build the
image and then use it to run [Jekyll](http://jekyllrb.com). Make sure
that you are in the repository root folder and then run:

```
$ docker build -t gh-pages .
$ docker run --rm -p 4000:4000 -v $PWD:/page gh-pages
```

This will build the image, calling it gh-pages, and then run the 
default command of that image, which is `jekyll serve`, exposing the
default port to the host system. The current working directory on the
host is mounted on the container and used as the source folder.
