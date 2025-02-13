import datetime
time_now = datetime.datetime.now()
minus_5 = time_now - datetime.timedelta(days=5)

print(time_now.strftime("%Y-%m-%d"))
print(minus_5.strftime("%Y-%m-%d"))