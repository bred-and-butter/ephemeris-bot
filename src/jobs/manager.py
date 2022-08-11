from typing import Callable

import schedule

from consts import EPHEMERIS_FETCH_TIME


class JobManager:
    def __init__(self) -> None:
        pass

    def init_jobs(self, job_to_do: Callable):
        # schedule.every().day.at(EPHEMERIS_FETCH_TIME).do(job_to_do())
        schedule.every(int(EPHEMERIS_FETCH_TIME)).seconds.do(job_to_do)

    def job_check(self):
        print("checking for pending jobs...")
        schedule.run_pending()
