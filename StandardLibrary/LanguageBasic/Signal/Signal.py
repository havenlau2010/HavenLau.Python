import signal
def myHandler(signum,frame):
    print('I received: ', signum)
    exit

def signal_fun_show():
    # register signal.SIGALRM's handler
    signal.signal(signal.SIGILL, myHandler)
    #signal(5)
    #while True:
        #print('not yet')

