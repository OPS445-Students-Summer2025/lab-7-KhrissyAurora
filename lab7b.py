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
    # Uses f-string formatting, corrected from the original source for Python 3.6+
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times ( t1 , t2 ) :
    """Add two time objects and return the sum."""
    sum   =  Time ( 0 , 0 , 0 )
    sum . hour  =  t1 . hour  +  t2 . hour
    sum . minute  =  t1 . minute  +  t2 . minute
    sum . second  =  t1 . second  +  t2 . second

    # Logic to carry over seconds to minutes (as fixed for lab7a)
    while sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    # Logic to carry over minutes to hours (as fixed for lab7a)
    while sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    # Logic to wrap hours around a 24-hour cycle (as fixed for lab7a)
    while sum.hour >= 24:
        sum.hour -= 24

    return sum

def change_time ( time_obj , seconds ) :
    """
    Modifies a Time object by adding/subtracting a given number of seconds.
    Handles carry-overs and borrows for seconds, minutes, and hours.
    This is a modifier function, as it changes the passed object directly [4].
    """
    time_obj.second += seconds

    # Handle seconds carry-over (for positive `seconds`)
    while time_obj.second >= 60:
        time_obj.second -= 60
        time_obj.minute += 1
    # Handle seconds borrowing (for negative `seconds`), as required by the lab [3]
    while time_obj.second < 0:
        time_obj.second += 60
        time_obj.minute -= 1

    # Handle minutes carry-over (for positive adjustments)
    while time_obj.minute >= 60:
        time_obj.minute -= 60
        time_obj.hour += 1
    # Handle minutes borrowing (for negative adjustments), as required by the lab [3]
    while time_obj.minute < 0:
        time_obj.minute += 60
        time_obj.hour -= 1

    # Handle hours wrapping around (both positive and negative)
    while time_obj.hour >= 24:
        time_obj.hour -= 24
    while time_obj.hour < 0:
        time_obj.hour += 24

    return None # Modifier functions typically return None [1]

def valid_time ( t ) :
    """check for the validity of the time object attributes:
    24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t . hour  <   0   or  t . minute  <   0   or  t . second  <   0 :
        return False
    if t . minute  >=   60   or  t . second  >=   60   or  t . hour  >=   24 :
        return False
    return True