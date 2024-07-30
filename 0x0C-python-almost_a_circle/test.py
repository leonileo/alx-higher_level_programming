#!/usr/bin/python3

import json

print(json.dumps(['kal']))

def test_var_args(**kwargs):
    for i, j in kwargs:
        print(i , j)

test_var_args(ar=2)
