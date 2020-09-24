import time, getpass

def countDown(a):
    timeLeft = a
    while timeLeft > 0:
        print(timeLeft, end='\n')
        time.sleep(1)
        timeLeft = timeLeft - 1
    print('End')


a = int(getpass.getpass('Please enter a number'))
countDown(a)
