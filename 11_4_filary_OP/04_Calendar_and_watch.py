from datetime import date, datetime
from calendar import monthrange


class Watch:
    def get_time(self):
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        return current_time


class Calendar:
    def get_day(self):
        today = date.today()
        return today

    def get_days_in_month(self):
        days = monthrange(2022, 11)[1]
        return days


class both(Calendar, Watch):
    def show_current_datetime(self):
        print(f"current time: {super().get_time()}")
        print(f'Current date: {super().get_day()}')
        print(f"current month: {super().get_days_in_month()}, days")


both = both()
both.show_current_datetime()




