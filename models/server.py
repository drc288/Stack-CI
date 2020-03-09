#!/usr/bin/python3
"""
Server Class from Models Module
"""
import os 
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String 
STORAGE_TYPE = os.environ.get('STACK_TYPE_STORAGE')

class Server(BaseModel, Base):
    """
    Server class handles all application servers 
    """
    if STORAGE_TYPE == "db":
        __tablename__ = 'servers'
        name = Column(String(128), nullable=False)
        labels = Column(String(255), nullable=True)
    else:
        name = ''
        labels = ''
