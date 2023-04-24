from yahoo_fin.stock_info import *
df = get_data('PETR4.SA', start_date='2020-08-14', end_date='2020-12-31')
print(df)
