FROM ubuntu:trusty

RUN apt-get update && apt-get install -y --force-yes \
        libz-dev \
        build-essential \
        python-pygments \
        nodejs \
        ruby \
        ruby-dev

RUN gem install --no-rdoc --no-ri github-pages

VOLUME /page
WORKDIR /page
EXPOSE 4000
CMD ["jekyll", "serve"]
