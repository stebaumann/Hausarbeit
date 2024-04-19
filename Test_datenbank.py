# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:03:02 2024

@author: bauma
"""

from sqlalchemy import create_engine
from sqlalchemy import text
import sqlalchemy as db

engine = create_engine("sqlite+pysqlite:///Datenbank.sqlite", echo=True)
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS some_table (x int, y int)"))
    conn.execute(text("DELETE FROM some_table"))
    conn.execute(
         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.commit()



engine = create_engine("sqlite+pysqlite:///Trainingsfunktion.sqlite", echo=True)
connection = engine.connect()
meta_data = db.MetaData()

train = db.Table("train", meta_data, db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False), 
                 db.Column("Y1", db.Float, nullable=False),db.Column("Y2", db.Float, nullable=False))
    
meta_data.create_all(engine)