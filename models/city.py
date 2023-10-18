#!/usr/bin/python3
"""Specifies the City SubClass module"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""
