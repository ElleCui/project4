import wx
class MyFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, title=''):
        wx.Frame.__init__(self, parent, id, title, size=(800, 1500))
        top = wx.Panel(self,-1)
        sizer = wx.BoxSizer(wx.VERTICAL)
        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        lb = wx.StaticText(top, -1, 'Configuration')
        sizer.Add(lb)

        c1 = wx.StaticText(top, -1, 'protocol')
        c1.SetFont(font)
        c1_01 = wx.StaticText(top, -1, 'choosing a new protocol restarts the simulation')
        ct = wx.ComboBox(top, -1, '', choices=('Go back N', 'Selective Repeat'))
        sizer.Add(c1)
        sizer.Add(c1_01)
        sizer.Add(ct)

        c2 = wx.StaticText(top, -1, 'window size')
        c2_01 = wx.StaticText(top, -1, 'sets the window size for windows')
        c2.SetFont(font)
        slider = wx.Slider(top, -1, 5, 1, 10, wx.DefaultPosition, (250,-1), style= wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        sizer.Add(c2)
        sizer.Add(c2_01)
        sizer.Add(slider)

        c3 = wx.StaticText(top, -1, 'end to end delay')
        c3_01 = wx.StaticText(top, -1, 'time a packet takes from one station to the other')
        c3.SetFont(font)
        slider = wx.Slider(top, -1, 10000, 1000, 20000, wx.DefaultPosition, (250,-1), style= wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        sizer.Add(c3)
        sizer.Add(c3_01)
        sizer.Add(slider)

        c4 = wx.StaticText(top, -1, 'time out')
        c4.SetFont(font)
        slider = wx.Slider(top, -1, 20000, 1000, 30000, wx.DefaultPosition, (250,-1), style= wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        sizer.Add(c4)
        sizer.Add(slider)

        c5 = wx.StaticText(top, -1, 'scroll mode')
        c5.SetFont(font)
        c5_01 = wx.StaticText(top, -1, 'change the style the window scrolls')
        cb = wx.ComboBox(top, -1, '', choices=('Typewrite', 'Fixed sender Windo'))
        sizer.Add(c5)
        sizer.Add(c5_01)
        sizer.Add(cb)

        c6 = wx.StaticText(top, -1, 'number of packets the upper layer tries to send per minute')
        c6_01 = wx.StaticText(top, -1, 'the number of packets the upper layer tries to spend per minute')
        c6.SetFont(font)
        slider = wx.Slider(top, -1, 60, 1, 120, wx.DefaultPosition, (250,-1), style= wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        sizer.Add(c6)
        sizer.Add(c6_01)
        sizer.Add(slider)

        start = wx.Button(top, -1, "start")
        start.SetBackgroundColour('green')
        start.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, lambda e: self.Close(True), start)
        sizer.Add(start)




        qb = wx.Button(top, -1, "QUIT")
        qb.SetBackgroundColour('red')
        qb.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, lambda e: self.Close(True), qb)
        sizer.Add(qb)

        top.SetSizer(sizer)
        self.Layout()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(title="Selective Repeat/Go Back N")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True
def main():
    app = MyApp()
    app.MainLoop()

if __name__ == '__main__':
    main()
