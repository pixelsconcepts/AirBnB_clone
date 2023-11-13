#!/usr/bin/python3
"""Review class"""


class Review(BaseModel):
    """City review inheriting BaseMode"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        """Initializes review class instance"""
        super().__init__()
    pass
