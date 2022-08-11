from typing import Protocol, Callable


class JobInterface(Protocol):
    def init_jobs(self, job_to_do: Callable):
        ...

    def job_check(self):
        ...