import pytest


def hello() -> str:
    return "hello"


def test_hell0():
    assert hello() == "hello"
