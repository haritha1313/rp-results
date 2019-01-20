import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d

data = pd.read_csv('hexapod-results/awareall.csv')
data_un = pd.read_csv('hexapod-results/unawareall.csv')
sf=7
sf_low=1

       # Extract the data we're interested in
q = data['Value-eval'].quantile(0.99)
rew = data[data['Value-eval'] < q]
ite = rew['Step-eval']
rew_smooth = gaussian_filter1d(rew['Value-eval'], sigma=sf)
rew_smooth_low = gaussian_filter1d(rew['Value-eval'], sigma=sf_low)

q1 = data['Value-eval1'].quantile(0.99)
rew1 = data[data['Value-eval1'] < q1]
ite1 = rew1['Step-eval1']
rew_smooth1 = gaussian_filter1d(rew1['Value-eval1'], sigma=sf)
rew_smooth1_low = gaussian_filter1d(rew1['Value-eval1'], sigma=sf_low)

q2 = data['Value-eval2'].quantile(0.99)
rew2 = data[data['Value-eval2'] < q2]
ite2 = rew2['Step-eval2']
rew_smooth2 = gaussian_filter1d(rew2['Value-eval2'], sigma=sf)
rew_smooth2_low = gaussian_filter1d(rew2['Value-eval2'], sigma=sf_low)

q3 = data['Value-eval3'].quantile(0.99)
rew3 = data[data['Value-eval3'] < q3]
ite3 = rew3['Step-eval3']
rew_smooth3 = gaussian_filter1d(rew3['Value-eval3'], sigma=sf)
rew_smooth3_low = gaussian_filter1d(rew3['Value-eval3'], sigma=sf_low)

# aware done

q_un = data_un['Value-eval'].quantile(0.99)
rew_un = data_un[data_un['Value-eval'] < q_un]
ite_un = rew_un['Step-eval']
rew_smooth_un = gaussian_filter1d(rew_un['Value-eval'], sigma=sf)
rew_smooth_un_low = gaussian_filter1d(rew_un['Value-eval'], sigma=sf_low)

q1_un = data_un['Value-eval1'].quantile(0.99)
rew1_un = data_un[data_un['Value-eval1'] < q1_un]
ite1_un = rew1_un['Step-eval1']
rew_smooth1_un = gaussian_filter1d(rew1_un['Value-eval1'], sigma=sf)
rew_smooth1_un_low = gaussian_filter1d(rew1_un['Value-eval1'], sigma=sf_low)

q2_un = data_un['Value-eval2'].quantile(0.99)
rew2_un = data_un[data_un['Value-eval2'] < q2_un]
ite2_un = rew2_un['Step-eval2']
rew_smooth2_un = gaussian_filter1d(rew2_un['Value-eval2'], sigma=sf)
rew_smooth2_un_low = gaussian_filter1d(rew2_un['Value-eval2'], sigma=sf_low)

q3_un = data_un['Value-eval3'].quantile(0.99)
rew3_un = data_un[data_un['Value-eval3'] < q3_un]
ite3_un = rew3_un['Step-eval3']
rew_smooth3_un = gaussian_filter1d(rew3_un['Value-eval3'], sigma=sf)
rew_smooth3_un_low = gaussian_filter1d(rew3_un['Value-eval3'], sigma=sf_low)


"""
plt.fill_between(ite3_un, perc_25_low_mut, perc_75_low_mut, alpha=0.25, linewidth=0, color='#B22400')
plt.fill_between(ite3, perc_25_high_mut, perc_75_high_mut, alpha=0.25, linewidth=0, color='#006BB2')

ite1, rew1 = data['Step-eval1'], data['Value-eval1']
rew1_smooth = gaussian_filter1d(rew1, sigma=sf)
ite2, rew2 = data['Step-eval2'], data['Value-eval2']
rew2_smooth = gaussian_filter1d(rew2, sigma=sf)
ite3, rew3 = data['Step-eval3'], data['Value-eval3']
rew3_smooth = gaussian_filter1d(rew3, sigma=sf)

  """     # Scatter the points, using size and color but no label
plt.plot(ite, rew_smooth, color='#FF5733', label='DA-healthy')
plt.plot(ite1, rew_smooth1, color='#C70039')
plt.plot(ite2, rew_smooth2, color='#900C3F' )
plt.plot(ite3, rew_smooth3,  color='#581845', label='DA-damaged')
plt.plot(ite_un, rew_smooth_un, color='#33caff', label='Vanilla-healthy')
plt.plot(ite1_un, rew_smooth1_un,color='#33a8ff')
plt.plot(ite2_un, rew_smooth2_un, color='#3361ff')
plt.plot(ite3_un, rew_smooth3_un, color='#4933ff', label='Vanilla-damaged')
"""
plt2.plot(ite, rew_smooth, color='#581845', label='DA-healthy')
plt2.plot(ite1, rew_smooth1, color='#581845')
plt2.plot(ite2, rew_smooth2, color='#581845' )
plt2.plot(ite3, rew_smooth3,  color='#581845', label='DA-damaged')
plt2.plot(ite_un, rew_smooth_un, color='#4933ff', label='Vanilla-healthy')
plt2.plot(ite1_un, rew_smooth1_un,color='#4933ff')
plt2.plot(ite2_un, rew_smooth2_un, color='#4933ff')
plt2.plot(ite3_un, rew_smooth3_un, color='#4933ff', label='Vanilla-damaged')

"""
plt.plot(ite, rew_smooth_low, color='#FF5733', label='DA-healthy', alpha=0.2)
plt.plot(ite1, rew_smooth1_low, color='#C70039', alpha=0.2)
plt.plot(ite2, rew_smooth2_low, color='#900C3F', alpha=0.2 )
plt.plot(ite3, rew_smooth3_low,  color='#581845', label='DA-damaged', alpha=0.2)
plt.plot(ite_un, rew_smooth_un_low, color='#33caff', label='Vanilla-healthy', alpha=0.2)
plt.plot(ite1_un, rew_smooth1_un_low,color='#33a8ff', alpha=0.2)
plt.plot(ite2_un, rew_smooth2_un_low, color='#3361ff', alpha=0.2)
plt.plot(ite3_un, rew_smooth3_un_low, color='#4933ff', label='Vanilla-damaged', alpha=0.2)

#plt.legend()
plt.show()
