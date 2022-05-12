# Djangofier v0.5
# Author: https://github.com/eo-uk
#
# Convert your HTML template to an almost Django-ready template
#  - Replaces static files with the static tag
#  - Replaced href urls with the url tag
#  - Adds loading of tags at the top of the file

import re
import os


STATIC_PATH     = ''
REPLACE_STATICS = True
REPLACE_URLS    = True

path = input('Enter path to .html file:\n')
with open(path, 'r', encoding='utf-8') as file:
    string = ''
    if REPLACE_STATICS:
        string += '{% load static %}\n'
    string += file.read()

#test = '<link rel="stylesheet" href="assets/css/fontawesome.css">'
#test2 = '<img src="assets/images/templatemo-eduwell.png" alt="EduWell Template">'
#test3 = '<a href="contact-us.html">Subscribe Course</a>'
#oldpattern = r"(<link.*href=\")(.*)(\")"

if REPLACE_STATICS:
    pattern = r'(<(?:link|img|script).*(?:href|src)=")((?!https:\/\/).*?)(")'
    string = re.sub(pattern, r"\1{% static '" + STATIC_PATH + r"\2' %}\3", string)

if REPLACE_URLS:
    pattern = r'(<a.*href=")(.*?)(.html)(")'
    string = re.sub(pattern, r"\1{% url '\2' %}\4", string)

filename = 'djangofied_' + os.path.basename(path)
with open(filename, 'w+', encoding='utf-8') as file:
    file.write(string)

print(string)
input()


