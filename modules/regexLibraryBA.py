# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regexLibraryBA.ui'
#
# Created: Wed Jan 13 23:30:07 2010
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RegexLibraryBA(object):
    def setupUi(self, RegexLibraryBA):
        RegexLibraryBA.setObjectName("RegexLibraryBA")
        RegexLibraryBA.resize(491, 490)
        self.widget = QtGui.QWidget(RegexLibraryBA)
        self.widget.setObjectName("widget")
        self.gridlayout = QtGui.QGridLayout(self.widget)
        self.gridlayout.setObjectName("gridlayout")
        self.groupBox5 = QtGui.QGroupBox(self.widget)
        self.groupBox5.setObjectName("groupBox5")
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox5)
        self.gridlayout1.setObjectName("gridlayout1")
        self.descriptionListBox = QtGui.QListWidget(self.groupBox5)
        self.descriptionListBox.setObjectName("descriptionListBox")
        self.gridlayout1.addWidget(self.descriptionListBox, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.groupBox5, 0, 0, 1, 1)
        self.tabWidget3 = QtGui.QTabWidget(self.widget)
        self.tabWidget3.setObjectName("tabWidget3")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridlayout2 = QtGui.QGridLayout(self.tab)
        self.gridlayout2.setObjectName("gridlayout2")
        self.regexTextBrowser = QtGui.QTextBrowser(self.tab)
        self.regexTextBrowser.setObjectName("regexTextBrowser")
        self.gridlayout2.addWidget(self.regexTextBrowser, 0, 0, 1, 1)
        self.tabWidget3.addTab(self.tab, "")
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridlayout3 = QtGui.QGridLayout(self.tab1)
        self.gridlayout3.setObjectName("gridlayout3")
        self.noteTextBrowser = QtGui.QTextBrowser(self.tab1)
        self.noteTextBrowser.setObjectName("noteTextBrowser")
        self.gridlayout3.addWidget(self.noteTextBrowser, 0, 0, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.textLabel3 = QtGui.QLabel(self.tab1)
        self.textLabel3.setWordWrap(False)
        self.textLabel3.setObjectName("textLabel3")
        self.hboxlayout.addWidget(self.textLabel3)
        self.contribEdit = QtGui.QLineEdit(self.tab1)
        self.contribEdit.setReadOnly(True)
        self.contribEdit.setObjectName("contribEdit")
        self.hboxlayout.addWidget(self.contribEdit)
        self.gridlayout3.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.tabWidget3.addTab(self.tab1, "")
        self.gridlayout.addWidget(self.tabWidget3, 1, 0, 1, 1)
        RegexLibraryBA.setCentralWidget(self.widget)
        self.toolBar = QtGui.QToolBar(RegexLibraryBA)
        self.toolBar.setProperty("label", QtCore.QVariant(QtGui.QApplication.translate("RegexLibraryBA", "Tools", None, QtGui.QApplication.UnicodeUTF8)))
        self.toolBar.setObjectName("toolBar")
        RegexLibraryBA.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.MenuBar = QtGui.QMenuBar(RegexLibraryBA)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 491, 24))
        self.MenuBar.setObjectName("MenuBar")
        self.fileMenu = QtGui.QMenu(self.MenuBar)
        self.fileMenu.setObjectName("fileMenu")
        self.editMenu = QtGui.QMenu(self.MenuBar)
        self.editMenu.setObjectName("editMenu")
        self.helpMenu = QtGui.QMenu(self.MenuBar)
        self.helpMenu.setObjectName("helpMenu")
        RegexLibraryBA.setMenuBar(self.MenuBar)
        self.editPasteAction = QtGui.QAction(RegexLibraryBA)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image1"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editPasteAction.setIcon(icon)
        self.editPasteAction.setProperty("name", QtCore.QVariant("editPasteAction"))
        self.editPasteAction.setObjectName("editPasteAction")
        self.helpHelpAction = QtGui.QAction(RegexLibraryBA)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image2"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpHelpAction.setIcon(icon1)
        self.helpHelpAction.setProperty("name", QtCore.QVariant("helpHelpAction"))
        self.helpHelpAction.setObjectName("helpHelpAction")
        self.exitAction = QtGui.QAction(RegexLibraryBA)
        self.exitAction.setProperty("name", QtCore.QVariant("exitAction"))
        self.exitAction.setObjectName("exitAction")
        self.toolBar.addAction(self.editPasteAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.editMenu.addAction(self.editPasteAction)
        self.editMenu.addSeparator()
        self.helpMenu.addAction(self.helpHelpAction)
        self.MenuBar.addAction(self.fileMenu.menuAction())
        self.MenuBar.addAction(self.editMenu.menuAction())
        self.MenuBar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(RegexLibraryBA)
        QtCore.QObject.connect(self.editPasteAction, QtCore.SIGNAL("activated()"), RegexLibraryBA.editPaste)
        QtCore.QObject.connect(self.exitAction, QtCore.SIGNAL("activated()"), RegexLibraryBA.close)
        QtCore.QObject.connect(self.descriptionListBox, QtCore.SIGNAL("currentRowChanged(int)"), RegexLibraryBA.descSelectedSlot)
        QtCore.QMetaObject.connectSlotsByName(RegexLibraryBA)

    def retranslateUi(self, RegexLibraryBA):
        RegexLibraryBA.setWindowTitle(QtGui.QApplication.translate("RegexLibraryBA", "Kodos - Regex Library", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox5.setTitle(QtGui.QApplication.translate("RegexLibraryBA", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget3.setTabText(self.tabWidget3.indexOf(self.tab), QtGui.QApplication.translate("RegexLibraryBA", "Regex", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel3.setText(QtGui.QApplication.translate("RegexLibraryBA", "Contributed By:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget3.setTabText(self.tabWidget3.indexOf(self.tab1), QtGui.QApplication.translate("RegexLibraryBA", "Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.fileMenu.setTitle(QtGui.QApplication.translate("RegexLibraryBA", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.editMenu.setTitle(QtGui.QApplication.translate("RegexLibraryBA", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.helpMenu.setTitle(QtGui.QApplication.translate("RegexLibraryBA", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.editPasteAction.setText(QtGui.QApplication.translate("RegexLibraryBA", "&Paste Example Into Kodos", None, QtGui.QApplication.UnicodeUTF8))
        self.editPasteAction.setIconText(QtGui.QApplication.translate("RegexLibraryBA", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.editPasteAction.setToolTip(QtGui.QApplication.translate("RegexLibraryBA", "Paste This Example Into Kodos", None, QtGui.QApplication.UnicodeUTF8))
        self.editPasteAction.setShortcut(QtGui.QApplication.translate("RegexLibraryBA", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.helpHelpAction.setText(QtGui.QApplication.translate("RegexLibraryBA", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.helpHelpAction.setIconText(QtGui.QApplication.translate("RegexLibraryBA", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.helpHelpAction.setShortcut(QtGui.QApplication.translate("RegexLibraryBA", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.exitAction.setText(QtGui.QApplication.translate("RegexLibraryBA", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.exitAction.setIconText(QtGui.QApplication.translate("RegexLibraryBA", "Exit", None, QtGui.QApplication.UnicodeUTF8))


class RegexLibraryBA(QtGui.QMainWindow, Ui_RegexLibraryBA):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)

