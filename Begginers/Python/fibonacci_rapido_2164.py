import math

num = int(input())

fibonacci = (pow(((1 + math.sqrt(5)) / 2), num) - pow(((1 - math.sqrt(5)) / 2), num)) / math.sqrt(5)

print(f"{fibonacci:.1f}")
