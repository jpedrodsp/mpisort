from mpi4py import MPI as mpi
import utils

def write_and_load_from_ndarray():
    myv = utils.generate_array(16)
    utils.write_ndarray("file.txt", myv)
    result, lv = utils.read_ndarray("file.txt")
    if result:
        print(lv)
    else:
        raise "Fail to read file"

def load_array_from_common_file():
    result, array = utils.get_array_from_file()
    if result:
        print(array)
    return result