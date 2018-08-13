english = []
spanish = []
chinese = []
arabic = []
hungarian = []
with open('english.txt', 'r',encoding="utf-8") as in_file:
    for line in in_file:
        line = line.strip('\n')
        english.append(line)
        
with open('chinese.txt', 'r',encoding="utf-8") as in_file:
    for line in in_file:
        line = line.strip('\n')
        chinese.append(line)
        
with open('spanish.txt', 'r',encoding="utf-8") as in_file:
    for line in in_file:
        line = line.strip('\n')
        spanish.append(line)
        
with open('arabic.txt', 'r',encoding="utf-8") as in_file:
    for line in in_file:
        line = line.strip('\n')
        arabic.append(line)
        
with open('hungarian.txt', 'r',encoding="utf-8") as in_file:
    for line in in_file:
        line = line.strip('\n')
        hungarian.append(line)
        
x = 0

with open('vocab.txt', 'w', encoding='utf-8') as out_file:
    while x < len(english):
        s = english[x] + "_" + spanish[x] + "_" + chinese[x] + "_" + arabic[x] + "_" + hungarian[x] + "_\n"
        out_file.write(s)
        x = x+1
