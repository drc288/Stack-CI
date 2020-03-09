#!/usr/bin/python3
"""
"""
from models import storage
from models.ssh import Ssh

"""
Objects creations
"""
ssh_1 = Ssh(pub_key="/path", priv_key="/path")
print("New Ssh {}".format(ssh_1))
ssh_1.save()
storage.save()
