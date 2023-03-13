from flask import Flask,render_template,request,flash,redirect,url_for
import sqlite3
web = Flask(__name__)
conn = sqlite3.connect('buspass.db')
conn.execute('CREATE TABLE IF NOT EXISTS register(ID INTEGER PRIMARY KEY,Firstname TEXT,Lastname TEXT,Address TEXT,PermanentAddress TEXT,AadharNo INTEGER, PANNo TEXT,MobileNo INTEGER)')
conn.close()
@web.route('/')
def intro():
    return render_template('index.html')
@web.route('/home')
def home():
    return render_template('home.html')
if __name__ == '__main__':
    web.run(debug = True)