# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultsBA.ui'
#
# Created: Wed Jan 13 17:29:23 2010
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form3(object):
    def setupUi(self, Form3):
        Form3.setObjectName("Form3")
        Form3.resize(715, 250)
        self.gridlayout = QtGui.QGridLayout(Form3)
        self.gridlayout.setMargin(11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.infoTabWidget = QtGui.QTabWidget(Form3)
        self.infoTabWidget.setObjectName("infoTabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.vboxlayout = QtGui.QVBoxLayout(self.tab)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setMargin(11)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupListView = QtGui.QTreeWidget(self.tab)
        self.groupListView.setRootIsDecorated(False)
        self.groupListView.setAllColumnsShowFocus(True)
        self.groupListView.setProperty("showSortIndicator", QtCore.QVariant(True))
        self.groupListView.setObjectName("groupListView")
        self.vboxlayout.addWidget(self.groupListView)
        self.infoTabWidget.addTab(self.tab, "")
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName("tab1")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab1)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setMargin(11)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.matchTextBrowser = QtGui.QTextBrowser(self.tab1)
        self.matchTextBrowser.setObjectName("matchTextBrowser")
        self.vboxlayout1.addWidget(self.matchTextBrowser)
        self.infoTabWidget.addTab(self.tab1, "")
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName("tab2")
        self.vboxlayout2 = QtGui.QVBoxLayout(self.tab2)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setMargin(11)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.codeTextBrowser = QtGui.QTextBrowser(self.tab2)
        self.codeTextBrowser.setObjectName("codeTextBrowser")
        self.vboxlayout2.addWidget(self.codeTextBrowser)
        self.infoTabWidget.addTab(self.tab2, "")
        self.gridlayout.addWidget(self.infoTabWidget, 1, 0, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.TextLabel3 = QtGui.QLabel(Form3)
        self.TextLabel3.setWordWrap(False)
        self.TextLabel3.setObjectName("TextLabel3")
        self.hboxlayout.addWidget(self.TextLabel3)
        self.matchNumberSpinBox = QtGui.QSpinBox(Form3)
        self.matchNumberSpinBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matchNumberSpinBox.sizePolicy().hasHeightForWidth())
        self.matchNumberSpinBox.setSizePolicy(sizePolicy)
        self.matchNumberSpinBox.setMinimum(1)
        self.matchNumberSpinBox.setObjectName("matchNumberSpinBox")
        self.hboxlayout.addWidget(self.matchNumberSpinBox)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.gridlayout.addLayout(self.hboxlayout, 0, 0, 1, 1)

        self.retranslateUi(Form3)
        self.infoTabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.matchNumberSpinBox, QtCore.SIGNAL("valueChanged(int)"), self.matchNumberSpinBox.match_num_slot)
        QtCore.QMetaObject.connectSlotsByName(Form3)

    def retranslateUi(self, Form3):
        Form3.setWindowTitle(QtGui.QApplication.translate("Form3", "Form3", None, QtGui.QApplication.UnicodeUTF8))
        self.groupListView.headerItem().setText(0, QtGui.QApplication.translate("Form3", "Group #", None, QtGui.QApplication.UnicodeUTF8))
        self.groupListView.headerItem().setText(1, QtGui.QApplication.translate("Form3", "Group Name", None, QtGui.QApplication.UnicodeUTF8))
        self.groupListView.headerItem().setText(2, QtGui.QApplication.translate("Form3", "Match", None, QtGui.QApplication.UnicodeUTF8))
        self.infoTabWidget.setTabText(self.infoTabWidget.indexOf(self.tab), QtGui.QApplication.translate("Form3", "Group", None, QtGui.QApplication.UnicodeUTF8))
        self.infoTabWidget.setTabText(self.infoTabWidget.indexOf(self.tab1), QtGui.QApplication.translate("Form3", "Match", None, QtGui.QApplication.UnicodeUTF8))
        self.infoTabWidget.setTabText(self.infoTabWidget.indexOf(self.tab2), QtGui.QApplication.translate("Form3", "Sample Code", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel3.setText(QtGui.QApplication.translate("Form3", "Match number:", None, QtGui.QApplication.UnicodeUTF8))


class Form3(QtGui.QWidget, Ui_Form3):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

