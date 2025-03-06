"""Earth celestial body implementation."""

from .base import Body
from typing import Tuple

class Earth(Body):
    """Earth celestial body model.
    
    Implements Earth-specific parameters and calculations based on WGS-84.
    
    References
    ----------
    .. [1] World Geodetic System 1984 (WGS-84)
    .. [2] Vallado, D. A., "Fundamentals of Astrodynamics and Applications"
    """
    
    def __init__(self):
        """Initialize Earth with WGS-84 parameters."""
        # WGS-84 Parameters
        equatorial_radius = 6378137.0  # meters
        flattening = 1.0 / 298.257223563
        polar_radius = equatorial_radius * (1 - flattening)
        
        super().__init__(
            name="Earth",
            mass=5.972168e24,  # kg
            j2=0.001082627,  # Earth's J2 coefficient
            flattening=flattening,
            radii=(equatorial_radius, polar_radius),  # meters
            rotation_rate=7.292115e-5,  # rad/s
            mu=3.986004418e14  # m³/s²
        ) 