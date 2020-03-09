import os
from models.base_model import BaseModel
from models.user import User
from models.app_server import AppServer
from models.firewall import Firewall
from models.server import Server
from models.ssh import Ssh
from models.ssl import Ssl

"""CNC - dictionary = { Class Name (string) : Class Type }"""

if os.environ.get('STACK_TYPE_STORAGE') == 'db':
    from models.engine import db_storage
    CNC = db_storage.DBStorage.CNC
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    CNC = file_storage.FileStorage.CNC
    storage = file_storage.FileStorage()

storage.reload()
