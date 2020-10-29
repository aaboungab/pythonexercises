import pytest
from easy import near

def test_near():
    assert near.near("reset", "rest") == True 

def test_pass():
    assert near.near("leave", "eave") == True 

def test_fail():
    assert near.near("eave", "leave") == False 

def test_lettermove():
    assert near.near("sleet", "lets") == False