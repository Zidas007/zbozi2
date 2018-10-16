novepole=[]
pole=[1,6,8,10,42,25,366,99,336,420]
print pole

idx=0
while pole.__len__()>0:
    minhodnota = 999
    for objpole in pole:
        if minhodnota >= objpole:
            minhodnota=objpole
    print minhodnota
    if minhodnota <> 999:
        pole.remove(minhodnota)
        novepole.append(minhodnota)
print novepole