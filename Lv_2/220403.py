# 영어 끝말잇기
def solution(n, words):
    used_words = []
    number, order = 0, 0

    used_words.append(words[0])
    last_word = words[0][-1]
    for i in range(1, len(words)):
        if words[i] not in used_words and words[i][0] == last_word:
            used_words.append(words[i])
            last_word = words[i][-1]
        else:
            number = (i % n) + 1
            order = (i // n) + 1
            break

    return [number, order]

# Test Case
ret = solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
print(ret)
ret = solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
print(ret)
ret = solution(2,["hello", "one", "even", "never", "now", "world", "draw"])
print(ret)