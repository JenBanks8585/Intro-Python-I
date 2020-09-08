# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

loc1 = LatLon(45.56, 87.3)
#print(loc1.lat)
#print(loc1.lon)


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class WayPoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return f"The name is {self.name}, the latitude reading is {self.lat} , and the longitude reading is {self.lon}."

    def __repr__(self):
        return f"WayPoint(name = {self.name}, lan={self.lat}, lon={self.lon})"

point1= WayPoint(42.3, 67.8, 'jen')
point1
print(point1)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class GeoCache(WayPoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size
    
    def __str__(self):
        return f'''The name is {self.name}, the latitude reading is {self.lat} , 
        and the longitude reading is {self.lon}. 
        The difficulty level is {self.difficulty}, the size is {self.size}'''
        


geo1 = GeoCache(23.2, 56.4, 'Jack', 'A', 'med')

print(geo1.lat)
print(geo1.size)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = WayPoint(41.70505, -121.51521, "Catacombs")
print(waypoint)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
##print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = GeoCache(44.052137, -121.41556,"Newberry Views", 1.5, 2 )

print(geocache)


