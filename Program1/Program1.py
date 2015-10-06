file object = open("output.dat" [, w][, 0])
print "Devin Ritter"
print "09/15/2015"
print "Program 1 - Intro to Quadtrees"

def lat2canvas(lat):
    """
    Turn a latitude in the form [-90 , 90] to the form [0 , 180]
    """
    return float(lat) % 180

def lon2canvas(lon):
    """
    Turn a longitude in the form [-180 , 180] to the form [0 , 360]
    """
    return float(lon) % 360

def canvas2lat(lat): 
    """
    Turn a latitutude in the form [0 , 180] to the form [-90 , 90]
    """
    return ((float(lat)+90) % 180) - 90

def canvas2lon(lon):
    """
    Turn a longitude in the form [0 , 360] to the form [-180 , 180]
    """
    return ((float(lon)+180) % 360) - 180

def displace(lat,lng,theta, distance,unit="miles"):
    """
    Displace a LatLng theta degrees clockwise and some feet in that direction.
    Notes:
        http://www.movable-type.co.uk/scripts/latlong.html
        0 DEGREES IS THE VERTICAL Y AXIS! IMPORTANT!
    Args:
        theta:    A number in degrees where:
                  0   = North
                  90  = East
                  180 = South
                  270 = West
        distance: A number in specified unit.
        unit:     enum("miles","kilometers")
    Returns:
        A new LatLng.
    """
    theta = np.float32(theta)
    radiusInMiles = 3959
    radiusInKilometers = 6371

    if unit == "miles":
        radius = radiusInMiles
    else:
        radius = radiusInKilometers

    delta = np.divide(np.float32(distance), np.float32(radius))

    theta = deg2rad(theta)
    lat1 = deg2rad(lat)
    lng1 = deg2rad(lng)

    lat2 = np.arcsin( np.sin(lat1) * np.cos(delta) +
                      np.cos(lat1) * np.sin(delta) * np.cos(theta) )

    lng2 = lng1 + np.arctan2( np.sin(theta) * np.sin(delta) * np.cos(lat1),
                              np.cos(delta) - np.sin(lat1) * np.sin(lat2))

    lng2 = (lng2 + 3 * np.pi) % (2 * np.pi) - np.pi

    return [rad2deg(lat2), rad2deg(lng2)]

  def midPoint(lat1, lon1, lat2, lon2):
    """
    Calculate the midpoint between two coordinate points
    """

    # phi = 90 - latitude
    lat1 = deg2rad(lat1)
    lat2 = deg2rad(lat2)

    # theta = longitude
    lon1 = deg2rad(lon1)
    lon2 = deg2rad(lon2)

    X1 = cos(lat1) * cos(lon1)
    Y1 = cos(lat1) * sin(lon1)
    Z1 = sin(lat1)

    X2 = cos(lat1) * cos(lon1)
    Y2 = cos(lat1) * sin(lon1)
    Z2 = sin(lat1)

    X = (X1+X2) / 2
    Y = (Y1+Y2) / 2
    Z = (Z1+Z2) / 2

    Lon = atan2(Y, X)
    Hyp = sqrt(X * X + Y * Y)
    Lat = atan2(Z, Hyp)

    lat = Lat * 180/math.pi
    lon = Lon * 180/math.pi

    return[lat,lon]


def haversine(lon1, lat1, lon2, lat2,units="miles"):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    if units == "miles":
       r = 3959 # Radius of earth in miles.
    else:
       r = 6371 # Radius of earth in kilometers.

    return c * r
