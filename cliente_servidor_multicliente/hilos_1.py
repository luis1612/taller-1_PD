import threading

def trabajo():
    print("Estoy trabajando")
    return

threads = list()

for i in range(3):
    t = threading.Thread(target=trabajo)
    threads.append(t)
    t.start()

print(threads)