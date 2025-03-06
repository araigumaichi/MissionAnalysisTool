"""Moon celestial body implementation."""

from .base import Body
import numpy as np

class Moon(Body):
    """Moon celestial body model.
    
    References
    ----------
    .. [1] NASA Moon Fact Sheet
    .. [2] Lunar Constants and Models Document, NASA/JPL
    """
    
    def __init__(self):
        """Initialize Moon with standard parameters."""
        equatorial_radius = 1738100.0  # meters
        flattening = 0.0012  # Moon's flattening
        polar_radius = equatorial_radius * (1 - flattening)
        
        super().__init__(
            name="Moon",
            mass=7.34767309e22,  # kg
            j2=2.027e-4,  # Moon's J2 coefficient
            flattening=flattening,
            radii=(equatorial_radius, polar_radius),  # meters
            rotation_rate=2.6617e-6,  # rad/s (27.322 day period)
            mu=4.9048695e12  # m³/s²
        )