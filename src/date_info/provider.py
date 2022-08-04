from datetime import datetime

from date_info.dates import EPHEMERIS_DICT

def provide_today_info():
    now = datetime.now()

    if now.month in EPHEMERIS_DICT:
        if now.day in EPHEMERIS_DICT[now.month]:
            return EPHEMERIS_DICT[now.month][now.day]
        else:
            return "Não se comemora nada hoje"
    else:
        return "Mês não encontrado"