#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template,session,request
from controllers.adminCon import adminCon
from controllers.loginCon import loginCon
import os
import cx_Oracle

global con, cur

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/admin', methods=['POST'])
def admin():
    return adminCon(con, cur).index()

@app.route('/login')
def login():
    return loginCon(con, cur).index()

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

