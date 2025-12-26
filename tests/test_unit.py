import pytest
from src.features import hash_feature

def test_hash_feature_consistency():

    assert hash_feature("kalem", 10) == hash_feature("kalem", 10)

def test_hash_feature_range():

    result = hash_feature("test_data", 5)
    assert 0 <= result < 5

def test_empty_input():

    assert hash_feature("", 10) == 0