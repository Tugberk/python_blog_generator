# -*- coding: cp1254 -*-

print "this is a general blog generator"

#the overhead and the footer
overhead = '''<!doctype html>
<html>
<head>
<title>%title%</title>
<meta charset="utf-8">
<style type="text/css">
body{margin:40px
auto;max-width:650px;line-height:1.6;font-size:18px;color:#444;padding:0
10px}h1,h2,h3{line-height:1.2}
</style>
</head><body>
'''

footer = '''
</body>
</html>
'''

#########################


print "Master, what is the file name you prefer? Please do not put spaces."
filename = raw_input('input as --> filename.html \n')

print "Master, please give us your text. We are hungry."
textfile = raw_input('input as --> filename.txt \n')

print "What do you want to see as a title?"
title = raw_input('>')


#lets read the textfile and get the text
text_in_file = ""
my_file = open(textfile, 'r')

for line in my_file:
    text_in_file = text_in_file + line

#lets combine everything
my_text = overhead + text_in_file + footer
#print my_text

print title
print filename


#lets create a new file
new_file = open(filename, 'w')
my_text = my_text.replace('%title%', title)
new_file.write(my_text)

