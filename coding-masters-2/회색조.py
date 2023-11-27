code = input()[1:]
print("#"+hex(round(sum(map(lambda d: int(d,16),[code[0:2],code[2:4],code[4:6]]))/3))[2:].upper().zfill(2)*3)