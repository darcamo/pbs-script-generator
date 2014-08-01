#!/bin/bash
#PBS -q projeto3
#PBS -l vmem=1000mb
#PBS -l walltime=24:00:00
#PBS -l nodes=1:ppn=8
#PBS -l x86_64=true
#PBS -j oe

### #PBS -N Indireto
### #PBS -l mem=1000mb

cd ~/find_codebooks/

~/sage-4.7.1-linux-64bit-ubuntu_10.04.1_lts-x86_64-Linux/sage apps/find_codebook.py -c {0}
