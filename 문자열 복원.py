import re
ctoa = lambda c: chr(int(c)+ord('a')-1) if c.isdigit() else c
encode = input()
decoding = re.sub('(\d{2})0(?!0)', lambda m:ctoa(m.group(1)), encode)
decoding = ''.join([ctoa(c) for c in decoding])
print(decoding)