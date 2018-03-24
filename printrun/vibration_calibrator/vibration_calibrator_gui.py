import wx

class VibrationCalibratorMainWindow(wx.Frame):

    def __init__(self, parent, vibration_calibrator):
        wx.Frame.__init__(self, parent,
                          title = "Vibration Calibrator",
                          style = wx.DEFAULT_FRAME_STYLE | wx.FRAME_FLOAT_ON_PARENT)
