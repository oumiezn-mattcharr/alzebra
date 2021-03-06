'''
Copyright (C) 2020 Oumayma Zinoun & Matthieu Charrier. All rights reserved.
No part of this document may be reproduced or transmitted in any form
or for any purpose without the express permission of Oumayma Zinoun and Matthieu Charrier.
'''

# !/usr/bin/env/ python3
# coding: utf-8

from importation import HistoricalData

def main ():
    tickers = ['^FCHI']
    data = HistoricalData (tickers=tickers, frequency='1wk')
    data.download ()
    data.candlesticks (tickers='all')
    data.plot (tickers='all', kind='close')
    #data.clear ()

main ()
