# Subtrat five days from the current date
import datetime

today = datetime.date.today()
date = today - datetime.timedelta(days=5)
print(date)
