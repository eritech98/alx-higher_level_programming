#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples."""
    new = ()
    while len(tuple_a) < 2:
        tuple_a = tuple_a + (0,)
    while len(tuple_b) < 2:
        tuple_b = tuple_b + (0,)
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]
    for x, y in zip(tuple_a, tuple_b):
        new = new + (x + y,)
    return new
