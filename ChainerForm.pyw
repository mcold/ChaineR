# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 28 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):
    def __init__(self, parent):

        self.file = ""
        self.txt = ""


        # data
        #self.prev = 0
        self.n = 1  # n-number of record
        ### TODO: make something with self.n_parent in functions next-previous
        self.n_parent = 0
        #self.nextus = 2
        self.d = dict() # data dictionary
        self.item = ""  # name of item
        self.mnemo = "" # mnemo of item



        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Chainer", pos=wx.DefaultPosition, size=wx.Size(591,275),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        wxSizer = wx.WrapSizer(wx.HORIZONTAL)

        filterSizer = wx.GridSizer(0, 2, 0, 0)

        self.m_Filter = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        filterSizer.Add(self.m_Filter, 0, wx.ALL, 5)

        wxSizer.Add(filterSizer, 1, wx.EXPAND, 5)

        # wxSizer.AddSpacer(0)
        upSizer = wx.FlexGridSizer(0, 2, 0, 0)
        upSizer.Add(wx.Size(220, 0))

        self.upBtn = wx.Button(self, wx.ID_ANY, u"^", wx.DefaultPosition, wx.Size(100, -1), 0)
        upSizer.Add(self.upBtn, 0, wx.ALL, 5)

        wxSizer.Add(upSizer, 1, wx.EXPAND, 5)

        middleSizer = wx.GridSizer(0, 2, 0, 0)

        leftSizer = wx.FlexGridSizer(0, 2, 0, 0)
        leftSizer.SetFlexibleDirection(wx.BOTH)
        leftSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        leftSizer.AddSpacer(0)

        self.first_main = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(175, -1), 0)
        self.first_main.Wrap(-1)
        leftSizer.Add(self.first_main, 0, wx.ALL, 5)

        self.leftBtn = wx.Button(self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0)
        leftSizer.Add(self.leftBtn, 0, wx.ALL, 5)

        self.second_main_text = wx.TextCtrl(self, 1, wx.EmptyString, wx.DefaultPosition, wx.Size(175, -1), 0)
        leftSizer.Add(self.second_main_text, 0, wx.ALL, 5)

        leftSizer.AddSpacer(0)

        self.third_main = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(175, -1), 0)
        self.third_main.Wrap(-1)
        leftSizer.Add(self.third_main, 0, wx.ALL, 5)

        middleSizer.Add(leftSizer, 1, wx.EXPAND, 5)

        rightSizer = wx.FlexGridSizer(0, 2, 0, 0)
        rightSizer.SetFlexibleDirection(wx.BOTH)
        rightSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.first_mnemo = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(175, -1), 0)
        self.first_mnemo.Wrap(-1)
        rightSizer.Add(self.first_mnemo, 0, wx.ALL, 5)

        rightSizer.AddSpacer(1)

        self.second_mnemo_text = wx.TextCtrl(self, 2, wx.EmptyString, wx.DefaultPosition, wx.Size(175, -1), 0)
        rightSizer.Add(self.second_mnemo_text, 0, wx.ALL, 5)

        self.rightBtn = wx.Button(self, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0)
        rightSizer.Add(self.rightBtn, 0, wx.ALL, 5)

        self.third_mnemo = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.Point(10, 10), wx.Size(175, -1), 0)
        self.third_mnemo.Wrap(-1)
        rightSizer.Add(self.third_mnemo, 0, wx.ALL, 5)

        middleSizer.Add(rightSizer, 1, wx.EXPAND, 5)

        wxSizer.Add(middleSizer, 1, wx.EXPAND, 5)

        downSizer = wx.FlexGridSizer(0, 2, 0, 0)


        downSizer.Add(wx.Size(220, 0))

        self.down_Btn = wx.Button(self, wx.ID_ANY, u"v", wx.DefaultPosition, wx.Size(100, -1), 0)
        downSizer.Add(self.down_Btn, 0, wx.ALL, 5)

        self.m_Mnemo = wx.CheckBox(self, wx.ID_ANY, u"Mnemo", wx.DefaultPosition, wx.DefaultSize, 0)
        downSizer.Add(self.m_Mnemo, 0, wx.ALL, 5)

        wxSizer.Add(downSizer, 1, wx.EXPAND, 5)

        self.SetSizer(wxSizer)
        self.Layout()
        self.menuBar = wx.MenuBar(0)
        self.m_File = wx.Menu()
        self.m_New = wx.MenuItem(self.m_File, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_New)

        self.m_Open = wx.MenuItem(self.m_File, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL)

        self.m_File.Append(self.m_Open)

        self.m_Save = wx.MenuItem(self.m_File, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_Save)

        self.m_SaveAs = wx.MenuItem(self.m_File, wx.ID_ANY, u"SaveAs", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_SaveAs)

        self.m_File.AppendSeparator()

        self.m_Exit = wx.MenuItem(self.m_File, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_Exit)

        self.menuBar.Append(self.m_File, u"File")


        self.Tree = wx.Menu()

        self.m_AppendBranch = wx.MenuItem(self.Tree, wx.ID_ANY, u"Append Branch", wx.EmptyString, wx.ITEM_NORMAL)
        self.Tree.Append(self.m_AppendBranch)
        self.m_DeleteBranch = wx.MenuItem(self.Tree, wx.ID_ANY, u"Delete Branch", wx.EmptyString, wx.ITEM_NORMAL)
        self.Tree.Append(self.m_DeleteBranch)
        self.m_DeleteItem = wx.MenuItem(self.Tree, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL)
        self.Tree.Append(self.m_DeleteItem)
        self.m_InsertItem = wx.MenuItem(self.Tree, wx.ID_ANY, u"Insert", wx.EmptyString, wx.ITEM_NORMAL)
        self.Tree.Append(self.m_InsertItem)

        self.menuBar.Append(self.Tree, "Tree")
        self.SetMenuBar(self.menuBar)

        self.m_Options = wx.Menu()
        self.m_Configuration= wx.MenuItem(self.m_Options, wx.ID_ANY, u"Configuration", wx.EmptyString,
                                               wx.ITEM_NORMAL)
        self.m_Options.Append(self.m_Configuration)
        ### TODO: option - open last file
        ### TODO: in menu file show last files
        self.menuBar.Append(self.m_Options, "Options")

        self.m_About = wx.Menu()
        self.m_About_Description = wx.MenuItem(self.m_About, wx.ID_ANY, u"About program", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_About.Append(self.m_About_Description)
        self.menuBar.Append(self.m_About, "About")
        # aboutItem = self.menuBar.Append(self.m_About, u"About")

        self.Centre(wx.BOTH)

        #Binding

        self.Bind(wx.EVT_MENU, self.CloseWin, self.m_Exit)
        self.Bind(wx.EVT_MENU, self.NewFile, self.m_New)
        self.Bind(wx.EVT_MENU, self.Save, self.m_Save)
        self.Bind(wx.EVT_MENU, self.SaveAs, self.m_SaveAs)
        self.Bind(wx.EVT_MENU, self.OpenFile, self.m_Open)

        self.Bind(wx.EVT_MENU, self.delete_branch, self.m_DeleteBranch)
        self.Bind(wx.EVT_MENU, self.insert_branch, self.m_AppendBranch)
        self.Bind(wx.EVT_MENU, self.insert_item, self.m_InsertItem)
        self.Bind(wx.EVT_MENU, self.delete_item, self.m_DeleteItem)

        self.Bind(wx.EVT_BUTTON, self.next_item, self.down_Btn)
        self.Bind(wx.EVT_BUTTON, self.prev_item, self.upBtn)
        self.Bind(wx.EVT_BUTTON, self.child_item, self.rightBtn)
        self.Bind(wx.EVT_BUTTON, self.parent_item, self.leftBtn)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)

        # Connect Enter Events
        self.m_Filter.Bind(wx.EVT_TEXT_ENTER, self.find_item)
        self.second_main_text.Bind(wx.EVT_TEXT_ENTER, self.next_item)
        self.second_mnemo_text.Bind(wx.EVT_TEXT_ENTER, self.next_item)

        self.m_Mnemo.Bind(wx.EVT_KEY_DOWN, self.set_value)

        #s = u"Test"
        #self.first_main.SetLabelText(s)
        #self.third_main.SetLabelText(s)
        #self.first_mnemo.SetLabelText(s)
        #self.third_mnemo.SetLabelText(s)
        # Key Down & Up
        #self.second_main_text.Bind(wx.EVT_KEY_DOWN, self.next_item)

        # Load file by default
        self.LoadFile()

        # set arrows
        self.set_arrows()


    def __del__(self):
        pass

    def Message(self, e=0):
        wx.MessageBox("Hello people!!!", "wxApp")
        return True

    def OpenFile_First(self, e=0):
        """
        Open choosen file
        :param e: 
        :return: 
        """
        with open(self.file, "rb") as f:
            txt = f.readlines()
            # txt = txt.split('\n')
            d = dict()
            for i in range(len(txt)):
                # split line
                l = txt[i].split('\t')
                k = l[0]
                # summon data for dict
                l_val = list()
                l_val.append(l[1].strip())
                l_val.append(l[2].strip())
                d[k] = l_val
            self.d = d


        k = self.find_minimal()
        self.n = 1
        self.n_parent = k.rpartition(':')[0]
        self.set_value(self.n_parent, self.n)

        # Raname Title of window
        self.SetTitle("Chainer - {0}".format(self.file))

    def OpenFile(self, e=0):
        """
        Open choosen file
        :param e: 
        :return: 
        """
        dlg = wx.FileDialog(self, "Open File",
                            #                       wildcard=self.wildcard,
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.file = dlg.GetPath()
            with open(self.file, "rb") as f:
                txt = f.readlines()
                # txt = txt.split('\n')
                d = dict()
                for i in range(len(txt)):
                    # split line
                    l = txt[i].split('\t')
                    k = l[0]
                    # summon data for dict
                    l_val = list()
                    l_val.append(l[1].strip())
                    l_val.append(l[2].strip())
                    d[k] = l_val
                self.d = d
        else:
            dlg.Destroy()
            return

        dlg.Destroy()

        k = self.find_minimal()
        self.n = 1
        self.n_parent = k.rpartition(':')[0]
        self.set_value(self.n_parent, self.n)

        # Raname Title of window
        self.SetTitle("Chainer - {0}".format(self.file))

    def LoadFile(self, e=0):
        """
        Load file by default
        :param e: 
        :return: 
        """
        try:
            with open(r'Options.txt', "rb") as f:
                self.file = f.readline().strip()
                self.OpenFile_First()
        except:
            pass

    def NewFile(self, e=0):
        """
        Create new File
        if fact just clear controlls
        :param e: 
        :return: 
        """

        #dlg = wx.FileDialog(self, "Create File",
     #                       wildcard=self.wildcard,
         #                   style=wx.FD_SAVE)
                            #style=wx.FD_OPEN)
        #print(dlg)
        #if dlg.ShowModal() == wx.ID_OK:
        #    self.file = dlg.GetPath()
        #dlg.Destroy()

        # clear all
        self.clear_controls()
        self.d = dict()

    def Save(self, e=0):
        """
        Save data
        :param e: 
        :return: 
        """
        # add item if it is
        self.add_item()

        if self.file == "":
            self.SaveAs()
            return
        with open(self.file, "w") as f:
            for k, v in self.d.items():
                s = k + '\t' + v[0] + '\t' + v[1] + '\n'
                f.write(s.encode('utf-8'))

    def SaveAs(self, e=0):
        """
        Save data
        :param e: nothing 
        :return: 
        """
        # add item if it is
        self.add_item()

        style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        dlg = wx.FileDialog(self, "Save As",
                                style=style)
        if dlg.ShowModal() == wx.ID_OK:
            self.file = dlg.GetPath()
        with open(self.file, "w") as f:
            for k, v in self.d.items():
                s = k + '\t' + v[0] + '\t' + v[1] + '\n'
                f.write(s.encode('utf-8'))
        dlg.Destroy()
        self.print_data()

    def WriteToDisk(self, fileName):
        with open(fileName, "wb") as handle:
            handle.write(self.txt.Value)
            self.file = fileName

    def print_data(self):
        """
        Print data of items
        :return: 
        """
        #print "n: " + str(self.n)
        #print "data dict: " + str(self.d)
        #print "file: " + self.file
        #print "content: " + self.txt
        #print(self.n)
        # print "n: " + str(self.n) + " parent: " + str(self.d[self.n][0]) + " previous: " + str(self.d[self.n][1]) + " mext: " + str(self.d[self.n][2]) + " item: " + str(self.d[self.n][3]) + " mnemo: " + str(self.d[self.n][4])

    def next_item(self, e=0):
        """
        Find next item
        :param e: 
        :param main: 
        :param name: 
        :return: 
        """
        self.add_item()

        self.clear_controls()
        mask = str(self.n_parent) + ":" + str(self.n+1)

        if self.d.get(mask):
            self.n = self.n + 1
            self.set_value(self.n_parent, self.n)
            self.rightBtn.Enable()
        else:
            try:
                self.n = self.find_next()
                self.set_value(self.n_parent, self.n)
            except:
                pass
        return


    def prev_item(self, e, main=0, name=0):

        ### TODO: add if exist data or update
        self.add_item()

        if self.n == 1:    # if first item do nothing
            return
        self.clear_controls()
        # change self data
        self.n = self.n - 1
        self.print_data()
        mask = str(self.n_parent) + ":" + str(self.n)
        if self.d.get(mask):
            self.n = self.n
            self.set_value(self.n_parent, self.n)
            self.leftBtn.Enable()
        #else:
        #    self.n = self.find_prev()
        #else:
        #    self.clear_controls()


    def child_item(self, e=0):
        # restrain if null
        if self.second_main_text.Value == '':
            return

        # write
        self.add_item()

        # clear
        self.clear_controls()

        # change parent
        self.n_parent = str(self.n_parent) + ":" + str(self.n)
        # change item
        self.n = 1

        # test if it is
        mask = str(self.n_parent) + ":" + str(self.n)
        if self.d.get(mask):
            self.set_value(self.n_parent, self.n)
        return
        # take child as first


    def parent_item(self, e=0):
        # restrain if first
        if len(str(self.n_parent)) == 1:
            return

        # write
        self.add_item()

        # clear
        self.clear_controls()

        # take current
        self.n = int(self.n_parent.rpartition(':')[-1])

        # take parent
        self.n_parent = self.n_parent.rpartition(':')[0]

        self.set_value(self.n_parent, self.n)
        return


    def add_item(self):
        if self.second_main_text.Value:
            item = self.second_main_text.Value
            mnemo = self.second_mnemo_text.Value
            l = [item, mnemo]
            mask = str(self.n_parent) + ":" + str(self.n)
            # add data
            self.d[mask] = l
            self.print_data()
        else:
            return

    def set_value(self, parent, n_item):
        """
        Set values of controlls
        :param parent: 
        :param n_item: 
        :return: 
        """
        try:
            mask = str(parent) + ":" + str(n_item)
            self.second_main_text.SetValue(self.d[mask][0])
            self.second_mnemo_text.SetValue(self.d[mask][1])
        #self.second_main_text.SetValue(self.d[self.n][3])
        #self.second_mnemo_text.SetValue(self.d[self.n][4])
        except:
            pass
        # find previous
        mask = str(self.n_parent) + ":" + str(self.n - 1)
        if self.d.get(mask):
            self.first_main.SetLabelText(self.d[mask][0])
            self.first_mnemo.SetLabelText(self.d[mask][1])
            self.upBtn.Enable()

        # find next
        mask = str(self.n_parent) + ":" + str(self.n + 1)
        if self.d.get(mask):
            self.third_main.SetLabelText(self.d[mask][0])
            self.third_mnemo.SetLabelText(self.d[mask][1])
            self.down_Btn.Enable()
        # set arrows
        self.set_arrows()
        self.cond_mnemo()

    def set_value_without_mnemo(self, parent, n_item):
        """
        Set values in controlls without mnemo check
        Use just for changes of checkbox mnemo
        :param parent: 
        :param n_item: 
        :return: 
        """
        try:
            mask = str(parent) + ":" + str(n_item)
            self.second_main_text.SetValue(self.d[mask][0])
            self.second_mnemo_text.SetValue(self.d[mask][1])
        #self.second_main_text.SetValue(self.d[self.n][3])
        #self.second_mnemo_text.SetValue(self.d[self.n][4])
        except:
            pass
        # find previous
        mask = str(self.n_parent) + ":" + str(self.n - 1)
        if self.d.get(mask):
            self.first_main.SetLabelText(self.d[mask][0])
            self.first_mnemo.SetLabelText(self.d[mask][1])
            self.upBtn.Enable()
        # find next
        mask = str(self.n_parent) + ":" + str(self.n + 1)
        if self.d.get(mask):
            self.third_main.SetLabelText(self.d[mask][0])
            self.third_mnemo.SetLabelText(self.d[mask][1])
            self.down_Btn.Enable()
        # set arrows
        self.set_arrows()


    def find_next(self):
        """
        Find next element
        :return: 
        """
        l = list()
        for k, v in self.d.items():
            try:
                #vv = self.n_parent.split(':')
                n_cur = len(self.n_parent.split(':')) + 1
            except:
                n_cur = 2

            vv = len(k.split(':'))
            kk = str(k)
            b = kk.startswith(str(self.n_parent))
            if b and vv == n_cur:
                a = int(k.split(':')[-1])
                l.append(a)
            # find maximum
        n = max(l) + 1
        return n


    def find_prev(self):
        """
        Find previous element
        :return: 
        """
        for k, v in self.d.items():
            try:
                #vv = self.n_parent.split(':')
                n_cur = len(self.n_parent.split(':')) + 1
            except:
                n_cur = 2
            l = list()
            vv = len(k.split(':'))
            kk = str(k)
            b = kk.startswith(str(self.n_parent))
            if b and vv == n_cur:
                a = int(k.split(':')[-1])
                l.append(a)
            # find maximum
            #### TODO: not maximum
            n = max(l) + 1
        return n

    def find_minimal(self):
        """
        Find minimal level & minimal number of this level
        :return: key of dictionary
        """
        ex = [0, 0] # key & length
        # find minimal level
        for k, v in self.d.items():
            try:
                l = k.split(':')
            except:
                l = k
            if ex[0] == 0:
                ex[0] = k
                ex[1] = len(l)
                continue
            if len(l) < ex[1]:
                ex[0] = k
                ex[1] = len(l)
        return ex[0]

    def find_parent(self):
        """
        Find parent for element
        :return: 
        """
        pass


    def clear_controls(self):
        self.first_main.SetLabelText("")
        self.first_mnemo.SetLabelText("")
        self.second_main_text.Clear()
        self.second_mnemo_text.Clear()
        self.third_main.SetLabelText("")
        self.third_mnemo.SetLabelText("")


    def CloseWin(self, e=0):
        """
        Close program
        :return: 
        """
        # TODO: dialog to write changes
        # test on empty
        self.add_item()
        if not len(self.d) == 0:
            self.Save()
        with open(r'Options.txt', "w") as f:
            f.write(self.file.encode('utf-8'))
        # save in options last file

        self.Destroy()

    def find_item_test(self, e=0):
        l_name = self.m_Filter.Value
        l_d = list()
        for k, v in self.d.items():
            l_d.append(v[0])
            l_d.append(v[1])
        for i in range(len(l_d)):
            set_d = set(l_d[i])  # set of each element of dictionary
            for j in range(len(l_name)):
                set_l = set(l_name[j])
                inter = set_d.intersection(set_l)
                l_i = len(inter)
                if len(inter) == len(set(l_name[j])):
                    for k, v in self.d.items():
                        if v[0] == l_d[i] or v[1] == l_d[i]:
                            res = k  # take key
                   # print("id: " + str(k) + " name: " + l_d[i] + " for data: " + l_name[j])
        self.set_value(res.rpartition(':')[0], res.rpartition(':')[-1])
        self.n_parent = res.rpartition(':')[0]
        self.n = res.rpartition(':')[-1]
        return

    def find_item(self, e=0):
        self.add_item()
        l_name = self.m_Filter.Value
        for k, v in self.d.items():
            ### TODO: problem with coding
            try:
                v1 = v[0].decode('utf-8')
                v2 = v[1].decode('utf-8')
                if v1.find(l_name) > -1 or v2.find(l_name) > -1:
                        self.set_value(k.rpartition(':')[0], k.rpartition(':')[-1])
                        self.n_parent = k.rpartition(':')[0]
                        self.n = int(k.rpartition(':')[-1])
            except:
                pass
        return

    def insert_branch(self, e=0):
        dlg = wx.FileDialog(self, "Open File",
                            #                       wildcard=self.wildcard,
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            file = dlg.GetPath()
            with open(file, "rb") as f:
                txt = f.readlines()
                # txt = txt.split('\n')
                d = dict()
                for i in range(len(txt)):
                    # split line
                    l = txt[i].split('\t')
                    k = str(self.n_parent) + ':' + str(self.n) + ':' + str(l[0])
                    # summon data for dict
                    l_val = list()
                    l_val.append(l[1].strip())
                    l_val.append(l[2].strip())
                    self.d[k] = l_val
                #self.d = d
        else:
            dlg.Destroy()
            return

        dlg.Destroy()
        return

    def delete_branch(self, e=0):
        d = dict()
        for k, v in self.d.items():
            if k.startswith(self.n):
                self.d.popitem()
        # TODO: delete current item

    def insert_item(self, e=0):
        pass

    def delete_item(self, e=0):
        pass

    def set_arrows(self):
        """
        Set labels of arrows
        :return: 
        """
        # Up
        mask = str(self.n_parent) + ":" + str(self.n - 1)
        if self.d.get(mask):
            self.upBtn.SetLabelText("^")
        else:
            self.upBtn.SetLabelText("")

        # down
        mask = str(self.n_parent) + ":" + str(self.n + 1)
        if self.d.get(mask):
            self.down_Btn.SetLabelText("v")
        else:
            if not self.m_Mnemo.Value:
                self.down_Btn.SetLabelText("+")
                self.down_Btn.Enable()
            else:
                self.down_Btn.SetLabelText("")
                self.down_Btn.Disable()

        # left
        mask = str(self.n_parent)
        if not self.n_parent == 0:
            if self.d.get(mask):
                self.leftBtn.SetLabelText("<")
            else:
                self.leftBtn.SetLabelText("")
        else:
            self.leftBtn.SetLabelText("")

        # right
        mask = str(self.n_parent) + ":" + str(self.n) + ":" + str(1)
        if self.d.get(mask):
            self.rightBtn.SetLabelText(">")
        else:
            if not self.m_Mnemo.Value:
                self.rightBtn.SetLabelText("+")
                self.rightBtn.Enable()
            else:
                self.rightBtn.SetLabelText("")
                self.rightBtn.Disable()


    def cond_mnemo(self, e=0):
        ### TODO: retype - something wrong
        """
        React on press mnemo checkbox
        :param e: 
        :return: 
        """
        if self.m_Mnemo.Value:
            self.first_mnemo.SetLabelText("")
            self.second_mnemo_text.SetValue("")
            self.second_mnemo_text.Disable()
            self.third_mnemo.SetLabelText("")
        else:
            self.second_mnemo_text.Enable()
            self.set_value_without_mnemo(self.n_parent, self.n)


