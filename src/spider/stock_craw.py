
import requests
import re
import json
import time


class StockSpider:
    def crawStockHistoryBySoHu(self, code, ctype='cn', start='20100101', end='20171201'):
        url = 'http://q.stock.sohu.com/hisHq?code=' + ctype + '_' + code + '&start=' + start + \
            '&end=' + end + '&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp'
        html = requests.get(url).text
        html = html[html.index('{'): html.rindex('}') + 1]
        data = []
        if html != '{}':
            data = json.loads(html)
            data = data['hq']
        return data

    def craw(self, conn, cur, ticker_list, start, end):
        insertStockSql = 'INSERT INTO stock (`id`, `name`, `code`) VALUES (%s, %s, %s)'
        insertContentSql = 'INSERT INTO history (`stock_id`, `date`, `opening`, `closing`, `difference`, `percentage_difference`, `lowest`, `highest`, `volume`, `amount`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        for ticker, ctype in ticker_list:
            cur.execute(insertStockSql, [ticker, "", ctype])
            stockId = conn.insert_id()
            data = self.crawStockHistoryBySoHu(ticker, ctype, start, end)
            for d in data:
                cur.execute(insertContentSql, [stockId, d[0], d[1],
                                               d[2], d[3], d[4][0:-1], d[5], d[6], d[7], d[8]])
                conn.commit()
