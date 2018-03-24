import wx

class VibrationCalibratorMainWindow(wx.Frame):

    def __init__(self, parent, vibration_calibrator):
        wx.Frame.__init__(self, parent,
                          title = "Vibration Calibrator",
                          style = wx.DEFAULT_FRAME_STYLE | wx.FRAME_FLOAT_ON_PARENT)

        self.vibration_calibrator = vibration_calibrator

        self.stop_button = wx.Button(parent=self, label="Stop")

        self.start_analysis_button = wx.Button(parent=self, label="Start")

        self.analyzis_sizer = wx.StaticBoxSizer(orient=wx.VERTICAL, parent=self, label="Analysis")
        self.analyzis_sizer.Add(self.start_analysis_button)


        self.full_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.full_sizer.Add(self.stop_button)
        self.full_sizer.Add(self.analyzis_sizer)
        self.full_sizer.SetSizeHints(self)


        self.SetSizer(self.full_sizer)

        self.start_analysis_button.Bind(wx.EVT_BUTTON, self.onClickStartAnalysis)

    def onClickStartAnalysis(self, event):
        self.vibration_calibrator.start_analysis()
