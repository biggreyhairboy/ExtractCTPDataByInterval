#!/usr/bin/env python
# coding=utf-8
from sqlalchemy import create_engine
import tushare as ts
df = ts.get_tick_data('000001', date = '2016-07-01')

engine = create_engine('mysql://root:223223@127.0.0.1/talk_is_cheap?charset=utf8')
df.to_sql('tick_data', engine, if_exists = 'append')
