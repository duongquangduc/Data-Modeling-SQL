import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

def process_song_file(cur, filepath):
    # open song file

def process_log_file(cur, filepath):
    pass


def process_data(cur, filepath):
    # get all files matching extension from directory

    # get total number of files found

    # iterate over files and process

def main():
    conn = psycopg2.connect("host=localhost dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()

if __name__ =="__main__":
    main()