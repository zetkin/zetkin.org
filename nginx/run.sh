#!/bin/sh

set -e

exec 2>&1

echo "Generating nginx config files"
rm /etc/nginx/sites-enabled/*
for tpl in /etc/nginx/sites-templates/*.conf
do
    conf=`basename $tpl`
    envtpl < $tpl > /etc/nginx/sites-enabled/$conf
done

if [ -n "$ZETKIN_USE_TLS" ]
then
    echo "Requesting TLS certificate"
    letsencrypt certonly \
        --standalone \
        --keep-until-expiring \
        --expand \
        --non-interactive \
        --agree-tos \
        --email info@zetkin.org \
        --domain $ZETKIN_DOMAIN \
        --domain www.$ZETKIN_DOMAIN \
        --domain manual.$ZETKIN_DOMAIN
else
    echo "Not using TLS"
fi

if [ -n "$ZETKIN_HTPASSWD" ]
then
    echo "Setting up password protection"
    echo -n 'zf:' >> /etc/nginx/.htpasswd
    echo $ZETKIN_HTPASSWD | openssl passwd -stdin -noverify -apr1 >> /etc/nginx/.htpasswd
fi

echo "Booting nginx"
exec nginx
