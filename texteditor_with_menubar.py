#!/usr/bin/env python3
import wx
class MainWindow(wx.Frame):
    '''We simply derive a new class of frame'''

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 300))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu = wx.Menu()
        menu_bar = wx.MenuBar()
        menu_bar.Append(filemenu, '&File')

        filemenu.Append(wx.ID_ABOUT, '&About', 'About this program')
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, 'E&xit', 'Terminate the program')

        self.SetMenuBar(menu_bar)

        self.Show(True)

app = wx.App(False)
frame = MainWindow(None, 'Simple editor')
app.MainLoop()
