from .calculator import Calculator
from .config import DIRECTORY_PATH, COLUMN_NUMBER, STUDENT_COEFFICIENT, ACCURACY
from .indications_reader import IndicationsReader


def calculate_results():
    reader = IndicationsReader(DIRECTORY_PATH, COLUMN_NUMBER)
    for file, indication in reader.get_indications().items():
        print(f'[{file}]: ')
        calculate_for_indication(indication, 0)
        print('====================')


def calculate_for_indication(indication, facility_inaccuracy):
    calculator = Calculator(
        indication,
        STUDENT_COEFFICIENT,
        facility_inaccuracy
    )

    print(f'Average: {round(calculator.calculate_average(), ACCURACY)}')
    print(f'Estimation of msd: {round(calculator.calculate_estimation_of_msd(), ACCURACY)}')
    print(f'Interval of random inaccuracy: {round(calculator.calculate_interval_of_random_inaccuracy(), ACCURACY)}')
    print(f'Absolute inaccuracy: {round(calculator.calculate_absolute_inaccuracy(), ACCURACY)}')
    print(f'Relative inaccuracy: {round(calculator.calculate_relative_inaccuracy(), ACCURACY)}')
