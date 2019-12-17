#from random import random
from time import sleep
from gpiozero import LED


ledg = LED(16)
ledy = LED(20)
ledr = LED(21)
ledG = LED(17)
ledY = LED(27)
ledR = LED(22)

delay = 1.5
delay2 = 1.5

x=1

print('north/south')

def led1(x):

    if x==1:
        x=0
        ledr.on()
        ledR.on()
        print ("red")
        sleep(delay)
        ledR.off()
        return led2(x)
    elif x==0:
        x=1
        ledR.on()
        ledr.on()
        print("red")
        sleep(delay)
        ledr.off()
        return led4(x)




def led2(x):
    ledY.on()
    ledR.on()
    print("yellowRed")
    sleep(delay2)
    ledY.off()
    ledR.off()
    return led3(x)


def led3(x):
    print("green")
    ledG.on()
    sleep(delay)
    ledG.off()
    return led0(x)

def led0(x):
    print('yellow')
    ledY.on()
    sleep(delay2)
    ledY.off()
    return led1(x)

def led4(x):
    ledy.on()
    ledr.on()
    print("yellowred")
    sleep(delay2)
    ledy.off()
    ledr.off()
    return led5(x)

def led5(x):
    print("green")
    ledg.on()
    sleep(delay2)
    ledg.off()
    return led6(x)

def led6(x):
    print("yellow")
    ledy.on()
    sleep(delay2)
    ledy.off()
    return led1(x)




state=led1    # start position
while state: state=state(x)  # launch state machine
print ("Done with states")
