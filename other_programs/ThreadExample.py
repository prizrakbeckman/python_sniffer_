import time,threading

def takeANap(a,b):
    print('Waiting for a bit')
    time.sleep(5)
    print('Wake up!')
    print('result is '+str(a+b))

print('Start of the program')
a = int(input())
b = int(input())

print('starting thread')
threadObj = threading.Thread(target = takeANap(a,b))
print('starting step 2')
threadObj.start()
print('starting step 3')
print('End of the program')
