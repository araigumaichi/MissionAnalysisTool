"""Mars celestial body implementation."""

from .base import Body
import numpy as np

class Mars(Body):
    """Mars celestial body model.
    
    References
    ----------
    .. [1] NASA Mars Fact Sheet
    .. [2] Mars-GRAM 2010 Model
    """
    
    def __init__(self):
        """Initialize Mars with standard parameters."""
        equatorial_radius = 3396200.0  # meters
        flattening = 0.00589  # Mars' flattening
        polar_radius = equatorial_radius * (1 - flattening)
        
        super().__init__(
            name="Mars",
            mass=6.4171e23,  # kg
            j2=1.960e-3,  # Mars' J2 coefficient
            flattening=flattening,
            radii=(equatorial_radius, polar_radius),  # meters
            rotation_rate=7.088218e-5,  # rad/s (24.623 hour period)
            mu=4.282837e13  # m³/s²
        )