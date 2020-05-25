import datetime
from threading import Thread
import cv2

class VideoStream:
  def __init__(self, src = 0):
    self.stream = cv2.VideoCapture(src)
    self.flag = self.stream.isOpened()
    if self.flag:
      self.grabbed, self.frame = self.stream.read()

    self.stopped = False
    self.frame_fps = 0

  def start(self):
    # Bat dau Thread de doc du lieu tu camera vao
    Thread(target=self.update, args=()).start()

    return self
  
  def update(self):
    while True:
      if self.stopped:
        return
      
      self.grabbed , self.frame = self.stream.read()
  
  def read(self):
    return self.frame

  def stop(self):
    self.stopped = True

  def get_FPS(self):
    self.frame_fps = self.stream.get(cv2.CAP_PROP_FPS)
    return self.frame_fps