import numpy as np

lst = list(map(int, input('enter tempratures in celcius (seprate them by space): ').split()))
lst = np.array(lst)
mean = np.mean(lst)
print(f'average temp is {mean}C')
print(f'maximum temperature was {max(lst)} and minimum was {min(lst)}')

# using standard deviation from numpy to detect abnormal temperatures
# using formula ∣x−μ|>k×std

std = lst.std()
# use 2 as a thresold for more rare spikes i used 1 for more common spikes
AT = lst[abs(lst - mean) > 1 * std]

print(f'abnormal temperature spikes are {AT}')