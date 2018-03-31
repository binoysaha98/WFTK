#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template,session,request
from controllers.adminCon import adminCon
from controllers.loginCon import loginCon
from SessionManager import SessionManager
import os
import cx_Oracle

global con, cur

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/admin', methods=['GET','POST'])
def admin():
    print(session['user'])
    if(session['user'] != None):
        print(session['user'])
        return adminCon(con, cur).index()
    else:
        print("What a")

@app.route('/dropSession')
def dropSession():
    SessionManager().destroy_session()
    return 'session_dropped'


@app.route('/login')
def login():
    return loginCon(con, cur).index()

@app.route('/employee')
def emloyee():
    return render_template('employee.html')

@app.route('/supervisor')
def supervisor():
    return render_template('supervisor.html')

@app.route('/loginUser', methods=['GET','POST'])
def loginUser():
    data = {'username':request.form['username'],'password':request.form['password']}
    return loginCon(con, cur).login(data)

def connect_db():
    con = cx_Oracle.connect('system/mansik123@127.0.0.1/XE')
    cur = con.cursor()
    return cur, con


if __name__ == '__main__':
    cur, con = connect_db()
    print('cur {} con {}'.format(cur, con))
    app.run(debug=True)

