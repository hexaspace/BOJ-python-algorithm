import datetime
# 검색결과 여러 방법이 있다.
# str(dt.now())[:10]
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d'))