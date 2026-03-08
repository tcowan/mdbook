import re
import sys
import os

level1 = r"^- \[(title)\] \(#(filename)$)"
level2 = r"^  - \[(title)\] \(#(filename)$)"
# open the toc file
try:
    with open('toc.txt', 'r') as toc:
        tocline = file.readline() # Reads the entire file content as a string
except FileNotFoundError:
    print("The TOC file was not found.")

# create the doc and doc/nested folders
nested_path = "doc/nested"
os.makedirs(nested_path, exist_ok=True)

# loop
while True:
#   read a line from toc
try:
    tocline = toc.readline()
    if not tocline:
        break
#   parse into title and filename
    match = re.search(level1, tocline)
#   if level 1:
    if match:
#   add .md to filename to create newfilename
    filename = filename + ".md"
#     open book as book
        try:
            open("user-guide.md") as book
#     open output doc/newfilename as outfile
            open(os.path.join("doc", newfilename))
#     read book until a title found
            while True:
            bookline = book.readline()
#     if eof:
            if not bookline:
                break
            if bookline[0] == '#':
                break
#       write newtitle to outfile
            outfile.write(bookline)
#           close book and outfile
            book.close()
            outfile.close()
#   if level 2:
#     open book as book
#     open output doc/nested/newfilename as outfile
#     loop
#       read book
#       if level 1 or level 2 or eof
#         close book
#       writre to outfile
#     end loop
# end loop
# close toc filename


