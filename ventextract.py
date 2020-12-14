# -*- coding: utf-8 -*-
"""
VentExtract.ipynb
Purab Patel

"""
import numpy as np
from matplotlib import pyplot as plt
import os
import sys

RAW_DATA = sys.argv[1]
RAW_DATA_NAME = sys.argv[2]
OUT_PATH = sys.argv[3]

x_extract = np.genfromtxt(RAW_DATA, dtype=str, deletechars="b'")


x = np.transpose(x_extract)
x = x[:,1:]

x = x.astype(float)
id = 0 
id_extract = []
plotnum = 0
fig = plt.figure(figsize=(100, 100))
while True:
  xx = x[17,id:(id+5)]
  if (len(xx)==0):
    break
  if (xx[0] == 16 and xx[-1] == 16):
    plotnum = plotnum+1
    plt.subplot(16,1,plotnum)
    plt.plot(x[3,(id-1000):(id+1001)])
    id_extract.append(id)
    id = id+1002
  else:
    id = id+1

run = np.genfromtxt(RAW_DATA, dtype=str, deletechars="b'")
run = np.transpose(run)

for i, start in enumerate(id_extract):
  run_sample = np.hstack((np.transpose([run[:,0]]), run[:,(start-1000):(start+1001)]))
  run_sample = np.vstack((run_sample[0:6,:], run_sample[14,:]))

  np.savetxt((OUT_PATH + "/" + RAW_DATA_NAME+"-ZAM"+str(i+1)+'.ASC'), np.transpose(run_sample), fmt='%s', delimiter = '\t')