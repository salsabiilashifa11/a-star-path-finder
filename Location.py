from math import radians, cos, sin, asin, sqrt

class Location:
    def __init__(self, longitude, latitude, name):
        self.longitude = longitude
        self.latitude = latitude
        self.name = name 

    def distance(self, location):
        # The math module contains a function named
        # radians which converts from degrees to radians.
        lon1 = radians(self.longitude)
        lon2 = radians(location.longitude)
        lat1 = radians(self.latitude)
        lat2 = radians(location.latitude)
        
        # Haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    
        c = 2 * asin(sqrt(a)) 
        
        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371
        
        # calculate the result
        return(c * r)

