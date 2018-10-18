mpicc -lm /scratch/pi_mc.c -o /scratch/pi_mc
mpirun -np 2 --hostfile /scratch/machine_list /scratch/pi_mc 100000
mpirun -np 4 --hostfile /scratch/machine_list /scratch/pi_mc 100000
mpirun -np 6 --hostfile /scratch/machine_list /scratch/pi_mc 100000
mpirun -np 8 --hostfile /scratch/machine_list /scratch/pi_mc 100000
mpirun -np 10 --hostfile /scratch/machine_list /scratch/pi_mc 100000
mpirun -np 12 --hostfile /scratch/machine_list /scratch/pi_mc 100000
