import re
text = u'You name is '
th = u'[ก-ฮ]+' # หรือใช้โค้ด th = u'[ก-ฮ]+'
match = re.search(th, text, re.U) # re.U เป็นคำสั่งใช้ Regular expression ใน unicode
try:
    print(match.group())
    print("TH")
except:
    print(ValueError)
    print("EN")