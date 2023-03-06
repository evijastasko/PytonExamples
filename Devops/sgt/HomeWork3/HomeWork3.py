# Subtrat five days from the current date
import datetime
from datetime import date
today = date.today()
date = today - datetime.timedelta(days=5)
print(date)
