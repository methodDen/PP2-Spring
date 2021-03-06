c = [[0] * 2] * 2
N = 2
mod = 1e9 + 7
def pasc():
	for i in range(0, N):
		c[i][0] = c[i][i] = 1
		for j in range(1, i):
			c[i][j] = (c[i-1][j-1] + c[i - 1][j]) % mod


	print(c)

pasc()				