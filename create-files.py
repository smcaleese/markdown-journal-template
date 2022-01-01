import os
import calendar
import shutil
from datetime import datetime

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
        create_and_enter_dir('{} {}'.format(month_index + 1, month_name))
        days_in_month = calendar.monthrange(current_year, month_index + 1)[1]

        for day_num in range(1, days_in_month + 1):
            file_name = '{0:02d}-{1:02d}-{2:02d}.md'.format(day_num, month_index + 1, current_year)
            with open(file_name, 'w') as f:
                f.write(template_content)
        
        os.chdir('..')

if __name__ == '__main__':
    main()
