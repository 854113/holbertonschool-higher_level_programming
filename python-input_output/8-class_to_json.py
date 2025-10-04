#!/usr/bin/python3
"""
In te module the function class_to_json is declarated
"""


def class_to_json(obj):
    """
    a function that returns the dictionary
    description with simple data structure
    """
    cont = obj.__dict__
    dic = {
        clave: valor
        for clave, valor in cont.items()
        if isinstance(valor, (list, dict, str, int, bool))
    }
    return dic
