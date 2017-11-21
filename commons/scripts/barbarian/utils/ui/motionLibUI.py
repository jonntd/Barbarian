# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/workspace_Python/PutaoTools/commons/ui/motionLib.ui'
#
# Created: Mon Sep 11 23:17:29 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from barbarian.utils import ui, config

class Ui_motionLibOption(ui.QtUI):
    def setupUi(self, motionLibOption):
        motionLibOption.setObjectName("motionLibOption")
        motionLibOption.resize(494, 647)
        motionLibOption.setMinimumSize(QtCore.QSize(494, 647))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        motionLibOption.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(config.getPath(config.kIcon, "logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        motionLibOption.setWindowIcon(icon)
        
        self.motionLibCentralwidget = QtGui.QWidget(motionLibOption)
        self.motionLibCentralwidget.setObjectName("motionLibCentralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.motionLibCentralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Label = QtGui.QLabel(self.motionLibCentralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.Label.setFont(font)
        self.Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label.setObjectName("Label")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.Label)
        self.motionLibCBProject = ui.OptionMenu(self.motionLibCentralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motionLibCBProject.sizePolicy().hasHeightForWidth())
        self.motionLibCBProject.setSizePolicy(sizePolicy)
        self.motionLibCBProject.setMinimumSize(QtCore.QSize(85, 30))
        self.motionLibCBProject.setMaximumSize(QtCore.QSize(85, 16777215))
        self.motionLibCBProject.setObjectName("motionLibCBProject")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.motionLibCBProject)
        self.Label_2 = QtGui.QLabel(self.motionLibCentralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.Label_2.setFont(font)
        self.Label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_2.setObjectName("Label_2")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.Label_2)
        self.motionLibCBCharactor = QtGui.QComboBox(self.motionLibCentralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motionLibCBCharactor.sizePolicy().hasHeightForWidth())
        self.motionLibCBCharactor.setSizePolicy(sizePolicy)
        self.motionLibCBCharactor.setMinimumSize(QtCore.QSize(0, 30))
        self.motionLibCBCharactor.setMaximumSize(QtCore.QSize(282, 16777215))
        self.motionLibCBCharactor.setObjectName("motionLibCBCharactor")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.motionLibCBCharactor)
        self.label_6 = QtGui.QLabel(self.motionLibCentralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.motionLibLEFilter = QtGui.QLineEdit(self.motionLibCentralwidget)
        self.motionLibLEFilter.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.motionLibLEFilter.setFont(font)
        self.motionLibLEFilter.setObjectName("motionLibLEFilter")
        self.horizontalLayout_4.addWidget(self.motionLibLEFilter)
        self.motionLibHSView = QtGui.QSlider(self.motionLibCentralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motionLibHSView.sizePolicy().hasHeightForWidth())
        self.motionLibHSView.setSizePolicy(sizePolicy)
        self.motionLibHSView.setMinimumSize(QtCore.QSize(0, 30))
        self.motionLibHSView.setMaximumSize(QtCore.QSize(50, 16777215))
        self.motionLibHSView.setMinimum(0)
        self.motionLibHSView.setMaximum(1)
        self.motionLibHSView.setOrientation(QtCore.Qt.Horizontal)
        self.motionLibHSView.setObjectName("motionLibHSView")
        self.horizontalLayout_4.addWidget(self.motionLibHSView)
        self.formLayout_2.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        
        self.shelf = ui.QShelfView(self.motionLibCentralwidget)
        
        self.verticalLayout_2.addWidget(self.shelf)
        self.motionLibTab = QtGui.QTabWidget(self.motionLibCentralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.motionLibTab.setFont(font)
        self.motionLibTab.setTabPosition(QtGui.QTabWidget.North)
        self.motionLibTab.setObjectName("motionLibTab")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.tab)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.motionLibHSCopies = QtGui.QSlider(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motionLibHSCopies.sizePolicy().hasHeightForWidth())
        self.motionLibHSCopies.setSizePolicy(sizePolicy)
        self.motionLibHSCopies.setMinimumSize(QtCore.QSize(0, 30))
        self.motionLibHSCopies.setMinimum(1)
        self.motionLibHSCopies.setMaximum(10)
        self.motionLibHSCopies.setOrientation(QtCore.Qt.Horizontal)
        self.motionLibHSCopies.setObjectName("motionLibHSCopies")
        self.horizontalLayout_3.addWidget(self.motionLibHSCopies)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setMinimumSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.motionLibRBInsert = QtGui.QRadioButton(self.tab)
        self.motionLibRBInsert.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.motionLibRBInsert.setFont(font)
        self.motionLibRBInsert.setChecked(True)
        self.motionLibRBInsert.setObjectName("motionLibRBInsert")
        self.horizontalLayout_2.addWidget(self.motionLibRBInsert)
        self.motionLibRBMerge = QtGui.QRadioButton(self.tab)
        self.motionLibRBMerge.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.motionLibRBMerge.setFont(font)
        self.motionLibRBMerge.setObjectName("motionLibRBMerge")
        self.horizontalLayout_2.addWidget(self.motionLibRBMerge)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.verticalLayout.addLayout(self.formLayout)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.motionLibBtnImport = QtGui.QPushButton(self.tab)
        self.motionLibBtnImport.setMinimumSize(QtCore.QSize(0, 50))
        self.motionLibBtnImport.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.motionLibBtnImport.setFont(font)
        self.motionLibBtnImport.setObjectName("motionLibBtnImport")
        self.verticalLayout.addWidget(self.motionLibBtnImport)
        self.verticalLayout.setStretch(0, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(config.getPath(config.kIcon, "arrowDown.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.motionLibTab.addTab(self.tab, icon1, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.motionLibLEExportFile = QtGui.QLineEdit(self.tab_2)
        self.motionLibLEExportFile.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.motionLibLEExportFile.setFont(font)
        self.motionLibLEExportFile.setObjectName("motionLibLEExportFile")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.motionLibLEExportFile)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.motionLibLEExportStart = QtGui.QLineEdit(self.tab_2)
        self.motionLibLEExportStart.setMinimumSize(QtCore.QSize(50, 28))
        self.motionLibLEExportStart.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.motionLibLEExportStart.setFont(font)
        self.motionLibLEExportStart.setMaxLength(4)
        self.motionLibLEExportStart.setAlignment(QtCore.Qt.AlignCenter)
        self.motionLibLEExportStart.setObjectName("motionLibLEExportStart")
        self.horizontalLayout.addWidget(self.motionLibLEExportStart)
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.motionLibLEExportEnd = QtGui.QLineEdit(self.tab_2)
        self.motionLibLEExportEnd.setMinimumSize(QtCore.QSize(50, 28))
        self.motionLibLEExportEnd.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.motionLibLEExportEnd.setFont(font)
        self.motionLibLEExportEnd.setMaxLength(4)
        self.motionLibLEExportEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.motionLibLEExportEnd.setObjectName("motionLibLEExportEnd")
        self.horizontalLayout.addWidget(self.motionLibLEExportEnd)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.formLayout_3.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.line_2 = QtGui.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.motionLibBtnExport = QtGui.QPushButton(self.tab_2)
        self.motionLibBtnExport.setEnabled(False)
        self.motionLibBtnExport.setMinimumSize(QtCore.QSize(0, 50))
        self.motionLibBtnExport.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.motionLibBtnExport.setFont(font)
        self.motionLibBtnExport.setObjectName("motionLibBtnExport")
        self.verticalLayout_3.addWidget(self.motionLibBtnExport)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(config.getPath(config.kIcon, "arrowUp.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.motionLibTab.addTab(self.tab_2, icon2, "")
        self.verticalLayout_2.addWidget(self.motionLibTab)
        self.verticalLayout_2.setStretch(1, 1)
        motionLibOption.setCentralWidget(self.motionLibCentralwidget)

        self.retranslateUi(motionLibOption)
        self.motionLibTab.setCurrentIndex(0)
        QtCore.QObject.connect(self.motionLibHSCopies, QtCore.SIGNAL("valueChanged(int)"), self.label_2.setNum)
        QtCore.QMetaObject.connectSlotsByName(motionLibOption)

    def retranslateUi(self, motionLibOption):
        motionLibOption.setWindowTitle(QtGui.QApplication.translate("motionLibOption", "动作库", None, QtGui.QApplication.UnicodeUTF8))
        self.Label.setText(QtGui.QApplication.translate("motionLibOption", "项目：", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_2.setText(QtGui.QApplication.translate("motionLibOption", "角色：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("motionLibOption", "筛选：", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("motionLibOption", "循环：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("motionLibOption", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.motionLibRBInsert.setText(QtGui.QApplication.translate("motionLibOption", "插入", None, QtGui.QApplication.UnicodeUTF8))
        self.motionLibRBMerge.setText(QtGui.QApplication.translate("motionLibOption", "混合", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("motionLibOption", "模式：", None, QtGui.QApplication.UnicodeUTF8))
        self.motionLibBtnImport.setText(QtGui.QApplication.translate("motionLibOption", "导入", None, QtGui.QApplication.UnicodeUTF8))
        self.motionLibTab.setTabText(self.motionLibTab.indexOf(self.tab), QtGui.QApplication.translate("motionLibOption", "导入", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("motionLibOption", "帧范围：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("motionLibOption", "文件名：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("motionLibOption", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.motionLibBtnExport.setText(QtGui.QApplication.translate("motionLibOption", "导出", None, QtGui.QApplication.UnicodeUTF8))
        self.motionLibTab.setTabText(self.motionLibTab.indexOf(self.tab_2), QtGui.QApplication.translate("motionLibOption", "导出", None, QtGui.QApplication.UnicodeUTF8))

