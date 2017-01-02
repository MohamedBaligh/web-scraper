def func():
   i = 0
   while True:
     i += 1
     yield i 


f = func()
print f.next()
print f.next()
