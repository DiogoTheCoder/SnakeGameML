from Game import Game
import SnakeBot
import mysql.connector
from multiprocessing import Process
from google.cloud import error_reporting
import os
import time

def runGame():
    # This JSON file is provided by DiogoTheCoder
    client = error_reporting.Client.from_service_account_json('error-reporter-cred.json')
    try:
        cnx = mysql.connector.connect(user='root', password='admin',
                                host='104.199.13.110',
                                database='snakegame', connect_timeout=2)

    except mysql.connector.Error as err:
        cnx = None
        print("Something went wrong: {}".format(err))
        client.report_exception()

    finally:
        app = Game(cnx)
        app.on_execute()
    
        if cnx != None:
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