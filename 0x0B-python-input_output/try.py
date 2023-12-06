#!/usr/bin/python3

n = 0
while n < 10:
    try:
        x = input()
        print ('Try using KeyboardInterrupt')
    except KeyboardInterrupt:
        print ('KeyboardInterrupt exception is caught')
        break
    #else:
    #    print ('No exceptions are caught')
    n += 1
