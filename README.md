# Requirements

```bash
sudo apt install openmpi-bin
sudo apt install python3 python3-pip
pip3 install numpy mpi4py
```

# Execution

First configure your MPI cluster `hostfile` file. You need more than one machine, at least.
Copy the source files to the same folder on each machine.
Then, execute the MPI code.

```bash
mpiexec --hostfile <hostfile> -np <machines_number> python3 <path/to/mpi_sort.py>
```