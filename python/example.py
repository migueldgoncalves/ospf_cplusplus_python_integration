def no_arguments():
    return "This function receives no arguments\n"

def string_example(input_string):
    return "This is the string supplied to Python: " + input_string + "\n"

def int_example(input_int):
    return input_int + 1

def bool_example(input_bool):
    return not input_bool

def bytes_example(input_bytes):
    return input_bytes + b'\x31\x32\x33\x34\x01\x02\x31'

def list_example(input_list):
    input_list.append("c")
    return input_list