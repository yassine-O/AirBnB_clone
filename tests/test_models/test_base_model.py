#!/usr/bin/python3

""" Unittest for BaseModel class """

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ BaseModel unit test """

    @classmethod
    def setUpClass(cls):
        """ set up class """
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """ tear down class """
        del cls.base

    def test_init(self):
        """ test __init__ method """
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save(self):
        """ test save method """
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        """ test to_dict method """
        base_dict = self.base.to_dict()
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
