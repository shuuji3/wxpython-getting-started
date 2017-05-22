#!/usr/bin/env python3
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello world")
frame.Show(True)
app.MainLoop()
