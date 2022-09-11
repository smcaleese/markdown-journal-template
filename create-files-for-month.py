import os
import calendar
import shutil
from datetime import datetime
import sys

'''
Fill a month directory with markdown files for each day of the month.
Each markdown file contains the journal template.

Usage: python3 create-files-for-month.py <month-dir-name> <month-num> <days-in-month> <journal-template>
Example: python3 create-files-for-month.py './journal/January' 1 31 'journal-template.md'
'''

def main():
    args = sys.argv[1:]
    if len(args) != 4:
        print('Error: incorrect number of arguments.')
        sys.exit(1)
    month_dir_name, month_num, num_days, template_file = args[0], int(args[1]), int(args[2]), args[3]
    current_year = datetime.now().year

    with open(template_file, 'r') as template_file:
        template_content = template_file.read()

    for day_num in range(1, num_days + 1):
        file_name = '{:02d}-{:02d}-{:02d}'.format(day_num, month_num, current_year)
        with open(os.path.join(month_dir_name, file_name), 'w') as f:
            f.write(template_content)

if __name__ == '__main__':
    main()