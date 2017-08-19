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
            line = text[i]
            d_line = dict()             # dictionary of tags for line

            # form dictionary
            ####
            l = re.findall(r'\w+="\w+"', line)
            try:
                for j in range(len(l)):
                    d_line[l[j].split('=')[0]] = l[j].split('=')[1][1:-1]
            # if mistake -> wrong format
            except:
                continue
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
                mask = str(parent) + ":" + num
                d[mask] = d_line['name']

                num += 1



            # if tag = record
            if tag == 'record':
                # form mask
                mask = str(parent) + ":" + num
                d[mask] = d_line['name']

                num += 1

            # if tag closing -> change parent & find next
            if tag[0] == r'//':
                new_par = parent.rpartition(":")[0]
                parent = new_par
                num = find_next(parent, d)

            # if recordtable
            if tag == 'recordtable':
                # form new level
                parent = str(parent) + ":" + num

                num = 1
    print(d)

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