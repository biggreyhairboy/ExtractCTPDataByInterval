#-*- coding: utf-8 -*-

from DBDriver import DBHanlder
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql://root:223223@127.0.0.1/talk_is_cheap?charset=utf8')
df = pd.read_sql_query("select * from tick_data_futures", engine)
#print df
#

print df["High"]
#DBHanlder dhq
#dh.ExtractMinuteData(6)


