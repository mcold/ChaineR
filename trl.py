#coding: utf-8

def take_trl(file, n_parent = '0'):
    """
    Function import treeline items
    :param file: 
    :return: 
    """
    d = dict()
    print(n_parent)
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
                        d[mask.decode('utf-8')] = item.decode('utf-8')
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
                    parent = str(parent).rpartition(':')[0]
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
                    d[mask.decode('utf-8')] = item.decode('utf-8')


                    # empty vars
                    st = False
                    cl = True
                    item = ''
            if str(parent)[0] == ':':
                parent = '0' + str(parent)
        print(d)
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
                if parent[0] == ':':
                    parent = '0' + parent
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
        print("l for next = " + str(l))
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


def export_trl(file, d):
    """
    Export to treeline
    :param file:
    :return:
    """
    tag = 'DEFAULT'
    print(d)

    with open(file, 'wb') as f:
        parent = '0'
        num = 1

        close_tag = '</DEFAULT>\n'
        name_file = (file.split(".")[0]).rpartition('\\')[-1]
        # first 3 lines of .trl
        first_line = "<?xml version='1.0' encoding='utf-8'?>\n"
        second_line = '<DEFAULT item="y" line0="{*Name*}" line1="{*Name*}" tlversion="2.1.2" uniqueid=' + '"{0}">\n'.format(name_file)
        # as root take name of file
        root_line = '<Name idref="y" lines="3" type="Text">{0}</Name>\n'.format(name_file)
        mnemo_line = '<mnemo type="Text" />\n'
        # write data
        f.write(first_line)
        f.write(second_line)
        f.write(root_line)
        f.write(mnemo_line)
        for i in range(len(d)):
            mask = str(parent) + ':' + str(num)
            if d.get(mask):
                print("-"*40)
                print(mask)
                #print(d[mask])
                v = d[mask]
                text = v[0]
                mnemo = v[1]
                line_tag = u'<DEFAULT item="y" uniqueid="{0}">\n'.format(text)
                line_name = u'<Name>{0}</Name>\n'.format(text)
                line_mnemo = u'<mnemo>{0}</mnemo>\n'.format(mnemo)
                close_tag = u'</DEFAULT>\n'

                # write data
                f.write(line_tag.encode('utf-8'))
                f.write(line_name.encode('utf-8'))
                if mnemo:
                    f.write(line_mnemo.encode('utf-8'))
                #num += 1
                print("num - " + str(num))
            else:
                print("-" * 40)
                print("I couldn't find " + mask)
                f.write(close_tag)
                try:
                    parent = parent.rpartition(":")[0]
                    i -= 1
                    print("result parent - " + parent)
                except:
                    print("can't rpartition parent - " + str(parent))
                    parent = "0"
                continue

            if b_have_childs(d, mask):
                print("-" * 40)
                print(mask + " have child = " + str(b_have_childs(d, mask)))
                parent = str(parent) + ':' + str(num)
                print("result parent from child - " + str(parent))
                num = 1
                continue
            else:
                print("-" * 40)
                print(mask + " - haven't childs")
                f.write(close_tag)
                # try to find next
                next = num + 1
                print("next - " + str(next))
                new_mask = str(parent) + ":" + str(next)
                print("try to find - " + str(new_mask))
                if d.get(new_mask):
                    #f.write(close_tag)
                    print("-" * 40)
                    print("found - " + str(new_mask))
                    num = next
                    print("num - " + str(num))
                    continue
                else:
                    f.write(close_tag)
                    if i < len(d)-1:
                        f.write(close_tag)
                    # go to higher level
                    # and find next element
                    print("didn't find " + new_mask)
                    try:
                        print("-" * 40)
                        print("try to find new parent for " + str(parent))
                        par = parent.rpartition(":")[0]
                        print('par - ' + str(par))
                        if par == '0':
                            num = int(parent.rpartition(":")[-1]) + 1
                            parent = '0'
                            print("suppose a new num - " + str(num))
                            continue
                        ll = par.rpartition(":")
                        new = int(ll[-1]) + 1                 # take next number
                        parent = ll[0]       # form next number
                        num = new
                        print("new parent - " + str(parent))
                    except:
                        parent = "0"
        #f.write(close_tag)        # close last item
        #f.write(close_tag)        # close root


def b_have_childs(d, mask):
    """
    Find childs for current mask
    :param d: dictionary
    :param mask: mask parent-child
    :return: boolean
    """
    for k, v in d.items():
        if k.startswith(mask) and not k == mask:
            return True
    return False


if __name__ == '__main__':
    d = take_trl(file)
    print_dict(d)