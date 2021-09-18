import statistics
from scipy import stats

size = int(input())
numbers = list(map(int, input()))
print(statistics.mean(numbers))
print(statistics.median(numbers))
print(int(stats.mode(numbers)[0]))