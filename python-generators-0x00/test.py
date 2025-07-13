import datetime
from dateutil import tz

x = datetime.datetime.now(tz=tz.gettz("Africa/Dar_es_Salaam"))
y = x.tzname()
print(y)
print(x)


import pytz
# Get all timezone names
all_timezones = pytz.all_timezones
tanzania_timezones = [tz for tz in all_timezones if 'Tanzania' in tz or any(city in tz for city in ['Dar_es_Salaam', 'Dodoma'])]
print(tanzania_timezones)