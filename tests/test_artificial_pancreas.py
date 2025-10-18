import pytest
from main.artificial_pancreas import ArtificialPancreasSystem

@pytest.fixture
def system():
    """Fixture to create a fresh system for each test."""
    return ArtificialPancreasSystem(100)

def test_glucose_increases_after_meal(system):
    before = system.glucose_level
    system.meal(40)
    assert system.glucose_level > before

def test_glucose_decreases_after_exercise(system):
    before = system.glucose_level
    system.exercise(30)
    assert system.glucose_level < before