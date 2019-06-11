if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2 = []
    maxscore = -100
    runnerup = -100
    
    # get the max
    for i in arr:
        if i > maxscore:
            runnerup = maxscore
            maxscore = i
        elif i > runnerup and i < maxscore:
            runnerup = i

    # print runner up
    print(str(runnerup))


