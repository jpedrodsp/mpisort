import utils
import tests
import numpy
from datetime import datetime
from mpi4py import MPI as mpi

TAG_DATARETURN = 1

def sort_method(array: numpy.ndarray) -> numpy.ndarray:
    a = numpy.sort(array)
    return a

if __name__ == "__main__":
    comm = mpi.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    status = mpi.Status()

    if rank == 0:
        result, array = utils.get_array_from_file()
        if result == False:
            raise "Failed to read array"
        if result:
            starttime = datetime.now()
            #print(array)
            pass
        node_array_size = int(array.size / (size - 1))
        print("For each node, get a array of size: %d" % node_array_size)
        for i in range(1, size):
            part = array[(i-1) * node_array_size : i * node_array_size]
            # print("Sending part to {}: {}".format(i, part))
            comm.send(part, i, 0)
        datareturns = 0
        sorted_array: numpy.ndarray = numpy.zeros(0)
        while datareturns < size - 1:
            data: numpy.ndarray = comm.recv(tag=TAG_DATARETURN, source=mpi.ANY_SOURCE, status=status)
            if status.Get_source():
                source = status.Get_source()
                # print("slave", source, data)
                sorted_array = numpy.append(sorted_array, data)
                datareturns += 1
        
        last_sort = sort_method(sorted_array)
        finaltime = datetime.now()

        elapsed = finaltime - starttime
        print(elapsed.microseconds, "ms")
        

    elif rank > 0:
        data = comm.recv(source=0)
        sorted = sort_method(data)
        # print("slave", rank, data)
        comm.send(data, 0, TAG_DATARETURN)
        
    else:
        raise "Ïnvalid MPI rank obtained"