import threading
def cube(num):
print(num * num * num)
def square(num):
print(num * num)
# create the thread
t1 = threading.Thread(target=square, args=(5,))
t2 = threading.Thread(target=cube, args=(5,))
# start the thread t1
t1.start()
# start the thread t2
t2.start()
# wait until t1 is completed
t1.join()
# wait until t2 is completed
t2.join()
# both threads completed
print('Done!!')
25
125
Done!!