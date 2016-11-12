# Zetkin.org Jekyll site
This repository contains the source for the zetkin.org website, built using
[Jekyll](http://jekyllrb.com).

Provided that you have docker installed, you can use the official Jekyll image
to build and run the site. Make sure that you are in the root folder of the
repository and run this command.

```
$ docker run --rm -v $PWD:/srv/jekyll -p 4000:4000 jekyll/jekyll
```

This will start serving the page from port 4000 on the host that Docker is
running on, usually localhost or whatever is returned by `docker-machine ip`.
