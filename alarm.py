import datetime
def alarm():
    #speak('Enter the time')
    time = input('Example:14:02:45\nTime : ')
    while True:
        time_ac=datetime.datetime.now()
        now=time_ac.strftime("%H:%M:%S")
        if now==time:
            #speak('Time to wake up, Sir!')
            from playsound import playsound
            print(int(time[3:5])+1)
            print(time_ac.minute)
            playsound('C:\\Users\\u1802\\Downloads\\alarm.wav')


alarm()