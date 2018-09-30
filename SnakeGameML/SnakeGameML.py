from Game import Game
import SnakeBot
import mysql.connector
from multiprocessing import Process
import os

def runGame():
    cnx = mysql.connector.connect(user='root', password='admin',
                            host='104.199.13.110',
                            database='snakegame')
    app = Game(cnx)
    app.on_execute()

    cnx.close()

if __name__ == "__main__":
    # Multiprocessing
    processes = []

    for x in range(os.cpu_count()):
        processes.append(Process(target=runGame))

    for process in processes:
        process.start()

    for process in processes:
        process.join()