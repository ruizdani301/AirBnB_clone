#!/usr/bin/python3
"""test Base models performs the tests of each
   of the requirements of each method
"""

from datetime import datetime
import unittest
from models.base_model import BaseModel


class Test_Base_Model(unittest.TestCase):
    """class test BaseModel performs the tests of each
       of the requirements of each method
    """

    base = BaseModel()

    def test_attributeExist(self):
        """prove if attribute exist"""

        self.assertTrue(hasattr(self.base, 'id'))
        self.assertTrue(hasattr(self.base, 'updated_at'))
        self.assertTrue(hasattr(self.base, 'created_at'))

    def test_correctType(self):
        """Verify if the type of the attribute is correct"""

        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_created_class(self):
        """test when create a BaseModel
           validating each operation
        """

        self.assertEqual(BaseModel, type(self.base))
        self.assertEqual(str, type(self.base.id))
        self.assertEqual(datetime, type(self.base.created_at))
        self.assertEqual(datetime, type(self.base.updated_at))

    def test__init__kwargs(self):
        """test create BaseModel with dictionary
           validating each operation
        """

        dic = self.base.to_dict()
        base2 = BaseModel(**dic)
        self.assertEqual(self.base.id, base2.id)
        self.assertNotEqual(self.base, base2)
        self.base.number = 10
        self.assertEqual(int, type(self.base.number))
        self.base.nomber = "carlos"
        self.assertEqual(str, type(self.base.nomber))

    def test_to_dict(self):
        """test that check the dictionary
           validating each operation
        """

        dic = self.base.to_dict()
        self.assertEqual(str, type(dic['updated_at']))
        self.assertEqual(str, type(dic['created_at']))
        self.assertEqual("BaseModel", dic['__class__'])
        self.assertEqual(dict, type(self.base.to_dict()))

    def test_save(self):
        """test check method save()
           validating each operation
        """

        date = self.base.updated_at
        self.base.save()
        date2 = self.base.updated_at
        self.assertNotEqual(date, date2)

    def testsaveUpdate(self):
        """Checks if save method updates the instances update_at"""

        self.base.first_name = "Holberton"
        self.base.save()

        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

        first_dic = self.base.to_dict()

        self.base.first_name = "School"
        self.base.save()
        second_dic = self.base.to_dict()

        self.assertEqual(first_dic['created_at'], second_dic['created_at'])
        self.assertNotEqual(first_dic['updated_at'], second_dic['updated_at'])

    def testBaseModel(self):
        """Test atributes value of a BaseModel instances"""

        self.base.name = "My First Model"
        self.base.my_number = "89"
        self.base.save()
        my_model_json = self.base.to_dict()

        self.assertEqual(self.base.name, my_model_json['name'])
        self.assertEqual(self.base.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])


if __name__ == '__main__':
    unittest.main()
