from pytest_bdd import *
from pathlib import Path
import pytest
import behave

featureFileName = "first_feature.feature"
featureFileDir = "features"

BASE_DIR = Path(__file__).resolve().parent.parent
print(str(BASE_DIR))
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFileName)


def pytest_configure():
    pytest.int1 = 0
    pytest.int2 = 0
    pytest.sum = 0


@scenario(FEATURE_FILE, 'Addition of two integers')
def test_addition():
    print("Test Ended.")


@given('Two Integers 2 and 3')
def test_two_integers():
    pytest.int1 = 2
    pytest.int2 = 3


@when('Integers 2 and 3 are added')
def test_add_integers():
    pytest.sum = pytest.int1 + pytest.int2


@then('Sum is equal to 5')
def test_sum():
    assert pytest.sum == 5
