import time
from datetime import datetime

import schedule

def say_hello():
    print("oi")

def good_night(date_time: datetime, outra_coisa: str):
    print(f"boa noite, a hora é: {date_time.isoformat()} {outra_coisa}")

schedule.every(3).seconds.do(say_hello)
schedule.every().day.at("00:07").do(good_night, datetime.now(), "outra coisa aqui")

while(True):
    print("checando trabalhos pendentes")
    print(f"A hora é: {datetime.now()}")
    schedule.run_pending()
    time.sleep(1)
