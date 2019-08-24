"""
Python code to demonstrate communication
between parent and child process using
python.
"""


import os


def communication(child_writes):
    """
    :param child_writes: ...
    :return: ...
    """

    # file descriptors r, w for reading and writing
    read_fd, write_fd = os.pipe()
    print(f'fd: r: {read_fd}, w: {write_fd}')

    # Creating child process using fork
    process_id = os.fork()
    print(f'process_id: {process_id}')
    if process_id:
        # This is the parent process
        # Closes file descriptor w
        os.close(write_fd)
        read_fd = os.fdopen(read_fd)
        print("Parent reading")
        str_read = read_fd.read()
        print("Parent reads =", str_read)
    else:
        # This is the child process
        os.close(read_fd)
        write_fd = os.fdopen(write_fd, 'w')
        print("Child writing")
        write_fd.write(child_writes)
        print("Child writes = ", child_writes)
        write_fd.close()


if __name__ == "__main__":
    TEST = "Hello geeks"
    communication(TEST)
