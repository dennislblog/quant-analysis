import pytest
from lib.spider import StockSpider
from lib.database import Database
import csv


def test_connect():
    conn, cur = Database.get_mysql("haha")
    print(cur.rowcount)
    try:
        print(cur.rowcount)
    finally:
        cur.close()
        conn.close()


@pytest.mark.parametrize('start', ["20200101"])
@pytest.mark.parametrize('end', ["20200201"])
def test_craw(start, end):
    conn, cur = Database.create_mysql("tmp")
    with open("./lib/spider/tickers.csv", "r") as f:
        reader = csv.reader(f, delimiter=',')
        tickers = list(reader)
    stock_collector = StockSpider()
    stock_collector.craw(conn, cur, tickers, start, end)
