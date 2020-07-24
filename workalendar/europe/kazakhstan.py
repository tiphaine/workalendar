from datetime import date

from ..core import WesternCalendar, MON
from ..registry_tools import iso_register

# MON, TUE, WED, THU, FRI, SAT, SUN = range(7)


@iso_register('KZ')
class Kazakhstan(WesternCalendar):
    'Kazakhstan'
    include_labour_day = True
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "New Year Holiday"),
        (1, 7, "Orthodox Christmas"),
        (3, 8, "International Women Day"),
        (3, 21, "Nauryz"),
        (3, 22, "Nauryz"),
        (3, 23, "Nauryz"),
        (5, 7, "Defender of the Fatherland"),
        (5, 9, "Victory Day"),
        (5, 10, "Victory Day Holiday"),
        (7, 6, "Capital City Day"),
        (8, 30, "Constitution Day"),
        (12, 1, "First President Day"),
        (12, 16, "Independence Day"),
    )

    def get_variable_days(self, year):
        # usual variable days
        days = super().get_variable_days(year)
        days.append(
            (self.find_following_working_day(date(year, 1, 2)),
             'New Year Holiday')
        )
        days.append(
            (Kazakhstan.get_nth_weekday_in_month(year, 5, MON),
             'Unity Day Holiday'),
        )
        if year in (2021,):
            days.append((date(2021, 7, 20), 'Kurban Ait'),)
            days.append(
                (self.find_following_working_day(date(2021, 12, 17)),
                    'Independence Day holiday')
            )
        if year in (2022,):
            days.append((date(2022, 7, 10), 'Kurban Ait'),)
            days.append(
                (self.find_following_working_day(date(2022, 12, 17)),
                 'Independence Day holiday')
            )
        return days
