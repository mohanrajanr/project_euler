import abc


class Challenge(abc.ABC):

    def __init__(self, problem_number: int):
        self.problem_number = problem_number
