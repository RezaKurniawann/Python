import datetime

x = datetime.datetime.now()
print ("1.",x)
print ("2.",x.year)
print ("3.",x. strftime ("%A"))
x = datetime.date.today()
print ("4.", x)

# Creating Date Objects
print ("\nCreating Date objects")
x = datetime.datetime(2020, 5, 17)
print ("1.",x)
x = datetime.datetime(2018, 6, 1)
print ("2.",x.strftime("%B"))

print ("\nReference of all the legal format")
now = datetime.datetime(2018, 12, 31, 17, 41, 8, 548513)
formatted_date_time = {
    "%a": now.strftime("%a"),     # Weekday, short version
    "%A": now.strftime("%A"),     # Weekday, full version
    "%w": now.strftime("%w"),     # Weekday as a number 0-6, 0 is Sunday
    "%d": now.strftime("%d"),     # Day of month 01-31
    "%b": now.strftime("%b"),     # Month name, short version
    "%B": now.strftime("%B"),     # Month name, full version
    "%m": now.strftime("%m"),     # Month as a number 01-12
    "%y": now.strftime("%y"),     # Year, short version, without century
    "%Y": now.strftime("%Y"),     # Year, full version
    "%H": now.strftime("%H"),     # Hour 00-23
    "%I": now.strftime("%I"),     # Hour 00-12
    "%p": now.strftime("%p"),     # AM/PM
    "%M": now.strftime("%M"),     # Minute 00-59
    "%S": now.strftime("%S"),     # Second 00-59
    "%f": now.strftime("%f"),     # Microsecond 000000-999999
    "%z": now.strftime("%z"),     # UTC offset
    "%Z": now.strftime("%Z"),     # Timezone
    "%j": now.strftime("%j"),     # Day number of year 001-366
    "%U": now.strftime("%U"),     # Week number of year, Sunday as the first day of week, 00-53
    "%W": now.strftime("%W"),     # Week number of year, Monday as the first day of week, 00-53
    "%c": now.strftime("%c"),     # Local version of date and time
    "%C": now.strftime("%C"),     # Century
    "%x": now.strftime("%x"),     # Local version of date
    "%X": now.strftime("%X"),     # Local version of time
    "%%": now.strftime("%%"),     # A % character
    "%G": now.strftime("%G"),     # ISO 8601 year
    "%u": now.strftime("%u"),     # ISO 8601 weekday (1-7)
    "%V": now.strftime("%V")      # ISO 8601 weeknumber (01-53)
}

# Print hasil format
for key, value in formatted_date_time.items():
    print(f"{key}\t{value}")
