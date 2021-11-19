from ExObject.ExStock import is_trading_day,get_last_trading_day,get_next_trading_day
from ExObject.DateTime import DateTime
print(is_trading_day(DateTime.Now()))
print(get_last_trading_day(DateTime.Now()))
print(get_next_trading_day(DateTime.Now()))