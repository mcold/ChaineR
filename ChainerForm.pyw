# -*- coding: utf-8 -*-

###########################################################################
## Ideas
## TODO: Export items current level
## TODO: restraint: not to export if none items
###########################################################################

import wx
import trl
from collections import defaultdict
#import wx.xrc


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):
    def __init__(self, parent):

        self.file = ""
        self.txt = ""
        self.b_ctrl_press = False
        self.b_alt_press = False
        self.b_shift_press = False

        # data
        #self.prev = 0
        self.n = 1  # n-number of record
        ### TODO: make something with self.n_parent in functions next-previous
        self.n_parent = 0
        #self.nextus = 2
        self.d = dict() # data dictionary
        self.item = ""  # name of item
        self.mnemo = "" # mnemo of item



        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"ChaineR", pos=wx.DefaultPosition, size=wx.Size(591,215),
                          style= wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        #self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        wxSizer = wx.WrapSizer(wx.HORIZONTAL)

        filterSizer = wx.GridSizer(0, 2, 0, 0)

        self.m_Filter = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        filterSizer.Add(self.m_Filter, 0, wx.ALL, 5)

        wxSizer.Add(filterSizer, 1, wx.EXPAND, 5)

        # wxSizer.AddSpacer(0)
        upSizer = wx.FlexGridSizer(0, 2, 0, 0)
        upSizer.Add(wx.Size(220, 0))

        #self.upBtn = wx.Button(self, wx.ID_ANY, u"^", wx.DefaultPosition, wx.Size(100, -1), 0)
        #upSizer.Add(self.upBtn, 0, wx.ALL, 5)

        wxSizer.Add(upSizer, 1, wx.EXPAND, 5)

        middleSizer = wx.GridSizer(0, 2, 0, 0)

        leftSizer = wx.FlexGridSizer(0, 2, 0, 0)
        leftSizer.SetFlexibleDirection(wx.BOTH)
        leftSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        leftSizer.AddSpacer(0)

        self.first_main = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(175, -1), wx.TE_CENTRE)
        self.first_main.Wrap(-1)
        leftSizer.Add(self.first_main, 0, wx.ALL, 5)

        self.leftBtn = wx.Button(self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0)
        leftSizer.Add(self.leftBtn, 0, wx.ALL, 5)

        self.second_main_text = wx.TextCtrl(self, 1, wx.EmptyString, wx.DefaultPosition, wx.Size(175, -1), wx.TE_CENTRE)
        leftSizer.Add(self.second_main_text, 0, wx.ALL, 5)

        leftSizer.AddSpacer(0)

        self.third_main = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(175, -1), wx.TE_CENTRE)
        self.third_main.Wrap(-1)
        leftSizer.Add(self.third_main, 0, wx.ALL, 5)

        middleSizer.Add(leftSizer, 1, wx.EXPAND, 5)

        rightSizer = wx.FlexGridSizer(0, 2, 0, 0)
        rightSizer.SetFlexibleDirection(wx.BOTH)
        rightSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.first_mnemo = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(175, -1), wx.TE_CENTRE)
        self.first_mnemo.Wrap(-1)
        rightSizer.Add(self.first_mnemo, 0, wx.ALL, 5)

        rightSizer.AddSpacer(1)

        self.second_mnemo_text = wx.TextCtrl(self, 2, wx.EmptyString, wx.DefaultPosition, wx.Size(175, -1), wx.TE_CENTRE)
        rightSizer.Add(self.second_mnemo_text, 0, wx.ALL, 5)

        self.rightBtn = wx.Button(self, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0)
        rightSizer.Add(self.rightBtn, 0, wx.ALL, 5)

        self.third_mnemo = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.Point(10, 10), wx.Size(175, -1), wx.TE_CENTRE)
        self.third_mnemo.Wrap(-1)
        rightSizer.Add(self.third_mnemo, 0, wx.ALL, 5)

        middleSizer.Add(rightSizer, 1, wx.EXPAND, 5)

        wxSizer.Add(middleSizer, 1, wx.EXPAND, 5)

        downSizer = wx.FlexGridSizer(0, 2, 0, 0)


        downSizer.Add(wx.Size(220, 0))

        #self.down_Btn = wx.Button(self, wx.ID_ANY, u"v", wx.DefaultPosition, wx.Size(100, -1), 0)
        #downSizer.Add(self.down_Btn, 0, wx.ALL, 5)

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
        self.m_Save = wx.MenuItem(self.m_File, wx.ID_ANY, u"Save", wx.EmptyString,
                                  wx.ITEM_NORMAL)  # done so (3 elements) specialy cause another side if write 's' execute 'SaveAs' function

#        self.m_Save = wx.MenuItem(self.m_File, wx.ID_ANY, u"Save " + u"\t" + u"+S", wx.EmptyString, wx.ITEM_NORMAL) # done so (3 elements) specialy cause another side if write 's' execute 'SaveAs' function
        self.m_File.Append(self.m_Save)

        self.m_SaveAs = wx.MenuItem(self.m_File, wx.ID_ANY, u"SaveAs", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_SaveAs)
        self.m_SaveSide = wx.Menu()


        self.m_SaveLeft = wx.MenuItem(self.m_File, wx.ID_ANY, u"Left", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_SaveSide.Append(self.m_SaveLeft)

        self.m_SaveRight = wx.MenuItem(self.m_File, wx.ID_ANY, u"Right", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_SaveSide.Append(self.m_SaveRight)

        self.m_File.Append(wx.NewId(), 'SaveSide', self.m_SaveSide)
        self.m_File.AppendSeparator()

        ### TreeLine

        self.m_Import_Trl = wx.MenuItem(self.m_File, wx.ID_ANY, u"Import Treeline", wx.EmptyString, wx.ITEM_NORMAL)
        #self.m_File.Append(self.m_Import_Trl)

        ### TODO: realize
        self.m_Export_Trl = wx.MenuItem(self.m_File, wx.ID_ANY, u"Export Treeline", wx.EmptyString, wx.ITEM_NORMAL)
        #self.m_File.Append(self.m_Export_Trl)

        self.m_Treeline = wx.Menu()
        self.m_Treeline.Append(self.m_Import_Trl)
        self.m_Treeline.Append(self.m_Export_Trl)
        self.m_File.Append(wx.NewId(), 'Treeline', self.m_Treeline)

        ### Tetra
        ### TODO: realize
        self.m_Import_Tetra = wx.MenuItem(self.m_File, wx.ID_ANY, u"Import Tetra", wx.EmptyString, wx.ITEM_NORMAL)

        ### TODO: realize
        self.m_Export_Tetra = wx.MenuItem(self.m_File, wx.ID_ANY, u"Export Tetra", wx.EmptyString, wx.ITEM_NORMAL)

        self.m_Tetra = wx.Menu()
        self.m_Tetra.Append(self.m_Import_Tetra)
        self.m_Tetra.Append(self.m_Export_Tetra)
        self.m_File.Append(wx.NewId(), 'Tetra', self.m_Tetra)

        ### Anki
        self.m_Anki = wx.Menu()
        ### TODO: add choice separator for anki-deck
        self.m_Export_Anki = wx.MenuItem(self.m_File, wx.ID_ANY, u"Export Anki", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_Anki.Append(self.m_Export_Anki)
        self.m_File.Append(wx.NewId(), 'Anki', self.m_Anki)


        self.m_File.AppendSeparator()

        self.m_Exit = wx.MenuItem(self.m_File, wx.ID_ANY, u"Exit \t Ctrl + ESC", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_Exit)

        self.menuBar.Append(self.m_File, u"File")


        self.Tree = wx.Menu()

        self.m_AppendBranch = wx.MenuItem(self.Tree, wx.ID_ANY, u"Insert Branch " u"\t" + u"Ctrl+I", wx.EmptyString, wx.ITEM_NORMAL)
        self.Tree.Append(self.m_AppendBranch)
        self.m_DeleteBranch = wx.MenuItem(self.Tree, wx.ID_ANY, u"Delete Item \t Ctrl+Delete", wx.EmptyString, wx.ITEM_NORMAL)
        self.Tree.Append(self.m_DeleteBranch)
        #self.m_DeleteItem = wx.MenuItem(self.Tree, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL)
        #elf.Tree.Append(self.m_DeleteItem)
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

        self.m_GoTo = wx.Menu()
        self.m_First = wx.MenuItem(self.m_GoTo, wx.ID_ANY, u"First \t PAGEUP", wx.EmptyString,
                                   wx.ITEM_NORMAL)
        self.m_GoTo.Append(self.m_First)
        self.m_Last = wx.MenuItem(self.m_GoTo, wx.ID_ANY, u"Last \t PAGEDOWN", wx.EmptyString,
                                               wx.ITEM_NORMAL)
        self.m_GoTo.Append(self.m_Last)

        self.menuBar.Append(self.m_GoTo, "GoTo")

        self.m_Move = wx.Menu()
        self.m_add_before = wx.MenuItem(self.m_Move, wx.ID_ANY, u"Add before", wx.EmptyString,
                                  wx.ITEM_NORMAL)
        self.m_Move.Append(self.m_add_before)

        self.m_Move.AppendSeparator()

        self.m_move_Up = wx.MenuItem(self.m_Move, wx.ID_ANY, u"Move Up", wx.EmptyString,
                                        wx.ITEM_NORMAL)
        self.m_Move.Append(self.m_move_Up)
        self.m_move_Down = wx.MenuItem(self.m_Move, wx.ID_ANY, u"Move Down", wx.EmptyString,
                                        wx.ITEM_NORMAL)
        self.m_Move.Append(self.m_move_Down)
        self.menuBar.Append(self.m_Move, "Move")

        self.m_Exchange = wx.Menu()
        self.m_Ex_Branch = wx.MenuItem(self.m_Exchange, wx.ID_ANY, u"Exchange sides", wx.EmptyString,
                                       wx.ITEM_NORMAL)
        self.m_Exchange.Append(self.m_Ex_Branch)
        self.m_Move.AppendSeparator()
        self.m_Left_Load = wx.MenuItem(self.m_Exchange, wx.ID_ANY, u"Left load", wx.EmptyString,
                                      wx.ITEM_NORMAL)
        self.m_Exchange.Append(self.m_Left_Load)
        self.m_Right_Load = wx.MenuItem(self.m_Exchange, wx.ID_ANY, u"Right load", wx.EmptyString,
                                       wx.ITEM_NORMAL)
        self.m_Exchange.Append(self.m_Right_Load)
        self.menuBar.Append(self.m_Exchange, "Exchange")

        self.m_About = wx.Menu()
        self.m_About_Description = wx.MenuItem(self.m_About, wx.ID_ANY, u"About program", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_About.Append(self.m_About_Description)
        self.menuBar.Append(self.m_About, "About")
        # aboutItem = self.menuBar.Append(self.m_About, u"About")

        self.Centre(wx.BOTH)

        self.statusbar = self.CreateStatusBar(1)
        self.statusbar.SetStatusText('')

        #Binding

        self.Bind(wx.EVT_MENU, self.CloseWin, self.m_Exit)
        self.Bind(wx.EVT_MENU, self.NewFile, self.m_New)
        self.Bind(wx.EVT_MENU, self.Save, self.m_Save)
        self.Bind(wx.EVT_MENU, self.SaveAs, self.m_SaveAs)
        self.Bind(wx.EVT_MENU, self.SaveAs_left, self.m_SaveLeft)
        self.Bind(wx.EVT_MENU, self.SaveAs_right, self.m_SaveRight)
        self.Bind(wx.EVT_MENU, self.OpenFile, self.m_Open)

        self.Bind(wx.EVT_MENU, self.import_trl, self.m_Import_Trl)
        self.Bind(wx.EVT_MENU, self.export_trl, self.m_Export_Trl)
        self.Bind(wx.EVT_MENU, self.import_tetra, self.m_Import_Tetra)
        self.Bind(wx.EVT_MENU, self.export_tetra, self.m_Export_Tetra)
        self.Bind(wx.EVT_MENU, self.export_anki, self.m_Export_Anki)

        self.Bind(wx.EVT_MENU, self.show_configuration, self.m_Configuration)

        self.Bind(wx.EVT_MENU, self.delete_branch, self.m_DeleteBranch)
        self.Bind(wx.EVT_MENU, self.insert_branch, self.m_AppendBranch)
        self.Bind(wx.EVT_MENU, self.insert_item, self.m_InsertItem)
        # self.Bind(wx.EVT_MENU, self.delete_item, self.m_DeleteItem)

        self.Bind(wx.EVT_MENU, self.exchange_mnemo_main, self.m_Ex_Branch)
        self.Bind(wx.EVT_MENU, self.left_side_load, self.m_Left_Load)
        self.Bind(wx.EVT_MENU, self.right_side_load, self.m_Right_Load)

        # self.Bind(wx.EVT_BUTTON, self.next_item, self.down_Btn)
        # self.Bind(wx.EVT_BUTTON, self.prev_item, self.upBtn)
        self.Bind(wx.EVT_BUTTON, self.child_item, self.rightBtn)
        self.Bind(wx.EVT_BUTTON, self.parent_item, self.leftBtn)

        self.Bind(wx.EVT_MENU, self.add_new, self.m_add_before)

        self.Bind(wx.EVT_MENU, self.go_first, self.m_First)
        self.Bind(wx.EVT_MENU, self.go_last, self.m_Last)

        self.Bind(wx.EVT_MENU, self.move_up, self.m_move_Up)
        self.Bind(wx.EVT_MENU, self.move_down, self.m_move_Down)

        self.Bind(wx.EVT_MENU, self.show_about, self.m_About_Description)

        # Connect Enter Events
        self.m_Filter.Bind(wx.EVT_TEXT_ENTER, self.find_item)
        self.second_main_text.Bind(wx.EVT_TEXT_ENTER, self.next_item)
        self.second_mnemo_text.Bind(wx.EVT_TEXT_ENTER, self.next_item)

        # self.m_Mnemo.Bind(wx.EVT_KEY_DOWN, self.mnemo_condition)
        # self.m_Mnemo.Bind(wx.EVT_SET_FOCUS, self.mnemo_condition)
        self.first_mnemo.Bind(wx.EVT_SET_FOCUS, self.mnemo_first)
        self.second_mnemo_text.Bind(wx.EVT_SET_FOCUS, self.mnemo_second)
        self.third_mnemo.Bind(wx.EVT_SET_FOCUS, self.mnemo_third)
        self.m_Mnemo.Bind(wx.EVT_CHECKBOX, self.mnemo_hide)

        ### TODO: debug
        self.m_Mnemo.Hide()     # hide while not work
        #self.third_mnemo.Bind(wx.EVT_MOTION, self.print_data)

        # HotKeys
        self.second_main_text.Bind(wx.EVT_KEY_DOWN, self.onTextKeyEvent)
        self.second_mnemo_text.Bind(wx.EVT_KEY_DOWN, self.onTextKeyEvent)
        self.m_Filter.Bind(wx.EVT_KEY_DOWN, self.onTextKeyEvent)
        self.leftBtn.Bind(wx.EVT_KEY_DOWN, self.onTextKeyEvent)
        self.rightBtn.Bind(wx.EVT_KEY_DOWN, self.onTextKeyEvent)

        self.Bind(wx.EVT_KEY_DOWN, self.onTextKeyEvent)
        self.menuBar.Bind(wx.EVT_KEY_DOWN, self.gen_StatusBar)

        #self.second_main_text.Bind(wx.EVT_COMMAND_SCROLL_BOTTOM, self.next_item)
        #self.second_main_text.Bind(wx.EVT_COMMAND_SCROLL, self.next_item)
        #self.second_main_text.Bind(wx.EVT_KEY_DOWN, self.onMainToMnemo)

        #s = u"Test"
        #self.first_main.SetLabelText(s)
        #self.third_main.SetLabelText(s)
        #self.first_mnemo.SetLabelText(s)
        #self.third_mnemo.SetLabelText(s)
        # Key Down & Up
        #self.second_main_text.Bind(wx.EVT_KEY_DOWN, self.next_item)

        # Load file by default
        #self.LoadFile()

        # set arrows
        self.set_arrows()
        self.second_main_text.SetFocus()


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
        self.n_parent = '0'

        # Raname Title of window
        self.SetTitle("Chainer - {0}".format(self.file))

    def OpenFile(self, e=0):
        """
        Open choosen file
        :param e: 
        :return: 
        """
        dlg = wx.FileDialog(self, "Open File", "", "",
                                      "ChaineR files (*.cr)|*.cr",
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.clear_controls()
            self.file = dlg.GetPath().encode('utf-8')
            with open(self.file.decode('utf-8'), "rb") as f:
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

        k = str(self.find_minimal())
        self.n = 1
        self.n_parent = k.rpartition(':')[0]
        self.set_value(self.n_parent, self.n)
        #self.n_parent = '0'

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

    def LastFiles(self, e=0):
        """
        Take last opened files
        :param e:
        :return:
        """
        try:
            with open(r'LastFiles.txt', "rb") as f:
                l = f.readlines().strip().split('\n')
                return l
        except:
            pass

    def AddLastFile(self, e=0):
        """
        Add last file to open
        :param e:
        :return:
        """
        l_new = list()
        try:
            with open(r'LastFiles.txt', "rb") as f:
                l = f.readlines().strip().split('\n')
        except:
            pass
        l.reverse()
        for i in range(3):
            try:
                l_new.append(l[i])
            except:
                pass
        # add new line
        l_new.append(self.file)
        f = open(r'LastFiles.txt', "wb")
        for j in range(len(l_new)):
            s = l_new[j] + '\n'
            f.write(s)


    def NewFile(self, e=0):
        """
        Create new File
        if fact just clear controlls
        :param e: 
        :return: 
        """

        self.m_Filter.SetValue('')

        self.m_Mnemo.Value = True
        self.m_Mnemo.SetValue(False)
        self.m_Mnemo
        self.first_mnemo.Show()
        self.second_mnemo_text.Show()
        self.third_mnemo.Show()

        # clear all
        self.clear_controls()
        self.d = dict()
        # Raname Title of window
        self.file = ""
        self.SetTitle("Chainer")
        self.n = 1
        self.mnemo_hide()

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
        else:
            f = open(self.file.decode('utf-8'), "wb")
            for k, v in self.d.items():
                s = k + '\t' + v[0] + '\t' + v[1] + '\n'
                if not s[0] == '0':
                    s = '0' + s
                s = s.encode('utf-8')
                f.write(s)
        #with open(self.file, "wb") as f:
        #    for k, v in self.d.items():
        #        s = k + '\t' + v[0] + '\t' + v[1] + '\n'
         #       f.write(s.encode('utf-8'))

    def SaveAs(self, e=0):
        """
        Save data
        :param e: nothing 
        :return: 
        """
        # add item if it is
        self.add_item()

        style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        #dlg = wx.FileDialog(self, "Save As",
        #                        style=style)
        dlg = wx.FileDialog(self, "Save As", "", "",
                                      "ChaineR files (*.cr)|*.cr",
                                      wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            d_p = dlg.GetPath()
            d_p = d_p#.encode('utf-8')
            self.file = d_p
            # Raname Title of window
            self.SetTitle("Chainer - {0}".format(self.file.encode('utf-8')))
            f = open(self.file, "wb")
            for k, v in self.d.items():
                v1 = v[0].encode('utf-8')
                v2 = v[1].encode('utf-8')
                s = k + '\t'.encode('utf-8') + v1 + '\t'.encode('utf-8') + v2 + '\n'.encode('utf-8')
                f.write(s)
            f.close()
        dlg.Destroy()
        #self.print_data()

    def SaveAs_left(self, e=0):
        self.SaveAs_side('left')

    def SaveAs_right(self, e=0):
        self.SaveAs_side('right')

    def SaveAs_side(self, side):
        """
        Save data
        :param e: nothing 
        :return: 
        """
        # add item if it is
        self.add_item()

        style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        #dlg = wx.FileDialog(self, "Save As",
        #                        style=style)
        dlg = wx.FileDialog(self, "Save As", "", "",
                                      "ChaineR files (*.cr)|*.cr",
                                      wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            d_p = dlg.GetPath()
            d_p = d_p#.encode('utf-8')
            self.file = d_p
            # Raname Title of window
            self.SetTitle("Chainer - {0}".format(self.file.encode('utf-8')))
            f = open(self.file, "wb")
            for k, v in self.d.items():
                v1 = v[0].encode('utf-8')
                v2 = v[1].encode('utf-8')
                if side == 'left':
                    v2 = ''
                if side == 'right':
                    v1 = ''
                s = k + '\t'.encode('utf-8') + v1 + '\t'.encode('utf-8') + v2 + '\n'.encode('utf-8')
                f.write(s)
            f.close()
        dlg.Destroy()
        self.print_data()

    def WriteToDisk(self, fileName):
        with open(fileName, "wb") as handle:
            handle.write(self.txt.Value)
            self.file = fileName

    def import_trl(self, e=0):
        """
        Import trl
        :return: 
        """
        dlg = wx.FileDialog(self, "Open File", "", "",
                            "TreeLine files (*.trl)|*.trl",
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.clear_controls()
            self.file = dlg.GetPath().encode('utf-8')
            #self.d = trl.take_trl(self.file)
            #with open(self.file.decode('utf-8'), "rb") as f:

        else:
            dlg.Destroy()
            return

        dlg.Destroy()

        # if current item not null
        mask = str(self.n_parent) + ":" + str(self.n)
        if not self.d.get(mask):
            d_trl = trl.take_trl(self.file, self.n_parent)
        else:
            d_trl = trl.take_trl(self.file, str(self.n_parent) + ":" + str(self.n))
        for k, v in d_trl.items():
            item = [v, '']
            self.d[k] = item
        self.clear_controls()
        self.set_value(self.n_parent, self.n)
        return

    def export_trl(self, e=0):
        """
        Export trl
        :return: 
        """
        self.show_debug()

    ### TODO: realize
    def import_tetra(self, e=0):
        """
        Import tetra
        :param e: 
        :return: 
        """
        dlg = wx.FileDialog(self, "Open File", "", "",
                            "(*.xml)|*.xml",
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.clear_controls()
            self.file = dlg.GetPath().encode('utf-8')


    ### TODO: realize
    def export_tetra(self, e=0):
        """
        Export tetra
        :param e: 
        :return: 
        """
        self.show_debug()

    def export_anki(self, e=0):
        """
        Export anki
        """
        sep = '`'

        ### Show dialog - about separator
        dlg = wx.FileDialog(self, "Save As", "", "",
                            "Text files (*.txt)|*.txt",
                            wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        if dlg.ShowModal() == wx.ID_OK:
            d_p = dlg.GetPath()

           # d_p = d_p.encode('utf-8')
            f = open(d_p, "wb")
            for k, v in self.d.items():
                # ask = font card
                # ans = bach card
                # mnemo = mnemonica
                ask = v[0]
                mnemo = v[1]
                ans = self.take_anki_childs_line(k)
                line = ask + sep + mnemo + sep + ans + '\n'
                f.write(line.encode('utf-8'))
            f.close()
        dlg.Destroy()
        # self.show_debug()

    def take_anki_childs_line(self, parent_mask):
        """"Take childs for anki items"""
        l_items = list()
        level = len(parent_mask.split(":")) + 1
        for k, v in self.d.items():
            if len(k.split(":")) == level and k.startswith(parent_mask):
                value = str(v[0]) + '\t' + str(v[1])
                l_items.append(value)

        # form line of anki deck
        if not len(l_items):
            return ''
        print(l_items)
        line = l_items[0]
        for i in range(1, len(l_items)):
            div = r'<div>' + str(l_items[i]) + r"</div>"
            line = line + div

        return line



    def print_data(self, e=0):
        """
        Print data of items
        :return: 
        """
        #self.third_mnemo.Hide()
        #print(self.d)
        #print "n: " + str(self.n)
        #print "data dict: " + str(self.d)
        #print "file: " + self.file
        #print "content: " + self.txt
        #print(self.n)
        # print "n: " + str(self.n) + " parent: " + str(self.d[self.n][0]) + " previous: " + str(self.d[self.n][1]) + " mext: " + str(self.d[self.n][2]) + " item: " + str(self.d[self.n][3]) + " mnemo: " + str(self.d[self.n][4])
        pass

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
            #self.upBtn.Enable()
            #self.upBtn.Show()
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
            #self.down_Btn.Enable()
            #self.down_Btn.Show()
        #else:
        #    self.n = self.find_prev()
        #else:
        #    self.clear_controls()

    def go_root(self):
        """Go to root"""
        self.clear_controls()
        self.n_parent = '0'
        self.n = 1
        self.set_value(parent=self.n_parent, n_item=self.n)

    def child_item(self, e=0):
        # restrain if null
        if self.second_main_text.Value == '' and self.second_mnemo_text.Value == '':
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
            self.leftBtn.Show()
        self.set_arrows()
        self.gen_StatusBar()
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


    def add_item(self, b_empty=False):
        if self.second_main_text.Value or self.second_mnemo_text.Value or b_empty:
            item = self.second_main_text.Value
            mnemo = self.second_mnemo_text.Value
            l = [item, mnemo]
            mask = str(self.n_parent) + ":" + str(self.n)
            # add data
            self.d[mask] = l
            #self.print_data()
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
            ss = self.d[mask][0]
            self.second_main_text.SetValue(ss)
            self.second_mnemo_text.SetValue(self.d[mask][1])
        #self.second_main_text.SetValue(self.d[self.n][3])
        #self.second_mnemo_text.SetValue(self.d[self.n][4])
        except:
            pass
        # find previous
        mask = str(self.n_parent) + ":" + str(int(n_item) - 1)

        if self.d.get(mask):
            self.first_main.SetLabelText(self.d[mask][0])
            self.first_mnemo.SetLabelText(self.d[mask][1])
            #self.upBtn.Enable()

        # find next
        mask = str(self.n_parent) + ":" + str(int(n_item) + 1)
        if self.d.get(mask):
            s1 = self.d[mask][0]
            s2 = self.d[mask][1]
            self.third_main.SetLabelText(s1)
            self.third_mnemo.SetLabelText(s2)
            #self.down_Btn.Enable()
        # set arrows
        self.set_arrows()
        #self.mnemo_condition()
        #self.cond_mnemo()

        # gemerate statisbar
        self.gen_StatusBar()

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
            #self.upBtn.Enable()
        # find next
        mask = str(self.n_parent) + ":" + str(self.n + 1)
        if self.d.get(mask):
            self.third_main.SetLabelText(self.d[mask][0])
            self.third_mnemo.SetLabelText(self.d[mask][1])
            #self.down_Btn.Enable()
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
                ex[0] = str(k)
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
        if not self.file=='':
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
        l_name = l_name.encode('utf-8')
        for k, v in self.d.items():
            ### TODO: problem with coding
            try:
                v1 = v[0].encode('utf-8')
                v2 = v[1].encode('utf-8')
                #v1 = v[0].decode('utf-8')
                #v2 = v[1].decode('utf-8')
                if v1.find(l_name) > -1 or v2.find(l_name) > -1:
                        self.clear_controls()
                        self.n_parent = k.rpartition(':')[0]
                        self.n = int(k.rpartition(':')[-1])
                        self.set_value(self.n_parent, self.n)
            except:
                pass
        self.second_main_text.SetFocus()
        return

    def insert_branch(self, e=0):
        #dlg = wx.FileDialog(self, "Open File",
        #                    #                       wildcard=self.wildcard,
        #                    style=wx.FD_OPEN)
        #dlg = wx.FileDialog(self, "Save As", "", "",
        #                    "ChaineR files (*.cr)|*.cr",
        #                    wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        dlg = wx.FileDialog(self, "Open File", "", "",
                            "ChaineR files (*.cr)|*.cr",
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            file = dlg.GetPath().encode('utf-8')
            with open(file.decode('utf-8'), "rb") as f:
                txt = f.readlines()
                # txt = txt.split('\n')
                d = dict()
                for i in range(len(txt)):
                    # split line
                    l = txt[i].split('\t')
                    mask = str(self.n_parent) + ':' + str(self.n)
                    # summon data for dict
                    l_val = list()

                    # exclude first element - 0  == '0: ...'
                    l_key = l[0].strip(":")

                    for w in range(1, len(l_key)):
                        if not w == 1:
                            mask = mask.strip(":") + ":" + l_key[w]
                        else:
                            mask = mask.strip(":") + l_key[w]
                    l_val.append(l[1].strip())
                    l_val.append(l[2].strip())

                    self.d[mask] = l_val
                #self.d = d
        else:
            dlg.Destroy()
            return

        dlg.Destroy()

        # refresh
        self.clear_controls()
        self.set_value(self.n_parent, self.n)
        return

    def left_side_load(self, e=0):
        """
        Execute load side to left frin file
        :param e:
        :return:
        """
        self.load_side('left')

    def right_side_load(self, e=0):
        """
        Execute load side to right from file
        :param e:
        :return:
        """
        self.load_side('right')

    def load_side(self, side='left'):
        """
        Load chosen side of items current level
        :param e:
        :param side:
        :return:
        """

        d_side = dict()
        dlg = wx.FileDialog(self, "Open File", "", "",
                            #"ChaineR files (*.cr)|*.cr",
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            file = dlg.GetPath().encode('utf-8')
            l_side = list()
            with open(file.decode('utf-8'), "rb") as f:
                txt = f.readlines()

                for i in range(len(txt)):
                    tt = txt[i].strip()
                    tt = tt.decode('utf-8')
                    l_side.append(tt)
                    d_side[i+1] = tt
        else:
            dlg.Destroy()
            return

        dlg.Destroy()

        level = len(str(self.n_parent).split(":")) + 1

        l_data = list()             # another side list of data

        d_data = dict()
        for k, v in self.d.items():
            if len(str(k).split(":")) == level and str(k).startswith(str(self.n_parent)):
                if side == 'left':
                    l_data.append(v[1])
                    k_n = int(str(k).split(":")[-1])
                    d_data[k_n] = v[1]
                else:
                    if side == 'right':
                        l_data.append(v[0])
                        k_n = int(str(k).split(":")[-1])
                        d_data[k_n] = v[0]
                #self.d.pop(k)

        # take maximum of length of lists of data
        m = max(len(d_side), len(d_data))


        # write data to level
        a = 0
        b = 0
        l_elem = list()
        for j in range(1, m+1):
            try:
                l_elem.append(d_side[j])
                a = 1
            except:
                if a==0:
                    l_elem.append('')
            try:
                l_elem.append(d_data[j])
                b = 1
            except:
                if b == 0:
                    l_elem.append('')
            # make reverse in order of side
            if side == 'right':
                l_elem.reverse()
            # add to dictionary
            if l_elem[0] == '' and l_elem[1] == '':
                l_elem = []
                continue
            mask = str(self.n_parent) + ":" + str(j)
            self.d[mask] = l_elem
            l_elem = []
            a = 0
            b = 0


        # refresh
        self.clear_controls()
        self.set_value(self.n_parent, self.n)
        return

    def delete_branch(self, e=0):
        """
        Delete branch of items
        :param e:
        :return:
        """
        ### TODO: debug
        #self.show_debug()
        # delete childs
        mask = str(self.n_parent) + ":" + str(self.n)
        for k, v in self.d.items():
            if str(k).startswith(mask):
                self.d.pop(k)

        # renum numbers above

        level = len(str(self.n_parent).split(":")) + 1
        self.renum_branches_minus(level, self.n)

        # delete current item
        #self.n = self.n
        #mask_next = str(self.n_parent) + ":" + str(self.n)
        #if self.d.get(mask_next):
        #    self.set_value(self.n_parent, self.n)
        #else:
        #    self.next_item()
        self.clear_controls()
        mask = str(self.n_parent) + ":" + str(self.n)
        print(mask)
        if self.d.get(mask):
            self.set_value(self.n_parent, self.n)
        else:
            self.second_main_text.SetValue('')
            self.second_mnemo_text.SetValue('')
            # set previous
            try:
                mask = str(self.n_parent) + ":" + str(self.n - 1)
                self.first_main.SetLabelText(self.d[mask][0])
                self.first_mnemo.SetLabelText(self.d[mask][1])
            except:
                pass

    def insert_item(self, e=0):
        """
        Insert branch of items
        :param e:
        :return:
        """
        # delete childs
        #mask = str(self.n_parent) + ":" + str(self.n)
        #for k, v in self.d.items():
        #    if str(k).startswith(mask):
        #        self.d.pop(k)
        # if main null exit
        if self.second_main_text.Value == '':
            return

        # renum numbers below
        level = len(str(self.n_parent).split(":")) + 1
        self.renum_branches_plus(level, self.n)

        # clear data
        self.clear_controls()
        # add empty item
        self.add_item(True)

        self.set_value(self.n_parent, self.n)
        self.second_main_text.SetFocus()
        #mask_next = str(self.n_parent) + ":" + str(self.n+1)
        #if self.d.get(mask_next):
        #    self.set_value(self.n_parent, self.n)
        #else:
        #    self.next_item()


    def set_arrows(self):
        """
        Set labels of arrows
        :return: 
        """
        # Up
        mask = str(self.n_parent) + ":" + str(self.n - 1)
        #if self.d.get(mask):
        #    self.upBtn.SetLabelText("^")
        #else:
        #    self.upBtn.SetLabelText("")
        #    if self.m_Mnemo.Value == True:
        #        self.upBtn.Hide()
        #    else:
        #        self.upBtn.Show()

        # down
        mask = str(self.n_parent) + ":" + str(self.n + 1)
        #if self.d.get(mask):
            #self.down_Btn.SetLabelText("v")
        #else:
        #    if not self.m_Mnemo.Value:
         #       self.down_Btn.SetLabelText("")
         #       self.down_Btn.Enable()
         #       self.down_Btn.Show()
         #   else:
         #       self.down_Btn.SetLabelText("")
         #       #self.down_Btn.Disable()
         #       #self.down_Btn.Hide()
         #       if self.m_Mnemo.Value == True:
         #           self.down_Btn.Hide()
         #       else:
         #           self.down_Btn.Show()

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
                self.rightBtn.SetLabelText("")
                self.rightBtn.Enable()
                self.rightBtn.Show()
            else:
                self.rightBtn.SetLabelText("")


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
            #self.set_value_without_mnemo(self.n_parent, self.n)

    def add_new(self, e=0):
        """
        Adding new item above chosen
        :return:
        """
        # clean controlls
        self.clear_controls()

        # new dictionary
        d_new = dict()
        # to add above

        # find level of current item
        level = len(str(self.n_parent).split(":"))+1
        # find items that level with higher number
        for k, v in self.d.items():
            num = int(str(k).split(":")[-1])
            if len(str(k).split(":")) >= level and num >= int(self.n):
                l_elem = str(k).split(":")
                num = int(l_elem[level-1]) + 1

                # summon key
                s_first = ""                 # first part of string
                s_last = ""                  # last part of string
                for i in range(0, level-1):
                    s_first = s_first + l_elem[i]
                try:
                    for j in range(level, len(l_elem)):
                        s_last = s_last + l_elem[j]
                except:
                    pass

                # summon
                if s_last:
                    s_summon = str(s_first) + ":" + str(num) + ":" + str(s_last)
                else:
                    s_summon = str(s_first) + ":" + str(num)

                # write to dictionary
                d_new[s_summon] = v

                # delete item from self.d
                self.d.pop(k)
            else:
                d_new[k] = self.d[k]

        # change dictionary
        self.d = d_new

        # renum childs
        self.go_down()

        # write data from dictionary even that current element is empty
        self.add_item(True)



        self.set_value(self.n_parent, self.n)

    def go_last(self, e=0):
        """
        Find last item of current level
        :return:
        """
        # find level of current item
        level = len(str(self.n_parent).split(":")) + 1

        l_elem = list()
        for k, v in self.d.items():
            if len(str(k).split(":")) == level and str(k).startswith(self.n_parent):
                elem = str(k).split(":")[-1]
                l_elem.append(int(elem))
        m = max(l_elem)
        # summont string
        #ss = str(self.n_parent) + ":" + str(m)
        self.clear_controls()
        self.n = m
        self.set_value(self.n_parent, str(m))


    def go_first(self, e=0):
        """
                Find first item of current level
                :return:
                """
        # find level of current item
        level = len(str(self.n_parent).split(":")) + 1

        l_elem = list()
        for k, v in self.d.items():
            if len(str(k).split(":")) == level and str(k).startswith(self.n_parent):
                elem = str(k).split(":")[-1]
                l_elem.append(int(elem))
        m = min(l_elem)
        self.clear_controls()
        self.n = m
        self.set_value(self.n_parent, str(m))

    def delete_item(self, e=0):
        # clean controlls
        self.clear_controls()

        # to add above

        # find level of current item
        level = len(str(self.n_parent).split(":")) + 1
        # find items that level with higher number
        for k, v in self.d.items():
            if len(str(k).split(":")) >= level:
                l_elem = str(k).split(":")
                print(level)
                num = int(l_elem[level]) + 1

                # summon key
                s_first = ""  # first part of string
                s_last = ""  # last part of string
                for i in range(0, level):
                    s_first = s_first + l_elem[i]
                try:
                    for j in range(level + 1, len(l_elem)):
                        s_last = s_last + l_elem[i]
                except:
                    pass

                # summon
                s_summon = str(s_first) + str(num) + str(s_last)

                # write to dictionary
                self.d[s_summon] = v

                # delete item from self.d
                self.d.pop(k)

        # write data from dictionary even that current element is empty
        self.set_value()

    def move_up(self, e=0):
        """
        Move item up
        :param e:
        :return: None
        """
        self.add_item(True)
        mask = str(self.n_parent) + ":" + str(self.n - 1)
        if self.d.get(mask):
            self.clear_controls()
            v1 = self.d.get(mask)
            k1 = mask
            self.add_item()
            mask2 = str(self.n_parent) + ":" + str(self.n)
            v2 = self.d.get(mask2)
            k2 = mask2

            # renum childs of current branch
            self.exchange_branches('Up')

            # change data
            self.d[k1] = v2
            self.d[k2] = v1

            self.n = self.n - 1
            # set new data
            self.set_value(self.n_parent, self.n)



    def move_down(self, e=0):
        """"
        Move item down
        """
        self.add_item(True)
        mask = str(self.n_parent) + ":" + str(self.n + 1)
        if self.d.get(mask):
            self.clear_controls()
            v1 = self.d.get(mask)
            k1 = mask
            self.add_item()
            mask2 = str(self.n_parent) + ":" + str(self.n)
            v2 = self.d.get(mask2)
            k2 = mask2



            # renum childs of current branch
            ### TODO: to debug
            self.exchange_branches('Down')

            # change data
            self.d[k1] = v2
            self.d[k2] = v1

            self.n = self.n + 1
            # set new data
            self.set_value(self.n_parent, self.n)

        else:
            self.next_item()


    def renum_branches_plus(self, level, n_num):
        """
        Renumber branches
        + 1 to number
        :param level: number in order of key
        :param num: from which number to do renumbering
        :return: None
        """
        # new dictionary
        d_new = dict()
        # to add above
        a = 0
        # find items that level with higher number
        mask = str(self.n_parent)
        for k, v in self.d.items():
            if len(str(k).split(":"))> level - 1:
                a = 1
            else:
                a = 0
            if a == 1:
                #print(k)
                num = int(str(k).split(":")[level-1])
                if len(str(k).split(":")) >= level and num >= int(n_num) and str(k).startswith(mask):
                    l_elem = str(k).split(":")
                    num = int(l_elem[level - 1]) + 1

                    # summon key
                    s_first = ""  # first part of string
                    s_last = ""  # last part of string
                    for i in range(0, level - 1):
                        s_first = s_first + l_elem[i]
                        if not i == (level - 1):
                            s_first = s_first + ":"
                    try:
                        for j in range(level, len(l_elem)):
                            s_last = s_last + l_elem[j]
                            if not j == len(l_elem):
                                s_last = s_last + ":"
                    except:
                        pass

                    # summon
                    if s_last:
                        s_summon = str(s_first) + str(num) + str(s_last)
                    else:
                        s_summon = str(s_first) + str(num)

                    # write to dictionary
                    d_new[s_summon] = v

                    # delete item from self.d
                    self.d.pop(k)
                    continue
                else:
                    d_new[k] = self.d[k]
                    continue
            a = 0
            d_new[k] = self.d[k]
        # change dictionary
        self.d = d_new
        mask = str(self.n_parent) + ":" + str(self.n)
        self.d[mask] = ''
        for k,v in self.d.items():
            print(str(k) + ' => ' + str(v))
        mask = str(self.n_parent) + ":" + str(self.n+1)
        #print(self.d[mask])

    def exchange_branches(self, straight='Down'):
        """
                Renumber branches
                + 1 to number
                :param level: number in order of key
                :param num: from which number to do renumbering
                :return: None
                """

        d_first = dict()          # up branch
        d_second = dict()         # down branch

        level = len(str(self.n_parent).split(":")) + 1
        n_num = int(self.n)
        if straight == 'Down':
            n_next = int(self.n) + 1
        else:
            if straight == 'Up':
                n_next = int(self.n) - 1
            else:
                print('Entered not right straingth!!!')
                return

        mask_cur = str(self.n_parent) + ":" + str(n_num)
        mask_next = str(self.n_parent) + ":" + str(n_next)
        # find elements above
        for k, v in self.d.items():
            num = int(str(k).split(":")[-1])
            if len(str(k).split(":")) >= level and str(k).startswith(mask_cur):
                l_elem = str(k).split(":")
                if straight == 'Down':
                    num = int(l_elem[level - 1]) + 1
                else:
                    num = int(l_elem[level - 1]) - 1
                # summon key
                s_first = ""  # first part of string
                s_last = ""  # last part of string
                for i in range(0, level - 1):
                    if i == 0:
                        s_first = s_first + l_elem[i]
                    else:
                        s_first = s_first + ":" + l_elem[i]
                try:
                    for j in range(level, len(l_elem)):
                        if j == 0:
                            s_last = s_last + l_elem[j]
                        else:
                            s_last = s_last + ":" + l_elem[j]
                except:
                    pass

                if s_last.startswith(":"):
                    s = ''
                    for w in range(1, len(s_last)):
                        s = s + s_last[w]
                    s_last = s
                # summon
                if s_last:
                    s_summon = str(s_first) + ":" + str(num) + ":" + str(s_last)
                else:
                    s_summon = str(s_first) + ":" + str(num)

                # write to dictionary
                d_first[s_summon] = v
                self.d.pop(k)

            if len(str(k).split(":")) >= level and str(k).startswith(mask_next):
                l_elem = str(k).split(":")
                if straight == 'Down':
                    num = int(l_elem[level - 1]) - 1
                else:
                    num = int(l_elem[level - 1]) + 1

                # summon key
                s_first = ""  # first part of string
                s_last = ""  # last part of string
                for i in range(0, level - 1):
                    if i == 0:
                        s_first = s_first + l_elem[i]
                    else:
                        s_first = s_first + ":" + l_elem[i]
                try:
                    for j in range(level, len(l_elem)):
                        if j == 0:
                            s_last = s_last + l_elem[j]
                        else:
                            s_last = s_last + ":" + l_elem[j]

                except:
                    pass

                if s_last.startswith(":"):
                    s = ''
                    for w in range(1, len(s_last)):
                        s = s + s_last[w]
                    s_last = s

                # summon
                if s_last:
                    s_summon = str(s_first) + ":" + str(num) + ":" + str(s_last)
                else:
                    s_summon = str(s_first) + ":" + str(num)

                # write to dictionary
                d_second[s_summon] = v
                self.d.pop(k)

        for kk, vv in d_first.items():
            self.d[kk] = vv

        for kkk, vvv in d_second.items():
            self.d[kkk] = vvv

    def exchange_mnemo_main(self, e=0):
        """
        Exchange sides mnamo with main
        :param e:
        :return:
        """
        for k, v in self.d.items():
            #l = list()
            #l = v
            v.reverse()
            self.d[k] = v
        self.clear_controls()
        self.set_value(self.n_parent, self.n)

    def go_down(self):
        """
                        Renumber branches
                        + 1 to number
                        :param level: number in order of key
                        :param num: from which number to do renumbering
                        :return: None
                        """

        d_first = dict()  # up branch
        #d_second = dict()  # down branch

        level = len(str(self.n_parent).split(":")) + 1
        n_num = int(self.n)

        n_next = int(self.n) + 1

        mask_cur = str(self.n_parent) + ":" + str(n_num)
        #mask_next = str(self.n_parent) + ":" + str(n_next)
        # find elements above
        for k, v in self.d.items():
            num = int(str(k).split(":")[-1])
            if len(str(k).split(":")) >= level and str(k).startswith(mask_cur):
                l_elem = str(k).split(":")

                num = int(l_elem[level - 1]) + 1
                #else:
                #    num = int(l_elem[level - 1]) - 1
                # summon key
                s_first = ""  # first part of string
                s_last = ""  # last part of string
                for i in range(0, level - 1):
                    if i == 0:
                        s_first = s_first + l_elem[i]
                    else:
                        s_first = s_first + ":" + l_elem[i]
                try:
                    for j in range(level, len(l_elem)):
                        if j == 0:
                            s_last = s_last + l_elem[j]
                        else:
                            s_last = s_last + ":" + l_elem[j]
                except:
                    pass

                if s_last.startswith(":"):
                    s = ''
                    for w in range(1, len(s_last)):
                        s = s + s_last[w]
                    s_last = s
                # summon
                if s_last:
                    s_summon = str(s_first) + ":" + str(num) + ":" + str(s_last)
                else:
                    s_summon = str(s_first) + ":" + str(num)

                # write to dictionary
                d_first[s_summon] = v
                self.d.pop(k)



        for kk, vv in d_first.items():
            self.d[kk] = vv

    def renum_branches_minus(self, level, n_num):
        """
        Renumber branches
        + 1 to number
        :param level: number in order of key
        :param num: from which number to do renumbering
        :return: None
        """
        # new dictionary
        d_new = {}
        # to add above

        mask = str(self.n_parent) + ":" + str(self.n)
        # find level of current item

        for k, v in self.d.items():
            print(level)
            try:
                num = int(str(k).split(":")[level-1])
                if len(str(k).split(":")) >= level and num > n_num:
                    l_elem = str(k).split(":")
                    num = int(l_elem[level - 1]) - 1

                    # summon key
                    s_first = ""  # first part of string
                    s_last = ""  # last part of string

                    for i in range(0, level - 1):
                        s_first = s_first + l_elem[i]
                        if not i == (level - 1):
                            s_first = s_first + ":"
                    try:
                        for j in range(level, len(l_elem)):
                            s_last = s_last + l_elem[j]
                            if not j == len(l_elem):
                                s_last = s_last + ":"
                    except:
                        s_last = ""


                    # summon
                    if s_last:
                        s_summon = str(s_first) + str(num) + str(s_last)
                    else:
                        s_summon = str(s_first) + str(num)

                        d_new[str(s_summon)] = v

                        # delete item from self.d
                        self.d.pop(k)
                else:
                    d_new[k] = self.d[k]
            except:
                d_new[k] = self.d[k]

        for k,v in d_new.items():
            print(str(k) + ' => ' + str(v))
        # change dictionary
        self.d = d_new

    def renum_from_cur_branches_plus(self):
        """
        Renumber brances
        + 1 to number
        use current parameters of item
        :return:
        """
        # new dictionary
        d_new = dict()
        # to add above

        # find level of current item
        level = len(str(self.n_parent).split(":")) + 1
        # find items that level with higher number
        for k, v in self.d.items():
            num = int(str(k).split(":")[-1])
            if len(str(k).split(":")) >= level and num >= int(self.n):
                l_elem = str(k).split(":")
                num = int(l_elem[level - 1]) + 1

                # summon key
                s_first = ""  # first part of string
                s_last = ""  # last part of string
                for i in range(0, level - 1):
                    s_first = s_first + l_elem[i]
                try:
                    for j in range(level, len(l_elem)):
                        s_last = s_last + l_elem[j]
                except:
                    pass

                # summon
                if s_last:
                    s_summon = str(s_first) + ":" + str(num) + ":" + str(s_last)
                else:
                    s_summon = str(s_first) + ":" + str(num)

                # write to dictionary
                d_new[s_summon] = v

                # delete item from self.d
                self.d.pop(k)
            else:
                d_new = self.d[k]

        # change dictionary
        self.d = d_new

    def renum_for_current_branch_plus(self):
        """
        Renumber items of branch
        + 1 to number
        use current parameters of item
        :return:
        """
        # new dictionary
        d_new = {}
        # to add above

        mask = str(self.n_parent) + ":" + str(self.n)
        # find level of current item
        level = len(str(self.n_parent).split(":")) + 1
        # find items that level with higher number

        d_parse = dict()
        for k, v in self.d.items():
            #num = int(str(k).split(":")[-1])
            if len(str(k).split(":")) >= level and str(k).startswith(mask):
                l_elem = str(k).split(":")
                num = int(l_elem[level - 1]) + 1

                # summon key
                s_first = ""  # first part of string
                s_last = ""  # last part of string


                for i in range(0, level - 1):
                    s_first = s_first + l_elem[i]
                try:
                    for j in range(level, len(l_elem)):
                        s_last = s_last + l_elem[j]
                except:
                    pass

                # summon
                if s_last:
                    s_summon = str(s_first) + ":" + str(num) + ":" + str(s_last)
                else:
                    s_summon = str(s_first) + ":" + str(num)

                d_new[str(s_summon)] = v

                # delete item from self.d
                self.d.pop(k)
            else:
                d_new[k] = self.d[k]

        # change dictionary
        self.d = d_new
        print(self.d)



    def renum_from_cur_branches_minus(self):
        """
        Renumber brances
        - 1 to number
        use current parameters of item
        :return:
        """
        # new dictionary
        d_new = dict()
        # to add above

        # find level of current item
        level = len(str(self.n_parent).split(":")) + 1
        # find items that level with higher number
        for k, v in self.d.items():
            num = int(str(k).split(":")[-1])
            if len(str(k).split(":")) >= level and num >= int(self.n):
                l_elem = str(k).split(":")
                num = int(l_elem[level - 1]) - 1

                # summon key
                s_first = ""  # first part of string
                s_last = ""  # last part of string
                for i in range(0, level - 1):
                    s_first = s_first + l_elem[i]
                try:
                    for j in range(level, len(l_elem)):
                        s_last = s_last + l_elem[j]
                except:
                    pass

                # summon
                if s_last:
                    s_summon = str(s_first) + ":" + str(num) + ":" + str(s_last)
                else:
                    s_summon = str(s_first) + ":" + str(num)

                # write to dictionary
                d_new[s_summon] = v

                # delete item from self.d
                self.d.pop(k)
            else:
                d_new = self.d[k]

        # change dictionary
        self.d = d_new

    def mnemo_hide(self, e=0):
        if self.m_Mnemo.Value == True:
            self.first_mnemo.Hide()
            self.second_mnemo_text.Hide()
            self.third_mnemo.Hide()
        else:
            self.first_mnemo.Show()
            self.second_mnemo_text.Show()
            self.third_mnemo.Show()
            self.set_value(self.n_parent, self.n)

    def mnemo_condition(self, e=0):
        if self.m_Mnemo.Value == True:
            self.set_value(self.n_parent, self.n)
        else:
            self.first_mnemo.SetLabelText("")
            self.second_mnemo_text.SetValue("")
            self.third_mnemo.SetLabelText("")

    def mnemo_first(self, e=0):
        if self.m_Mnemo.Value == True:
            mask = str(self.n_parent) + ":" + str(int(self.n) - 1)
            if self.d.get(mask):
                s2 = self.d[mask][1]
                self.first_mnemo.SetLabelText(s2)
        else:
            self.first_mnemo.SetLabelText("")

    def mnemo_second(self, e=0):
        if self.m_Mnemo.Value == True:
            mask = str(self.n_parent) + ":" + str(int(self.n))
            if self.d.get(mask):
                s2 = self.d[mask][1]
                self.second_mnemo_text.SetValue(s2)
        else:
            self.second_mnemo_text.SetValue("")

    def mnemo_third(self, e=0):
        if self.m_Mnemo.Value == True:
            mask = str(self.n_parent) + ":" + str(int(self.n) + 1)
            if self.d.get(mask):
                s2 = self.d[mask][1]
                self.third_mnemo.SetLabelText(s2)
        else:
            self.third_mnemo.SetLabelText("")

    def gen_StatusBar(self):
        """
        Generate statusbar text for current element
        :return: 
        """
        self.statusbar.SetStatusText('')
        # if root -> exit
        if self.n_parent == '0':
            return
        level = len(str(self.n_parent).split(":")) - 1
        par = self.n_parent
        result = ''
        l_res = list()
        for i in range(level):
            mask = par
            item = self.d[mask][0]
            l_res.append(item)
            par = par.rpartition(":")[0]
            if par == '0':
                break
        l_res.reverse()

        # take just last 3 elements
        if len(l_res) > 3:
            result = l_res[-3] + " \\ " + l_res[-2] + " \\ " + l_res[-1]
        else:
            result = " \\ ".join(l_res)
        self.statusbar.SetStatusText(result)

    def show_configuration(self, e=0):
        """
        Configuration window
        :param e: 
        :return: 
        """
        self.show_debug()

    def show_about(self, e=0):
        """
        About dialog window
        :param e: 
        :return: 
        """
        self.dlg = AboutDialog(None)
        self.dlg.Show()
        return True

    def show_debug(self, e=0):
        """
        Debug dialog window
        :param e: 
        :return: 
        """
        self.dlg = DebugDialog(None)
        self.dlg.Show()
        return True

    def left_save(self):
        # take level
        level = len(self.n_parent.split(":")) + 1

        # take elements with this level
        l_items = list()
        for k,v in self.d.items():
            item = v[0]
            if len(item.split(":")) == level:
                l_items.append(item)

        # take name of file
        dlg = wx.FileDialog(self, "Save As", "", "",
                            "ChaineR files (*.cr)|*.cr",
                            wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            pass

    def right_save(self):
        pass

    def onMainToMnemo(self):
        """Change focus from main to mnemo"""
        self.second_mnemo_text.SetFocus()

    def onMnemoToMain(self):
        """Change focus from mnemo to main"""
        self.second_mnemo_text.SetFocus()

    def onTextKeyEvent(self, event):
        """
        HotKeys
        """

        keycode = event.GetKeyCode()
        print(keycode)
        if keycode == wx.WXK_RIGHT:
            self.child_item()

        if keycode == wx.WXK_ESCAPE:
            self.CloseWin()

        ###
        # first and last
        if keycode == wx.WXK_PAGEDOWN:
            self.go_last()

        if keycode == wx.WXK_PAGEUP:
            self.go_first()
        ###


        ###
        # change focus
        if keycode == wx.WXK_TAB and self.second_main_text.HasFocus():
            self.onMainToMnemo()
        if keycode == wx.WXK_TAB and self.second_mnemo_text.HasFocus():
            self.onMnemoToMain()
        ###

        if keycode == wx.WXK_HOME:
            ### TODO: realize function go to root
            self.go_root()



        if keycode == wx.WXK_LEFT:
            self.parent_item()

        if keycode == wx.WXK_UP:
            self.prev_item(0)

        if keycode == wx.WXK_DOWN:
            self.next_item()
        #event.Skip()

        # Ctrl
        if keycode == wx.WXK_CONTROL:
            self.b_ctrl_press = True
            event.Skip()
            return

        # Shift
        if keycode == wx.WXK_SHIFT:
            self.b_shift_press = True
            event.Skip()
            return

        if keycode == 70 and self.b_ctrl_press:     # Ctrl + F
            self.m_Filter.SetFocus()
        if keycode == 78 and self.b_ctrl_press:     # Ctrl + N
            self.NewFile()
        if keycode == 79 and self.b_ctrl_press:     # Ctrl + O
            self.OpenFile()
        if keycode == 83 and self.b_ctrl_press and self.b_shift_press:     # Ctrl + Shift + S
            self.SaveAs()
            self.b_ctrl_press = False
            self.b_alt_press = False
            self.b_shift_press = False
            return
        if keycode == 83 and self.b_ctrl_press:     # Ctrl + S
            self.Save()

        if keycode == 127 and self.b_ctrl_press:     # Delete
            self.delete_branch()
        if keycode == 73 and self.b_ctrl_press:     # Ctrl + I
            self.insert_branch()

        # alt
        if keycode == wx.WXK_ALT:
            self.b_alt_press = True
            event.Skip()
            return

        if keycode == 85 and self.b_alt_press:     # Alt + U
            self.move_up()
        if keycode == 68 and self.b_alt_press:     # Alt + d
            self.move_down()
        if keycode == 70 and self.b_alt_press:     # Alt + f
            self.go_first()
        if keycode == 69 and self.b_alt_press:     # Alt + e
            self.exchange_branches()
        if keycode == 76 and self.b_alt_press:     # Alt + l
            self.go_last()

        self.b_ctrl_press = False
        self.b_alt_press = False
        self.b_shift_press = False
        event.Skip()

        self.gen_StatusBar()

    def sorting_dict(self):
        """
        Sorting dictionary in ascender order
        """
        ### take length of key and write in new dictionary repaired number without dots
        d_rekey = dict()
        # take level of number
        level = len(max((self.d)))
        l_res_key = list()
        for k in self.d.items():
            # renum key
            res_key = "".join([x for x in k.split(':')])
            delta = level - len(res_key)                         # number of zeros
            res_key = int(res_key + str('0'*delta))
            d_rekey[key] = res_key
            l_res_key.append(res_key)                            # combine numbers
        l_res_key.sort()                                         # sort numbers
        ### TODO: write numbers to file
        ### TODO: in argument - file and extension

class AboutDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"About ChaineR", pos=wx.DefaultPosition,
                           size=wx.Size(400, 125), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY,
                                           u"Program is written for work with mnemonic items in tree format\nParticularly can be used for construct Ciceron memory palace\n\nAll rights reserved\nEnjoy!",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer1.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class DebugDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Debug", pos=wx.DefaultPosition, size=wx.Size(400, 125),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY,
                                           u"Current element in process of realization\nComing soon\n\nAll information you can receive at https://github.com/mcold/ChaineR",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer1.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
