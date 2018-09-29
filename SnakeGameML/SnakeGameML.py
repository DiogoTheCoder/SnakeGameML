from Game import Game
import SnakeBot
import mysql.connector

if __name__ == "__main__":
    cnx = mysql.connector.connect(user='root', password='admin',
                              host='104.199.13.110',
                              database='snakegame')

    app = Game(cnx)
    app.on_execute()
    #SnakeBot.randy()
    cnx.close()