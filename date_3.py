import datetime
time_now = datetime.datetime.now()
drop_microseconds = time_now.replace(microsecond=0)

print(drop_microseconds)
