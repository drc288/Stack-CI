#!/usr/bin/python3
"""
"""
from models import storage
from models.ssl import Ssl

"""
Objects creations
"""
ssl_1 = Ssl(email="monik@gmail.com", domain_name="unicorn.tech")
print("New ssl {}".format(ssl_1))
ssl_1.save()
storage.save()
