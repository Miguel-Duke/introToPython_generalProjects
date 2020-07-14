
user_score = 0
simon_pattern = input()
user_pattern = input()
#above is the non-alterable code given by zybooks

for i in range(len(simon_pattern)):
    if user_pattern[i] == simon_pattern[i]:
        user_score += 1
    else:
        break

#below is the non-alterable code given by zybooks
print('User score:', user_score)
