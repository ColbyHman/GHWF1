
from grades import compute_hw_average


def test_zero_grades():
    grades = []
    assert compute_hw_average(grades) == 0


def test_single_grade():
    grades = [42]
    assert compute_hw_average(grades) == 42

def test_two_grades():
    # This verifies that two grades work
    grades = [20, 60]
    assert compute_hw_average(grades) == 40

def test_three_grades():
    # This verifies that three grades work
    grades = [20, 40, 60]
    assert compute_hw_average(grades) == 40

def test_four_grades():
    grades = [20, 40, 60, 80]
    assert compute_hw_average(grades) == 50

def test_five_grades():
    # This verifies that three grades work
    grades = [20, 40, 60, 80, 50]
    assert compute_hw_average(grades) == 30
