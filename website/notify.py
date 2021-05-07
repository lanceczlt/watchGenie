from flask import Flask, render_template, request, Blueprint, session
from flask_mail import Mail, Message
import socket
from .db_connection import connect

connection, cursor = connect()




    # msg = Message(
    #     subject='',
    #     recipients=[],
    #     body='',
    #     html='',
    #     sender='',
    #     cc=[],
    #     bcc=[],
    #     attachments=[],
    #     reply_to=[],
    #     date= 'date',
    #     charset= '',
    #     extra_headers= {'headername' : 'headervalue'},
    #     #mail options from esmtp
    #     mail_options=[],
    #     rcpt_options=[]


    # )



def send_bulk_mail():
    user_id = session['id']

    users = [{ 'name' : '', 'email' : 'email@gmail.com'}] 

    usersList = []
    with mail.connect() as conn:
        for user in usersList:
            msg = Message('Bulk!', recipients=[user['email']])
            msg.body = 'Hey There, here is your movie recommendation of the week!, so exciting'
            conn.send(msg)






