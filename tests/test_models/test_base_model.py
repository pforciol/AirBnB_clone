#!/usr/bin/python3
"""
    UnitTest for BaseModel
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from unittest.mock import patch


class TestBase_model(unittest.TestCase):

    """Basic instanciation object__init__"""

    def test_is_id_created(self):
        """ Test id created """
        obj = BaseModel()
        self.assertTrue(obj.id is not None)

    def test_class_type(self):
        """ Test class type """
        obj = BaseModel()
        self.assertTrue(type(obj) is BaseModel)

    def test_attributes_type(self):
        """Test attr types"""
        b = BaseModel()
        b.name = "empty"
        b.age = 13
        self.assertEqual(type(b.id), str)
        self.assertEqual(type(b.created_at), datetime)
        self.assertEqual(type(b.updated_at), datetime)

    def test_datetime(self):
        """Test date different"""
        before = datetime.now()
        b = BaseModel()
        after = datetime.now()
        self.assertEqual(b.created_at, b.updated_at)
        self.assertTrue(before <= b.created_at <= after)
        n_b = BaseModel()
        self.assertNotEqual(b.created_at,  n_b.created_at)

    def test_to_dict(self):
        """test attributes types in dict"""
        b = BaseModel()
        b.name = "Mark"
        b.age = 12
        dict_base = b.to_dict()
        self.assertEqual(dict_base['updated_at'], b.updated_at.isoformat())
        self.assertEqual(dict_base['__class__'], "BaseModel")
        self.assertEqual(dict_base['name'], "Mark")
        self.assertEqual(dict_base['age'], 12)
        self.assertEqual(dict_base['created_at'], b.created_at.isoformat())

    def test_value_attr_type(self):
        b = BaseModel()
        b.name = "empty"
        b.age = 13
        f = "%Y-%m-%dT%H:%M:%S.%f"
        d = b.to_dict()
        self.assertEqual(d['created_at'], b.created_at.strftime(f))
        self.assertEqual(d['updated_at'], b.updated_at.strftime(f))
        self.assertEqual("empty", b.name)
        self.assertEqual(13, b.age)

    def test_is_id_is_string(self):
        """Test id is a string"""
        obj = BaseModel()
        self.assertEqual(type(obj.id), str)

    def test_is_id_different_multiple_instance(self):
        """ Test that id is different with two instance object """
        obj = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj.id, obj2.id)

    def test_is__created_date_is_created(self):
        """ Test that a date has been well created """
        obj = BaseModel()
        self.assertTrue(obj.created_at is not None)

    def test_uuid(self):
        """ test uuid diff"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_is_created_date_is_created(self):
        """ Test that a date has been well created """
        obj = BaseModel()
        obj2 = BaseModel()
        d1 = obj.created_at
        d2 = obj.created_at
        self.assertTrue(d1 is not None and d2 is not None)

    def test_is__created_date_is_object_datatime(self):
        """ Test that created_at is a object date"""
        obj = BaseModel()
        self.assertEqual(type(obj.created_at), datetime)

    def test_is_updated_at_is_created(self):
        """ Test that updated_at attribute has been well created """
        obj = BaseModel()
        self.assertTrue(obj.updated_at is not None)

    def test_is_updated_at_is_created_multiple_instance(self):
        """ Test that updated_at attribute
        has been well created with multiple instance"""
        obj = BaseModel()
        obj2 = BaseModel()
        d1 = obj.updated_at
        d2 = obj.updated_at
        self.assertTrue(d1 is not None and d2 is not None)

    def test_is_updated_at_is_object_datatime(self):
        """ Test that updated_at is a object date"""
        obj = BaseModel()
        self.assertEqual(type(obj.updated_at), datetime)

    """
        kwargs
    """

    def test_is_kwargs_created_at_date_object(self):
        """ Test that kwargs is instance created_at to date object """
        obj = BaseModel()
        save_dict = obj.to_dict()
        new_obj = BaseModel(**save_dict)
        self.assertEqual(type(new_obj.created_at), datetime)

    """
    Method to_dict()
    """

    def test_is_to_dict_return_a_dict(self):
        """ Test that the to_dict() method return well a dictionnary """
        obj = BaseModel()
        s = obj.to_dict()
        self.assertEqual(type(s), dict)

    def test_is_to_dict_created_at_is_str(self):
        """ Test that to_dict() created_at is str in dictionary"""
        obj = BaseModel()
        s = obj.to_dict()
        for i in s:
            if i == "created_at":
                self.assertEqual(type(s[i]), str)

    def test_is_to_dict_updated_at_is_str(self):
        """ Test that to_dict() updated_at is str in dictionary"""
        obj = BaseModel()
        s = obj.to_dict()
        for i in s:
            if i == "updated_at":
                self.assertEqual(type(s[i]), str)

    """
        Method __str__
    """

    def test_is_str_return_a_string(self):
        """ Test that __str__return well a string """
        obj = BaseModel()
        s = str(obj)
        self.assertEqual(type(s), str)

    def test_str(self):
        """ Test that str correct """
        obj = BaseModel()
        s = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(s, str(obj))

    """
        Method save()
    """
    @patch('models.storage')
    def testA_save(self, mock):
        """ Test that str correct """
        obj = BaseModel()
        before = obj.updated_at
        before2 = obj.created_at
        obj.save()
        n1 = obj.created_at
        n2 = obj.updated_at
        self.assertNotEqual(before, n2)
        self.assertEqual(before2, n1)
