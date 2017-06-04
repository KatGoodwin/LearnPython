#!/bin/bash

find . -type d -name py-html -exec rm -fr {} \;
find . -name "*.pyc" -exec rm -fr {} \;
