import pytest
from Intermediate import route_planner

def test_planner():
    assert route_planner.route_planner('0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15') == '0 8 12 14 15'