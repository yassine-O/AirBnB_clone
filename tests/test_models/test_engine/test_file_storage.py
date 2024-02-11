#!/usr/bin/python3

""" Unit tests for file storage Module """

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ unittest FileStorage """

    @classmethod
    def setUpClass(cls):
        """ set up class """
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """ tear down class """
        del cls.base

    def test_all(self):
        """ test all method """
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)
