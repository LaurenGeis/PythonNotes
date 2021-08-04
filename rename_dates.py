#! python3
#rename_dates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re                   # shutil.move() renames files, takes 2 arguments

# Create a regex that matches files with the American date format:
date_pattern = re.compile(r"""^(.*?)    # all the text before the date, re.compile() used to create regex object
    ((0|1)?\d)-                         # one or 2 digits for the month 
    ((0|1|2|3)?\d)-                     # one or 2 digits for the day
    ((19|20)\d\d)                       # 4 digits for the year
    (.*?)$                              # all of the text after the date
    """, re.VERBOSE)                    # passing re.VERBOUS for the second argument



#TODO: Loop over the files in the working directory

for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

#TODO: Skip files without a date
    # this should skip any files w/o dates
    if mo == None:
        continue

#TODO: Get different parts of the filename
    # this gets parts of the filename and separates into groups
    before_part = mo.group(1)
    month_part  = mo.group(2)
    day_part    = mo.group(4)
    year_part   = mo.group(6)
    after_part  = mo.group(8)

#TODO: Form the European style filename

euro_filename = before_part + day_part + '-' + month_part + '-' + year_part +
            after_part

#TODO: Get the full, absolute file paths

abs_working_dir = os.path.abspath('.')
amer_filename = os.path.join(abs_working_dir, amer_filename)
euro_filename = os.path.join(abs_working_dir, euro_filename)

#TODO: Rename the files

print(f'Renaming "{amer_filename}" to "{euro_filename}"...')
#shutil.move (amer_filename, euro_filename      # uncomment after testing.