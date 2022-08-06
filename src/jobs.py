import time
from datetime import datetime

import schedule

from date_info.provider import provide_today_info

def create_schedules():
    schedule.every().day.at("08:00").do(provide_today_info)

