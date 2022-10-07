import calendar
import datetime

YEAR_CHOICES = [(y, y) for y in range(1950, datetime.date.today().year + 2)]
MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]
