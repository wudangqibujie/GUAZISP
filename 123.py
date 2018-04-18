import time
a = time.time()
while True:
    if time.time() != a+10:
        print("run")
        time.sleep(1)
    else:
        print("hehe")
        a = time.time()


