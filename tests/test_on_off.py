from src.on_off import on, off
import pytest


def test_on():
    result = on()
    assert result == True


def test_off():
    result = off()
    assert result == True
