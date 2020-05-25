#Test send email
# gmail_user = 'yoonalearning@gmail.com'
# gmail_password = 'yeuyoona98'

# sent_from = gmail_user

# to = ['yoonachien@gmail.com']
# subject = 'Warning Message'
# body = 'Ha Noi University of Science and Technology'
# message = 'Subject: {}\n\n{}'.format(subject, body)

# import smtplib

# server = smtplib.SMTP('smtp.gmail.com', 587)

# server.starttls()
# server.login(gmail_user, gmail_password)
# server.sendmail(sent_from, to, message)
# server.quit()


# Test draw point
# import cv2
# from threading import Thread
# image = cv2.imread('/home/yoona/Pictures/84534587_2692473420836014_4507958916096720896_o.jpg')
# def getPoint(image):
#   (width, height) = image.shape[:2]
#   return int(0.7 * width), int(0.2 * height)
# def showImage(image, sizeImage:tuple, windowName:str):
#   image_show = image.copy()
#   image_show = cv2.resize(image_show, sizeImage)
#   width, height = getPoint(image_show)
#   cv2.circle(image_show, (width, height), radius=0, color=(0, 0, 255), thickness= 10)
#   cv2.imshow(windowName, image_show)


# image1 = image.copy()
# image1 = cv2.resize(image1, (640, 480))
# w1, h1 = getPoint(image1)
# cv2.circle(image1, (w1, h1), radius=0, color=(0, 0, 255), thickness=9)

# image2 = image.copy()
# image2 = cv2.resize(image2, (980, 720))
# w2, h2 = getPoint(image2)
# cv2.circle(image2, (w2, h2), radius=0, color=(0, 0, 255), thickness=9)


# cv2.imshow("1", image1)
# cv2.imshow('2', image2)

# cv2.waitKey(0)

# print('ok')


# Test send SMS
# from twilio.rest import Client


# # Your Account Sid and Auth Token from twilio.com/console
# # DANGER! This is insecure. See http://twil.io/secure
# account_sid = 'ACb0f57f89aed94e673c4d2ff094c53ff4'
# auth_token = '4804e39f1e6519ebd675dd73af2e5b2b'
# client = Client(account_sid, auth_token)

# message = client.messages \
#     .create(
#          body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#          messaging_service_sid='MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
#          to='+84812749258'
#      )

# print(message.sid)

# from twilio.rest import Client


# # Your Account Sid and Auth Token from twilio.com/console
# # DANGER! This is insecure. See http://twil.io/secure
# account_sid = 'ACb0f57f89aed94e673c4d2ff094c53ff4'
# auth_token = '4804e39f1e6519ebd675dd73af2e5b2b'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               from_='+12057820497',
#                               body='Le Minh Chien Someone are entering the restricted area',
#                               to='+84812749258'
#                           )

# print(message.sid)


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QGridLayout, \
    QHBoxLayout, QVBoxLayout, QLabel, QSlider, QStyle, QSizePolicy, QFileDialog, QDialog
from PyQt5.QtGui import QIcon, QPalette, QImage, QPixmap, QMouseEvent
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QUrl, QTimer
import sys
class Form(QDialog):
   def __init__(self, parent=None):
      super(Form, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.b1 = QPushButton("Button1")
      self.b1.setCheckable(True)
      # self.b1.toggle()
      self.b1.clicked.connect(lambda:self.whichbtn(self.b1))
      self.b1.clicked.connect(self.btnstate)
      layout.addWidget(self.b1)
		
      self.b2 = QPushButton()
      self.b2.setIcon(QIcon(QPixmap("python.gif")))
      self.b2.clicked.connect(lambda:self.whichbtn(self.b2))
      layout.addWidget(self.b2)
      self.setLayout(layout)
      self.b3 = QPushButton("Disabled")
      self.b3.setEnabled(False)
      layout.addWidget(self.b3)
		
      self.b4 = QPushButton("&Default")
      self.b4.setDefault(True)
      self.b4.clicked.connect(lambda:self.whichbtn(self.b4))
      layout.addWidget(self.b4)
      
      self.setWindowTitle("Button demo")

   def btnstate(self):
      if self.b1.isChecked():
         print ("button pressed")
      else:
         print ("button released")
			
   def whichbtn(self,b):
      print ("clicked button is "+b.text())

def main():
   app = QApplication(sys.argv)
   ex = Form()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()