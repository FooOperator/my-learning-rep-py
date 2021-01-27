def check_exam(correct, inputted):
    score = 0
    for i in range(len(correct)):
        if correct[i] == inputted[i]:
            score += 4
        elif inputted[i] == '':
            continue
        else:
            score -= 1
    print(score)
    if score < 0:
        return 0
    return score