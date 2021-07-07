#coding: utf-8
import math
from pyproj import Geod

def waypoint(s_lat,s_lon,g_lat,g_lon):
    # gpsÆ»ÝnÌÜxAox©ç£AûÊpA½ûÊpðßé

    g = Geod(ellps='WGS84')
    azimuth, back_azimuth, distance_2d = g.inv(
        s_lat, s_lon, g_lat, g_lon)

    gps = {'azimuth': azimuth, 'back_azimuth': back_azimuth,
        'distance_2d': distance_2d}

    return gps
