"""
Utility module wind_tools for gfs2sms.

Functions for processing u and v vectors.
"""

import math


def get_wind_spd_kts(u, v):
    """
    Add u and v vectors convert from m/s to kts.

    Using pythagoras theorem in math.hypot() calculate the hypotenuse,
    which is the magnitude of u and v combined. Convert from m/s to knots.

    parameters:
        u: float. X-axis value
        v: float. Y-axis value

    return:
        wind speed in knots: float.
    """
    spd_mps = math.hypot(u, v)
    return spd_mps * 1.943844 # The constant for calculating kts from m/s.


def get_wind_spd_ms(u, v):
    """
    Add u and v vectors.

    Using pythagoras theorem in math.hypot() calculate the hypotenuse,
    which is the magnitude of u and v combined.

    parameters:
        u: float. X-axis value
        v: float. Y-axis value

    return:
        wind speed in meters per second.
    """
    return math.hypot(u, v)


def get_wind_dir_deg(u, v):
    """
    Calculate atan(y / x), in radians. Convert to degrees.
    The result is between -pi and pi.
    The vector in the plane from the origin to point (x, y)
    makes this angle with the positive X axis.

    parameters:
        u: float. X-axis value
        v: float. Y-axis value

    return:
        angle of hypothenuse from positiv x-axis. float.
    """
    radians = math.atan2(u, v)
    return math.degrees(radians)
