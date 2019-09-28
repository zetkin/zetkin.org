#!/bin/sh

dir=`dirname $0`
fname=$dir/seed-`date +%Y%m%d_%H%M%S`.sql

echo "Generating seed $fname";
docker-compose exec -e PGPASSWORD=password db pg_dump -U django django > $fname

echo "Generating $dir/seed.sql.gz"
gzip -9 -c $fname > $dir/seed.sql.gz
