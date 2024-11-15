from   typing import Union
import sqlite3

dataBaseSchemes = {
    'users': 'users (id int primary key, link varchar(32), userType varchar(1), groupName varchar(32))',
    'marks': 'marks (id int primary key, link varchar(32), USERNAME varchar(32), USERPASS varchar(32), authorized varchar(1))'
}

class DataBase:

    def __init__(self, dataBaseName: str) -> None:

        self.dataBaseName: str = dataBaseName
        self.scheme:       str = dataBaseSchemes[dataBaseName]

    def envelopeDB(function):

        def envelope(self, *args) -> any:

            connect = sqlite3.connect(f'bd/rasp.db')
            cursor  = connect.cursor()

            cursor.execute(f'CREATE TABLE IF NOT EXISTS {self.scheme}')
            result: any = function(self, cursor, *args)
            connect.commit()

            cursor.close()
            connect.close()

            return result

        return envelope 

    @envelopeDB
    def createUser(self, cursor, data) -> bool:

        if not self.getUser(data['id']):

            cursor.execute(f'INSERT INTO {self.dataBaseName}(id, link) VALUES ("%s", "%s")' % (data['id'], data['link']))

            return True
        
        else:

            return False

    @envelopeDB
    def updateUser(self, cursor, data) -> bool:

        if bool(self.getUser(data['id'])):

            cursor.execute(f'UPDATE {self.dataBaseName} SET {data['dataName']}=? WHERE id=?', (data['data'], data['id']))

            return True
        
        else:

            return False

    @envelopeDB
    def getUser(self, cursor, id):
        
        user = cursor.execute(f'SELECT * FROM {self.dataBaseName} WHERE id=?', (id,)).fetchone()
        
        if user != None:

            return user
        
        else:

            return False




