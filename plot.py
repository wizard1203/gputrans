import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import argparse

# TODO ========== add parser
parser = argparse.ArgumentParser()
parser.add_argument('--customize', action='store_true',default=False,
                    help='choose model from pytorch or self-defined')

# todo ========= temp code

# pd.iloc()
# pd.loc()
# pd['xx']
# pd[pd.xx > xxx]

# plt.subplot(235)
# plt.plot([0,1],[0,4])
# plt.figure(num=0, figsize=(8,5),)
# plot1 = plt.plot(x, y, color='red', linewidth=1.0, )
# plot2 = plt.scatter(x, y, s=75, c=T, alpha=.5)
#
# plt.xlim(minrange, maxrange)
# plt.ylim(minrange, maxrange)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
#
# plt.legend([plot1], ('xxx'), loc='best')
#
# plt.show()

# x1 = [ , , , ]
# y1 = [ , , , ]
# plot1 = pl.plot(x1, y1, 'o')
# pl.title('xxxx')

#
# pl.xlim(minrange, maxrange)
# pl.ylim(minrange, maxrange)
#
# todo ======== run

# todo ======== read csv



# todo ======== plot figure
file1 = 'C:\\Users\\zhtang\\Desktop\\NV-DVFS-Benchmark\\csvs\\v1\\gtx980-high-dvfs-real-small-workload-Performance.csv'
file2 = 'C:\\Users\\zhtang\\Desktop\\NV-DVFS-Benchmark\\csvs\\v1\\gtx1080ti-dvfs-real-Performance.csv'

df1 = pd.read_csv(file1, header=0)
df2 = pd.read_csv(file2, header=0)

gtx980achi = df1[(df1.coreF == 1100) & (df1.memF == 2100)]['achieved_occupancy']
gtx1080achi = df2[(df2.coreF == 1700) & (df2.memF == 4000)]['achieved_occupancy']

plt.figure(num=0, figsize=(8,5),)
plot1 = plt.scatter(gtx980achi, gtx1080achi, s=75, alpha=.5)
# plot2 = plt.scatter(x, y, s=75, c=T, alpha=.5)

#plt.xlim(minrange, maxrange)
#plt.ylim(minrange, maxrange)
plt.xlabel('gtx980achi axis')
plt.ylabel('gtx1080achi axis')

plt.legend([plot1], loc='best')

plt.show()




