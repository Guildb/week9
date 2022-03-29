import pytest
import Motorbike

def test_create_motorbike():
    vehicle = Motorbike.Motorbike("abc", 950)
    assert vehicle.weight == 950
    assert vehicle.registration == "abc"
    assert vehicle.calculatefee() == 3
