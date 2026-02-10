from src.main import print_name
import pytest


def test_shiri_doitch():
    assert print_name() == "shiri is the most perfect girl"
