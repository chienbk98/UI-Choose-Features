import cv2
import numpy as np
import datetime
from lib_warning import *
from playsound import playsound
from threading import Thread

bkgM = cv2.createBackgroundSubtractorMOG2(500, 51, 1)
kernelOp = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

kernelCl = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))

def backgroundSubtraction(frame, bkg_list):
  fgmask = bkgM.apply(frame)

  fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernelOp)

  fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernelCl)

  _, fgmask = cv2.threshold(fgmask, 150, 255, cv2.THRESH_BINARY)

  (contours, hierachy) = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  if len(contours) != 0:
    for idx in contours:
      approx = cv2.approxPolyDP(idx, 5, 1) # Đưa tập hợp điểm trong contour về dưới dạng đa giác.
      s = cv2.contourArea(approx)
      x, y, w, h = cv2.boundingRect(approx)
      if (w*h > 900):
        bkg_list.append((x, y, w, h))
  return bkg_list

def remove_list(name_list):
  if(len(name_list)!=0):
    for i in range(len(name_list)):
      name_list.pop()


def detectObject(frame, points:list, flag_Warning, numWarning):
  """
  points : list points of Polygon
  flag_Warning: flag to choose warning type:
  0 - send email,
  1 - send SMS,
  2 - make a Call,
  3 - sound,
  """
  bkg_list = []

  Canhbao = WarningMessage()


  frame  = cv2.resize(frame, (1280, 720))
  point1 = []
  for point in points:
    x = point[0] * 1280
    y = point[1] * 720
    point1.append((int(x), int(y)))
  bkg_list = backgroundSubtraction(frame, bkg_list)

  for va in bkg_list:
    x_center, y_center = int(va[0] + va[2]/2), int(va[1] + va[3])
    cv2.circle(frame, center=(x_center, y_center), radius=0, color=(0, 255, 0), thickness= 7)
    if len(point1) > 2:
      dist = cv2.pointPolygonTest(np.array([point1]), (x_center, y_center), False)
      if dist > 0 and numWarning == 0:
        # Canhbao.start()
        # if flag_Warning == 0:
        #   sendemail(message)
        #   pass
        # elif flag_Warning == 1:
        #   sendSMS()
        #   pass
        # elif flag_Warning == 2:
        #   makeCall()
        #   pass
        # elif flag_Warning == 3:
        #   soundWarning()
        #   pass
        # else:
          print('<<<<<<< Warning >>>>>>>', datetime.datetime.now())
        # numWarning = numWarning + 1
    cv2.rectangle(frame, (va[0], va[1]), (va[0] + va[2], va[1]+va[3]), (255, 0, 0), 2, 1)
  remove_list(bkg_list)

  return frame, numWarning


class WarningMessage:
  def __init__(self):
    pass

  def start(self):
    Thread(target=self.play(), args=()).start
    return self
    pass

  def play(self):
    playsound('warning.mp3')
