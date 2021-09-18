def weightedMean(X, W):
    weighted = sum([a*b for a,b in zip(X,W)])
    print(round((weighted/sum(W)),1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split(' ')))

    weights = list(map(int, input().rstrip().split(' ')))

    weightedMean(vals, weights)