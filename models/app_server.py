#!/usr/bin/python3
"""
App-server class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
STORAGE_TYPE = os.environ.get('STACK_TYPE_STORAGE') 

class AppServer(BaseModel, Base):
    """
    App_server class handles all application server
    """
    if STORAGE_TYPE == "db":
        __tablename__ = 'app_servers'
        type = Column(String(128), nullable=False)
        status = Column(String(128), nullable=False)
    else:
        type = ''
        status = ''
