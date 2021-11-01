**Number System Task**

```.py
def convert(i):
	if (i == 0):
		return
	x = i % base
	i //= 3
	if (x < 0):
		i += 1
		
	convert(i)
	if (x < 0):
		print(x + (3 * -1), end = "")
	else:
		print(x, end = "")

def count_base(base):
    for y in range(1,101):
        a=y
        def convert(i):
        	if (i == 0):
        		return
        	x = i % base
        	i //= base
        	if (x < 0):
        		i += 1
        		
        	convert(i)
        	if (x < 0):
        		print(x + (base * -1), end = "")
        	else:
        		print(x, end = "")
        print(str(a) + " demical with base " + str(base) + " is ")
        convert(a)
        print('\n')
count_base(3)
```
