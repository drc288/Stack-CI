#!/usr/bin/python3
"""
"""
from models import storage
from models.user import User

"""
Objects creations
"""
user_1 = User(email="monikmaja@gmail.com", password="hola", first_name="monica", last_name="jaimes")
print("New User {}".format(user_1))
user_1.save()
storage.save()
