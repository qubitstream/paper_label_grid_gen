# Paper label grid generator

A simple generator for label grids useful for printing.
The output file will be a PDF with the desired grid on it.

Fabulous ASCII illustration - a page with 2x4 grid (4 rows, 2 columns):

    +-------------------+
    |                   | <---------+
    |  +-------------+  |           |
    |  |      |      |  |           +
    |  +-------------+  |        pagesize
    |  |      |      |  |
    |  +-------------+  |
    |  |      |      |  |
    |  +-------------+  |
    |  |      |      |  |
    |  +-------------+  | <---+
    |                   |     | padding
    +-------------------+ <---+
                    ^  ^
                    |  |
                    +--+
                   padding


## Installation

 - tested with Python 3.6, should work on any Python 3 installation
 - needs the [ReportLab PDF library](https://www.reportlab.com/opensource/): Install it via `pip3 install reportlab`
   or your OS installation facilities

## Help

    $ python paper_label_grid_gen.py --help
    usage: paper_label_grid_gen.py [-h] [--version] [--rows ROWS]
                                [--columns COLUMNS] [--strokegray PERCENT]
                                [--overwrite]
                                [--pagesize {A0,A1,A2,A3,A4,A5,A6,B0,B1,B2,B3,B4,B5,B6,LETTER,LEGAL,ELEVENSEVENTEEN}]
                                [--padding PADDING]
                                pdf_file

    Simple script for generating a grid on a paper (for labels)

    positional arguments:
    pdf_file              generated PDF file name

    optional arguments:
    -h, --help            show this help message and exit
    --version             show program's version number and exit
    --rows ROWS           number of desired rows per page, default: 8
    --columns COLUMNS     number of desired columns per page, default: 2
    --strokegray PERCENT  stroke gray (0=black, 100=white), default: 50
    --overwrite, -y       overwrite existing output file
    --pagesize {A0,A1,A2,A3,A4,A5,A6,B0,B1,B2,B3,B4,B5,B6,LETTER,LEGAL,ELEVENSEVENTEEN}, -p {A0,A1,A2,A3,A4,A5,A6,B0,B1,B2,B3,B4,B5,B6,LETTER,LEGAL,ELEVENSEVENTEEN}
                            paper size, default: A4
    --padding PADDING     paper padding in cm, default: 2.5

    Written by Christoph Haunschmidt, Version 2019-01-04.01


## Usage Example

Defaults: 2x8 grid on A4 with 2.5cm padding and 50% gray colored grid

    python paper_label_grid_gen.py grid_example_1.pdf

Custom: 3x5 grid on LETTER paper with 2cm padding and 70% white colored grid, overwriting an existing file

    python paper_label_grid_gen.py grid_example_2.pdf --rows=5 --columns=3 --strokegray=70 --padding=2 --pagesize=LETTER --overwrite

## Credits

Written by Christoph Haunschmidt

License: GNU GPL 2.0
