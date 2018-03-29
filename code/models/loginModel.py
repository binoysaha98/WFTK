class loginModel:
    def __init__(self, con, cur):
        print("Login model constructor")
        self.con = con
        self.cur = cur

    def auth(self,data):
        print('login model auth')
        returndata = self.cur.execute(
            "SELECT * FROM binoy.employee where name='{0}' AND password='{1}'".format(data['username'],
                                                                                      data['password']))
        data = returndata.fetchall();
        users = self.zip_data(self.cur, data)
        for user in users:
            return (True,user)
        return (False,None)

    def zip_data(self, cur, rows):
        print('Zipping data')
        columns = [i[0].lower() for i in cur.description]
        return [dict(zip(columns, row)) for row in rows]

