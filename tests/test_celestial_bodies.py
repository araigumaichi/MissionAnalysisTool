"""Tests for specific celestial body implementations."""

import pytest
import numpy as np
from mission_analysis.body.earth import Earth
from mission_analysis.body.moon import Moon
from mission_analysis.body.mars import Mars

def test_earth_properties():
    """Test Earth physical properties."""
    earth = Earth()
    
    assert earth.name == "Earth"
    assert abs(earth.gravity(0) - 9.81) < 0.1  # Surface gravity
    assert earth.equatorial_radius == 6378137.0
    assert abs(earth.flattening - 1/298.257223563) < 1e-10

def test_moon_properties():
    """Test Moon physical properties."""
    moon = Moon()
    
    assert moon.name == "Moon"
    assert abs(moon.gravity(0) - 1.62) < 0.1  # Surface gravity
    assert moon.equatorial_radius == 1738100.0
    assert abs(moon.flattening - 0.0012) < 1e-10

def test_mars_properties():
    """Test Mars physical properties."""
    mars = Mars()
    
    assert mars.name == "Mars"
    assert abs(mars.gravity(0) - 3.71) < 0.1  # Surface gravity
    assert mars.equatorial_radius == 3396200.0
    assert abs(mars.flattening - 0.00589) < 1e-10

def test_gravity_altitude_scaling():
    """Test that gravity decreases with altitude according to inverse square law."""
    earth = Earth()
    
    g0 = earth.gravity(0)
    g1000 = earth.gravity(1000000)  # 1000 km altitude
    
    # Should decrease by factor of (r/(r+h))^2
    r = earth.equatorial_radius
    expected_ratio = (r / (r + 1000000)) ** 2
    actual_ratio = g1000 / g0
    
    assert abs(actual_ratio - expected_ratio) < 1e-3

def test_earth_j2_gravity():
    """Test Earth's gravity with J2 effects."""
    earth = Earth()
    altitude = 0.0
    
    # Gravity should be stronger at poles than at equator due to J2
    equator_gravity = earth.gravity(altitude, latitude=0.0)
    pole_gravity = earth.gravity(altitude, latitude=np.pi/2)
    
    assert pole_gravity > equator_gravity
    
    # Known values from literature (approximately)
    assert abs(equator_gravity - 9.780) < 0.1  # ~9.78 m/s² at equator
    assert abs(pole_gravity - 9.832) < 0.1     # ~9.83 m/s² at poles

def test_earth_gravity_with_altitude_and_latitude():
    """Test Earth's gravity variation with both altitude and latitude."""
    earth = Earth()
    
    # Test at various altitudes and latitudes
    test_points = [
        (0, 0, 9.78),        # Surface, equator
        (0, np.pi/2, 9.83),  # Surface, pole
        (1000e3, 0, 7.33),   # 1000km, equator
        (1000e3, np.pi/2, 7.37)  # 1000km, pole
    ]
    
    for altitude, latitude, expected_gravity in test_points:
        gravity = earth.gravity(altitude, latitude)
        assert abs(gravity - expected_gravity) < 0.1 

def test_moon_j2_gravity():
    """Test Moon's gravity with J2 effects."""
    moon = Moon()
    altitude = 0.0
    
    # Gravity should be stronger at poles than at equator due to J2
    equator_gravity = moon.gravity(altitude, latitude=0.0)
    pole_gravity = moon.gravity(altitude, latitude=np.pi/2)
    
    assert pole_gravity > equator_gravity
    
    # Known values from literature (approximately)
    assert abs(equator_gravity - 1.62) < 0.01  # m/s² at equator
    assert abs(pole_gravity - 1.622) < 0.01    # m/s² at poles

def test_mars_j2_gravity():
    """Test Mars' gravity with J2 effects."""
    mars = Mars()
    altitude = 0.0
    
    # Gravity should be stronger at poles than at equator due to J2
    equator_gravity = mars.gravity(altitude, latitude=0.0)
    pole_gravity = mars.gravity(altitude, latitude=np.pi/2)
    
    assert pole_gravity > equator_gravity
    
    # Known values from literature (approximately)
    assert abs(equator_gravity - 3.709) < 0.01  # m/s² at equator
    assert abs(pole_gravity - 3.727) < 0.01     # m/s² at poles

def test_gravity_with_altitude_all_bodies():
    """Test gravity variation with altitude for all bodies."""
    bodies = [Earth(), Moon(), Mars()]
    test_altitudes = [0, 100e3, 1000e3]  # 0 km, 100 km, 1000 km
    
    for body in bodies:
        g0 = body.gravity(0)  # surface gravity
        
        for altitude in test_altitudes:
            g = body.gravity(altitude)
            # Gravity should decrease with altitude
            if altitude > 0:
                assert g < g0
                # Test inverse square law approximately
                expected_ratio = (body.equatorial_radius / (body.equatorial_radius + altitude))**2
                actual_ratio = g / g0
                assert abs(actual_ratio - expected_ratio) < 0.1