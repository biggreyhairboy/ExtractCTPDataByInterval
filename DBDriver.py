from sqlalchemy import create_engine
import tushare as ts
## alter database talk_is_cheap character set utf8 collate utf8_unicode_ci;
## alter table tick_data convert to character set utf8 collate utf8_unicode_ci;
class DBHanlder:
    ConnectionStr = "mysql://root:223223@127.0.0.1/talk_is_cheap?charset=utf8"

    def InitializeConnection(self, con):
        engine = create_engine()
        pass

    def ExtractMinuteData(self, frequency):
        pass

    def ExtractDailyData(self, frequency):
        pass


