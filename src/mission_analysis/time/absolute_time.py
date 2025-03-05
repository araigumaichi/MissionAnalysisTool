"""Time management implementation.

This module provides classes and functions for handling time in space mission analysis.
"""

from datetime import datetime, timedelta
import numpy as np

class AbsoluteTime:
    """Handles absolute time representation for mission analysis.
    
    This class manages simulation time, providing conversions between different
    time representations used in space mission analysis.
    
    Parameters
    ----------
    time : datetime
        UTC datetime object representing the absolute time
    
    Attributes
    ----------
    utc : datetime
        The UTC datetime representation
    julian_date : float
        The Julian Date representation
    modified_julian_date : float
        The Modified Julian Date representation
    
    Notes
    -----
    Supports conversions between:
    - UTC datetime
    - Julian Date
    - Modified Julian Date
    - GPS time
    
    References
    ----------
    .. [1] Vallado, D. A., "Fundamentals of Astrodynamics and Applications", 
           4th ed., 2013. pp. 182-187.
    """
    
    # Reference epoch for Julian Date calculations
    _JULIAN_EPOCH = datetime(1858, 11, 17, 0, 0, 0)  # MJD epoch
    _SECONDS_PER_DAY = 86400.0
    
    def __init__(self, time: datetime):
        """
        Initialize AbsoluteTime.
        
        Args:
            time: UTC datetime object
        """
        self._time = time
        
    @property
    def utc(self) -> datetime:
        """UTC datetime representation.
        
        Returns
        -------
        datetime
            The stored UTC time
        """
        return self._time 
    
    @property
    def julian_date(self) -> float:
        """Julian Date representation.
        
        Returns
        -------
        float
            The Julian Date corresponding to the UTC time
        
        Notes
        -----
        The Julian Date is the number of days elapsed since 
        January 1, 4713 BCE at 12:00 UT
        """
        delta = self._time - self._JULIAN_EPOCH
        return 2400000.5 + delta.days + delta.seconds / self._SECONDS_PER_DAY
    
    @property
    def modified_julian_date(self) -> float:
        """Modified Julian Date representation.
        
        Returns
        -------
        float
            The Modified Julian Date (JD - 2400000.5)
        
        Notes
        -----
        The Modified Julian Date is defined as JD - 2400000.5,
        which makes it start at midnight rather than noon
        """
        return self.julian_date - 2400000.5