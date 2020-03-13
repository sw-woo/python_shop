# import numpy as np
# import pandas as pd
#
# a = np.array(1, 2)
# b = np.array(2, 3, 4, 5, 6, 7)
#
# for i in a:
#     print(a)
#
# for i in range(1, 10):
#     for j in range(1, 10):
#         print("%dX%d=%d", i, j, i * j)


cur_price = {'Daum KAKAO': 80000, 'NAVER': 800000, 'Dashin': 30000}
price_Key = cur_price.keys()
print(price_Key)
print(list(price_Key))

price_value = cur_price.values()
print(price_value)

print(cur_price['NAVER'])
cur_price['NAVER'] = 8000000
print(cur_price)

del cur_price['Dashin']
print(cur_price)

naver_closing_price = [488500, 461500, 50100, 500500, 488500]
print(naver_closing_price)

max_price = max(naver_closing_price)
print(max_price)

min_price = min(naver_closing_price)
print(min_price)
print("가격차", max_price - min_price)

print("수요일 종가:", naver_closing_price[2])

naver_closing_price2 = {'09/07': 474500, '09/08': 461500, '09/09': 501000,
                        '09/10': 500500, '09/11': 488500}
day_price = naver_closing_price2['09/07']
print(day_price)
