#!/usr/bin/python3
"""
Ssl Class from Models Module 
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
STORAGE_TYPE = os.environ.get('STACK_TYPE_STORAGE')

class Ssl(BaseModel, Base):
    """
    Ssl class handles all application ssl
    """
    if STORAGE_TYPE =="db":
        __tablename__ = 'ssls'
        domain_name = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
    else:
        domain_name = ''
        email = ''
