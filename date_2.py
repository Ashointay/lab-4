import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(today.strftime("%Y-%m-%d"))
print(yesterday.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))