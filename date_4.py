import datetime
x = datetime.datetime.now()
y = x - datetime.timedelta(days=10)
difference_in_seconds = (x - y).total_seconds()

print(difference_in_seconds)