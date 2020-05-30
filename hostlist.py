# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hostlist.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import  QMainWindow, QLabel,QApplication, QPushButton
from PyQt5.QtCore import QPoint, Qt,QRect
from PyQt5.QtGui import QFont,QPainterPath,QPainter,QBrush,QColor,QPen
import math
from PyQt5.QtCore import QRect, QSize, QMetaObject, QCoreApplication,QPropertyAnimation,QSize
from ssh.Main_Window import  Window,QHead_Button
from PyQt5.QtGui import QPixmap
import sys,base64,json,re
ico_remote=b'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'
ico_remote_dir = b'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'
from PyQt5.QtWidgets import QLabel,QVBoxLayout,QHBoxLayout,QMenu
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from DB import db
class HostItemWidget(QLabel):
    Send_env = pyqtSignal(list)
    Send_edit = pyqtSignal(list)
    def __init__(self, title, ico, host,hosts):
        super(HostItemWidget, self).__init__()
        self.setObjectName('HostItemWidget')
        # self.setMaximumSize(98, 98)
        # self.setMinimumSize(98, 98)
        self.hosts= hosts
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        if len(host)==2:
            self.Left_lable = QLabel('〉', self)
            self.Left_lable.setStyleSheet('color:#FFFFFF')
            self.Left_lable.setGeometry(300,10,38,38)
        else:
            self.Left_QPush = QPushButton('✎',self)
            self.Left_QPush.setObjectName('Left_QPush')
            self.Left_QPush.hide()
            self.Left_QPush.clicked.connect(self.Edit)
            self.Left_QPush.setGeometry(300, 0, 58, 58)
        self.Title_name = QLabel(title, self)
        self.Title_name.setObjectName('HostItemTitleName')
        self.Title_name.setAttribute(Qt.WA_DeleteOnClose)
        # self.Title_Up.setAlignment(Qt.AlignCenter)
        self.Title_name.setMaximumSize(240, 18)
        self.Title_name.setMinimumSize(96, 18)
        self.host = QLabel(host, self)
        # self.host.setMaximumSize(240, 18)
        self.host.setObjectName('HostItemHost')
        # self.host.setText('192.169.111.111')
        # self.Title_Dow = QLabel(alias,self)
        # self.Title_name.setStyleSheet('font: 75 9pt "微软雅黑";color:#DDDDDD;text-shadow:0px 0px 1px #7b7d7c;')
        flayout = QHBoxLayout(self)
        layout = QVBoxLayout()
        layout.addWidget(self.Title_name)
        layout.addWidget(self.host)
        # layout = QVBoxLayout(self)
        self.host_ico = QLabel(self)
        self.host_ico.setScaledContents(True)
        self.host_ico.setPixmap(ico)
        self.host_ico.setMaximumSize(38, 38)
        self.host_ico.setMinimumSize(38, 38)
        flayout.addWidget(self.host_ico)
        flayout.addLayout(layout)
    def Edit(self):
        self.Send_edit.emit(list(self.hosts))
    def mouseDoubleClickEvent (self,event):
        self.Send_env.emit(list(self.hosts))
    def enterEvent(self, event):
        try:
            self.Left_QPush.show()
        except:
            pass
    def leaveEvent(self, event):
        try:
            self.Left_QPush.hide()
        except:
            pass
class TabWindow(QtWidgets.QTableWidget):
    def __init__(self,*args, **kwargs):
        super(TabWindow, self).__init__(*args, **kwargs)
        self.setFocusPolicy(Qt.NoFocus)
        self.setGeometry(QtCore.QRect(30, 240, 551, 301))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.setAutoScroll(False)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setTabKeyNavigation(False)
        self.setProperty("showDropIndicator", False)
        self.setDragEnabled(False)
        self.setDragDropOverwriteMode(False)
        self.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.setAlternatingRowColors(False)
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.setTextElideMode(QtCore.Qt.ElideNone)
        self.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.setShowGrid(False)
        self.setGridStyle(QtCore.Qt.NoPen)
        self.setWordWrap(False)
        self.setCornerButtonEnabled(False)
        self.setObjectName("HostTabWindow")

        # self.tableWidget.setItemDelegate(QtWidgets.QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setItemDelegate()

        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalHeader().setDefaultSectionSize(400)
        self.horizontalHeader().setHighlightSections(False)
        # self.horizontalHeader().setMinimumSectionSize(36)
        self.horizontalHeader().setSortIndicatorShown(False)
        self.horizontalHeader().setStretchLastSection(False)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setCascadingSectionResizes(False)
        self.verticalHeader().setDefaultSectionSize(56)
        self.verticalHeader().setHighlightSections(False)
        # self.verticalHeader().setMinimumSectionSize(40)
        self.verticalHeader().setSortIndicatorShown(True)
        self.verticalHeader().setStretchLastSection(False)
        self.setColumnCount(1)
class Updata_Host(QtWidgets.QLabel):
    Send_clos = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(Updata_Host, self).__init__(*args, **kwargs)
        self.resize(436, 540)
        self.host_id =''
        self.setObjectName('UpdateHostWindow')
        # self.setStyleSheet('background-color:#000000;')
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setContentsMargins(10, 0, 20, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 38))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("Updatelabel")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setMinimumSize(QtCore.QSize(56, 0))
        self.label_2.setObjectName("Updatelabel_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 38))
        self.lineEdit.setObjectName("UpdatelineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setMinimumSize(QtCore.QSize(56, 0))
        self.label_3.setObjectName("Updatelabel_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_2.setObjectName("UpdatelineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setObjectName("Updatelabel_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(48, 16777215))
        self.lineEdit_3.setObjectName("UpdatelineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("UpdatehorizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setMinimumSize(QtCore.QSize(56, 0))
        self.label_5.setObjectName("Updatelabel_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_4.setObjectName("UpdatelineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("UpdatehorizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setMinimumSize(QtCore.QSize(56, 0))
        self.label_6.setObjectName("Updatelabel_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_5.setDragEnabled(False)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setClearButtonEnabled(False)
        self.lineEdit_5.setObjectName("UpdatelineEdit_5")
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setObjectName("UpdatepushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("UpdatehorizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setMinimumSize(QtCore.QSize(56, 0))
        self.label_7.setObjectName("Updatelabel_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_6.setObjectName("UpdatelineEdit_6")
        self.horizontalLayout_6.addWidget(self.lineEdit_6)
        self.toolButton = QtWidgets.QPushButton(self)
        self.toolButton.setMinimumSize(QtCore.QSize(93, 32))
        self.toolButton.setObjectName("UpdatetoolButton")
        self.horizontalLayout_6.addWidget(self.toolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setMinimumSize(QtCore.QSize(56, 0))
        self.label_8.setObjectName("Updatelabel_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_7.setObjectName("UpdatelineEdit_7")
        self.horizontalLayout_7.addWidget(self.lineEdit_7)
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setObjectName("UpdatepushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setMinimumSize(QtCore.QSize(56, 0))
        self.label_9.setObjectName("Updatelabel_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_8.setObjectName("UpdatelineEdit_8")
        self.horizontalLayout_8.addWidget(self.lineEdit_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("UpdatepushButton")
        self.horizontalLayout_9.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setObjectName("UpdatepushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.re_pub = QPushButton('返回',self)
        self.label.setText( "添加服务器")
        self.label.setMinimumSize(100,38)
        self.label_2.setText( "名称:")
        self.lineEdit.setPlaceholderText( "*必填")
        self.label_3.setText( "地址:")
        self.lineEdit_2.setPlaceholderText( "*必填")
        self.lineEdit_2.setMaxLength(15)
        self.label_4.setText( "端口:")
        self.lineEdit_3.setText( "22")
        self.label_5.setText( "用户:")
        self.lineEdit_4.setText( "root")
        self.lineEdit_4.setPlaceholderText( "*必填")
        self.label_6.setText("密码:")
        self.lineEdit_5.setText("")
        self.pushButton_4.setText( "查看")
        self.pushButton_4.setMinimumSize(92,32)
        self.label_7.setText( "证书:")
        self.lineEdit_6.setText( "")
        self.lineEdit_6.setPlaceholderText("选填")
        self.toolButton.setText( "查找")
        self.label_8.setText( "分组:")
        self.lineEdit_7.setText( "")
        self.lineEdit_7.setPlaceholderText("选填")
        self.pushButton_3.setText("选择")
        self.pushButton_3.setMinimumSize(92,32)
        self.label_9.setText( "命令:")
        self.lineEdit_8.setText( "")
        self.lineEdit_8.setPlaceholderText( "选填")
        self.pushButton.setText( "添加")
        self.pushButton.setMinimumHeight(38)
        self.pushButton.clicked.connect(self.addhost)
        self.pushButton_2.close()
        self.pushButton_2.setText("删除")
        self.pushButton_2.clicked.connect(self.addhost)

    def clear_text(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("22")
        self.lineEdit_4.setText("root")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
    def addhost(self):
        if not self.lineEdit.text() or not self.lineEdit_2.text() or not self.lineEdit_3.text():
            return
        if not re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                    self.lineEdit_2.text()):
            print('IP地址格式不正确')
            return
        if self.sender().text()== '更新':
            self.pushButton.setText("添加")
            db().upda("update ssh_host set name='%s',host='%s',port='%s',user='%s',passwd='%s',cer='%s',hgroup='%s',cmd='%s' where id='%s'"%\
                      (self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text(),\
                       self.lineEdit_5.text(),self.lineEdit_6.text(),self.lineEdit_7.text(),self.lineEdit_8.text(),self.host_id))
        elif self.sender().text()== '删除':
            db().upda("delete from ssh_host where id='%s'" % self.host_id)
        else:
            # 判断是否有重复IP
            if  db().upda("select * from ssh_host where name ='%s'"%self.lineEdit.text())[0]:
                print('名称重复')
                return
            if db().upda("select * from ssh_host where host ='%s'" % self.lineEdit_2.text())[0]:
                print('IP重复')
                return
            db().upda("insert into ssh_host values (null,'%s','%s','%s','%s','%s','%s','%s','%s') " % \
                      (self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text(),\
                       self.lineEdit_5.text(),self.lineEdit_6.text(),self.lineEdit_7.text(),self.lineEdit_8.text()))
        if not db().upda("select * from ssh_group where hgroup ='%s'" % self.lineEdit_7.text())[
            0] and self.lineEdit_7.text() != '':
            db().upda("insert into ssh_group values(null,'%s')" % self.lineEdit_7.text())
        for item in db().upda("select * from ssh_group")[0]:
            if item:
                if not db().upda("select * from ssh_host where hgroup='%s'"%item[1])[0]:
                    db().upda("delete from ssh_group where id='%s'"%item[0])
        self.Send_clos.emit()
        self.clear_text()
class HostListWindow(QtWidgets.QLabel):
    Send_items = pyqtSignal(list)
    def __init__(self,host_type=False,*args):
        super(HostListWindow, self, ).__init__(*args)
        self.setObjectName("HostListWindow")
        self.resize(340, 628)
        self.host_type = host_type
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        # self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        # self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = TabWindow()
        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setContentsMargins(0,10,0,0)
        self.horizontalLayout.setContentsMargins(20,5,20,12)
        self.pushButton_2.setText("搜索")
        self.pushButton_2.setObjectName("Search")
        self.pushButton_2.setMinimumSize(28, 30)
        # self.pushButton_2.clicked.connect(self.search)
        self.pushButton.setText("+添加服务器")
        self.pushButton.setObjectName("AddHost")
        self.pushButton.setMinimumSize(28, 38)
        # self.pushButton.setMaximumSize(160, 38)
        self.lineEdit.setGeometry(self.width()+40,10,200,38)
        if self.host_type:
            self.pushButton_2.setText("↩")
            self.pushButton.close()
            self.lineEdit.close()
    def hostItem(self,send_list):
        self.Send_items.emit(send_list)
class HostWindow(QtWidgets.QWidget):
    Send_host = pyqtSignal(list)
    def __init__(self,*args):
        super(HostWindow, self, ).__init__(*args)
        self.resize(400,600)
        self.hostvh = QtWidgets.QHBoxLayout()
        self.HostListWindow = HostListWindow(False,self)
        self.setObjectName('HostWindow')
        # self.tableWidget = TabWindow()
        # self.HostListWindow.verticalLayout.addWidget(self.tableWidget)
        # self.verticalLayout.addWidget(self.tableWidget)
        self.hostvh.addWidget(self.HostListWindow)
        self.HostListWindow.pushButton.clicked.connect(lambda :self.Add_host(True))
        self.HostListWindow.pushButton_2.clicked.connect(lambda :self.search(False))
        self.HostListWindow.Send_items.connect(self.Items_host)
        self.Updata_Host = Updata_Host(self)
        self.Updata_Host.re_pub.clicked.connect(lambda :self.Add_host(False))
        self.Updata_Host.setGeometry(self.width(), 0, self.width(), self.height())
        self.Updata_Host.Send_clos.connect(lambda :self.Add_host(False))
        # self.HostList = HostList(self)
        self.HostList = HostListWindow(True,self)
        self.HostList.pushButton_2.clicked.connect(lambda :self.search(True))
        # self.HostList.pushButton_2
        self.HostList.setGeometry(self.width(), 0, self.width(), self.height())
        self.Re_Pixmap = QPixmap()
        self.Dir_Pixmap = QPixmap()
        self.Re_Pixmap.loadFromData(base64.b64decode(ico_remote))
        self.Dir_Pixmap.loadFromData(base64.b64decode(ico_remote_dir))
        self.HostListWindow_Out = QPropertyAnimation(self.HostListWindow, b"geometry")
        self.HostList_Out = QPropertyAnimation(self.HostList, b"geometry")
        self.Updata_Host_Out = QPropertyAnimation(self.Updata_Host, b"geometry")
        self.Updata_Host_Out.setDuration(500)
        self.HostListWindow_Out.setDuration(500)
        self.HostList_Out.setDuration(500)
        self.Host_item_list()
    def search(self,host_type):
        if host_type:
            self.HostListWindow_Out.setStartValue(
                QRect(0 - self.width(), 0, self.width(), self.height()))
            self.HostListWindow_Out.setEndValue(
                QRect(0, 0, self.width(), self.height()))
            self.HostList_Out.setStartValue(
                QtCore.QRect(0, 0, self.width(), self.height()))
            self.HostList_Out.setEndValue(QRect(self.width(), 0, self.width(), self.height()))
            self.HostListWindow_Out.start()
            self.HostList_Out.start()
        else:
            self.HostList.pushButton_2.setText('返回')
            self.HostList.outani = QPropertyAnimation(self.HostList.lineEdit, b"geometry")
            self.HostList.outani.setStartValue(QtCore.QRect(self.HostList.width()+40, 10, 200, 38))
            self.HostList.outani.setDuration(300)  # 1s
            self.HostList.outani.setEndValue(QRect(12, 10, 200, 38))
            self.HostList.outani.start()
    def return_hosts(self,data):
        self.Send_host.emit(data)
    def Items_host(self,ItemsList):
        self.HostList.tableWidget.clear()
        if len(ItemsList) == 2:
            host = db().upda("select * from ssh_host where hgroup='%s'"%ItemsList[1])
        # if host[0]and len(ItemsList[0])==2:
            self.HostList.tableWidget.setRowCount(host[1])
            for _id,item in enumerate(host[0]):
                items = HostItemWidget(item[1], self.Re_Pixmap, item[2],item)
                items.Send_edit.connect(self.Updata_host)
                # items.Left_QPush.clicked.connect(lambda:self.Add_host(True,True,item))
                items.Send_env.connect(self.return_hosts)
                self.HostList.tableWidget.setCellWidget(_id, 0, items)
        else:
            self.return_hosts(ItemsList)
            return
        self.HostListWindow_Out.setStartValue(
            QRect(0 , 0, self.width(), self.height()))
        self.HostListWindow_Out.setEndValue(
            QRect(0 - self.width(), 0, self.width(), self.height()))
        self.HostList_Out.setStartValue(
           QtCore.QRect(self.width(), 0, self.width(), self.height()))
        self.HostList_Out.setEndValue(QRect(0 , 0, self.width(), self.height()))
        self.HostListWindow_Out.start()
        self.HostList_Out.start()
    def Host_item_list(self):
        self.HostListWindow.tableWidget.clear()
        hosts =  db().upda("select * from ssh_host")
        host_g =  db().upda("select * from ssh_group")
        self.HostListWindow.tableWidget.setRowCount(len(host_g[0]+hosts[0]))
        for _id,item in enumerate(host_g[0]+hosts[0]):
            if len(item) ==2:
                items = HostItemWidget(item[1], self.Dir_Pixmap, '分组',item)
            else:
                items = HostItemWidget(item[1], self.Re_Pixmap, item[2],item)
                items.Send_edit.connect(self.Updata_host)
                # items.Left_QPush.clicked.connect(lambda:self.Add_host(True,True,item))
                # items.Left_QPush.clicked.connect(lambda:)
            items.Send_env.connect(self.Items_host)
            self.HostListWindow.tableWidget.setCellWidget(_id, 0, items)
    def Updata_host(self,data):
        self.Updata_Host.host_id = data[0]
        self.Updata_Host.pushButton.setText('更新')
        self.Updata_Host.label.setText('更新服务器')
        self.Updata_Host.pushButton_2.show()
        self.Updata_Host.lineEdit.setText(data[1])
        self.Updata_Host.lineEdit_2.setText(data[2])
        self.Updata_Host.lineEdit_3.setText(data[3])
        self.Updata_Host.lineEdit_4.setText(data[4])
        self.Updata_Host.lineEdit_5.setText(data[5])
        self.Updata_Host.lineEdit_6.setText(data[6])
        self.Updata_Host.lineEdit_7.setText(data[7])
        self.Updata_Host.lineEdit_8.setText(data[8])
        self.Add_host(True,True)
    def Add_host(self,Property_type,win_type=False):
        self.Host_item_list()
        if not win_type:
            self.Updata_Host.pushButton.setText('添加')
            self.Updata_Host.pushButton_2.close()
            self.Updata_Host.clear_text()
        if self.HostList.x() == 0:
            self.HostList_Out.setStartValue(
                QRect(0, 0, self.width(), self.height()))
            self.HostList_Out.setEndValue(
                QRect(0 - self.width() if Property_type else 0, 0, self.width(), self.height()))
            self.Updata_Host_Out.setStartValue(
                QtCore.QRect(self.width() , 0, self.width(), self.height()))
            self.Updata_Host_Out.setEndValue(
                QRect(0, 0, self.width(), self.height()))
            self.HostList_Out.start()
            self.Updata_Host_Out.start()
            return
        # elif self.Updata_Host.width() ==400
        self.HostListWindow_Out.setStartValue(
            QRect(0 if Property_type else 0 - self.width(), 0, self.width(), self.height()))
        self.HostListWindow_Out.setEndValue(
            QRect(0 - self.width() if Property_type else 0, 0, self.width(), self.height()))
        self.Updata_Host_Out.setStartValue(
            QtCore.QRect(self.width() if Property_type else 0, 0, self.width(), self.height()))
        self.Updata_Host_Out.setEndValue(QRect(0 if Property_type else self.width(), 0, self.width(), self.height()))
        self.HostListWindow_Out.start()
        self.Updata_Host_Out.start()
    def resizeEvent(self, QResizeEvent):
        self.HostListWindow.setGeometry(0,0,self.width(),self.height())
        self.Updata_Host.setGeometry(self.width(), 0, self.width(), self.height())







if __name__ == "__main__":

    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QPixmap
    app = QApplication(sys.argv)
    # print(b'\xef\x81\xb0'.decode("utf-8"))
    # data = {'host': '39.107.100.236', 'port': '1993', 'username': 'root', 'ispwd':  True, 'secret': '@Scjz1993'}
    # data = {'host': '192.168.110.134', 'port': '22', 'username': 'root', 'ispwd': True, 'secret': '123456'}

    # Pixmap = QPixmap()
    # Pixmap.loadFromData(base64.b64decode(ico_remote))


    fennbk = HostWindow()
    # fennbk = HostListWindow()
    fennbk.show()
    sys.exit(app.exec_())