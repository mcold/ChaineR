#coding: utf-8

import ChainerForm
import wx

class MyApp(wx.App):
    def OnInit(self):
        self.frame = ChainerForm.MainFrame(None)
        ico = wx.Icon('del.ico', wx.BITMAP_TYPE_ICO)
        self.frame.SetIcon(ico)
        self.frame.Show()
        return True

    def test(self):
        self.frame.next_item(0, 'first', '11')
        self.frame.next_item(0, 'second', '22')
        self.frame.prev_item(0)
        self.frame.prev_item(0)
        self.frame.next_item(0)

if __name__ == '__main__':
    app = MyApp(False)
    #app.test()
    app.MainLoop()
