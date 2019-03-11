import threading
import time

def trabajo():
    print(threading.currentThread().getName(), "lanzado")
    time.sleep(2)
    print(threading.currentThread().getName(), "detenido")
    return

def servicio():
    print(threading.currentThread().getName(), "lanzado")
    print(threading.currentThread().getName(), "detenido")
    return

s = threading.Thread(target=servicio, name="servicio")
t = threading.Thread(target=trabajo, name="trabajo")
u = threading.Thread(target=trabajo)
s.start()
t.start()
u.start()
