import gmaps
import gmaps.datasets
#from haversine import haversine, Unit
from math import radians, cos, sin, asin, sqrt

gmaps.configure(api_key='AIzaSyBlvE6HXrmuztPHa5sa6JIKXraPGrGlBcc')

frontgate = (-6.893216, 107.610438)
simpangDago = (-6.885203, 107.613683)
tigaanBorromeus = (-6.893766, 107.612949)

fig = gmaps.figure()
frontgateBorom = gmaps.directions_layer(frontgate, simpangDago, waypoints=[tigaanBorromeus])
fig.add_layer(frontgateBorom)
fig