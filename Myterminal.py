

import paramiko,json,base64,os
from paramiko.ssh_exception import AuthenticationException, SSHException
import  threading
from multiprocessing import Process
from io import StringIO
try:
    from cStringIO import StringIO
except ImportError:
    pass
import select
import socket,subprocess
import logging
from threading import Thread
from subprocess import run
MAX_DATA_BUFFER = 32*1024
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
class IOLoop(Thread):
    READ = 0x001
    WRITE = 0x004
    ERROR = 0x008 | 0x010

    def __init__(self, impl):
        super(IOLoop, self).__init__()
        self.daemon = True
        self.impl = impl
        self.bridges = {}
        self.futures = {}

    @staticmethod
    def instance():
        IOLoop._instance = SelectIOLoop()
        return IOLoop._instance
    def register(self, bridge):
        raise NotImplemented("the register method should be implemented")

    def _add_bridge(self, bridge):
        self.bridges[bridge.id] = bridge
    def add_future(self, future):
        fd = next(future)
        self.futures[fd] = future
        next(future)
    def close(self, fd):
        self.impl.unregister(fd)
        self.bridges[fd].detroy()
        del self.bridges[fd]
class SelectIOLoop(IOLoop):

    def __init__(self):
        super(SelectIOLoop, self).__init__(impl=select.select)
        self.read_fds = set()
        self.write_fds = set()
        self.error_fds = set()
        self.fd_sets = (self.read_fds, self.write_fds, self.error_fds)

    def register(self, bridge):
        self._add_bridge(bridge)
        self.read_fds.add(bridge.id)
    def run(self):
        # import time
        while True:
            if self.read_fds:
                readable, writeable, errors = self.impl(
                    self.read_fds, self.write_fds, self.error_fds, 1)
                events = {}
                for fd in readable:
                    events[fd] = events.get(fd, 0) | self.READ
                for fd in errors:
                    events[fd] = events.get(fd, 0) | self.ERROR
                for fd, events in events.items():
                    if self.READ & events:
                        while True:
                            try:
                                data = self.bridges[fd].shell.recv(MAX_DATA_BUFFER)
                                logger.debug('接受到服务端数据:%s'%data)
                                if data == b'':
                                    self.close(fd)
                                    self.bridges[fd].close()
                                    break
                            except socket.error as e:
                                logger.debug('错误：socket.error %s'%str(e) )
                                if isinstance(e, socket.timeout):
                                    break
                                else:
                                    self.close(fd)
                            try:
                                self.futures[fd].send(data)
                            except Exception as e:
                                break
                    elif self.ERROR & events:
                        self.close(fd)
                    else:

                        continue
            else:
                pass
                # time.sleep(1)
class Bridge(object):
    def __init__(self,IOST,Qtext):
        self.IOST = IOST
        self.Qtext = Qtext
        self.SHELL = None
        self._id = 0
        self.ssh = paramiko.SSHClient()

    @property
    def id(self):
        return self._id

    @property
    def websocket(self):
        return self.IOST
    @property
    def shell(self):
        return self.SHELL
    def privaterKey(self, _PRIVATE_KEY, _PRIVATE_KEY_PWD):
        try:
            pkey = paramiko.RSAKey.from_private_key(StringIO(_PRIVATE_KEY), _PRIVATE_KEY_PWD)
        except paramiko.SSHException:
            pkey = paramiko.DSSKey.from_private_key(StringIO(_PRIVATE_KEY), _PRIVATE_KEY_PWD)
        return pkey

    def open(self,data={}):
        self.ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
        try:
            if data['ispwd']:
                self.ssh.connect(
                    hostname=data["host"],
                    port=int(data["port"]),
                    username=data["username"],
                    password=data["secret"],
                )
                logger.debug('密码认证成功: 主机:{} 用户:{} 端口：{}'.format(data["host"],data["username"],data["port"]))
            else:
                self.ssh.connect(
                    hostname=data["host"],
                    port=int(data["port"]),
                    username=data["username"],
                    pkey=self.privaterKey(data["secret"], None)
                )
                logger.debug('秘钥认证成功: 主机:{} 用户:{} 端口：{}'.format(data["host"], data["username"], data["port"]))
            self.establish()
        except AuthenticationException:
            logger.debug('密码认证失败: 主机:{} 用户:{} 端口：{}'.format(data["host"], data["username"], data["port"]))
            raise Exception("auth failed user:%s ,passwd:%s" %
                            (data["username"], data["secret"]))
        except SSHException:
            logger.debug('秘钥认证失败: 主机:{} 用户:{} 端口：{}'.format(data["host"], data["username"], data["port"]))
            raise Exception("could not connect to host:%s:%s" %
                            (data["hostname"], data["port"]))
        except Exception as E:
            logger.debug('认证失败: 主机:{} 用户:{} 端口：{} 没有响应'.format(data["host"], data["username"], data["port"]))
            jscode = "completeAndReturnName('%s');" % json.dumps({'data': base64.b64encode(bytes('认证失败: 主机:{} 用户:{} 端口：{} 没有响应'.format(data["host"], data["username"], data["port"]),encoding='UTF-8')).decode('utf-8')})
            self.Qtext.QWebEng.page().runJavaScript(jscode)
            self.Qtext.open_win =False
            return
    def establish(self,term="xterm"):
        logger.debug('开启ssh会话')
        self.SHELL = self.ssh.invoke_shell(term)
        self.SHELL.setblocking(0)
        self._id = self.SHELL.fileno()
        self.IOST.register(self)
        self.IOST.add_future(self.trans_back())
    def trans_forward(self, data=""):
        if self.SHELL:
            logger.debug('向服务端发送信息:%s'%data)
            self.SHELL.send(data)

    def trans_back(self):
        yield self.id
        connected = True
        while connected:
            result = yield
            # if self._websocket:
            # if self.IOST:
            try:
                logger.debug('发送到客户端信息：%s'%str(result))
                jscode = "completeAndReturnName('%s');"% json.dumps({'data':base64.b64encode(result).decode('utf-8')})
                self.Qtext.QWebEng.page().runJavaScript(jscode)
            except Exception as E:
                logger.debug('客户端 WebSocketClosed：%s' % str(E))
                connected = False
            if str(result.strip(),'utf-8') == 'logout':
                connected = False
        self.destroy()
    def destroy(self):
        self.IOST.close()
        self.ssh.close()
        del  self.IOST
        del  self.ssh
        del self

from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
from ssh.Main_Window import *

class Print(QWidget):
    sendf = pyqtSignal(str)
    @pyqtSlot(str, result=str)
    def print(self, content):
        logger.debug('客户端事件')
        self.sendf.emit(content)
class Term(QWidget):
    clients = dict()
    def __init__(self,data,open_win=False):
        super(Term, self).__init__()
        self.resize(900, 600)
        self.hv = QHBoxLayout(self)
        # self.setWindowFlags(QtCore.Qt.Widget)
        self.open_win = open_win
        self.QWebEng = QWebEngineView(self)
        self.QWebEng.setObjectName('QWebEng')
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet('background-color:transparent')

        self.setContentsMargins(0, 0, 0, 0)
        # self.setSpacing(0)
        self.QWebEng.resize(400,400)
        self.hv.addWidget(self.QWebEng)
        self.hv.setContentsMargins(10, 10, 10, 10)
        self.hv.setSpacing(0)
        url = QUrl(QFileInfo("xterm.html").absoluteFilePath())
        self.QWebEng.load(url)
        self.QWebEng.showMaximized()
        # self.QWebEng.setHtml(xterm)
        self.data = data
        self.channel = QWebChannel()
        self.printer = Print()
        self.channel.registerObject('printer', self.printer)
        # self.QWebEng.page().setBackgroundColor(QColor(255, 0, 0, 0))
        self.QWebEng.page().setWebChannel(self.channel)
        # self.QWebEng.page().setBackgroundColor(Qt.transparent)
        self.QWebEng.page().setBackgroundColor(Qt.transparent)
        self.setWindowOpacity(0)

        self.printer.sendf.connect(self.send)
        self.defcmd="[%s:\~]$ "%os.getcwd().split(':')[0]
        self.Dos_Cmd=b''
        # print(os.path())
        if not self.open_win:
            jscode = "completeAndReturnName('%s');" % json.dumps({'data': base64.b64encode(b'aaaaa').decode('utf-8')})
            # print(jscode)
            #
            self.QWebEng.page().runJavaScript(jscode)
            # self.QWebEng.loadStarted()
        else:
            # self.open_client()
           threading.Thread(target=self.open_client).start()
            # Process(target=self.open_client).start()

    def open_client(self):


        if self.open_win:
            IOST = IOLoop.instance()
            IOST.start()
            bridge = Bridge(IOST, self)
            self.clients[self._id()] = bridge
            self.Start()
    def defalut_client(self,data):
        logger.debug('接受到默认端数据：%s' % data)
        if str(data) ==  str(b'\x7f'):
            print('退格键')
            print('>>>',data,str(data,'gbk'),bytes(str(data,'gbk'),encoding='utf-8'))
            data = b'\x07'
            if len(self.Dos_Cmd) != 0:
                self.Dos_Cmd = self.Dos_Cmd[:-1]
                data = b'\x08\x1b[K'
        elif str(data) == str(b'\r'):
            print('回车键')
            # data = b'\r\n'
            print( self.Dos_Cmd)
            if self.Dos_Cmd == b'clear':
                data = b'\x1b[3;J\x1b[H\x1b[2J\x1b]0;\x07'
            elif self.Dos_Cmd == b'ls':
                self.Dos_Cmd =b'dir'
            else:
                if self.Dos_Cmd !=b'':
                    try:
                        proc = subprocess.Popen(str(self.Dos_Cmd,'utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
                        std = str(proc.stdout.read(), 'gbk')
                        data = b'\r\n'+bytes((std if std else str(proc.stderr.read(), 'gbk')).replace('\n','\r\n'),encoding='utf-8')
                    except Exception as  e:
                        print(e)
            data = data +bytes('\r\n'+self.defcmd,encoding='utf-8')
            self.Dos_Cmd =b''
        else:
            self.Dos_Cmd = self.Dos_Cmd + data
        jscode = "completeAndReturnName('%s');" % json.dumps({'data': base64.b64encode(data).decode('utf-8')})
        # jscode = "completeAndReturnName('%s');" % json.dumps({'data': base64.b64encode(b'\n').decode('utf-8')})
        # print(jscode)
        self.QWebEng.page().runJavaScript(jscode)

    def get_client(self):
        return self.clients.get(self._id(), None)
    def _id(self):
        return id(self)
    def Start(self):
        self.bridge = self.get_client()
        logger.debug('打开ssh：%s'%self.data)
        # threading.Thread(target=self.bridge.open,args=).run()
        self.bridge.open(self.data)

    def send(self,data):
        data = json.loads(data)
        if self.open_win:
            logger.debug('发送到服务端数据：%s' % data)
            try:
                self.bridge.SHELL.resize_pty(width=data['cols'], height=data['rows'])
                if data['data']:
                    self.bridge.trans_forward(data['data'].encode())
            except Exception as E:
                logger.debug('客户端 Error:%s'%str(E))
        else:
            logger.debug('发送到默认数据：%s' % data)
            # Thread(target=self.defalut_client,args=bytes(data['data'], 'utf-8')).start()
            self.defalut_client(bytes(data['data'], 'utf-8'))



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     data = {'host': '39.107.100.236', 'port': '1993', 'username': 'root', 'ispwd':  True, 'secret': '@Scjz1993'}
#     # data = {'host': '192.168.110.134', 'port': '22', 'username': 'root', 'ispwd': True, 'secret': '123456'}
#     # fennbk = Terminal(data={})
#     fennbk = Term(data=data,open_win=True)
#     fennbk.show()
#     sys.exit(app.exec_())