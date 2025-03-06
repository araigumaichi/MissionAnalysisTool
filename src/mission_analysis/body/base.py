"""Base class for celestial bodies."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple
import numpy as np

@dataclass
class Body(ABC):
    """Abstract base class for celestial bodies.
    
    Attributes
    ----------
    name : str
        Name of the celestial body
    mass : float
        Mass of the body in kg
    j2 : float
        Second zonal harmonic coefficient
    flattening : float
        Body's flattening factor
    radii : Tuple[float, float]
        Equatorial and polar radii in meters (a, b)
    rotation_rate : float
        Sidereal rotation rate in rad/s
    mu : float
        Standard gravitational parameter (GM) in m³/s²
    """
    
    name: str
    mass: float
    j2: float
    flattening: float
    radii: Tuple[float, float]  # (equatorial_radius, polar_radius)
    rotation_rate: float
    mu: float

    @property
    def equatorial_radius(self) -> float:
        """Get the equatorial radius in meters."""
        return self.radii[0]
    
    @property
    def polar_radius(self) -> float:
        """Get the polar radius in meters."""
        return self.radii[1]
    
    def gravity(self, altitude: float, latitude: float = 0.0) -> float:
        """Calculate gravitational acceleration including J2 effect.
        
        Parameters
        ----------
        altitude : float
            Altitude above reference surface in meters
        latitude : float, optional
            Planetocentric latitude in radians, by default 0.0 (equator)
            
        Returns
        -------
        float
            Gravitational acceleration in m/s²
            
        Notes
        -----
        Includes J2 perturbation effect due to body's oblateness.
        The formula used is:
        g = μ/r² * [1 + J2*(R_e/r)²*(3/2*sin²(φ) - 1/2)]
        where:
        - μ is the gravitational parameter
        - r is the distance from body's center
        - R_e is body's equatorial radius
        - φ is the planetocentric latitude
        - J2 is body's second zonal harmonic coefficient
        """
        r = self.equatorial_radius + altitude
        sin_lat = np.sin(latitude)
        
        # Basic inverse square law
        g0 = self.mu / (r * r)
        
        # J2 perturbation term
        j2_term = self.j2 * (self.equatorial_radius / r)**2 * (1.5 * sin_lat**2 - 0.5)
        
        return g0 * (1 + j2_term)