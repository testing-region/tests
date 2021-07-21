import math

tt = 180.96

sd = math.modf(tt)

degs = int(sd[1])

sf1 = sd[0]*60
sf = math.modf(sf1)

mins = int(sf[1])

sa1 = sf[0]*60
secs = round(sa1, 2)

print(tt)
print(deg)
print(mins)
print(secs)