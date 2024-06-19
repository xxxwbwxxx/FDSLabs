print("hello world")
import re

def time_clean(t):
    """Clean a string from the survey data to a consistent string format ('%H:%M').
    This function should handle the string cases found in Exercise 02."""
    if isinstance(t, str):  # NaN values will be of type float
        # re.sub replaces the parts of a string matching a pattern with a desired replacement
        t = re.sub(' +', '', t) # Remove spaces in the middle of the string
        t = re.sub('\.', ':', t) # Remove spaces in the middle of the string
        t = re.sub('：', ':', t) # Replace "fullwidth colon" (Unicode character U+FF1A) with standard colon
        t = re.sub('^(\d\d)(\d\d)', '\\1:\\2', t) # 1700 -> 17:00
        t = re.sub('^(\d+)[Aa][Mm]', '\\1:00', t) # 10am -> 10:00
        t = re.sub('^(\d\d)$', '\\1:00', t) # 10 -> 10:00
        if re.match('^([^:]+)[Pp][Mm]', t): # 5pm -> 17:00
            hour = re.sub('^([^:]+)[Pp][Mm]', '\\1', t)
            t = str((int(hour) + 12)) + ":00"
        t = re.sub('[Aa][Mm]', '', t) # 10:00am -> 10:00
        t = re.sub('(\d\d):(\d\d).*', '\\1:\\2', t) # 10:00 plus a long comment -> 10:00
    return(t)