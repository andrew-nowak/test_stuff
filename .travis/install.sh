#!/bin/bash

#wget http://sourceforge.net/projects/samtools/files/samtools/0.1.19/samtools-0.1.19.tar.bz2/download -O samtools-0.1.19.tar.bz2
#tar jxf samtools-0.1.19.tar.bz2
#pushd samtools-0.1.19
#make
#popd

#ls -al
#echo "!! samtools 0.1.19 :"
#ls -al samtools*/*

git clone --branch v0.7.15 --depth 1 https://github.com/lh3/bwa.git bwa

pushd bwa
make
echo "!! bwa :"
ls -al
popd

#git clone --branch v1.0.1-dkj-fopen_with_MM --depth 1 https://github.com/dkj/bowtie.git bowtie
#pushd bowtie
#make
#echo "!! Bowtie :"
#ls -al
#popd

#git clone --branch v2.2.7 --depth 1 https://github.com/BenLangmead/bowtie2.git bowtie2
#pushd bowtie2
#make
#echo "!! Bowtie2 :"
#ls -al
#popd
