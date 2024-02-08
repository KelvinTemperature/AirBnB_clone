#!/usr/bin/python3
"""
    Review Module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
