#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template,redirect,url_for,session
from models.loginModel import loginModel
from SessionManager import SessionManager
class loginCon:

    def __init__(self, con, cur):
        self.con = con
        self.cur = cur
        print('login Controller constructor')

    def index(self):
        return render_template('login.html')

    def login(self,data):
        (res,user) = loginModel(self.con,self.cur).auth(data)
        if(res == True):
            SessionManager().set_session(user)
            return redirect(url_for('admin'),code=307)
        else:
            return redirect(url_for('login'))
