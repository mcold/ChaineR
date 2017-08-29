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
    print(n_parent)
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
            line = text[i].strip().decode('utf-8')
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

def result_gen_tetra(f_file, d):
    root_tag = '<root>\n <format version="1" subversion="2"/>\n'
    close_root_tag = ' </content>\n</root>\n'



    start_tag = '<node>\n'
    close_tag = '</node>\n'
    name_file = (f_file.split(".")[0]).rpartition('\\')[-1]
    first_line = "<?xml version='1.0' encoding='utf-8'?>\n"
    second_line = '<!DOCTYPE mytetradoc>\n'
    #format_line = ' <format subversion="2" version="1"/>\n'
    content_line = '<content>\n'
    #dicsontent_line = '</content>\n'


    # as root take name of file
    root_line = '<Name idref="y" lines="3" type="Text">{0}</Name>\n'.format(name_file)
    mnemo_line = '<mnemo type="Text" />\n'

    parent = '0'

    l_root = take_childs(d, parent)         # take high level of elements '0:1 ...'

    l_root = resort(l_root)

    d_trans = transform_data(d)             # take transformed data-dictionary

    l_res, num = gen_cycle_tags(d, d_trans, l_root)      # list of tags

    with open(f_file.decode('utf-8'), 'wb') as f:
        f.write(first_line)
        f.write(second_line)
        f.write(root_tag)
        #f.write(format_line)
        #f.write(content_line)
        f.write(content_line)
        for i in range(len(l_res)):
            f.write(l_res[i].encode('utf-8'))
        #f.write(dicsontent_line)
        f.write(close_root_tag)

def gen_cycle_tags(d, d_trans, l_elem, num = 1):
    """
    Generate list of tags for write to file trl-format
    :param d: dictionary of program
    :param d_trans: transfromed dictionary
    :param l_elem: list of elements
    :return:
    """
    # typical tags:
    start_tag = '<node>\n'
    close_tag = '</node>\n'

    l_res = list()          # result list of tags
    l_yet = list()          # list of element which used yet
    parent = 0
    #num = 1                 # order the number of elements
    for i in range(len(l_elem)):
        # prove if it is a list
        elem = d_trans[l_elem[i]]
        if type(elem) == list:
            #elem = resort(elem)             # resort elements
            v = d[l_elem[i]]
            #d.pop(l_elem[i])
            text = v[0]
            #mnemo = v[1]

            line_tag = u'<node crypt="0" name="{0}" id="{1}">\n'.format(text, num)
            l_res.append(line_tag)
            num += 1
            l_e, num = gen_cycle_tags(d, d_trans, elem, num)  # result = list of tags
            for j in range(len(l_e)):
                l_res.append(l_e[j])
            l_res.append(close_tag)
        else:
            if not l_elem[i] in l_yet:
                v = d[l_elem[i]]
                l_yet.append(l_elem[i])
                #d.pop(l_elem[i])
                text = v[0]
                mnemo = v[1]

                line_tag = u'<node crypt="0" name="{0}" id="{1}"/>\n'.format(text, num)
                l_res.append(line_tag)
        num += 1             # increase order
    return l_res, num

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
    take_tetra()