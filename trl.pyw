#coding: utf-8

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
        mnemo = ''
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
                        line = [item, mnemo]
                        d[mask] = line
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
                    item = take_text(text[i]).decode('utf-8')
                    continue

                # if block started and tag == 'Name' -> take text for item
                if take_tag_name(text[i]) == 'mnemo' and st == True:
                    mnemo = take_text(text[i]).decode('utf-8')
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
                    line = [item, mnemo]
                    d[mask] = line


                    # empty vars
                    st = False
                    cl = True
                    item = ''
                    mnemo = ''
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
                v = d[mask]
                text = v[0]
                mnemo = v[1]
                line_tag = '<DEFAULT item="y" uniqueid="{0}">\n'.format(text)
                line_name = '<Name>{0}</Name>\n'.format(text)
                line_mnemo = '<mnemo>{0}</mnemo>\n'.format(mnemo)
                close_tag = '</DEFAULT>\n'

                # write data
                f.write(line_tag)
                f.write(line_name)
                if mnemo:
                    f.write(line_mnemo)

                if b_have_childs(d, mask):
                    parent = str(parent) + ':' + str(num)
                    num = 1
                    continue
                else:
                    f.write(close_tag)
                    # try to find next
                    next = find_next(parent, d)
                    if d.get(next):
                        num = next
                        continue
                    else:
                        f.write(close_tag)
                        # go to higher level
                        try:
                            parent = parent.rpartition(":")[0]
                        except:
                            parent = "0"



def take_childs(d, mask):
    """
    Form list of childs it they are
    Otherwise False
    :param d: 
    :param mask: 
    :return: 
    """
    lev_mask = len(mask.split(":")) + 1
    l_mask = list()
    for k,v in d.items():
        if len(k.split(":")) == lev_mask and k.startswith(mask):
            l_mask.append(k)
    if l_mask:
        return l_mask
    else:
        return False




def transform_data(d, n_parent = 0, num = 1, h_elem = []):
    """
    Transfrom data from trl to data intern structure
    :return: 
    """
    __b_have_next = lambda parent, num: d.get(str(parent) + ":" + str(num+1))
    __b_have_child = lambda parent, num: d.get(str(parent) + ":" + str(num))

    ### 1) form dictionary of father-child

    d_trans = dict()


    for k,v in d.items():
        elem = take_childs(d, k)
        if take_childs(d, k):
            d_trans[k] = elem
        else:
            d_trans[k] = k
    return d_trans

def take_max_branch(d):
    """
    Take number of branch out of range of dictionary
    :param d: 
    :return: 
    """
    pass


def result_gen_trl(f_file, d, num = 1):
    close_tag = '</DEFAULT>\n'
    name_file = (f_file.split(".")[0]).rpartition('\\')[-1]
    first_line = "<?xml version='1.0' encoding='utf-8'?>\n"
    second_line = '<DEFAULT item="y" line0="{*Name*}" line1="{*Name*}" tlversion="2.1.2" uniqueid="id_{0}"' + '"{0}">\n'.format(num)
    # as root take name of file
    root_line = '<Name idref="y" lines="3" type="Text">{0}</Name>\n'.format(name_file)
    mnemo_line = '<mnemo type="Text" />\n'

    parent = '0'

    l_root = take_childs(d, parent)         # take high level of elements '0:1 ...'

    l_root = resort(l_root)

    d_trans = transform_data(d)             # take transformed data-dictionary

    num += 1
    l_res, num = gen_cycle_tags(d, d_trans, l_root, num)      # list of tags

    with open(f_file.decode('utf-8'), 'wb') as f:
        f.write(first_line)
        f.write(second_line)
        f.write(root_line)
        f.write(mnemo_line)
        for i in range(len(l_res)):
            f.write(l_res[i].encode('utf-8'))
        f.write(close_tag)


def resort(l):
    """
    Sort masks of dictionary
    :param l: 
    :return: 
    """
    d_t = dict()
    for i in range(len(l)):
        d_t[int(l[i].split(":")[-1])] = l[i]
    l_res = list()
    for k, v in d_t.items():
        l_res.append([k, v])
        l_res.sort(key=lambda l: l[0])
    l_new = list()
    for j in range(len(l_res)):
        l_new.append(l_res[j][1])
    return l_new



def gen_cycle_tags(d, d_trans, l_elem, num = 1):
    """
    Generate list of tags for write to file trl-format
    :param d: dictionary of program
    :param d_trans: transfromed dictionary
    :param l_elem: list of elements
    :return: 
    """
    # typical tags:
    tag = 'DEFAULT'
    close_tag = '</DEFAULT>\n'


    l_res = list()          # result list of tags
    l_yet = list()          # list of element which used yet
    parent = 0

    for i in range(len(l_elem)):
        # prove if it is a list
        elem = d_trans[l_elem[i]]
        if type(elem) == list:
            num += 1
            #elem = resort(elem)             # resort elements
            v = d[l_elem[i]]
            #d.pop(l_elem[i])
            text = v[0]
            mnemo = v[1]

            line_tag = u'<DEFAULT item="y" uniqueid="id_{0}">\n'.format(num)
            line_name = u'<Name>{0}</Name>\n'.format(text)
            line_mnemo = u'<mnemo>{0}</mnemo>\n'.format(mnemo)
            l_res.append(line_tag)
            l_res.append(line_name)
            l_e, num = gen_cycle_tags(d, d_trans, elem, num)  # result = list of tags
            for j in range(len(l_e)):
                l_res.append(l_e[j])
            l_res.append(close_tag)

        else:
            if not l_elem[i] in l_yet:
                num += 1
                v = d[l_elem[i]]
                l_yet.append(l_elem[i])
                #d.pop(l_elem[i])
                text = v[0]
                mnemo = v[1]

                line_tag = u'<DEFAULT item="y" uniqueid="id_{0}">\n'.format(num)
                line_name = u'<Name>{0}</Name>\n'.format(text)
                line_mnemo = u'<mnemo>{0}</mnemo>\n'.format(mnemo)
                l_res.append(line_tag)
                l_res.append(line_name)
                l_res.append(line_mnemo)
                l_res.append(close_tag)

    return l_res, num

def b_have_childs(d, mask):
    """
    Find childs for current mask
    :param d: dictionary
    :param mask: mask parent-child
    :return: boolean
    """
    for k, v in d.items():
        if k.startswith(mask):
            return True
    return False

def b_have_next(d, parent, num):
    "Define if have next item"
    mask = str(parent) + ":" + str(num+1)
    return d.get(mask)

if __name__ == '__main__':
    pass