
import matplotlib.pyplot as plt
age_list=[1,1,2,3,3,5,7,8,9,10,10,11,11,13,13,15,16,17,18,18,18,19,20,21,21,23,24,24,25,25,25,25,26,26,26,27,27,27,27,27,29,30,30,31,33,34,34,34,35,36,36,37,37,38,38,39,40,41,41,42,43,44,45,45,46,47,48,48,49,50,51,52,53,54,55,55,56,57,58,60,61,63,64,65,66,68,70,71,72,74,75,77,81,83,84,87,89,90,90,91]
fig=plt.figure(figsize=(5,4))
plt.title("histogram")
plt.xlabel("age")
plt.ylabel("frequency")
plt.hist(age_list,bins=10,edgecolor="red")
plt.show()