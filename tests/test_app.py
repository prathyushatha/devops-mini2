import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import main


def test_main():
    result = main()
    assert result == "DevOps Mini Project 2 Running!"