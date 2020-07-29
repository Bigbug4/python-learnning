import sys


def maxSlideWindow(s, t, size):
	n = len(s)
	for i in range(0, n - size + 1):
		num = 0
		tmp = s[i:i + size]
		for j in t:
			if j in tmp:
				num += 1
		if num == len(t):
			return tmp

'''
line=[]
for _ in range(2):
	line.append(sys.stdin.readline().strip())

s,t=line[0],line[1]
'''
res=[]
#lines=sys.stdin.readlines()
#for line in lines:
while True:
	line=sys.stdin.readline().strip()
	if not line:
		print("\n".join(res))
		break
	s,t=line.split()
#	s,t=s.strip('\n'),t.strip('\n')
	n = len(s)
	size = len(t)
	ans=''
	for i in range(size, n+1):
		ans = maxSlideWindow(s, t, i)
		if ans:
			#print(res)
			res.append(ans)
			break
	if not ans:
		res.append('\n')
