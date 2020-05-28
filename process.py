
import multiprocessing
from log import __log, __init_log, States, Colors, __log_summary
from time import sleep

NUM_CPUS = 1
THREADS = []

def __init():
    global NUM_CPUS
    __init_log()

    __log(States.INFO, "num cpu: {}".format(multiprocessing.cpu_count()))
    NUM_CPUS = multiprocessing.cpu_count()

def __spawn_thread(name, target, args):
    global THREADS

    if (len(THREADS) > NUM_CPUS):
        __log(States.WARN, "spawning a thread but no more cpus available.")
    THREADS.append(multiprocessing.Process(target=target, args=(args), name=name))
    THREADS[len(THREADS)-1].start()
    __log(States.INFO, "spawned & started new thread '{}'".format(name))

def __join_threads():
    global THREADS

    for thread in THREADS:
        thread.join()
        __log(States.INFO, "joined '{}'".format(thread.name))


def f(a='helo'):
    sleep(3)
def b(a='kiwi'):
    sleep(6)

if __name__ == '__main__':
    __init()
    __spawn_thread('roland', f, ('helo',))
    __spawn_thread('martha', b, ('helo',))

    __join_threads()
    __log_summary()
