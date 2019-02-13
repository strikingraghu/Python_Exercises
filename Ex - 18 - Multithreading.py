"""
    Running several threads is similar to running several different programs concurrently, by providing below benefits -

        Multiple threads within a process share the same data space with the main thread and
        can therefore share information or communicate with each other more easily than if they were separate processes.

        Threads sometimes called light-weight processes and they do not require much memory overhead.
        They are cheaper than processes.

        A thread has a beginning, an execution sequence, and a conclusion.
        It has an instruction pointer that keeps track of where within its context it is currently running.

        It can be pre-empted (interrupted). It can temporarily be put on hold (also known as sleeping) while other
        threads are running - this is called yielding.


        The threading module provided with Python includes a simple-to-implement locking mechanism that allows you to
        synchronize threads. A new lock is created by calling the Lock() method, which returns the new lock.
        The acquire(blocking) method of the new lock object is used to force threads to run synchronously.
        The optional blocking parameter enables you to control whether the thread waits to acquire the lock.
        If blocking is set to 0, the thread returns immediately with a 0 value if the lock cannot be acquired
        and with a 1 if the lock was acquired. If blocking is set to 1, the thread blocks and wait for
        the lock to be released. The release() method of the new lock object is used to release the lock when
        it is no longer required.
"""
# Generic Syntax
# thread.start_new_thread ( function, args[, kwargs] )

import threading
import os

# Example 1


def cube_calculation(cube_number):
    print("You have passed {} number for calculating cube root & it's value is {}!"
          .format(cube_number, cube_number * cube_number * cube_number))


def square_calculation(square_number):
    print("You have passed {} number for calculating square root & it's value is {}!"
          .format(square_number, square_number * square_number * square_number))

if __name__ == "__main__":
    thread_1 = threading.Thread(target=cube_calculation, args=(3,))
    thread_2 = threading.Thread(target=square_calculation, args=(2,))

    # Starting threads in this stage
    thread_1.start()
    thread_2.start()

    # Joining both the threads for completion
    thread_1.join()
    thread_2.join()
    print("Displaying thread information")
    print(thread_1.getName(), thread_1.isAlive, thread_1.__class__)
    print(thread_2.getName(), thread_2.isAlive, thread_2.__class__)
    print("All steps are completed")
else:
    print("Issues within example # 1 code!")

print("--------------------------")

# Example 2


def first_task():
    print("first_task assigned to the thread {}".format(threading.current_thread().name))
    print("ID of first_task running process {}".format(os.getpid()))


def second_task():
    print("second_task assigned to the thread {}".format(threading.current_thread().name))
    print("ID of second_task running process {}".format(os.getpid()))

if __name__ == '__main__':
    print("Main program PID value is {}".format(os.getpid()))
    print("Main thread name is {}".format(threading.main_thread().name))

    # Creating 2 threads
    thread_01 = threading.Thread(target=first_task, name='FIRST TASK')
    thread_02 = threading.Thread(target=second_task, name='SECOND TASK')

    # Starting 2 threads
    thread_01.start()
    thread_02.start()

    # Joining 2 threads
    thread_01.join()
    thread_02.join()
else:
    print("Issues within example # 2 code!")

print("--------------------------")

# Example 3

x_value = 0


def increment():
    global x_value
    x_value += 1


def thread_task(lock):
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()


def main_task():
    global x_value
    x_value = 0

    # Creating a lock
    lock = threading.Lock()

    # Creating 2 threads
    thread_sync_01 = threading.Thread(target=thread_task, args=(lock,))
    thread_sync_02 = threading.Thread(target=thread_task, args=(lock,))

    # Starting threads
    thread_sync_01.start()
    thread_sync_02.start()

    # Joining 2 threads
    thread_sync_01.join()
    thread_sync_02.join()

if __name__ == '__main__':
    for iterator in range(10):
        main_task()
        print("Iteration {0} & X_Value = {1}".format(iterator, x_value))
