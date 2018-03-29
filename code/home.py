#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from controllers.adminCon import adminCon
import cx_Oracle

global con, cur

app = Flask(__name__)


@app.route('/admin')
def admin():
    return adminCon(con, cur).index()


def connect_db():
    con = cx_Oracle.connect('system/mansik123@127.0.0.1/XE')
    cur = con.cursor()
    return (cur, con)


if __name__ == '__main__':
    (cur, con) = connect_db()
    print('cur {} con {}'.format(cur, con))
    app.run(debug=True)
