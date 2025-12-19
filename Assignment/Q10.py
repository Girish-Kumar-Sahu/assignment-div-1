lst = list(map(int, input('enter tempratures in celcius (seprate them by space): ').split()))
print(f'average temp is {sum(lst)/len(lst)}C')
print(f'maximum temperatur was {max(lst)} and minimum was {min(lst)}')
# using standard deviation from numpy to detect abnormal temperatures
import numpy as np
lst = np.array(lst)
print(f'abnormal temperature spikes are {np.std(lst)}')