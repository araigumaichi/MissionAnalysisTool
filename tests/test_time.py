"""Tests for the time management module."""

import pytest
from datetime import datetime
from mission_analysis.time import AbsoluteTime

def test_absolute_time_creation():
    """Test creation and basic properties of AbsoluteTime.
    
    This test verifies that:
    - An AbsoluteTime object can be created with a datetime
    - The UTC property returns the correct datetime
    """
    dt = datetime(2024, 3, 19, 12, 0, 0)
    time = AbsoluteTime(dt)
    assert time.utc == dt

def test_julian_date():
    """Test Julian Date conversions.
    
    This test verifies that:
    - Julian Date is correctly calculated from UTC
    - Known reference dates convert to correct Julian Dates
    """
    # Test J2000.0 epoch (2000-01-01 12:00:00 UTC)
    j2000 = AbsoluteTime(datetime(2000, 1, 1, 12, 0, 0))
    assert abs(j2000.julian_date - 2451545.0) < 1e-6
    
    # Test another known date (2024-03-19 12:00:00 UTC)
    dt = AbsoluteTime(datetime(2024, 3, 19, 12, 0, 0))
    assert abs(dt.julian_date - 2460389.0) < 1e-6

def test_modified_julian_date():
    """Test Modified Julian Date conversions.
    
    This test verifies that:
    - Modified Julian Date is correctly calculated from Julian Date
    - MJD = JD - 2400000.5
    """
    # Test J2000.0 epoch
    j2000 = AbsoluteTime(datetime(2000, 1, 1, 12, 0, 0))
    assert abs(j2000.modified_julian_date - 51544.5) < 1e-6
    
    # Test conversion relationship
    dt = AbsoluteTime(datetime(2024, 3, 19, 12, 0, 0))
    assert abs(dt.modified_julian_date - (dt.julian_date - 2400000.5)) < 1e-6 