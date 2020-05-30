# -*- coding: utf-8 -*-
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import  QMainWindow, QLabel,QApplication, QPushButton
from PyQt5.QtCore import QPoint, Qt,QRect
from PyQt5.QtGui import QFont,QPainterPath,QPainter,QBrush,QColor,QPen
import math
class QHead_Button(QPushButton):
    def __init__(self, *args):
        super(QHead_Button, self).__init__(*args)
        self.setFont(QFont("Webdings"))
        self.setFixedWidth(40)

class Window(QMainWindow):
    def __init__(self):
        super(Window, self, ).__init__(None, Qt.FramelessWindowHint, )
        geometry = QApplication.instance().desktop().availableGeometry()
        # print('屏幕大小', geometry.width(), geometry.height())
        self.screenWidth = geometry.width()
        self.screenHeight = geometry.height()
        # self.setMouseTracking(True)
        # self.resize(self.screenWidth, self.screenHeight)

        self._padding = 5
        self.initDrag()
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.main_widget = QtWidgets.QWidget()
        self.main_widget.setMouseTracking(True)

        self.setCentralWidget(self.main_widget)
        self.main_widget.setObjectName('main_widget')

        # self.verticalLayout_main = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout_main = QtWidgets.QVBoxLayout(self.main_widget)


        # 标题栏 与工具栏
        self._TitleLabel = QLabel(self.main_widget)
        self._TitleLabel.setStyleSheet(
            'color:#FFFFFF;background-color:#000000;border-top-left-radius:5px;border-top-right-radius:5px;')
        self._ClosButton = QHead_Button(b'\xef\x81\xb2'.decode("utf-8"), self.main_widget)
        # self._ClosButton = QHead_Button(b'\xef\x81\xb2'.decode("utf-8"), self.main_widget)
        self._MaximumButton = QHead_Button(b'\xef\x80\xb1'.decode("utf-8"), self)
        self._MaximumButton.setObjectName("MinMaxButton")
        self._MaximumButton.setMaximumSize(30, 30)
        self._MaximumButton.setMinimumSize(30, 30)
        self._MaximumButton.clicked.connect(self._changeNormalButton)
        self._ClosButton.setObjectName("ClosButton")
        self._ClosButton.setMaximumSize(30, 30)
        self._ClosButton.setMinimumSize(30, 30)
        self._ClosButton.clicked.connect(self.close)

        # 全局样式

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

    def _changeNormalButton(self):
        # 切换到恢复窗口大小按钮
        try:
            self.showMaximized()  # 先实现窗口最大化
            self._MaximumButton.setText(b'\xef\x80\xb2'.decode("utf-8"))  # 更改按钮文本
            self._MaximumButton.setToolTip("恢复")  # 更改按钮提示
            self._MaximumButton.disconnect()  # 断开原本的信号槽连接
            self._MaximumButton.clicked.connect(self._changeMaxButton)  # 重新连接信号和槽
        except:
            pass

    def _changeMaxButton(self):
        # 切换到最大化按钮
        try:
            self.showNormal()
            self._MaximumButton.setText(b'\xef\x80\xb1'.decode("utf-8"))
            self._MaximumButton.setToolTip("最大化")
            self._MaximumButton.disconnect()
            self._MaximumButton.clicked.connect(self._changeNormalButton)
        except:
            pass
    def mousePressEvent(self, event):
        print('sc')
        if event.y() < 42:
            self._MoveVarl = True
            self.move_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        print('sa')
        if self._MoveVarl:
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        print('sb')
        self._MoveVarl = False

    def initDrag(self):
        # 设置鼠标跟踪判断扳机默认值
        self._MoveVarl = False
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

    def resizeEvent(self, QResizeEvent):

        # self._TitleLabel.setGeometry(0, 0, self.width(), 38)

        self._right_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                            for y in range(1, self.height() - self._padding)]
        self._bottom_rect = [QPoint(x, y) for x in range(1, self.width() - self._padding)
                             for y in range(self.height() - self._padding, self.height() + 1)]
        self._corner_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                             for y in range(self.height() - self._padding, self.height() + 1)]
    def mousePressEvent(self, event):
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

    def mouseMoveEvent(self, QMouseEvent):
        # 判断鼠标位置切换鼠标手势
        self.update()
        if self._MoveVarl:
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            QMouseEvent.accept()
        elif QMouseEvent.pos() in self._corner_rect:
            self.setCursor(Qt.SizeFDiagCursor)
        elif QMouseEvent.pos() in self._bottom_rect:
            self.setCursor(Qt.SizeVerCursor)
        elif QMouseEvent.pos() in self._right_rect:
            self.setCursor(Qt.SizeHorCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        if Qt.LeftButton and self._right_drag:
            # 右侧调整窗口宽度
            self.resize(QMouseEvent.pos().x(), self.height())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._bottom_drag:
            # 下侧调整窗口高度
            self.resize(self.width(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._corner_drag:
            # 右下角同时调整高度和宽度
            self.resize(QMouseEvent.pos().x(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        # elif Qt.LeftButton and self._move_drag:
        #     # 标题栏拖放窗口位置
        #     self.move(QMouseEvent.globalPos() - self.move_DragPosition)
        #     QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，各扳机复位
        self._MoveVarl = False
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

    def enterEvent(self,QMouseEvent):
        self.setMouseTracking(True)

    # def paintEvent(self, event):
    #     m = 9
    #
    #     path = QPainterPath()
    #     path.setFillRule(Qt.WindingFill)
    #     path.addRect(m, m, self.width() - m * 2, self.height() - m * 2)
    #
    #     painter = QPainter(self)
    #     # # painter.drawLine(QLineF)
    #     # # painter.setRenderHint(QPainter.Antialiasing, True)
    #     painter.fillPath(path, QBrush(Qt.white))
    #     #
    #     color = QColor(100, 100, 100, 30)
    #     # for(int i=0; i<10; i++)
    #
    #     for i in range(m):
    #         path = QPainterPath()
    #         path.setFillRule(Qt.WindingFill)
    #         path.addRoundRect(m - i, m - i, self.width() - (m - i) * 2, self.height() - (m - i) * 2, 1, 1)
    #         color.setAlpha(90 - math.sqrt(i) * 30)
    #         painter.setPen(QPen(color, 1, Qt.SolidLine))
            # painter.drawRoundRect(QRect(m - i, m - i, self.width() - (m - i) * 2, self.height() - (m - i) * 2), 0, 0)
#
# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     fennbk = Window()
#     fennbk.show()
#     sys.exit(app.exec_())