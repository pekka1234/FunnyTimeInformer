import time
from tkinter import *
from datetime import datetime

# List of funny times
same_num = [[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5],[6,6,6],[7,7,7],[8,8,8],[9,9,9],[10,10,10],[11,11,11],[12,12,12],[13,13,13],[14,14,14],[15,15,15],[16,16,16],[17,17,17],[18,18,18],[19,19,19],[20,20,20],[21,21,21],[22,22,22],[23,23,23]]

# While loop that keeps the script going (becouse this script is supposed to always inform about funny time and not just once)
while True:
    # Getting current datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S").split(":")

    # Turning current datetime to seconds
    time_overall = 0
    for x in range(len(current_time)):
        time_overall += int(current_time[x]) * [3600,60,1][x]
    
    # Counting how many seconds till funny time (and displayedFun is for printing the result)
    funny_time = 0
    displayedFun = []
    for y in same_num:
        utime = y[0] * 3600 + y[1] * 60 + y[2]
        if utime > time_overall:
            funny_time = utime
            displayedFun = ':'.join([str(x) for x in y])
            break
    
    # Waiting
    waiting_time = funny_time - time_overall
    time.sleep(waiting_time)

    # Displaying funny time
    root = Tk()
    l = Label(root, text = displayedFun)
    l.config(font =("Courier", 14))
    l.pack()
    root.mainloop()



