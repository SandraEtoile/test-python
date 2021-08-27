# print("Hello, World!")
#
# # fibonacci
# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a + b
#
#

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

#
# txns = [1.09, 23.56, 57.84, 4.56, 6.78]
# TAX_RATE = .08
# def get_price_with_tax(txn):
#     return txn * (1 + TAX_RATE)
# final_prices = map(get_price_with_tax, txns)
# print(final_prices)
# print(list(final_prices))