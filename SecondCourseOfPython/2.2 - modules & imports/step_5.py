from datetime import date, timedelta

start_date = date(*(int(i) for i in input().split()))
end_date = start_date + timedelta(days = int(input()))
print(end_date.year, end_date.month, end_date.day)

# знал бы функцию map, написал бы так:
# from datetime import date, timedelta
# inp1 = list(map(int, input().split()))
# inp2 = int(input())
#
# date = date(*inp1)
# days = timedelta(inp2)
# result = date + days
#
# print(result.year, result.month, result.day)
