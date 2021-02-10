#!/usr/bin/python3
"""This is the base_model.py unittest module."""
from unittest import TestCase
from datetime import datetime

from models.base_model import BaseModel


class Test_BaseModel___init__(TestCase):
    """Test cases for BaseModel's __init__ method."""

    def test_BaseModel___init___no_args(self):
        """Tests __init__ in normal conditions."""
        self.assertEqual(type(BaseModel()), BaseModel)

    def test_BaseModel___init___too_many_args(self):
        """Tests __init__ with expected failure."""
        with self.assertRaises(TypeError):
            BaseModel(42)


class Test_BaseModel_id(TestCase):
    """Test cases for BaseModel's id attribute."""

    def test_BaseModel_id(self):
        """Tests basic id initialization."""
        self.assertIsNotNone(BaseModel().id)

    def test_BaseModel_id_string(self):
        """Tests if id initialization is string."""
        self.assertEqual(type(BaseModel().id), str)

    def test_BaseModel_id_random(self):
        """Tests if id initialization is random."""
        self.assertNotEqual(BaseModel().id, BaseModel().id)


class Test_BaseModel_created_at(TestCase):
    """Test cases for BaseModel's created_at attribute."""

    def test_BaseModel_created_at(self):
        """Tests basic created_at initialization."""
        self.assertIsNotNone(BaseModel().created_at)

    def test_BaseModel_created_at_datetime(self):
        """Tests if created_at initialization is datetime."""
        self.assertEqual(type(BaseModel().created_at), datetime)


class Test_BaseModel_updated_at(TestCase):
    """Test cases for BaseModel's updated_at attribute."""

    def test_BaseModel_updated_at(self):
        """Tests basic updated_at initialization."""
        self.assertIsNotNone(BaseModel().updated_at)

    def test_BaseModel_updated_at_datetime(self):
        """Tests if updated_at initialization is datetime."""
        self.assertEqual(type(BaseModel().updated_at), datetime)

    def test_BaseModel_updated_at_same_as_created_at(self):
        """Tests if updated_at is equal to created_at on initialization."""
        model = BaseModel()
        self.assertEqual(model.updated_at, model.created_at)


class Test_BaseModel___str__(TestCase):
    """Test cases for BaseModel's __str__ method."""

    def test_BaseModel___str__(self):
        """Tests basic __str__ call."""
        self.assertIsNotNone(BaseModel().__str__)


class Test_BaseModel_save(TestCase):
    """Test cases for BaseModel's save method."""

    def test_BaseModel_save_no_args(self):
        """Tests save in normal conditions."""
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.updated_at, model.created_at)

    def test_BaseModel_save_too_many_args(self):
        """Tests save with expected failure."""
        with self.assertRaises(TypeError):
            BaseModel().save(42)


class Test_BaseModel_to_dict(TestCase):
    """Test cases for BaseModel's to_dict method."""

    def test_BaseModel_to_dict_no_args(self):
        """Tests to_dict in normal conditions."""
        self.assertIsNotNone(BaseModel().to_dict())

    def test_BaseModel_to_dict_no_args(self):
        """Tests if to_dict returns a dict."""
        self.assertEqual(type(BaseModel().to_dict()), dict)

    def test_BaseModel_to_dict___class___presence(self):
        """Tests if to_dict has __class__ key/value pair."""
        self.assertIn("__class__", BaseModel().to_dict())

    def test_BaseModel_to_dict_created_at_string(self):
        """Tests if to_dict created_at key/value is string type."""
        self.assertEqual(type(BaseModel().to_dict()['created_at']), str)

    def test_BaseModel_to_dict_updated_at_string(self):
        """Tests if to_dict updated_at key/value is string type."""
        self.assertEqual(type(BaseModel().to_dict()['updated_at']), str)

    def test_BaseModel_save_too_many_args(self):
        """Tests to_dict with expected failure."""
        with self.assertRaises(TypeError):
            BaseModel().to_dict(42)
