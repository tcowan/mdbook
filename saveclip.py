# read the rest of the user guide into an array
restlines = guide.readlines()

header2 = r'^## (.*)'
header3 = r'^### (.*)'

index = 0
level = 0
while index < len(restlines):
# look for a header 2 
    print(f'looking for h2: {restlines[index][:-1]}')
    matchh2 = re.search(header2, restlines[index])
    if matchh2:
        print(f'found h2: {restlines[index][:-1]}')
        name = matchh2.group(1) 
# make name lower case and add .md
        filename = name.lower()
        trans = str.maketrans(" -","&&")
        filename = name.translate(trans)
        filename = filename + '.md'
# open the file for writing
        file = open(os.path.join('doc', filename), 'w')
        print(f'translation of header 2: {name}')
# write the header as a header 1
        file.write(f'# {name}\n')
# go to next line in array        
        index = index + 1
# don't exceed array length
        if index >= len(restlines):
            break
# loop until next header found
        while True:
# open file and write until another header is found
            file.write(f'restlines[index]')
            index = index + 1
            if index >= len(restlines):
                break
        continue

# look for a header 3 
    print(f'looking for h3: {restlines[index][:-1]}')

    matchh3 = re.search(header3, restlines[index])
    if matchh3:
        print(f'found h3: {restlines[index][:-1]}')

        name = matchh3.group(1) 
# make name lower case and add .md
        filename = name.lower()
        trans = str.maketrans(" -","&&")
        filename = name.translate(trans)
        filename = filename + '.md'
# open the file for writing
        print(f'opening {filename}')
        file = open(os.path.join('doc/nested', filename), 'w')
        print(f'translation of header 3: {name}')
        file.close()
        index = index + 1
        continue
# # write the header as a header 2
#         file.write(f'## {name}\n')
# # go to next line in array        
#         index = index + 1
# # don't exceed array length
#         if index >= len(restlines):
#             break
# # loop until next header found
#         while True:
# # open file and write until another header is found
#             file.write(f'restlines[index]')
#             index = index + 1
#             if index >= len(restlines):
#                 break
#         continue
#     index = index + 1
#     if index >= len(restlines):
#         break

# # skip lines ahead of first header
#     continue

    
