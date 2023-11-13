#!/usr/bin/python3
"""Place class"""


class Place(BaseModel):
    """Place class inheriting BaseMode"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night: 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self):
        """Initializes  place class instance"""
        super().__init__()
    pass
