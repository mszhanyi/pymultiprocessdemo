
from multiprocessing import Process, Queue

def f(q):
    q.put('hello world')

def run_mp():
    q = Queue()
    p = Process(target=f, args=[q])
    p.start()
    print (q.get())
    p.join()

if __name__ == "__main__":
    run_mp()
