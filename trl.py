#coding: utf-8

file = "KnowledgeBase backup.trl"

def take_trl(file, n_parent = '0'):
    """
    Function import treeline items
    :param file: 
    :return: 
    """
    d = dict()
    with open(file.decode('utf-8'), "rb") as f:
        text = f.readlines()
        parent = n_parent
        num = 1             # number of element
        tag = ''
        st = False          # if block started
        cl = False          # if was Close tag
        item = ''
        for i in range(len(text)):
        # take name of main tag
            line = text[i]
            #if line == 'Ребенок':
            #    print('some')
            if i == 1:
                tag = take_tag(text[i])     # tag of start block
                continue
            if i > 1:
                if take_tag(text[i]) == tag and st == True:
                    if item:
                        mask = str(parent) + ":" + str(num)
                        d[mask] = item
                    # add level to mask
                    parent = str(parent) + ":" + str(num)
                    num = 1
                    continue
                # if tag == tag -> block is started
                if take_tag(text[i]) == tag:
                    st = True
                    cl = False
                    continue
                # if block started and not closed -> write item and go to new level


                # if block started and tag == 'Name' -> take text for item
                if take_tag_name(text[i]) == 'Name' and st == True:
                    item = take_text(text[i])
                    continue

                # if item empty and block closed -> go to higher level
                if b_close(text[i]) and item == '':
                    parent = parent.rpartition(':')[0]
                    num = find_next(parent, d)
                    continue

                # if block closed -> write to dictionary
                if b_close(text[i]):
                    # form mask
                    mask = str(parent) + ":" + str(num)
                    if d.get(mask):
                        num = num + 1
                    mask = str(parent) + ":" + str(num)

                    #if i == 14:
                    #    print("there")
                    d[mask] = item


                    # empty vars
                    st = False
                    cl = True
                    item = ''
        return d

def append_trl(file):
    d = dict()
    with open(file) as f:
        text = f.readlines()
        parent = ""
        num = 1             # number of element
        tag = ''
        st = False          # if block started
        cl = False          # if was Close tag
        item = ''
        for i in range(len(text)):
        # take name of main tag
            line = text[i]
            if i == 1:
                tag = take_tag(text[i])     # tag of start block
                continue
            if i > 1:
                if take_tag(text[i]) == tag and st == True:
                    if item:
                        mask = parent + ":" + str(num)
                        d[mask] = item
                    # add level to mask
                    parent = parent + ":" + str(num)
                    num = 1
                    continue
                # if tag == tag -> block is started
                if take_tag(text[i]) == tag:
                    st = True
                    cl = False
                    continue
                # if block started and not closed -> write item and go to new level


                # if block started and tag == 'Name' -> take text for item
                if take_tag_name(text[i]) == 'Name' and st == True:
                    item = take_text(text[i])
                    continue

                # if item empty and block closed -> go to higher level
                if b_close(text[i]) and item == '':
                    parent = parent.rpartition(':')[0]
                    num = find_next(parent, d)
                    continue

                # if block closed -> write to dictionary
                if b_close(text[i]):
                    # form mask
                    num = num + 1
                    mask = parent + ":" + str(num)
                    #if i == 14:
                    #    print("there")
                    d[mask] = item


                    # empty vars
                    st = False
                    cl = True
                    item = ''
        return d

def take_tag(line):
    "Take tag of line"
    t_tag = line.split()[0].rpartition('<')[-1]
    return t_tag

def take_tag_name(line):
    "Take tag name of line"
    t_tag = line.split('>')[0].rpartition('<')[-1]
    return t_tag

def take_text(line):
    return (line.split('>')[1]).split('<')[0]

def b_close(line):
    return take_tag(line)[0] == '/'

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

def print_dir(d):
    """
    Print dictionary of data
    :param d: 
    :return: 
    """
    for k, v in d.items():
        print(k + " => " + v)


if __name__ == '__main__':
    d = take_trl(file)
    print_dir(d)