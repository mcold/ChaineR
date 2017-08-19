#coding: utf-8
import re

f = 'mytetra.xml'

def take_tetra(file=f, n_parent = '0'):
    """
    Import tetra tree
    :param file: 
    :param n_parent: 
    :return: 
    """
    d = dict()
    with open(file.decode('utf-8'), "rb") as f:
        text = f.readlines()
        parent = n_parent
        num = 1             # number of element
        tag = ''
        node = ''           # dir = node
        record = ''         # record
        st = False  # if block started
        ### TODO: take just knowledge
        my_tag = 'knowledge'
        for i in range(len(text)):
            line = text[i].strip()
            d_line = dict()             # dictionary of tags for line

            # form dictionary
            ####
            l = [x[:-2] for x in re.findall(r'\w+="', line)]
            tt = [x.rsplit('"')[-1] for x in line.split('" ')]
            try:
                tt[-1] = line.split('"')[-2]                        # rewrite last item, cause fail in above method
            except:
                pass
            for w in range(len(l)):
                d_line[l[w]] = tt[w]
            #l = re.findall(r'\w+=".*"', line)
            #try:
            #    for j in range(len(l)):
            #        d_line[l[j].split('=')[0]] = l[j].split('=')[1][1:-1]
            # if mistake -> wrong format
            #except:
            #    continue
                # print(d_line)
                ####

            # take tag
            ####
            tag = take_tag(line)
            if tag == '':
                continue
            ####

            # if tag = node -> new child-level
            if tag == 'node':
                # form mask
                mask = str(parent) + ":" + str(num)
                d[mask] = d_line['name']
                parent = str(parent) + ":" + str(num)
                num = 1



            # if tag = record
            if tag == 'record' and d_line['tags'].find(my_tag) >= 0:# and d_line['tags'] == 'knowledge':
                # form mask
                mask = str(parent) + ":" + str(num)
                d[mask] = d_line['name']

                num += 1

            # if tag closing -> change parent & find next
            try:
                if line.startswith(r'</node>') or (line.startswith(r'<node ') and line.endswith(r'/>')):
                    new_par = parent.rpartition(":")[0]
                    parent = new_par
                    num = find_next(parent, d)
            except:
                pass
            # if recordtable
            #if tag == 'recordtable':
            #    num = 1
                # form new level
            #    parent = str(parent) + ":" + str(num)

            #    num = 1
    return d

def take_tag(line):
    """
    Take tag of line
    """
    try:
        l = re.match(r'<\w+', line)
        return l.group(0)[1:]
    except:
        pass

def take_name(line):
    """
    Take tag of line
    :param line:
    :return:
    """
    t_name = line.split()[0].rpartition('=')[-1][1:-3]
    return t_name

def take_tag_name(line):
    """
    Take tag name of line
    """
    t_tag = line.split('>')[0].rpartition('<')[-1]
    return t_tag

def find_next(parent, d):
    "Find next number of current level"
    l = list()
    for k, v in d.items():
        if len(k.split(":")) == len(parent.split(":"))+1:
            try:
                ll = k.rpartition(":")
                x = int(ll[-1])
                l.append(x)
            except:
                return 1
    if l:
        return max(l)+1
    else:
        return 2

def print_dict(d):
    """
    Print dictionary of data
    :param d:
    :return:
    """
    for k, v in d.items():
        print(k + " => " + v)


if __name__ == '__main__':
    take_tetra()