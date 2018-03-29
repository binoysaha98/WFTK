from flask import session
class SessionManager:
    def __init__(self):
        print("Session manager is now awake")

    def set_session(self,data):
        print('sm data {}'.format(data))
        session['user'] = data;

    def get_session(self):
        print(session['user'])