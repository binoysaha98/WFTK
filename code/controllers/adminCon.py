#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template
from models.adminModel import adminModel


class adminCon:

    def __init__(self, con, cur):
        self.con = con
        self.cur = cur
        print('admin Controller constructor')

    def index(self):
        print('cur')
        sites = adminModel(self.con, self.cur).index()
        print('got data from model {}'.format(sites))
        return render_template('admin.html', sites=sites)
