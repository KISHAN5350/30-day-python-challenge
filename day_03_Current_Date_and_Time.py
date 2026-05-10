# Experiment 3: Current Date and Time
import time
t = time.localtime()
print(time.strftime("%a %d %H:%M:%S IST %Y", t))


#for 12 hour format
# import time
# t = time.localtime()
# print(time.strftime("%a %d %I:%M:%S %p IST %Y", t))