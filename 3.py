f0 = 0
f1 = 1
f = []
f.append(f0)
f.append(f1)

print('f(0) = 0')
print('f(1) = 1')
print('f(n) = f(n-1)+f(n-2)')
print('Input N : ')
n = input()

# fn = f[n-1]+f[n-2]

for i in range(2,int(n)+1):
	fn=f[i-1]+f[i-2]
	f.append(fn)

print('result f(',n,') = ',f[int(n)])