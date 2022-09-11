import os
import calendar
import shutil
from datetime import datetime

'''
1. Create a directory named 'journal'.
2. Fill this directory with directories for each month.
3. Fill each month directory with markdown files for each day of the month.
'''

def create_and_enter_dir(name):
    if os.path.exists(name):
        shutil.rmtree(name)
    os.mkdir(name)
    os.chdir(name)

def main():
    current_year = datetime.now().year
    month_names = calendar.month_name[1:]

    with open('journal-template.md', 'r') as template_file:
        template_content = template_file.read()

    create_and_enter_dir('journal')
    create_and_enter_dir(f'{current_year}')

    for month_index, month_name in enumerate(month_names):
        month_dir_name = f'{month_index + 1} {month_name}'
        create_and_enter_dir(month_dir_name)
        days_in_month = calendar.monthrange(current_year, month_index + 1)[1]

        for day_num in range(1, days_in_month + 1):
            file_name = '{:02d}-{:02d}-{:02d}.md'.format(day_num, month_index + 1, current_year)
            with open(file_name, 'w') as f:
                f.write(template_content)
        
        os.chdir('..')

if __name__ == '__main__':
    main()
