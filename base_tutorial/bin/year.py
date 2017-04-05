months = [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Sep',
        'Oct',
        'Nov',
        'Dec'
        ]

suffix = ['st', 'nd', 'rd'] + 17 * ['th'] + \
         ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']

year = raw_input("Year: ")
month = raw_input("Month: ")
day = raw_input("Day: ")

mon = months[int(month) - 1]
date = str(int(day))
datestr = mon + " " + date + suffix[int(day) - 1] + " " + year
print datestr
