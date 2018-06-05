#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 0006 上午 12:00
# @Author  : toby
# @Site    : 
# @File    : generate_html.py
# @Software: PyCharm

import csv ,os


# '''
#     csv to html 转化
# '''

def write_csv_to_html(csvfilepath,htmlfilepath):
    print(os.getcwd())
    # Open the CSV file for reading
    reader = csv.reader(open(csvfilepath))
    # Create the HTML file for output
    htmlfile = open(htmlfilepath, "w")

    rownum = 0
    htmlfile.write("""<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Csv_Html</title>
                    </head>
                    <body>
                    <table border ="1">
                    """)

    for line in reader:
        sig =True
        for each  in line:
            if (('failed' in each ) or ('Exception in' in each)):
                sig = False
        if sig:
            htmlfile.write('<tr bgcolor="#00FF7F">')    #正确是这个颜色
        else:
            htmlfile.write('<tr bgcolor="#8B2323">')  #错误是这个颜色

        for each in line:
            htmlfile.write('<td>'+each+'</td>')

        htmlfile.write('</tr>')

    htmlfile.write("""</table></body>""")




