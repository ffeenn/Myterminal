
from ssh.Main_Window import *
import sys,base64
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import  QMainWindow, QLabel,QApplication,QStackedWidget
from PyQt5 import QtWidgets
from ssh.hostlist import HostWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QRect, QSize, QMetaObject, QCoreApplication,QPropertyAnimation,QSize

from ssh.Myterminal import Term
Maimwin_ico='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'

# class Title_Menu(QtWidgets.QPushButton):
#     def __init__(self, *args, **kwargs):
#         super(Title_Menu, self).__init__(*args, **kwargs)
#         self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
#
class ItemWidget(QtWidgets.QWidget):
    Send_env = pyqtSignal(list)
    Send_ck = pyqtSignal(list)
    def __init__(self, title,terw,*args, **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        self.setObjectName("itemwidget")
        self.tab_name = QLabel(title, self)
        self.terw = terw
        #overlay
        # self.tab_name = QLabel('192.168.111.111:22222222222222222222222222222222', self)
        # self.setMinimumWidth(200)
        self.tab_name.setMinimumSize(28, 18)
        self.tab_name.setStyleSheet('border-right: 1px solid #222222;')
        self.tab_name.setMaximumSize(160, 18)
        flayout = QtWidgets.QHBoxLayout(self)
        self.tab_clos = QHead_Button(b'\xef\x81\xb2'.decode("utf-8"), self)
        # self.tab_clos.setFont(QtGui.QFont("Webdings"))
        # self.tab_clos.setFixedWidth(20)
        self.tab_clos.setObjectName("tabclos")
        self.tab_clos.setMaximumSize(15, 18)
        print(self.width(),self.tab_name.width())
        # self.tab_clos.setGeometry(self.tab_name.width(),9,15,18)
        # self.tab_clos.move(self.width()-100,9)
        # self.tab_clos.move(self.width()-100,9)
        # self.tab_clos.setMinimumSize(15, 38)
        self.tab_clos.clicked.connect(self.tabclos)
        self.tab_clos.hide()
        # self.Lable_left.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        flayout.addWidget(self.tab_name)
        flayout.addWidget(self.tab_clos)
        flayout.setContentsMargins(0, 0, 0, 0)
        # flayout.setSpacing(0)
        self.setContentsMargins(10, 0, 0, 0)
        # layout.addLayout(flayout)
        # self.setStyleSheet('''
        # QWidget#itemwidget{
        #     border-left: 2px solid #76797C;
        # }
        # QLabel{
        #     border-left: 0px;
        # }
        # ''')
        # layout.setContentsMargins(0, 0, 0, 0)
    def tabclos(self):
        self.Send_env.emit([self.terw,self])
        # self.clos()
    def mousePressEvent(self, event):
        self.Send_ck.emit([self.terw,self])
    def enterEvent(self, event):
        try:
            self.tab_clos.show()
        except:
            pass
    def leaveEvent(self, event):
        try:
            self.tab_clos.hide()
        except:
            pass
# class table(QtWidgets.QWidget):
class table(QtWidgets.QLabel):
    def __init__(self,*args, **kwargs):
        # super(table, self ).__init__(None, QtCore.Qt.FramelessWindowHint)
        super(table, self ).__init__( *args, **kwargs)
        # self.resize(700, 50)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self._TitleLabel.close()
        # self._ClosButton.close()
        self.add_tab = QtWidgets.QPushButton('+',self)
        self.add_tab.setObjectName("addtab")
        self.add_tab.setMaximumSize(38, 38)
        self.add_tab.setMinimumSize(38, 38)
        self.verticalLayout = QtWidgets.QHBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        # self.label = ItemWidget('192.168.110.110:6880')
        # self.label2 = ItemWidget()
        # self.label3 = ItemWidget()
        # self.label.setMinimumSize(30, 30)
        # self.label.setObjectName("label")
        # self.horizontalLayout.addWidget(self.label)
        # self.horizontalLayout.addWidget(self.label2)
        # self.horizontalLayout.addWidget(self.label3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.add_tab)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.setStyleSheet('''
        QWidget{
        color:#777777;
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));
        }
        /*
        QPushButton{

        border:none;
       line-height: 1;
       font: 10pt "微软雅黑";
       padding: 9px;
       text-align:left;
       outline: none;
        }
        */
        QPushButton#addtab{
         border:none;
         font: 18pt;
         color:#AAAAAA;
        }
        QPushButton#addtab:hover{
         color:#00CC66;
        }
        QPushButton#tabclos{
         color:#CC6666;
         background-color:#000000;
         /*border-right: 1px solid #222222;*/
         /*border:none;*/
         border-radius: 10px;
         padding: 0px 0px 0px 0px ;
        }
        ''')
class terminal(Window):
    def __init__(self):
        super(terminal, self, ).__init__()
        self.resize(900, 600)
        self.setObjectName('terminal')
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Main_HB = QtWidgets.QHBoxLayout()
        Pixmap = QtGui.QPixmap()
        Pixmap.loadFromData(base64.b64decode(bytes(Maimwin_ico, encoding='utf-8')))
        self.Window_out = False
        ico = QtGui.QIcon()
        ico.addPixmap(Pixmap)
        self.iclab = QLabel(self)
        self.tab_menu = QtWidgets.QPushButton('☰',self)
        self.tab_menu.setStyleSheet('line-height: 0.1;font: 7pt "微软雅黑";border-top-right-radius:10px;')
        self.tab_menu.setObjectName("tabmenu")
        self.tab_menu.clicked.connect(self.Title_men)
        self.tab_menu.setMaximumSize(30, 30)
        self.tab_menu.setMinimumSize(30, 30)
        self._MinimumButton = QHead_Button(b'\xef\x80\xb0'.decode("utf-8"), self)
        self._MinimumButton.setObjectName("MinMaxButton")
        self._MinimumButton.setMaximumSize(30, 30)
        self._MinimumButton.setMinimumSize(30, 30)
        self._MinimumButton.clicked.connect(self.showMinimized)

        self.iclab.setMaximumSize(30, 30)
        self.iclab.setMinimumSize(30, 30)
        self.iclab.setScaledContents(True)
        self.iclab.setPixmap(Pixmap)
        self.setWindowIcon(ico)
        self.Main_HB.addWidget(self.iclab)

        self.title_tab = table(self)
        self.title_tab.setMinimumSize(38, 38)
        self.title_tab.add_tab.clicked.connect(self.Init_lab)
        # self.title_tab.setGeometry(38,0,self.width() - self._ClosButton.width()-38,48)
        # self.title_tab.setStyleSheet('background-color:#FFFFFF')
        # self.title_hb.addWidget(self.title_tab)
        self.Main_HB.addWidget(self.title_tab)
        self.Main_HB.addWidget(self.tab_menu)

        self.Main_HB.addWidget(self._MinimumButton)
        self.Main_HB.addWidget(self._MaximumButton)
        self.Main_HB.addWidget(self._ClosButton)
        self.Main_HB.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_main.addLayout(self.Main_HB)
        self.window_docker = QStackedWidget(self)

        # spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_main.addWidget(self.window_docker)
        # self.verticalLayout_main.addItem(spacerItem)
        self.verticalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_main.setSpacing(0)
        self._Men = QtWidgets.QMenu(self)
        # self._Men.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self._Men.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self._Men.setObjectName('TabMen')
        self.Host_often = self._Men.addAction('最近会话')
        self.Host_list = self._Men.addAction('远程管理')
        self.Host_list.triggered.connect(lambda :self.Host_win(True))
        self.Theme = self._Men.addAction('切换主题')
        self._Men.addSeparator()
        self.Setting = self._Men.addAction('设置')
        self.Help = self._Men.addAction('帮助')
        self.Author = self._Men.addAction('关于')
        # self._ClosButton.move(self.width() - self._ClosButton.width() - 1, 5)
        # float_host = QtWidgets.QVBoxLayout(self)
        self.HostListWindow = HostWindow(self)
        # self.HostListWindow = HostWindow()

        # self.HostListWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.HostListWindow.Send_host.connect(self.Add_lab)
        # self.HostListWindow.

        self.win_out = QPropertyAnimation(self.HostListWindow, b"geometry")
        self.win_out.setDuration(300)


        # float_host.addWidget(self.HostListWindow)
        # self.title_hb = QtWidgets.QHBoxLayout(self)
        # self.title_tab = table(self)
        # self.title_tab.setGeometry(38,0,self.width() - self._ClosButton.width()-38,48)
        # self.title_tab.setStyleSheet('background-color:#FFFFFF')
        # self.title_hb.addWidget(self.title_tab)

    # def enterEvent(self,QMouseEvent):
    #     self.setMouseTracking(True)
        self.Lable_viwe =[]
        self.Init_lab()
        # self.winqss()
    # def winqss(self):

        self.setStyleSheet(''' 
        
                   QTableView
                       {
                           outline:0px;
                       }
            
            QWidget#main_widget{
                       border-top-right-radius:10px;
                       border-top-left-radius:10px;
                       border-bottom-left-radius:4px;
                       border-bottom-right-radius:4px;
                       /*background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 163));*/
                       /*background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 200));*/
                       background-color: qlineargradient(spread:pad, x1:0.506, y1:0.567818, x2:1, y2:0, stop:1 rgba(0, 37, 56, 200));

             }
             
             QWebEngineView#QWebEng{
                background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 163));
             }
             
             QWidget#QWebEng{
                background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 163));
             }
              QWidget#HostItemWidget:hover{
                background-color:#111111;
            }
            QWidget#UpdateHostWindow{
            background-color:#000000;
            color:#FFFFFF;
            }
             QWidget#HostListWindow{
             background-color:#000000;

             }
             
              QPushButton:hover{
              background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(47, 47, 47, 171));
              }
             QPushButton{
              color:#CCCCCC;
               border:none;
               /*font-family: "微软雅黑";*/
               border-radius:3px;
               background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(37, 37, 37, 171));
             }

             QPushButton#Left_QPush{
             color:#CCCCCC;
             border:none;
             background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));
             }
             /*
              QPushButton{
                color:#CCCCCC;
                border:none;
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));
              }*/





             QPushButton#AddHost:hover{
             background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(47, 47, 47, 171));
             }

                       QPushButton#subButton{
                           border:none;
                           border-radius:3px;
                           line-height: 1;
                           font: 10pt "微软雅黑";
                           padding: 0px;
                           color:#FFFFFF;
                            background-color:#CC6633;
                           outline: none;
                       }
                       QPushButton#subButton:hover {
                            background-color:#AAAAAA;

                       }
                       QPushButton#toolbarbutton{
                           border:none;
                           line-height: 1;
                           font: 10pt "微软雅黑";
                           padding: 9px;
                           text-align:left;
                           outline: none;
                       }
                        QPushButton#toolbarbutton:hover {
                            background-color:#AAAAAA;

                       }

                       QPushButton#toolbarbutton:focus
                       {

                            background-color:#CCCCCC;
                       }
                       QPushButton#ClosButton,#MinMaxButton,#tabmenu,#MinMaxButton{
                       color:#AAAAAA;
                       border:0px;
                       background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));
                       }
                       QPushButton#MinMaxButton:hover,#tabmenu:hover,#MinMaxButton:hover{
                           color:#FFFFFF
                       }

                       QPushButton#ClosButton:hover{
                           color:#FF0033
                       }
                        
                       QLabel{
                           line-height: 1.5;
                           color:#999999;
                           font: 6pt "微软雅黑";
                           font-weight: normal;
                           opacity: 0.7;
                           font-size: 16px;
                       }
                        QLabel#TitleLabel{
                        color: #000000;
                        }
                       QLabel#HostItemTitleName{
                       color:#CCCCCC;

                       font: 8pt "微软雅黑";
                       }
                       QLabel#HostItemHost{
                       color:#555555;

                       font: 7pt "微软雅黑";
                       }
                   QLineEdit
                   {
                       background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));
                       padding: 5px;
                       border-style: solid;
                       border: 1px solid #00CCFF;
                       border-radius: 2px;
                       color: #999999;

                   }
                   QWebEngineView{
                   background-color: #FFFFFF;
                   }
                   QLineEdit:hover
                   {
                       border: 1px solid #99CC99;

                   }
                   
                   QMenu#TabMen{
                  /* font: 9pt "SimSun";*/
                   font-weight: 400;
                   width: 128px;
                   color:#333333;
                   background-color:  #F7F7F7;
                    border-radius: 5px;
                   }
                   QMenu::item
                    {
                    background-color: transparent;
                    padding:3px 30px;
                    margin:2px 0px; 
                    }
                    QMenu::item:selected
                    {
                        background-color:#00CCFF;
                    }
                    QMenu::separator {
                        height: 2px;
                        background: lightblue;
                        margin-left: 0px;
                        margin-right: 5px;
                    }
                    QMenu::indicator {
                        width: 18px;
                        height: 18px;
                    }
                    
                    QTableWidget#HostTabWindow{
                    border-top: 1px solid #76797C;
                    border-bottom: 1px solid #76797C;
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));
                    }

                   QScrollBar:vertical
        {
           /* background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));
            */
            background-color:#111111;
            width: 10px;
            margin: 15px 3px 15px 3px;
            border: 0px transparent #2A2929;
            border-radius: 4px;
        }
        QScrollBar::handle:vertical
        {
            /*background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 80));
            */
            background-color: #222222;
            min-height: 5px;
            border-radius: 4px;
        }

        QScrollBar::sub-line:vertical
        {
            margin: 3px 0px 3px 0px;
            border-image: url(rc/up_arrow_disabled.png);
            height: 10px;
            width: 10px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }

        QScrollBar::add-line:vertical
        {
            margin: 3px 0px 3px 0px;
            border-image: url(rc/down_arrow_disabled.png);
            height: 10px;
            width: 10px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }

        QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
        {

            border-image: url(rc/up_arrow.png);
            height: 10px;
            width: 10px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }


        QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
        {
            border-image: url(rc/down_arrow.png);
            height: 10px;
            width: 10px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }

        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
        {
            background: none;
        }


        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
        {
            background: none;
        }
        

                           ''')
    def Remove_lab(self,window):
        print(window)

        if len(self.Lable_viwe) !=1:
            window[1].setParent(None)
            self.title_tab.horizontalLayout.removeWidget(window[1])
            self.Lable_viwe.remove(window[1])
            self.window_docker.removeWidget(window[0])
            del window[1]
        else:
            print('关闭主窗口')
        print(self.Lable_viwe,self.window_docker.count())
        # self.window_docker.indexOf()
    def show_docker(self,window=None):

        self.window_docker.setCurrentWidget(window[0])
        # self.window_docker.setCurrentIndex(1)
    def Init_lab(self):
        term = Term(data={}, open_win=False)
        label = ItemWidget('本地Shell', term)
        # itemwidget = ItemWidget(label)
        # itemwidget.Send_env.connect(self.Remove_lab)
        label.Send_env.connect(self.Remove_lab)
        label.Send_ck.connect(self.show_docker)
        self.Lable_viwe.append(label)
        self.window_docker.addWidget(term)
        cont = len(self.Lable_viwe)-1
        self.title_tab.horizontalLayout.addWidget(self.Lable_viwe[cont])
        # self.title_tab.horizontalLayout.addWidget(self.Lable_viwe[len(self.Lable_viwe)-1])

    def Add_lab(self,host):
        print(host)
        data= {'host':host[2], 'port':host[3], 'username':host[4], 'ispwd':  True, 'secret':host[5]}
        term = Term(data=data,open_win=True)
        label = ItemWidget(host[1], term)
        label.Send_env.connect(self.Remove_lab)
        label.Send_ck.connect(self.show_docker)
        self.Lable_viwe.append(label)
        self.window_docker.addWidget(term)
        self.title_tab.horizontalLayout.addWidget(self.Lable_viwe[len(self.Lable_viwe) - 1])
        self.window_docker.setCurrentIndex(len(self.Lable_viwe)-1)


    def Title_men(self):
        self._Men.exec_(self.tab_menu.mapToGlobal(QtCore.QPoint(-40, self.tab_menu.height())))
    def Host_win(self,win_type=True):
        self.Window_out =True


        self.HostListWindow.setGeometry(0, 38, 360, self.height() - 38)
        self.win_out.setStartValue(QtCore.QRect(self.width()if win_type else self.width()-360,38,360,self.height()-38))
        self.win_out.setEndValue(QRect(self.width()-360 if win_type else self.width(),38,360,self.height()-38))
        # if win_type:
        #     self.HostListWindow.show()
        # else:
        #     pass
            # self.HostListWindow.hide()

        self.win_out.start()
    def resizeEvent(self, QResizeEvent):
        self._TitleLabel.setGeometry(0, 0, self.width(), 38)
        if self.Window_out:
            self.HostListWindow.setGeometry(self.width()-360,38,360,self.height()-38)
        else:
            self.HostListWindow.setGeometry(self.width(), 38, 360, self.height()-38)
        self._right_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                            for y in range(1, self.height() - self._padding)]
        self._bottom_rect = [QPoint(x, y) for x in range(1, self.width() - self._padding)
                             for y in range(self.height() - self._padding, self.height() + 1)]
        self._corner_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                             for y in range(self.height() - self._padding, self.height() + 1)]

    def mousePressEvent(self, event):
        if self.Window_out:
            self.Host_win(False)
            self.Window_out = False
        # 重写鼠标点击的事件
        if event.y() < 42:
            self._MoveVarl = True
            self.move_DragPosition = event.globalPos() - self.pos()
            event.accept()

        elif (event.button() == Qt.LeftButton) and (event.pos() in self._corner_rect):
            # 鼠标左键点击右下角边界区域
            self._corner_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._right_rect):
            # 鼠标左键点击右侧边界区域
            self._right_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._bottom_rect):
            # 鼠标左键点击下侧边界区域
            self._bottom_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.y() < self._TitleLabel.height()):
            # 鼠标左键点击标题栏区域
            self._move_drag = True
            self.move_DragPosition = event.globalPos() - self.pos()
            event.accept()
        # self.HostListWindow.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    aaa=''.format()
    # print(b'\xef\x81\xb0'.decode("utf-8"))
    # data = {'host': '39.107.100.236', 'port': '1993', 'username': 'root', 'ispwd':  True, 'secret': '@Scjz1993'}
    # data = {'host': '192.168.110.134', 'port': '22', 'username': 'root', 'ispwd': True, 'secret': '123456'}
    fennbk = terminal()
    fennbk.show()
    sys.exit(app.exec_())
#
# import base64
# with open('./rc/zd.png','rb') as F:
#     data = base64.b64encode(F.read())
# print(data)