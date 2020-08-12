from ..core import IslamicCalendar
from ..registry_tools import iso_register


@iso_register('MA')
class Morocco(IslamicCalendar):
    "Morocco"
    # Civil holidays
    include_labour_day = True
    # Islamic holidays
    include_prophet_birthday = True
    include_eid_al_fitr = True
    length_eid_al_fitr = 2
    include_eid_al_adha = True
    length_eid_al_adha = 2
    include_day_of_sacrifice = True
    include_islamic_new_year = True

    FIXED_HOLIDAYS = IslamicCalendar.FIXED_HOLIDAYS + (
            (1, 11, "Manifeste de l’Indépendance"),
            (7, 30, "Fete du Trone"),
            (8, 14, "Fête de la récupération de Oued Eddahab"),
            (8, 20, "Anniversaire de la Révolution du roi et du peuple"),
            (8, 21, "Fête de la jeunesse"),
            (11, 6, "Anniversaire de la Marche Verte"),
            (11, 18, "Fête de l'indépendance"),
        )
