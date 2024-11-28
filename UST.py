word=" In the bustling bustling city city of New York, New York, the the bright bright lights lights and and the the constant constant hum hum of of activity activity create create an an atmosphere atmosphere that that is is both both exhilarating exhilarating and and exhausting exhausting. The bustling city lights and the constant hum of activity create an atmosphere that is both exhilarating and exhausting."
l= word.split()
m=l.copy()
count=0
for i in range(len(l)-1):
    if l[i] == l[i+1] or l[i]+"." == (l[i+1]):
        del m[i-count]
        count += 1
count=0
n=m.copy()
for i in range(len(m)-3):
    if m[i]+m[i+1] == m[i+2]+m[i+3]:
        del n[i-count],n[i-count]
        count += 1
print(" ".join(n))
