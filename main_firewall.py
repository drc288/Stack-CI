#!/usr/bin/python3
"""
"""
from models import storage
from models.firewall import Firewall

"""
Objects creations
"""
firewall_1 = Firewall(port="531", status="ok", protocol="HTTP")
print("New Firewall {}".format(firewall_1))
firewall_1.save()
storage.save()
