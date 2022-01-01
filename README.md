# Markdown Journal Template

## Description

This project contains a script which creates a markdown journal template for the current year by creating a markdown file for every day of the year and copying a markdown template into each file.

A Python script named `create-files.py` creates the directories and files and copies the markdown template from `journal-template.md` into each file.

In the same directory as this README, the script creates a directory named `journal` with the following format:

- journal
    - 2022
        - 1 January
            - 01-01-2022.md
            - 02-01-2022.md
            - 03-01-2022.md
            - etc.
        - 2 February
        - 3 March
        - etc.

Current title format for each month directory: `MONTH_NUM MONTH_NAME` (eg. `1 January`).

Current title format for each markdown file created: `DD-MM-YYYY` (eg. `15-01-2022.md`).

Note: the script detects the current year.

## Setup Steps

1. Clone this repository.
2. Type out the markdown template you want for every day of the year in `journal-template.md`.
3. Create the journal directory and files by running the `create-files.py` script with the command `python3 create-files.py`.

Then you can use the journal by typing your journal entries as markdown into the files using a markdown editor such as Typora.

The files can be kept secure by backing them up in the cloud (eg. in Google drive) or in a git repository.

Feel free to modify:
- the journal template
- the current year used
- the title formats of the month directories or markdown files
- anything else
