from printrun import pronsole


class VibrationCalibrator(object):

    def __init__(self, parent):
        self.parent = parent # type: pronsole.pronsole

    def start_analysis(self):
        if self.parent.p.online:
            self.parent.p.send_now("G28") # Home all axis
