"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertH1(line):
  if line[:1] == '#':
    return '<h1>'+line[1:]+'</h1>'
  else:
    return line

def convertH2(line):
  if line[:2] == '##':
    return '<h2>'+line[2:]+'</h2>'
  else:
    return line

def convertH3(line):
  if line[:3] == '###':
    return '<h3>'+line[3:]+'</h3>'
  else:
    return line

def block(line, bq):
  if line[0] == '>':
    if bq == False:
      return '<blockquote>'+line[1:]
      
    else:
      return line[1:]
      
  else:
    if bq == True:
      return '</blockquote>'+line
      
    else:
      return line
    
    


bqmode = False
for line in fileinput.input():
  line = line.rstrip() 
  line = convertStrong(line)
  line = convertEm(line)
  # test headings in reverse order
  line = convertH3(line)
  line = convertH2(line)
  line = convertH1(line)
  line = block(line, bqmode)
  if '<blockquote>' in line:
    bqmode = True
  if '</blockquote>' in line:
    bqmode = False
    
  print '<p>' + line + '</p>',