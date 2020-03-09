#!/usr/bin/python3
"""
Firewall Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
STORAGE_TYPE = os.environ.get('STACK_TYPE_STORAGE')

class Firewall(BaseModel, Base):
    """
    Firewall class handles all application firewalls
    """
    if STORAGE_TYPE == "db":
        __tablename__ = 'firewalls'
        port  = Column(Integer(), nullable=False)
        status = Column(String(128), nullable=False)
        protocol = Column(String(128), nullable=False)
    else:
        port =''
        status = ''
        protocol = ''
