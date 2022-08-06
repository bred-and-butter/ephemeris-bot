import time
from datetime import datetime

import schedule

from date_info.provider import provide_today_info


def create_jobs():
    #schedule.every().day.at("08:00").do(provide_today_info)
    schedule.every(6).seconds.do(print_provider)

def print_provider():
    print(f"{datetime.now().isoformat()}\n{provide_today_info()}")
