#!/bin/bash
#SBASH -p RM
#SBASH -t 1:00:00
#SBASH -N 1
#SBASH --ntasks-per-node 28

#echo command to stdout
set -x

#where do I start?
echo $SLURM_SUBMIT_DIR

module load mpi/gcc_openmpi

cd $SCRATCH
cp ~/examples/mpi/mpiio_bigwrite.c .
mpicc mpiio_bigwrite.c

for i in {2..28..2}
do
  echo "With ${i} processes"
  time mpirun -np $i ./a.out
done
