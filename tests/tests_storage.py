import unittest
from assertpy import *
from unittest.mock import *
from src.storage import *

class TestsStorage(unittest.TestCase):
    def setUp(self):
        self.storage = Storage()