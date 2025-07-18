#!/usr/bin/env python3
class Time :
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__ ( self , hour = 12 , minute = 0 , second = 0 ) :
        """constructor for time object"""
        self . hour  =  hour
        self . minute  =  minute
        self . second  =  second

def format_time ( t ) :
    """Return time object (t) as a formatted string"""
    # The original source [1] had an incorrect f-string format for Python 3.6+
    # The correct way to format with f-string is f'{variable:format_specifier}'
    # The % (t.hour, t.minute, t.second) part is for older string formatting,
    # which is redundant when using an f-string in this manner.
    # This corrected line uses f-string formatting directly for consistency and correctness.
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times ( t1 , t2 ) :
    """Add two time objects and return the sum."""
    sum   =  Time ( 0 , 0 , 0 )
    sum . hour  =  t1 . hour  +  t2 . hour
    sum . minute  =  t1 . minute  +  t2 . minute
    sum . second  =  t1 . second  +  t2 . second

    # Insert Python code here to check for minute and second attribute here, and carry over when necessary [2, 3]
    # Handle seconds carry-over to minutes
    while sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    # Handle minutes carry-over to hours
    while sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    # Handle hours wrapping around (e.g., 25 hours becomes 1 hour)
    while sum.hour >= 24:
        sum.hour -= 24

    return sum

def valid_time ( t ) :
    """check for the validity of the time object attributes:
    24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t . hour  <   0   or  t . minute  <   0   or  t . second  <   0 :
        return False
    if t . minute  >=   60   or  t . second  >=   60   or  t . hour  >=   24 :
        return False
    return True