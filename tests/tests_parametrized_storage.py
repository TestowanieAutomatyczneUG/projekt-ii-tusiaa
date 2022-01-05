import unittest
from assertpy import *
from parameterized import *
from unittest.mock import *
from src.storage import *

@parameterized_class(('str_wrong_value', 'int_wrong_value', 'positive_float_wrong_value'), [
    (1, "int", -5.0),
    (1.5, 1.5, "float"),
    (True, True, True),
    (None, None, None),
    ("", "", ""),
    ([1,2,3], [1,2,3], [1,2,3]),
    ({'name': 2, 'grades': 4}, {'name': 2, 'grades': 4}, {'name': 2, 'grades': 4}),
])
class TestsParametrizedStorage(unittest.TestCase):
    def setUp(self):
        self.storage = Storage()