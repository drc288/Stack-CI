#!/usr/bin/python3
"""
"""
from models import storage
from models.app_server import AppServer

"""
Objects creations
"""
app_server_1 = AppServer(type="python", status="ok")
print("App_server {}".format(app_server_1))
app_server_1.save()
storage.save()
