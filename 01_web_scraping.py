import requests as re
url="https://www.saramin.co.kr/zf_user/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"} #user agent string
res = re.get(url, headers=headers)
print("응답코드 : ", res.status_code)
#res.raise_for_status()  #문제가 있으면 종료 없으면 진행

with open("saramin.html", "w", encoding="utf8") as f:
  f.write(res.text)










'''
if res.status_code == re.codes.ok:
  print("정상입니다")
else:
  print("문제가 생겼습니다.[에러코드",res.requests_code,"]")
'''