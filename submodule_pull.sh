#!/bin/sh
cd mtrack
for dir in `find . -maxdepth 1 -type d`
do
  (cd $dir && git pull)
done

