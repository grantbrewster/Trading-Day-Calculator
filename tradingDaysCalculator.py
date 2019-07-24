import datetime
import pandas as pd
from pandas.tseries.offsets import BDay
from pandas.tseries.holiday import AbstractHolidayCalendar,Holiday, USMemorialDay,  USMartinLutherKingJr, USPresidentsDay, GoodFriday, \
    USLaborDay, USThanksgivingDay, nearest_workday
from pandas.tseries.offsets import CDay

class NYSECalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('New Years Day', month=1, day=1, observance=nearest_workday),
        USMartinLutherKingJr,
        USPresidentsDay,
        GoodFriday,
        USMemorialDay,
        Holiday('USIndependenceDay', month=7, day=4, observance=nearest_workday),
        USLaborDay,
        USThanksgivingDay,
        Holiday('ColumbusDay', month=10, day=14, observance=nearest_workday),
        Holiday('VeteransDay', month=11, day=11, observance=nearest_workday),
        Holiday('Christmas', month=12, day=25, observance=nearest_workday),
        ]

# # method to get the number of trading days for the current month
def numOfTradingDaysTotal():
    now = datetime.datetime.now()
    start = datetime.datetime(year=now.year, month=now.month, day=1)
    end = start + pd.offsets.MonthEnd(1)
    # Creating a custom calendar
    cal = NYSECalendar()
    # Getting the holidays (off-days) between two dates
    cal.holidays(start=start, end=end)
    se = pd.bdate_range(start=start, 
                    end=end,
                    freq=CDay(calendar=cal)).to_series()
    # Counting the number of working days by month
    num = se.count()
    print(num)
    return num

# method to get the ith trading day we are in right now
def numberOfDay():
    now = datetime.datetime.now()
    start = datetime.datetime(year=now.year, month=now.month, day=1)
    end = start + pd.offsets.Day(now.day)
    # Creating a custom calendar
    cal = NYSECalendar()
    # Getting the holidays (off-days) between two dates
    cal.holidays(start=start, end=end)
    se = pd.bdate_range(start=start, 
                    end=end,
                    freq=CDay(calendar=cal)).to_series()
    # Counting the number of working days in range
    num = se.count() - 1
    return num

if __name__ == '__main__':
    totalTDays = numOfTradingDaysTotal()
    currentDay = numberOfDay()
    print(f"There are {totalTDays} trading days this month. This is the {currentDay} trading day in that month. ")