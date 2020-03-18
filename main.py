from Solution import Solution

def main():
	s = ["key", "egg", "car", "night"]
	t = ["git", "see", "eye","knife"]
	print("S1: ", s)
	print("S2: ",t)
	print()
	print("Solution: ")
	sol = [True, True, False, True]
	l = []*len(s)
	for i in range(len(s)):
		b = Solution.charMapping(s[i],t[i])
		l.append(b)
	print(l)
	print()
	print("Expected : ")
	print(sol)

if __name__== "__main__":
	main()
