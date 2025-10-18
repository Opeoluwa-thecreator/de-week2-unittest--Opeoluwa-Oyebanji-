import pytest
from main.artificial_pancreas import ArtificialPancreasSystem

@pytest.fixture
def system():
    """Fixture to create a fresh system for eachgi test."""
    return ArtificialPancreasSystem(100)

def test_glucose_increases_after_meal(system):
    before = system.glucose_level
    system.meal(40)
    assert system.glucose_level > before

def test_glucose_decreases_after_exercise(system):
    before = system.glucose_level
    system.exercise(30)
    assert system.glucose_level < before

def test_glucose_never_below_min(system):
    system.exercise(1000)  # unrealistically long, should hit floor
    assert system.glucose_level >= system.MIN_GLUCOSE

def test_high_glucose_triggers_insulin(system):
    # Make it very high to trigger insulin
    system.glucose_level = 200
    action, _ = system.predict_action()
    assert action == "deliver_insulin"
    assert system.total_insulin_delivered > 0

def test_low_glucose_triggers_warning(system):
    system.glucose_level = 80  # below 90 (target - tolerance)
    action, _ = system.predict_action()
    assert action == "warn_low_glucose"

def test_stable_glucose_maintains(system):
    system.glucose_level = 105  # within 90–110
    action, _ = system.predict_action()
    assert action == "maintain"

def test_multiple_sequence(system):
    # meal → exercise → action
    system.meal(50)
    system.exercise(20)
    action, level = system.predict_action()
    assert level >= system.MIN_GLUCOSE
    assert action in ["deliver_insulin", "maintain", "warn_low_glucose"]

def test_invalid_meal_input():
    sys = ArtificialPancreasSystem(100)
    with pytest.raises(ValueError):
        sys.meal(-5)

def test_invalid_exercise_input():
    sys = ArtificialPancreasSystem(100)
    with pytest.raises(ValueError):
        sys.exercise(-10)