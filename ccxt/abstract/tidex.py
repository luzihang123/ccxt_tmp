from ccxt.base.types import Entry


class ImplicitAPI:
    web_get_currency = webGetCurrency = Entry('currency', 'web', 'GET', {})
    web_get_pairs = webGetPairs = Entry('pairs', 'web', 'GET', {})
    web_get_tickers = webGetTickers = Entry('tickers', 'web', 'GET', {})
    web_get_orders = webGetOrders = Entry('orders', 'web', 'GET', {})
    web_get_ordershistory = webGetOrdershistory = Entry('ordershistory', 'web', 'GET', {})
    web_get_trade_data = webGetTradeData = Entry('trade-data', 'web', 'GET', {})
    web_get_trade_data_id = webGetTradeDataId = Entry('trade-data/{id}', 'web', 'GET', {})
    public_get_info = publicGetInfo = Entry('info', 'public', 'GET', {})
    public_get_ticker_pair = publicGetTickerPair = Entry('ticker/{pair}', 'public', 'GET', {})
    public_get_depth_pair = publicGetDepthPair = Entry('depth/{pair}', 'public', 'GET', {})
    public_get_trades_pair = publicGetTradesPair = Entry('trades/{pair}', 'public', 'GET', {})
    private_post_getinfoext = privatePostGetInfoExt = Entry('getInfoExt', 'private', 'POST', {})
    private_post_getinfo = privatePostGetInfo = Entry('getInfo', 'private', 'POST', {})
    private_post_trade = privatePostTrade = Entry('Trade', 'private', 'POST', {})
    private_post_activeorders = privatePostActiveOrders = Entry('ActiveOrders', 'private', 'POST', {})
    private_post_orderinfo = privatePostOrderInfo = Entry('OrderInfo', 'private', 'POST', {})
    private_post_cancelorder = privatePostCancelOrder = Entry('CancelOrder', 'private', 'POST', {})
    private_post_tradehistory = privatePostTradeHistory = Entry('TradeHistory', 'private', 'POST', {})
    private_post_getdepositaddress = privatePostGetDepositAddress = Entry('getDepositAddress', 'private', 'POST', {})
    private_post_createwithdraw = privatePostCreateWithdraw = Entry('createWithdraw', 'private', 'POST', {})
    private_post_getwithdraw = privatePostGetWithdraw = Entry('getWithdraw', 'private', 'POST', {})