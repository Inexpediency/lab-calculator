from math import sqrt
from typing import List


class Calculator:
    _average = None
    _estimation_of_msd = None
    _interval_of_random_inaccuracy = None
    _absolute_inaccuracy = None
    _relative_inaccuracy = None

    def __init__(self, indications, student_coefficients, facility_inaccuracy):
        self._indications = indications
        self._indications_count = len(self._indications)
        self._student_coefficient = self._choose_student_coefficient(student_coefficients)
        self._facility_inaccuracy = facility_inaccuracy

    def calculate_average(self):
        if self._average:
            return self._average

        self._average = sum(self._indications) / self._indications_count

        return self._average

    def calculate_estimation_of_msd(self):
        if self._estimation_of_msd:
            return self._estimation_of_msd

        self._estimation_of_msd = sqrt(
            sum((indication - self._average) ** 2 for indication in self._indications) /
            (self._indications_count * (self._indications_count - 1))
        )

        return self._estimation_of_msd

    def calculate_interval_of_random_inaccuracy(self):
        if self._interval_of_random_inaccuracy:
            return self._interval_of_random_inaccuracy

        self._interval_of_random_inaccuracy = self._student_coefficient * self._estimation_of_msd

        return self._interval_of_random_inaccuracy

    def calculate_absolute_inaccuracy(self):
        if self._absolute_inaccuracy:
            return self._absolute_inaccuracy

        self._absolute_inaccuracy = sqrt(
            self._interval_of_random_inaccuracy ** 2 + (2 / 3 * self._facility_inaccuracy) ** 2
        )

        return self._absolute_inaccuracy

    def calculate_relative_inaccuracy(self):
        if self._relative_inaccuracy:
            return self._relative_inaccuracy

        self._relative_inaccuracy = self._absolute_inaccuracy / self._average * 100

        return self._relative_inaccuracy

    def _choose_student_coefficient(self, student_coefficients: List):
        student_coefficients.sort(key=lambda x: x[1])

        for indication_number, coefficient in student_coefficients:
            if self._indications_count >= indication_number:
                return coefficient

        return student_coefficients[-1][1]
