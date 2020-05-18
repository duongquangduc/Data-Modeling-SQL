# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:13:53 2020

@author: DucDQ1
"""
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    # connect to default database
    conn = psycopg2.connect("host=localhost dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database using UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkify")
    cur.execute("CREATE DATABASE sparkify WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host=localhost dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    return cur, conn

def drop_table(cur, conn):
    for query in drop_table_queries:
        curr.execute(query)
        conn.commit()

def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    cur, conn = create_database()
    drop_table(cur, conn)
    create_tables(cur, conn)

if __name__ == "__main__":
    main()

