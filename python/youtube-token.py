s = input()
g = "https://youtu.be/"
f = "https://www.youtube.com/watch?v="
if g in s:
   er = s.split('/')
   print(er[3])
elif f in s:
   ed = s.split('=')
   print(ed[1])
