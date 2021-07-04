def longest_pal(s):
    return next((sub for sub in sorted([s[i:j] for i in range(0, len(s)) for j in range(i+1, len(s) + 1)], key=len, reverse=True) if sub == sub[::-1]), None)
