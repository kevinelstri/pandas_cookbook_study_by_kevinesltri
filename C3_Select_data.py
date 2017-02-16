# -*-coding:utf-8-*-

# ---------------------
# Chapter 3 - Which borough has the most noise complaints (or, more selecting data).ipynb
# ---------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

complaints = pd.read_csv('../data/311-service-requests.csv')  # 读取csv文件
print complaints.head()
print complaints[:5]

'''
    3.1 Selecting only noise complaints
'''
noise_complaints = complaints[complaints['Complaint Type'] == 'Noise - Street/Sidewalk']
print noise_complaints[:3]
print complaints['Complaint Type'] == 'Noise - Street/Sidewalk'  # 返回True False

is_noise = complaints['Complaint Type'] == 'Noise - Street/Sidewalk'
in_brooklyn = complaints['Borough'] == 'BROOKLYN'
print complaints[is_noise & in_brooklyn][:5]

print complaints[is_noise & in_brooklyn][['Complaint Type', 'Borough', 'Created Date', 'Descriptor']][:10]
'''
    3.2 A digression about numpy arrays
'''
pf = pd.Series([1, 2, 3])
print pf
print pf.values
print pf.index
nf = np.array([1, 2, 3])
print nf
print nf != 2
print nf[nf != 2]

'''
    3.3 So, which borough has the most noise complaints?
'''
is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
noise_complaints = complaints[is_noise]
print noise_complaints['Borough'].value_counts()

noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()

print noise_complaint_counts / complaint_counts

print noise_complaint_counts / complaint_counts.astype(float)

(noise_complaint_counts / complaint_counts.astype(float)).plot(kind='bar')
plt.show()