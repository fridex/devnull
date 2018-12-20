#!/bin/env python
# -*- coding: utf-8 -*-

class Type(object):
    _mapping = {
        "string": str,
        "bool": bool,
        "int": int,
        "long": long,
        "float": float,
        "tuple": tuple,
        "list": list,
        "dict": dict,
        "none": None
    }

    @classmethod
    def string2type(cls, string):
        if string not in cls._mapping:
            raise ValueError("Unknown string representing type %s" % string)
        return cls._mapping[string]

    @classmethod
    def type2string(cls, type_):
        for k, v in cls._mapping.iteritems():
            if type_ == v:
                return k

        raise KeyError("Unknown type %s" % type_)
