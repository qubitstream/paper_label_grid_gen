#!/usr/bin/env python3

# Simple script for generating a grid on a paper.
# Useful for printing labels
#
# Written by: Christoph Haunschmidt 2019
# License: GNU GPL 2.0

__version__ = '2019-01-04.01'

import argparse
import os
import sys

import reportlab.lib.pagesizes
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm

# from reportlab.lib.pagesizes:
PAPER_CHOICES = 'A0 A1 A2 A3 A4 A5 A6 B0 B1 B2 B3 B4 B5 B6 LETTER LEGAL ELEVENSEVENTEEN'.split()


class Page:
    def __init__(self, pdf_file, rows, columns, pagesize='A4', padding=2.5, strokegray=50, overwrite=False):
        self.page_padding = padding * cm
        self.pdf_file = pdf_file

        self.pagesize = getattr(reportlab.lib.pagesizes, pagesize.upper())
        self.canvas = canvas.Canvas(self.pdf_file, pagesize=self.pagesize)
        self.width, self.height = self.pagesize
        self.usable_width = self.width - 2 * self.page_padding
        self.usable_height = self.height - 2 * self.page_padding
        self.rows, self.columns = rows, columns

        self.strokegray = strokegray / 100

        self.canvas.setAuthor(__file__)
        self.canvas.setTitle('{0.columns}x{0.rows} grid on {1} paper, padding: {2:.02f} inch'.format(
            self, pagesize, self.page_padding))

        self.generate_grid()

    def generate_grid(self):
        xdata = [self.page_padding + i * self.usable_width / self.columns for i in range(self.columns + 1)]
        ydata = [self.page_padding + i * self.usable_height / self.rows for i in range(self.rows + 1)]
        self.canvas.setStrokeGray(self.strokegray)
        self.canvas.setDash(1, 2)
        self.canvas.grid(xdata, ydata)

    def save(self):
        self.canvas.save()


if __name__ == '__main__':
    # argument parsing
    parser = argparse.ArgumentParser(description='Simple script for generating a grid on a paper (for labels)',
                                     epilog='Written by Christoph Haunschmidt, Version %s' % __version__)

    parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=__version__))

    parser.add_argument('pdf_file',  help='generated PDF file name')

    parser.add_argument('--rows', type=int, default=8, help='number of desired rows per page, default: %(default)s')

    parser.add_argument('--columns', type=int, default=2,
                        help='number of desired columns per page, default: %(default)s')

    parser.add_argument('--strokegray', metavar='PERCENT', type=int, default=50,
                        help='stroke gray (0=black, 100=white), default: %(default)s')

    parser.add_argument('--overwrite', '-y', action='store_true', help='overwrite existing output file')

    parser.add_argument('--pagesize', '-p', choices=PAPER_CHOICES,
                        default='A4', help='paper size, default: %(default)s')

    parser.add_argument('--padding', type=float, default=2.5, help='paper padding in cm, default: %(default)s')

    args = parser.parse_args()

    # check if given inputs are correct
    invalid_inputs = []
    if os.path.isfile(args.pdf_file) and not args.overwrite:
        invalid_inputs.append('File already exists: {0.pdf_file}'.format(args))
    if not args.rows > 0 or not args.columns > 0:
        invalid_inputs.append('Invalid grid size: {0.columns}x{0.rows}'.format(args))
    if not 0 <= args.strokegray <= 100:
        invalid_inputs.append('Stroke gray color must be a valid percentage: {0.strokegray}'.format(args))

    if invalid_inputs:
        print('\n'.join(invalid_inputs), file=sys.stderr)
        sys.exit(1)

    page = Page(**vars(args))
    page.save()
