import time

irange = 1000000
jrange = 10

iarr = []
for x in range(irange):
    iarr.append(x)

jarr = []
for x in range(jrange):
    jarr.append(x)

starttime = time.time()

for j in jarr:
    for i in iarr:
        iarr[i] *= jarr[j]


print time.time() - starttime

starttime = time.time()

for i in iarr:
    for j in jarr:
        iarr[i] *= jarr[j]

print time.time() - starttime