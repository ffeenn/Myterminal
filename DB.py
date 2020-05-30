
import sqlite3,paramiko,json
class db(object):
    def __init__(self,DBname = 'platform.db'):
        self.crdb = sqlite3.connect(DBname)
        self.crdb.isolation_level = None
        self.yb = self.crdb.cursor()
        if DBname == 'platform.db':
            try:
                self.yb.execute('CREATE TABLE ssh_host (id integer primary key autoincrement,name varchar(42) not null,host varchar(15) not null,port varchar(5),user varchar(1024),passwd varchar(1024),cer varchar(1024),hgroup varchar(1024),cmd varchar(1024))')
            except Exception as E:
                pass
            try:
                self.yb.execute(
                    'CREATE TABLE ssh_group (id integer primary key autoincrement,hgroup varchar(1024) not null)')
            except Exception as E:
                pass

    def upda(self,a_data):
        self.ub = self.crdb.cursor()
        self.ub.execute(a_data)
        da = self.ub.fetchall()
        self.crdb.close()
        return da,len(da)

# db = db()
# print(db.upda("select * from szy_config"))
# print(db.upda("select * from szy_config"))
import json
#
# a='1,2'
# b = str(a)
# print(b)
# print(list(b))
# print(','.join(a))
# a = {
#     'cy':[],
#     'soft':[],
#     'dir':[],
#     'word':[],
#     'zip':[],
#     'szy':[]
#
# }
# print(json.dumps(a))
