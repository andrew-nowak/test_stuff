#!/bin/bash

wget http://sourceforge.net/projects/samtools/files/samtools/0.1.19/samtools-0.1.19.tar.bz2/download -O samtools-0.1.19.tar.bz2
tar jxf samtools-0.1.19.tar.bz2
pushd samtools-0.1.19
make
popd

ls -al
ls -al samtools*/*

git clone --branch 0.5.10-mt_fixes.2 --depth 1 https://github.com/wtsi-npg/bwa.git bwa

pushd bwa
make
ls -al
popd

