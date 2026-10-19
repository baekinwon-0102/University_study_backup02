import numpy as np
import cv2

m = np.random.rand(3,5) * 1000//10

reduce_sum = cv2.reduce(m, dim=0, rtype = cv2.REDUCE_SUM)
reduce_avg = cv2.reduce(m, dim=1, rtype = cv2.REDUCE_AVG)
reduce_max = cv2.reduce(m, dim=0, rtype = cv2.REDUCE_MAX)
reduce_min = cv2.reduce(m, dim=1, rtype = cv2.REDUCE_MIN)

print("[m1] = \n%s\n" %m)
print("[reduce_sum] = ", reduce_sum.flatten())
print("[reduce_avg] = ", reduce_avg.flatten())
print("[reduce_max] = ", reduce_max.flatten())
print("[reduce_min] = ", reduce_min.flatten())