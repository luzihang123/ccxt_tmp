from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_v1_time = publicGetV1Time = Entry('v1/time', 'public', 'GET', {'cost': 1})
    public_get_v1_exchangeinfo = publicGetV1ExchangeInfo = Entry('v1/exchangeInfo', 'public', 'GET', {'cost': 1})
    public_get_v1_depth = publicGetV1Depth = Entry('v1/depth', 'public', 'GET', {'cost': 1})
    public_get_v1_aggtrades = publicGetV1AggTrades = Entry('v1/aggTrades', 'public', 'GET', {'cost': 1})
    public_get_v1_klines = publicGetV1Klines = Entry('v1/klines', 'public', 'GET', {'cost': 1})
    public_get_v1_ticker_24hr = publicGetV1Ticker24hr = Entry('v1/ticker/24hr', 'public', 'GET', {'cost': 1})
    public_get_v2_time = publicGetV2Time = Entry('v2/time', 'public', 'GET', {'cost': 1})
    public_get_v2_exchangeinfo = publicGetV2ExchangeInfo = Entry('v2/exchangeInfo', 'public', 'GET', {'cost': 1})
    public_get_v2_depth = publicGetV2Depth = Entry('v2/depth', 'public', 'GET', {'cost': 1})
    public_get_v2_aggtrades = publicGetV2AggTrades = Entry('v2/aggTrades', 'public', 'GET', {'cost': 1})
    public_get_v2_klines = publicGetV2Klines = Entry('v2/klines', 'public', 'GET', {'cost': 1})
    public_get_v2_ticker_24hr = publicGetV2Ticker24hr = Entry('v2/ticker/24hr', 'public', 'GET', {'cost': 1})
    marketcap_get_v1_assets = marketcapGetV1Assets = Entry('v1/assets', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_candles = marketcapGetV1Candles = Entry('v1/candles', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_orderbook = marketcapGetV1Orderbook = Entry('v1/orderbook', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_summary = marketcapGetV1Summary = Entry('v1/summary', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_ticker = marketcapGetV1Ticker = Entry('v1/ticker', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_token_assets = marketcapGetV1TokenAssets = Entry('v1/token/assets', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_token_orderbook = marketcapGetV1TokenOrderbook = Entry('v1/token/orderbook', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_token_summary = marketcapGetV1TokenSummary = Entry('v1/token/summary', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_token_ticker = marketcapGetV1TokenTicker = Entry('v1/token/ticker', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_token_trades = marketcapGetV1TokenTrades = Entry('v1/token/trades', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_token_crypto_ohlc = marketcapGetV1TokenCryptoOHLC = Entry('v1/token_crypto/OHLC', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_token_crypto_assets = marketcapGetV1TokenCryptoAssets = Entry('v1/token_crypto/assets', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_token_crypto_orderbook = marketcapGetV1TokenCryptoOrderbook = Entry('v1/token_crypto/orderbook', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_token_crypto_summary = marketcapGetV1TokenCryptoSummary = Entry('v1/token_crypto/summary', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_token_crypto_ticker = marketcapGetV1TokenCryptoTicker = Entry('v1/token_crypto/ticker', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_token_crypto_trades = marketcapGetV1TokenCryptoTrades = Entry('v1/token_crypto/trades', 'marketcap', 'GET', {'cost': 1})
    marketcap_get_v1_trades = marketcapGetV1Trades = Entry('v1/trades', 'marketcap', 'GET', {'cost': 1})
    private_get_v1_account = privateGetV1Account = Entry('v1/account', 'private', 'GET', {'cost': 1})
    private_get_v1_currencies = privateGetV1Currencies = Entry('v1/currencies', 'private', 'GET', {'cost': 1})
    private_get_v1_deposits = privateGetV1Deposits = Entry('v1/deposits', 'private', 'GET', {'cost': 1})
    private_get_v1_depositaddress = privateGetV1DepositAddress = Entry('v1/depositAddress', 'private', 'GET', {'cost': 1})
    private_get_v1_ledger = privateGetV1Ledger = Entry('v1/ledger', 'private', 'GET', {'cost': 1})
    private_get_v1_leveragesettings = privateGetV1LeverageSettings = Entry('v1/leverageSettings', 'private', 'GET', {'cost': 1})
    private_get_v1_mytrades = privateGetV1MyTrades = Entry('v1/myTrades', 'private', 'GET', {'cost': 1})
    private_get_v1_openorders = privateGetV1OpenOrders = Entry('v1/openOrders', 'private', 'GET', {'cost': 1})
    private_get_v1_tradingpositions = privateGetV1TradingPositions = Entry('v1/tradingPositions', 'private', 'GET', {'cost': 1})
    private_get_v1_tradingpositionshistory = privateGetV1TradingPositionsHistory = Entry('v1/tradingPositionsHistory', 'private', 'GET', {'cost': 1})
    private_get_v1_transactions = privateGetV1Transactions = Entry('v1/transactions', 'private', 'GET', {'cost': 1})
    private_get_v1_withdrawals = privateGetV1Withdrawals = Entry('v1/withdrawals', 'private', 'GET', {'cost': 1})
    private_get_v2_account = privateGetV2Account = Entry('v2/account', 'private', 'GET', {'cost': 1})
    private_get_v2_currencies = privateGetV2Currencies = Entry('v2/currencies', 'private', 'GET', {'cost': 1})
    private_get_v2_deposits = privateGetV2Deposits = Entry('v2/deposits', 'private', 'GET', {'cost': 1})
    private_get_v2_depositaddress = privateGetV2DepositAddress = Entry('v2/depositAddress', 'private', 'GET', {'cost': 1})
    private_get_v2_ledger = privateGetV2Ledger = Entry('v2/ledger', 'private', 'GET', {'cost': 1})
    private_get_v2_leveragesettings = privateGetV2LeverageSettings = Entry('v2/leverageSettings', 'private', 'GET', {'cost': 1})
    private_get_v2_mytrades = privateGetV2MyTrades = Entry('v2/myTrades', 'private', 'GET', {'cost': 1})
    private_get_v2_openorders = privateGetV2OpenOrders = Entry('v2/openOrders', 'private', 'GET', {'cost': 1})
    private_get_v2_tradingpositions = privateGetV2TradingPositions = Entry('v2/tradingPositions', 'private', 'GET', {'cost': 1})
    private_get_v2_tradingpositionshistory = privateGetV2TradingPositionsHistory = Entry('v2/tradingPositionsHistory', 'private', 'GET', {'cost': 1})
    private_get_v2_transactions = privateGetV2Transactions = Entry('v2/transactions', 'private', 'GET', {'cost': 1})
    private_get_v2_withdrawals = privateGetV2Withdrawals = Entry('v2/withdrawals', 'private', 'GET', {'cost': 1})
    private_get_v2_fetchorder = privateGetV2FetchOrder = Entry('v2/fetchOrder', 'private', 'GET', {'cost': 1})
    private_post_v1_order = privatePostV1Order = Entry('v1/order', 'private', 'POST', {'cost': 1})
    private_post_v1_updatetradingposition = privatePostV1UpdateTradingPosition = Entry('v1/updateTradingPosition', 'private', 'POST', {'cost': 1})
    private_post_v1_updatetradingorder = privatePostV1UpdateTradingOrder = Entry('v1/updateTradingOrder', 'private', 'POST', {'cost': 1})
    private_post_v1_closetradingposition = privatePostV1CloseTradingPosition = Entry('v1/closeTradingPosition', 'private', 'POST', {'cost': 1})
    private_post_v2_order = privatePostV2Order = Entry('v2/order', 'private', 'POST', {'cost': 1})
    private_post_v2_updatetradingposition = privatePostV2UpdateTradingPosition = Entry('v2/updateTradingPosition', 'private', 'POST', {'cost': 1})
    private_post_v2_updatetradingorder = privatePostV2UpdateTradingOrder = Entry('v2/updateTradingOrder', 'private', 'POST', {'cost': 1})
    private_post_v2_closetradingposition = privatePostV2CloseTradingPosition = Entry('v2/closeTradingPosition', 'private', 'POST', {'cost': 1})
    private_delete_v1_order = privateDeleteV1Order = Entry('v1/order', 'private', 'DELETE', {'cost': 1})
    private_delete_v2_order = privateDeleteV2Order = Entry('v2/order', 'private', 'DELETE', {'cost': 1})
