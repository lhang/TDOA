# -*- coding: utf-8 -*-
import os
import MySQLdb
import re

def SQLconn():
	#SQL连接参数
	conn = {"host":"127.0.0.1", "user":"root", "passwd":"lihang", "charset":"utf8", "db":"tdoa_tdoa"}
	#conn = {"host":"127.0.0.1", "user":"root", "passwd":"root", "charset":"utf8", "db":"tdoa_tdoa"}
	#conn = {cc}
	return conn

def checkin(user):
	#校验密码
	c = SQLconn()
	conn = MySQLdb.connect(host=c["host"], user=c["user"], passwd=c["passwd"], charset=c["charset"], db=c["db"])
	cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
	print "connect mysql"
	cursor.execute("SELECT account_password,account_name FROM account WHERE account_username='%s';"%user)
	print "select passwd in mysql"
	passwd = cursor.fetchall()
	conn.close()
	return passwd

def md5(passwd):
	import hashlib
	m = hashlib.md5()
	m.update(passwd)
	return m.hexdigest()

def get_calendar_data(arg):
	pass


def permission_check():
	pass
"""
def mission_check(mission_name, mission_content, mission_starttime, mission_plan_end_time):
	check_result = []
	if len(mission_name)>200 or len(mission_name)==0:
		check_result.append("任务名字不为空，且小于200字")
		return check_result
	elif len(mission_content)>10000 or len(mission_content)==0:
		check_result.append("任务内容不超过1万字，且不能为空")
		return check_result


def mission_save(mission_name, mission_content, mission_starttime, mission_plan_end_time):
	pass
"""