import json
import numpy

ARRAY_FILENAME = "array.dat"
DEFAULT_ARRAY_SIZE = 51200

# Read common vector to file
def read_vector(filepath) -> list:
    file = open(filepath, "r")
    string = file.readline()
    file.close()
    vector = json.loads(string)
    return vector

# Write common vector to file
def write_vector(filepath, vector) -> bool:
    file = open(filepath, "w")
    string = json.dumps(vector)
    file.write(string)
    file.close()
    return True

# Read a Numpy array from file
def read_ndarray(filepath) -> (bool, numpy.ndarray):
    try:
        array = numpy.fromfile(filepath)
        return True, array
    except Exception as e:
        print(e)
        return False, None
        

# Write Numpy array to a file
def write_ndarray(filepath, vector: numpy.ndarray) -> bool:
    try: 
        vector.tofile(filepath, "", "%s")
    except Exception as e:
        print(e)
        return False
    return True

# Generate a random array with specified size
def generate_array(size) -> numpy.ndarray:
    array = numpy.random.rand(size)
    return array

# Guarantees that reads/generates a common readable array
def get_array_from_file() -> (bool, numpy.ndarray):
    result, array = read_ndarray(ARRAY_FILENAME)
    if result == True:
        return True, array
    else:
        array = generate_array(DEFAULT_ARRAY_SIZE)
        write_result = write_ndarray(ARRAY_FILENAME, array)
        if write_result == True:
            return True, array 
        return False, None
