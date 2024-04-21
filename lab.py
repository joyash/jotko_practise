"""num = (input("Enter the number or quit by pressing enter: "))
number = []
maxi = 0
mini = None
while num != "":
    number.append(int(num))
    num = (input("Enter the number or quit by pressing enter: "))


for element in number:
    if element > maxi:
        maxi = element
for bum in range(len(num)):
       if mini is None or num[bum] < mini:
           mini = num[bum]

print(maxi)
print(number)
print(mini)"""

from machine import Pin, Timer
import RPi.GPIO as GPIO
import time

button = Pin(7, Pin.IN, Pin.PULL_UP)
led = Pin(20, Pin.OUT)

OFF = 0
ONW = 1
ON = 2
OFFW = 3
current_state = OFF

button_state = button.value()
btn = False

def transition():
    global current_state
    if current_state == OFF:
        led.value(0)
        current_state = ONW
    elif current_state == ONW:
        led.value(1)
        current_state = ON
    elif current_state == ON:
        led.value(0)
        current_state = OFFW
    elif current_state == OFFW:
        led.value(1)
        current_state = OFF

def tick(timer):
    global button_state, btn
    if button.value() == 1 and not btn:
        btn = True
        transition()
    elif button.value() == 0 and btn:
        btn = False

timer = Timer(freq=20)
timer.init(period=50, mode=Timer.PERIODIC, callback=tick)

while True:
    pass



