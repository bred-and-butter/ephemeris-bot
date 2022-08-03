import time
from datetime import datetime

import schedule

from date_info.provider import format_data

def create_schedules():
    schedule.every().day.at("00:07").do(format_data)

