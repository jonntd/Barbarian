# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/workspace/Barbarian/commons/ui/CGTW.ui'
#
# Created: Wed Oct 25 09:38:26 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from barbarian.utils import ui, config

class Ui_CGTWWin(ui.QtUI):
    def setupUi(self, CGTWWin):
        CGTWWin.setObjectName("CGTWWin")
        CGTWWin.resize(800, 480)
        CGTWWin.setMinimumSize(QtCore.QSize(800, 480))
        self.centralwidget = QtGui.QWidget(CGTWWin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.CGTWCBProject = ui.QOptionMenu(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CGTWCBProject.sizePolicy().hasHeightForWidth())
        self.CGTWCBProject.setSizePolicy(sizePolicy)
        self.CGTWCBProject.setMinimumSize(QtCore.QSize(85, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.CGTWCBProject.setFont(font)
        self.CGTWCBProject.setObjectName("CGTWCBProject")
        self.horizontalLayout.addWidget(self.CGTWCBProject)
        self.CGTWLBLUser = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CGTWLBLUser.sizePolicy().hasHeightForWidth())
        self.CGTWLBLUser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.CGTWLBLUser.setFont(font)
        self.CGTWLBLUser.setText("")
        self.CGTWLBLUser.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CGTWLBLUser.setObjectName("CGTWLBLUser")
        self.horizontalLayout.addWidget(self.CGTWLBLUser)
        self.CGTWLEUsername = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CGTWLEUsername.sizePolicy().hasHeightForWidth())
        self.CGTWLEUsername.setSizePolicy(sizePolicy)
        self.CGTWLEUsername.setMinimumSize(QtCore.QSize(100, 30))
        self.CGTWLEUsername.setMaximumSize(QtCore.QSize(100, 16777215))
        self.CGTWLEUsername.setAlignment(QtCore.Qt.AlignCenter)
        self.CGTWLEUsername.setObjectName("CGTWLEUsername")
        self.horizontalLayout.addWidget(self.CGTWLEUsername)
        self.CGTWLEPassword = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CGTWLEPassword.sizePolicy().hasHeightForWidth())
        self.CGTWLEPassword.setSizePolicy(sizePolicy)
        self.CGTWLEPassword.setMinimumSize(QtCore.QSize(100, 30))
        self.CGTWLEPassword.setMaximumSize(QtCore.QSize(100, 16777215))
        self.CGTWLEPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.CGTWLEPassword.setObjectName("CGTWLEPassword")
        self.horizontalLayout.addWidget(self.CGTWLEPassword)
        self.CGTWBtnConnect = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CGTWBtnConnect.sizePolicy().hasHeightForWidth())
        self.CGTWBtnConnect.setSizePolicy(sizePolicy)
        self.CGTWBtnConnect.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.CGTWBtnConnect.setFont(font)
        self.CGTWBtnConnect.setObjectName("CGTWBtnConnect")
        self.horizontalLayout.addWidget(self.CGTWBtnConnect)
        self.CGTWLEDeregister = QtGui.QPushButton(self.centralwidget)
        self.CGTWLEDeregister.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.CGTWLEDeregister.setFont(font)
        self.CGTWLEDeregister.setObjectName("CGTWLEDeregister")
        self.horizontalLayout.addWidget(self.CGTWLEDeregister)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.treeWidget.setFont(font)
        self.treeWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(80)
        self.treeWidget.header().setMinimumSectionSize(30)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.CGTWPyblish = QtGui.QWidget(self.centralwidget)
        self.CGTWPyblish.setMinimumSize(QtCore.QSize(300, 0))
        self.CGTWPyblish.setMaximumSize(QtCore.QSize(300, 16777215))
        self.CGTWPyblish.setObjectName("CGTWPyblish")
        self.pyblishLayout = QtGui.QVBoxLayout(self.CGTWPyblish)
        self.pyblishLayout.setSpacing(0)
        self.pyblishLayout.setContentsMargins(0, 0, 0, 0)
        self.pyblishLayout.setContentsMargins(0, 0, 0, 0)
        self.pyblishLayout.setObjectName("pyblishLayout")
        self.horizontalLayout_2.addWidget(self.CGTWPyblish)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(2, 1)
        CGTWWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(CGTWWin)
        QtCore.QMetaObject.connectSlotsByName(CGTWWin)

    def retranslateUi(self, CGTWWin):
        CGTWWin.setWindowTitle(QtGui.QApplication.translate("CGTWWin", "Teamwork", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CGTWWin", "项目：", None, QtGui.QApplication.UnicodeUTF8))
        self.CGTWBtnConnect.setText(QtGui.QApplication.translate("CGTWWin", "登录", None, QtGui.QApplication.UnicodeUTF8))
        self.CGTWLEDeregister.setText(QtGui.QApplication.translate("CGTWWin", "注销", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CGTWWin", "我的任务：", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("CGTWWin", " ", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("CGTWWin", "状态", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("CGTWWin", "截止日期", None, QtGui.QApplication.UnicodeUTF8))

