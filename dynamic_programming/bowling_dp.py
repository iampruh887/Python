#solves the last dp problem of first lecture of mit 6.0006 latest lectures
def solve(v, i):
	score = 0
	if i >= len(v): 
		return 0
	else:
		if i<len(v) and i+1 < len(v):
			score += max([solve(v, i+1), v[i] + solve(v, i+1), v[i]*v[i+1] + solve(v, i+2)]);
		return score
 
v = []
n = int(input());
for i in range(n):
	v.append(int(input()))
print(solve(v, 0))
