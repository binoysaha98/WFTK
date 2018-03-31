class supervisorModel:
    def __init__(self, con, cur):
        print("supervisor model constructor")
        self.con = con
        self.cur = cur

    def index(self):
        print('supervisor model index')
        data = self.cur.execute('select * from binoy.site');
        sites = data.fetchall()
        return self.zip_data(self.cur, sites)

    def zip_data(self, cur, rows):
        print('Zipping data')
        columns = [i[0].lower() for i in cur.description]
        return [dict(zip(columns, row)) for row in rows]

