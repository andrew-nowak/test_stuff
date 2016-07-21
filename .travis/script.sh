#!/bin/bash

if [ ! -e date.txt ]; then
date > ./dir/date.txt;
fi

cat ./dir/date.txt
