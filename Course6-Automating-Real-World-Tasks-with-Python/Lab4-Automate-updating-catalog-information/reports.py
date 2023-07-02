

#!/usr/bin/env python3

import reportlab

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate(filename, title, body_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  #table_style = [('GRID', (0,0), (-1,-1), 1, colors.white)]
  #report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  report_body = Paragraph(body_data, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_body])
