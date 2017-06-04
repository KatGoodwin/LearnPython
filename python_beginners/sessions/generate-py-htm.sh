#!/bin/bash

# loop through all directories, running py2html on each .py file. Output to py-html directory

#set -x
curr=`pwd`

# "make clean"
for f in `find . -type d -name py-html -print`
do
    rm -Rf $f
    mkdir $f
done

# "make install"
for f in `find . -type f -name '*.py' -print`
do
    mkdir -p $curr/`dirname $f`/../py-html >/dev/null
    python $curr/../py2html/py2html.py -i $f -o $curr/`dirname $f`/../py-html/`basename $f .py`.htm
done
