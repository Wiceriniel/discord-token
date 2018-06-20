import sqlite3
import os

path = (os.getenv('APPDATA')) + r"\discord\Local Storage\https_discordapp.com_0.localstorage"
data = sqlite3.connect(path)
selectdata = data.cursor()
read = selectdata.execute('SELECT value FROM ItemTable WHERE key="token"')
token = read.fetchone()[0].decode('utf-16le')
data.commit()
data.close()
print("Your Discord token: " + token + "\n\nPress Enter to exit.")
input()