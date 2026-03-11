#!/usr/bin/env python3

import re
import sys
import os

def findSection(document, section):
    begin = 0
    print(f'looking for a section starting with {section}')
    for index, sect in enumerate(document):
# if begin is not zero, we found our section. 
# Find the next section boundary or the end of the list
        if begin != 0:
# not at a section boundary.  Keep looking.
            if sect[:2] != '##':
                continue
# we have found a section boundary and our fragment.  Back up one line
#   and return fragment
            end = index
            print(f'found fragment: {section} at B={begin} E={end}')
            return document[begin:end]

# if begin is zero, we haven't found our section yet
        if begin == 0:
# look for a match, if so, set begin and keep looking
            if sect[:len(section)] == section:
                begin = index + 1
                continue
# end of the for loop
    if begin != 0:
        print(f'found the beginning of {section} at the end of the document')
        return document[begin:]
# we are here because begin is zero and we ran off the end of the list
#   otherwise we would have exited the function when we found a boundary
    print(f'cannot find {section} in document')
    return None

#############################################################

# open the user guide
try:
    guide = open('user-guide.md', 'r')
    guidelines = guide.readlines()
    guide.close()
    guide = open('user-guide.md', 'r')
except:
    print('Error opening user-guide.md')

# create the src and src/nested folders
nested_path = "src/nested"
os.makedirs(nested_path, exist_ok=True)

# open the summary file and write the header
try:
    summary = open('SUMMARY.md', 'w')
except:
    print("The summary file had an error in opening")
summary.write("# Summary\n")
summary.write('''[Introduction](README.md)\n''')

# loop until end of table of contents looking for levels
level1 =   r'^- \[(.*)\]\(#(.+)\)'
level2 = r'^  - \[(.*)\]\(#(.+)\)'


guideline = ''
linecount = 0
while guideline[0:18] != '## Getting Started':
    guideline = guide.readline().rstrip()
    # if guideline == '':
    #     print('EOF on user guide')
    #     break
    linecount = linecount + 1
#   print(str(linecount)+' '+guideline)
    match = re.search(level1, guideline)
#   if level 1 write the summary line with file name
    if match:
        title = match.group(1)
        filename = match.group(2)+'.md'
#       print('found a match at level 1')
        fragment = findSection(guidelines, f'## {title}\n')
        if fragment is None:
            print(f'cannot find ## {title}. {filename} will be empty')
            continue
# if fragment consists of empty lines, write only a H1 header to summary.md
#   else write the fragment
        is_empty = True
        for line in fragment:
            if not line.isspace():
                is_empty = False
        if is_empty:
            summary.write(f'''# {title}\n''')
        else:
            summary.write(f'''- [{title}]({filename})\n''')
# open the .md file for output
        file = open(os.path.join('src', filename),'w')
        file.write(f'''# {title}\n''')
        for line in fragment:
            file.write(line)
        file.write('\n')
        file.close()
        continue
    match2 = re.search(level2, guideline)
#   if level 2 write the summary line with file name
    if match2:
        title = match2.group(1)
        filename = match2.group(2)+'.md'
#   print('found a match at level 2')
        summary.write(f'''    - [{title}](nested/{filename})\n''')
        # open the .md file and create an empty file
        file = open(os.path.join('src/nested', filename),'w')
        fragment = findSection(guidelines, f'### {title}\n')
        if fragment is None:
            print(f'cannot find ### {title}. {filename} will be empty')
            continue
        file.write(f'''# {title}\n''')
        for line in fragment:
            file.write(line)
        file.write('\n')
        file.close()
        continue
    
# error
    print(f'not level 1 or 2: {guideline}')
    continue
summary.close()
