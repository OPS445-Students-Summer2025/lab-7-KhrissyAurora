#!/usr/bin/env python3
# Student ID: [seneca_id]
class Time :
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    function attributes: __init__, __str__, __repr__
    time_to_sec, format_time,
    change_time, sum_time
    """
    def __init__ ( self , hour = 12 , minute = 0 , second = 0 ) :
        """constructor for time object"""
        self . hour  =  hour
        self . minute  =  minute
        self . second  =  second

    def __str__ ( self ) :
        '''return a string representation for the object self'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__ ( self ) :
        '''return a string representation for the object self
        just instead of ':', you are required use the '.' in the formatting string.'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}' # Note the '.' here

    def format_time ( self ) :
        """Return time object (t) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec ( self ) :
        '''convert a time object to a single integer representing the number of seconds from mid-night'''
        minutes  =  self . hour  *   60   +  self . minute
        seconds  =  minutes  *   60   +  self . second
        return  seconds

    def sum_times ( self ,  t2 ) :
        """Add two time objects and return the sum using time_to_sec and sec_to_time."""
        # Convert both time objects to seconds, add them, and convert back
        sec1 = self.time_to_sec()
        sec2 = t2.time_to_sec()
        total_seconds = sec1 + sec2

        # Ensure the total seconds wrap around a 24-hour cycle (86400 seconds in a day)
        total_seconds %= (24 * 60 * 60) # 86400 seconds in a day

        return sec_to_time(total_seconds)

    def change_time ( self ,  seconds ) :
        """
        Modifies a Time object by adding/subtracting a given number of seconds
        using time_to_sec and sec_to_time.
        This is a modifier function.
        """
        time_seconds  =  self . time_to_sec ( )
        nt  =  sec_to_time ( (time_seconds  +  seconds) % (24 * 60 * 60) ) # Apply modulo here for wrapping
        self . hour ,  self . minute ,  self . second  =  nt . hour ,  nt . minute ,  nt . second
        return   None

    def valid_time ( self ) :
        """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
        if  self . hour  <   0   or  self . minute  <   0   or  self . second  <   0 :
            return False
        if  self . minute  >=   60   or  self . second  >=   60   or  self . hour  >=   24 :
            return False
        return True

# This function remains outside the class block as per the instructions
def sec_to_time ( seconds ) :
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time  =  Time ( )
    minutes ,  time . second  =   divmod ( seconds ,   60 )
    time . hour ,  time . minute  =   divmod ( minutes , 60 )
    return  time