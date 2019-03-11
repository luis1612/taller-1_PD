import threading

def trabajo(contador):
    print("Este es mi trabajo numero = ", contador)
    return

threads = list()

for i in range(3):
    t = threading.Thread(target=trabajo, args=(i,))
    threads.append(t)
    t.start()

print(threads)