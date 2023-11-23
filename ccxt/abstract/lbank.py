from ccxt.base.types import Entry


class ImplicitAPI:
    spot_public_get_currencypairs = spotPublicGetCurrencyPairs = Entry('currencyPairs', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_accuracy = spotPublicGetAccuracy = Entry('accuracy', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_usdtocny = spotPublicGetUsdToCny = Entry('usdToCny', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_withdrawconfigs = spotPublicGetWithdrawConfigs = Entry('withdrawConfigs', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_timestamp = spotPublicGetTimestamp = Entry('timestamp', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_ticker_24hr = spotPublicGetTicker24hr = Entry('ticker/24hr', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_ticker = spotPublicGetTicker = Entry('ticker', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_depth = spotPublicGetDepth = Entry('depth', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_incrdepth = spotPublicGetIncrDepth = Entry('incrDepth', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_trades = spotPublicGetTrades = Entry('trades', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_kline = spotPublicGetKline = Entry('kline', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_supplement_system_ping = spotPublicGetSupplementSystemPing = Entry('supplement/system_ping', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_supplement_incrdepth = spotPublicGetSupplementIncrDepth = Entry('supplement/incrDepth', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_supplement_trades = spotPublicGetSupplementTrades = Entry('supplement/trades', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_supplement_ticker_price = spotPublicGetSupplementTickerPrice = Entry('supplement/ticker/price', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_get_supplement_ticker_bookticker = spotPublicGetSupplementTickerBookTicker = Entry('supplement/ticker/bookTicker', ['spot', 'public'], 'GET', {'cost': 2.5})
    spot_public_post_supplement_system_status = spotPublicPostSupplementSystemStatus = Entry('supplement/system_status', ['spot', 'public'], 'POST', {'cost': 2.5})
    spot_private_post_user_info = spotPrivatePostUserInfo = Entry('user_info', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_subscribe_get_key = spotPrivatePostSubscribeGetKey = Entry('subscribe/get_key', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_subscribe_refresh_key = spotPrivatePostSubscribeRefreshKey = Entry('subscribe/refresh_key', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_subscribe_destroy_key = spotPrivatePostSubscribeDestroyKey = Entry('subscribe/destroy_key', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_get_deposit_address = spotPrivatePostGetDepositAddress = Entry('get_deposit_address', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_deposit_history = spotPrivatePostDepositHistory = Entry('deposit_history', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_create_order = spotPrivatePostCreateOrder = Entry('create_order', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_batch_create_order = spotPrivatePostBatchCreateOrder = Entry('batch_create_order', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_cancel_order = spotPrivatePostCancelOrder = Entry('cancel_order', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_cancel_clientorders = spotPrivatePostCancelClientOrders = Entry('cancel_clientOrders', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_orders_info = spotPrivatePostOrdersInfo = Entry('orders_info', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_orders_info_history = spotPrivatePostOrdersInfoHistory = Entry('orders_info_history', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_order_transaction_detail = spotPrivatePostOrderTransactionDetail = Entry('order_transaction_detail', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_transaction_history = spotPrivatePostTransactionHistory = Entry('transaction_history', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_orders_info_no_deal = spotPrivatePostOrdersInfoNoDeal = Entry('orders_info_no_deal', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_withdraw = spotPrivatePostWithdraw = Entry('withdraw', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_withdrawcancel = spotPrivatePostWithdrawCancel = Entry('withdrawCancel', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_withdraws = spotPrivatePostWithdraws = Entry('withdraws', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_user_info = spotPrivatePostSupplementUserInfo = Entry('supplement/user_info', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_withdraw = spotPrivatePostSupplementWithdraw = Entry('supplement/withdraw', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_deposit_history = spotPrivatePostSupplementDepositHistory = Entry('supplement/deposit_history', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_withdraws = spotPrivatePostSupplementWithdraws = Entry('supplement/withdraws', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_get_deposit_address = spotPrivatePostSupplementGetDepositAddress = Entry('supplement/get_deposit_address', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_asset_detail = spotPrivatePostSupplementAssetDetail = Entry('supplement/asset_detail', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_customer_trade_fee = spotPrivatePostSupplementCustomerTradeFee = Entry('supplement/customer_trade_fee', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_api_restrictions = spotPrivatePostSupplementApiRestrictions = Entry('supplement/api_Restrictions', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_system_ping = spotPrivatePostSupplementSystemPing = Entry('supplement/system_ping', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_create_order_test = spotPrivatePostSupplementCreateOrderTest = Entry('supplement/create_order_test', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_supplement_create_order = spotPrivatePostSupplementCreateOrder = Entry('supplement/create_order', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_supplement_cancel_order = spotPrivatePostSupplementCancelOrder = Entry('supplement/cancel_order', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_supplement_cancel_order_by_symbol = spotPrivatePostSupplementCancelOrderBySymbol = Entry('supplement/cancel_order_by_symbol', ['spot', 'private'], 'POST', {'cost': 1})
    spot_private_post_supplement_orders_info = spotPrivatePostSupplementOrdersInfo = Entry('supplement/orders_info', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_orders_info_no_deal = spotPrivatePostSupplementOrdersInfoNoDeal = Entry('supplement/orders_info_no_deal', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_orders_info_history = spotPrivatePostSupplementOrdersInfoHistory = Entry('supplement/orders_info_history', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_user_info_account = spotPrivatePostSupplementUserInfoAccount = Entry('supplement/user_info_account', ['spot', 'private'], 'POST', {'cost': 2.5})
    spot_private_post_supplement_transaction_history = spotPrivatePostSupplementTransactionHistory = Entry('supplement/transaction_history', ['spot', 'private'], 'POST', {'cost': 2.5})
    contract_public_get_cfd_openapi_v1_pub_gettime = contractPublicGetCfdOpenApiV1PubGetTime = Entry('cfd/openApi/v1/pub/getTime', ['contract', 'public'], 'GET', {'cost': 2.5})
    contract_public_get_cfd_openapi_v1_pub_instrument = contractPublicGetCfdOpenApiV1PubInstrument = Entry('cfd/openApi/v1/pub/instrument', ['contract', 'public'], 'GET', {'cost': 2.5})
    contract_public_get_cfd_openapi_v1_pub_marketdata = contractPublicGetCfdOpenApiV1PubMarketData = Entry('cfd/openApi/v1/pub/marketData', ['contract', 'public'], 'GET', {'cost': 2.5})
    contract_public_get_cfd_openapi_v1_pub_marketorder = contractPublicGetCfdOpenApiV1PubMarketOrder = Entry('cfd/openApi/v1/pub/marketOrder', ['contract', 'public'], 'GET', {'cost': 2.5})