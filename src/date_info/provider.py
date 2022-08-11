from datetime import datetime

from date_info.dates import EPHEMERIS_DICT


def provide_date_info(year: int, month: int, day: int) -> str:
    moment = datetime.now()

    if moment.month in EPHEMERIS_DICT:
        if moment.day in EPHEMERIS_DICT[moment.month]:
            return format_date_info(moment, EPHEMERIS_DICT[moment.month][moment.day])
        else:
            return format_date_info(moment, "Não se comemora nada hoje")
    else:
        return format_date_info(moment, "Mês não encontrado")


def format_date_info(selected_date: datetime, answer: str):
    return f"Data selecionada: {selected_date.day}/{selected_date.month}/{selected_date.year}\n{answer}"
