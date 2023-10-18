#!/usr/bin/python3
"""User Class Module to manage objects"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class manages objects"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
