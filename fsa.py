import serial

comport = "COMxx"
apogee = 850
#state 0 -> ground
# state 1 -> 0 to 30
# state 2 - > 30 to apogee
# state 3-> apogee = 850m
# rocket deployment, parachute deployment
# state 3-> apogee to 770m
# state 4 -> 770 to 500
# state 5 -> alt <500 
# deploy secondary parachute
# state 6 - > 450 to 10
# state 7 -> alt < 10 ; (landing) ; stop telemetry ; sound buzzer


# to check if state function has been called or not and avoid calling it twice
state2done = False 
state3done = False
state4done = False
state5done = False
state6done = False
state7done = False

def state0():
    pass
def state1():
    pass

def state2():
    pass
def state3():
    pass
def state4():
    pass
def state5():
    pass
def state6():
    pass
def state7():
    pass
def calibrate():
    alt_home = 0
def plot_state(state,movement):
    pass

movement = "ascend"
ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read
state = 0 

#calibration
calibrate()
state1()
state  = 1

while True:
    data = ser.readline().decode().strip()
    if not data:
        continue
    alt = data - alt_home

    if alt >0 and alt <30 and movement == "ascend":
        state = 1
        plot_state(state,movement)

    if alt == 30 and movement == "ascend" and state2done == False:
        state2()
        state = 2
        plot_state(state, movement)
        state2done = True

    if alt >30 and alt< apogee and movement == "ascend":
        state = 2 
        plot_state(state,movement)

    if alt == apogee and movement == "ascend" and state3done == False:
        state = 3
        state3()
        movement = "descend"
        plot_state(state,movement)
        state3done = True

    if alt > (apogee - 80) and movement == "descend":
        state = 3
        plot_state(state,movement)

    if alt == (apogee - 80) and state4done == False:
        state = 4
        state4()
        plot_state(state,movement)
        state4done = True
    
    if alt > 500 and alt < (apogee-80) and movement == "descend":
        state = 4
        plot_state(state,movement)

    if alt ==500 and movement == "descend" and state5done == False: 
        state = 5
        state5()
        plot_state(state,movement)
        state5done = True

    if alt > 450 and alt <500 and movement == "descend":
        state = 5
        plot_state(state,movement)

    if alt == 450 and movement == "descend" and state6done == False:
        state = 6
        state6()
        plot_state(state,movement)
        state6done = True

    if alt <450 and alt >10 and movement == "descend":
        state = 6
        plot_state(state,movement)

    if alt ==10 and movement == "descend" and state7done == False:
        state = 7 
        movement = "landing"
        state7()
        plot_state(state,movement)
        state7done == True

    if alt <10 and movement == "landing":
        state = 7
        plot_state(state,movement)

    if alt <0.5 and movement == "landing":
        movement = "landed"
        plot_state(state,movement)
        break



    


    


