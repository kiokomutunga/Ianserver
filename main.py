import numpy

from scipy import stats

marks = (23,45,98,67,89,90,74,56,90)
speed = [99, 56, 78, 34, 90, 45, 45, 67, 245]


modee = stats.mode(speed)

lemmeintroducex = numpy.mean(marks)

print(lemmeintroducex)
print(modee)

