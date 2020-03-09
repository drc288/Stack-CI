#!/usr/bin/python3
"""
Ssb Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
STORAGE_TYPE = os.environ.get('STACK_TYPE_STORAGE')

class Ssh(BaseModel, Base):
    """
    Ssh class handles all application ssh
    """
    if STORAGE_TYPE == 'db':
        __tablename__ = 'ssh'
        pub_key = Column(String(128), nullable=False)
        priv_key = Column(String(128), nullable=False)
    else:
        pub_key = ''
        priv_key = ''
