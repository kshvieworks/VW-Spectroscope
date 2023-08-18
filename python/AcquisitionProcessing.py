"""
Camera Acquisition Processing
"""
import threading
import queue
import os
import sys
import numpy as np
import time
import cv2
from PIL import Image
from PyQt6 import QtCore


try:
    from AddLibraryPath import configure_path
    configure_path()
except ImportError:
    configure_path = None

import sCMOSs

class getFrame(QtCore.QThread):
    FrameUpdate = QtCore.pyqtSignal(np.ndarray)
    def __init__(self, parent=None):
        QtCore.QObject.__init__(self)
        self.Camera = sCMOSs.VwCAM()
        self.Camera.OpenCamera()
        self.Camera.Grab()
        time.sleep(0.1)
    def run(self):
        self.ThreadActive = True
        while self.ThreadActive:
            pic = self.Camera.getImage()
            self.FrameUpdate.emit(pic)