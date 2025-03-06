def solve(words, banned):
    anss = []
    for w in words:
        ans = "SAFE"
        for b in banned:
            if b in w:
                ans = "BANNED"
        anss.append(ans)
    return anss

N, M = map(int, input().strip().split())

words = []
banned = []

for _ in range(M):
    banned.append(input().strip())

for _ in range(N):
    words.append(input().strip())

ans = solve(words, banned)

for a in ans:
    print(a)
