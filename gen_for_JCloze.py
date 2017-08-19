#coding: utf-8

file = 'for_jcloze.txt'
with open(file, "rb") as f:
    l_txt = f.readlines()
    #l_txt = txt.split()
    l_res = list()
    for i in range(len(l_txt)):

        line = l_txt[i]
        res = line.strip()
        count = 0
        for j in range(len(line)):
            if line[j] == ' ':
                count = count + 1
            else:
                break
        if int(count/4) > 0:
            #res = r'<p style="text-indent:10%;">' + res + r'</p>' + '\n'
            res = r'<p style="text-indent:' + str(int(count/4)) + r'0%;">' + res + '\n'#+ r'</p>' + '\n'
            l_res.append(res)
            continue
        if not res == '':
            res = res + '\n'
            l_res.append(res)
            continue
        #l_res.append(res)

f = open('res.txt', "wb")
for i in range(len(l_res)):
    f.write(l_res[i].encode('utf-8'))


#print(l_res)

