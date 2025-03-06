"""Tests for celestial body implementations."""

import pytest
from mission_analysis.body.base import Body

# Create a concrete test class since Body is abstract
class TestBody(Body):
    def gravity(self, altitude: float) -> float:
        return self.mu / ((self.equatorial_radius + altitude) ** 2)

def test_body_properties():
    """Test basic body properties."""
    body = TestBody(
        name="Test",
        mass=5.972e24,  # kg
        j2=0.001082,
        flattening=1/298.257223563,
        radii=(6378137.0, 6356752.314245),  # meters
        rotation_rate=7.292115e-5,  # rad/s
        mu=3.986004418e14  # m³/s²
    )
    
    assert body.name == "Test"
    assert body.equatorial_radius == 6378137.0
    assert body.polar_radius == 6356752.314245
    assert abs(body.gravity(0) - 9.81) < 0.1  # Approximate surface gravity