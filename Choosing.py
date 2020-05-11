# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Choosing.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from MainUI import Ui_MainWindow
class Ui_Form(object):
    def openNewWindow(self):
        feature= {
        'car1': self.carCAM1.isChecked(),
        'mpa1': self.monitorCAM1.isChecked(),
        'person1': self.personSearchingCAM1.isChecked(),
        'illegal1': self.illegalCAM1.isChecked(),

        'car2': self.carCAM2.isChecked(),
        'mpa2': self.monitorCAM2.isChecked(),
        'person2': self.personSearchingCAM2.isChecked(),
        'illegal2': self.illegalCAM2.isChecked(),   

        'car3': self.carCAM3.isChecked(),
        'mpa3': self.monitorCAM3.isChecked(),
        'person3': self.personSearchingCAM3.isChecked(),
        'illegal3': self.illegalCAM3.isChecked()
        }
        self.window = QtWidgets.QWidget()
        self.ui = Ui_MainWindow(feature=feature)
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()
        print(feature)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(229, 495)
        Form.setMaximumSize(QtCore.QSize(229, 495))
        self.finishBtn = QtWidgets.QPushButton(Form)
        self.finishBtn.setGeometry(QtCore.QRect(60, 440, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.finishBtn.setFont(font)
        self.finishBtn.setObjectName("finishBtn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 300, 159, 116))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_6.addWidget(self.label_19)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.monitorCAM3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.monitorCAM3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.monitorCAM3.setText("")
        self.monitorCAM3.setObjectName("monitorCAM3")
        self.horizontalLayout_9.addWidget(self.monitorCAM3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.carCAM3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.carCAM3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.carCAM3.setText("")
        self.carCAM3.setObjectName("carCAM3")
        self.horizontalLayout_10.addWidget(self.carCAM3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.illegalCAM3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.illegalCAM3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.illegalCAM3.setText("")
        self.illegalCAM3.setObjectName("illegalCAM3")
        self.horizontalLayout_11.addWidget(self.illegalCAM3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.personSearchingCAM3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.personSearchingCAM3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.personSearchingCAM3.setText("")
        self.personSearchingCAM3.setObjectName("personSearchingCAM3")
        self.horizontalLayout_12.addWidget(self.personSearchingCAM3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 20, 159, 116))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_7.addWidget(self.label_17)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.monitorCAM1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.monitorCAM1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.monitorCAM1.setText("")
        self.monitorCAM1.setObjectName("monitorCAM1")
        self.horizontalLayout.addWidget(self.monitorCAM1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.carCAM1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.carCAM1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.carCAM1.setText("")
        self.carCAM1.setObjectName("carCAM1")
        self.horizontalLayout_2.addWidget(self.carCAM1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.illegalCAM1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.illegalCAM1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.illegalCAM1.setText("")
        self.illegalCAM1.setObjectName("illegalCAM1")
        self.horizontalLayout_3.addWidget(self.illegalCAM1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.personSearchingCAM1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.personSearchingCAM1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.personSearchingCAM1.setText("")
        self.personSearchingCAM1.setObjectName("personSearchingCAM1")
        self.horizontalLayout_4.addWidget(self.personSearchingCAM1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 160, 159, 116))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.monitorCAM2 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.monitorCAM2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.monitorCAM2.setText("")
        self.monitorCAM2.setObjectName("monitorCAM2")
        self.horizontalLayout_5.addWidget(self.monitorCAM2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.carCAM2 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.carCAM2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.carCAM2.setText("")
        self.carCAM2.setObjectName("carCAM2")
        self.horizontalLayout_6.addWidget(self.carCAM2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.illegalCAM2 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.illegalCAM2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.illegalCAM2.setText("")
        self.illegalCAM2.setObjectName("illegalCAM2")
        self.horizontalLayout_7.addWidget(self.illegalCAM2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.personSearchingCAM2 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.personSearchingCAM2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.personSearchingCAM2.setText("")
        self.personSearchingCAM2.setObjectName("personSearchingCAM2")
        self.horizontalLayout_8.addWidget(self.personSearchingCAM2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.finishBtn.clicked.connect(self.openNewWindow)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.finishBtn.setText(_translate("Form", "FINISH"))
        self.label_19.setText(_translate("Form", "IP - CAM III"))
        self.label_9.setText(_translate("Form", "Monitor Prohibited area"))
        self.label_10.setText(_translate("Form", "Car protection"))
        self.label_11.setText(_translate("Form", "Illegal access action"))
        self.label_12.setText(_translate("Form", "Persion Searching"))
        self.label_17.setText(_translate("Form", "IP - CAM I"))
        self.label.setText(_translate("Form", "Monitor Prohibited area"))
        self.label_2.setText(_translate("Form", "Car protection"))
        self.label_3.setText(_translate("Form", "Illegal access action"))
        self.label_4.setText(_translate("Form", "Persion Searching"))
        self.label_18.setText(_translate("Form", "IP - CAM II"))
        self.label_5.setText(_translate("Form", "Monitor Prohibited area"))
        self.label_6.setText(_translate("Form", "Car protection"))
        self.label_7.setText(_translate("Form", "Illegal access action"))
        self.label_8.setText(_translate("Form", "Persion Searching"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())