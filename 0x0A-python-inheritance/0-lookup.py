#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """returns a list of an object's available attributes."""
    return (dir(obj))
