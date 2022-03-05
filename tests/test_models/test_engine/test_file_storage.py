#!/usr/bin/python3
"""This is the unittest for FileStorage"""
import unittest
from models.engine.file_storage import FileStorage
from models.engine import file_storage
from models.base_model import BaseModel
import os


FileStorage = file_storage.FileStorage


class Test_FileStorage(unittest.TestCase):
    """unitest - Test FileStorage class"""

    @classmethod
    def createClass(cls):
        """set up before every test method"""
        cls.storage = FileStorage()

    @classmethod
    def del_json(cls):
        """Remove test instances"""
        del cls.storage
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_all(self):
        """Test method All"""
        s_dict = self.storage.all()
        self.assertIsInstance(s_dict, dict)
        self.assertIs(s_dict, self.storage._FileStorage__objects)

    def test_new(self):
        """test method new"""
        s_dict = self.storage.all()
        bas = BaseModel()
        kk = "{}.{}".format(type(bas).__name__, bas.id)
        self.assertTrue(kk in s_dict.keys())

    def test_save(self):
        """test method save"""
        self.assertIsNotNone(FileStorage.save)
        self.storage.save()
        with open("file.json", 'r') as reader:
            string = reader.readlines()

        try:
            os.remove("file.json")
        except BaseException:
            pass

        self.storage.save()

        with open("file.json", 'r') as reader:
            string2 = reader.readlines()

        self.assertEqual(string, string2)
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """test method reload"""
        self.assertIsNotNone(FileStorage.reload)
        try:
            os.remove("file.json")
        except BaseException:
            pass
        with open("file.json", "w") as writer:
            writer.write("{}")
        with open("file.json", "r") as reader:
            for l in reader:
                self.assertEqual(l, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
