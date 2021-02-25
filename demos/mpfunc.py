from multiprocessing import Process, Queue
import torch
import sys
import os

def get_subproc_info(i):
    print(sys.modules["__main__"].__dict__)
    return os.getpid()
    
def f1(x):
    return x*x

def worker_init_fn(id):
    print(sys.modules["__main__"].__dict__)