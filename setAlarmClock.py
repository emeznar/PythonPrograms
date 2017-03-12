#ask user to input time in hours
current_time = int(input("What time is it now(hours only please)?"))
#ask user how many hours they want to wait for an alarm
alarm_set = int(input("When do you want to set an alarm(in hours)"))
#compute time with alarm hours added to it
wake_time = (current_time + alarm_set)%24
print ("Your alarm is set for " +str(wake_time) +" hundred hours")
