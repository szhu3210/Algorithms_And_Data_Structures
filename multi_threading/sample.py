# Python code to demonstrate communication
# between parent and child process using
# python.

import os


def communication(child_writes):
    # file descriptors r, w for reading and writing
    r, w = os.pipe()
    print(f'fd: r: {r}, w: {w}')

    # Creating child process using fork
    process_id = os.fork()
    print(f'process_id: {process_id}')
    if process_id:
        # This is the parent process
        # Closes file descriptor w
        os.close(w)
        r = os.fdopen(r)
        print("Parent reading")
        str_read = r.read()
        print("Parent reads =", str_read)
    else:
        # This is the child process
        os.close(r)
        w = os.fdopen(w, 'w')
        print("Child writing")
        w.write(child_writes)
        print("Child writes = ", child_writes)
        w.close()

        # Driver code


test_str = "Hello geeks"
communication(test_str)
