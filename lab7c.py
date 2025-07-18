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
    # Corrected f-string formatting for Python 3.6+ [5]
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def time_to_sec ( time_obj ) :
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    # Converts Time object attributes into a total number of seconds [1, 2]
    minutes  =  time_obj . hour  *   60   +  time_obj . minute
    seconds  =  minutes  *   60   +  time_obj . second
    return  seconds

def sec_to_time ( seconds ) :
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    # Converts a total number of seconds back into a Time object [1, 2]
    time  =  Time ( )
    minutes ,  time . second  =   divmod ( seconds ,   60 )
    time . hour ,  time . minute  =   divmod ( minutes , 60 )
    return  time

def sum_times ( t1 , t2 ) :
    """Add two time objects and return the sum using time_to_sec and sec_to_time."""
    # Convert both time objects to seconds, add them, and convert back [4]
    sec1 = time_to_sec(t1)
    sec2 = time_to_sec(t2)
    total_seconds = sec1 + sec2

    # Ensure the total seconds wrap around a 24-hour cycle (86400 seconds in a day)
    total_seconds %= (24 * 60 * 60) # 86400 seconds in a day

    return sec_to_time(total_seconds)

def change_time ( time_obj , seconds ) :
    """
    Modifies a Time object by adding/subtracting a given number of seconds
    using time_to_sec and sec_to_time.
    This is a modifier function.
    """
    # Convert the time object to seconds, add the given seconds, and convert back [4]
    current_seconds = time_to_sec(time_obj)
    new_total_seconds = current_seconds + seconds

    # Ensure the new total seconds wrap around a 24-hour cycle (86400 seconds)
    # Python's % operator handles negative results correctly for wrapping around
    new_total_seconds %= (24 * 60 * 60) # 86400 seconds in a day

    # Convert the new total seconds to a temporary Time object
    nt = sec_to_time(new_total_seconds)

    # Update the attributes of the original time_obj in place
    time_obj.hour = nt.hour
    time_obj.minute = nt.minute
    time_obj.second = nt.second

    return None # Modifier functions typically return None

def valid_time ( t ) :
    """check for the validity of the time object attributes:
    24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t . hour  <   0   or  t . minute  <   0   or  t . second  <   0 :
        return False
    if t . minute  >=   60   or  t . second  >=   60   or  t . hour  >=   24 :
        return False
    return True