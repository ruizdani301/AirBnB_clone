#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
dir = my_model.to_dict()

print (dir)
""""
new_model = BaseModel()
new_model.name = "nueva_prueba"
new_model.my_number = 753
dir2 = new_model.to_dict()

file = FileStorage()
file.new(dir)
file.new(dir2)

file.save()
file.reload()

for i, x in (file.all()).items():
    print (i, x)
"""