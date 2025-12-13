import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Calibri'
plt.rcParams['font.size'] = 10

df = pd.read_csv("iris_data.csv")
df_sorted = df.sort_values("SepalLengthCm")

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax6 = fig.add_subplot(326)

ax1.scatter(df["SepalLengthCm"], df["PetalLengthCm"])
ax1.set_xlabel("SepalLengthCm")
ax1.set_ylabel("PetalLengthCm")
ax1.set_title("SepalLengthCm/PetalLengthCm")

x_measured = df_sorted["SepalLengthCm"].values
y_measured = df_sorted["PetalLengthCm"].values
x = [x_measured.min(), x_measured.max()]
y = np.interp(x, x_measured, y_measured)
ax1.plot(x,y, color= 'black')


ax3.scatter(df["SepalLengthCm"], df["SepalWidthCm"])
ax3.set_xlabel("SepalLengthCm")
ax3.set_ylabel("SepalWidthCm")
ax3.set_title("SepalWidthCm/SepalLengthCm")


ax5.scatter(df["SepalLengthCm"], df["PetalWidthCm"])
ax5.set_xlabel("SepalLengthCm")
ax5.set_ylabel("PetalWidthCm")
ax5.set_title("SepalLengthCm/PetalWidthCm")


ax2.scatter(df["SepalWidthCm"], df["PetalLengthCm"])
ax2.set_xlabel("SepalWidthCm")
ax2.set_ylabel("PetalLengthCm")
ax2.set_title("SepalWidthCm/PetalLengthCm")


ax4.scatter(df["SepalWidthCm"], df["PetalWidthCm"])
ax4.set_xlabel("SepalWidthCm")
ax4.set_ylabel("PetalWidthCm")
ax4.set_title("SepalWidthCm/PetalWidthCm")


ax6.scatter(df["PetalLengthCm"], df["PetalWidthCm"])
ax6.set_xlabel("PetalLengthCm")
ax6.set_ylabel("PetalWidthCm")
ax6.set_title("PetalLengthCm/PetalWidthCm/")

x_measured = df_sorted["PetalLengthCm"].values
y_measured = df_sorted["PetalWidthCm"].values
x = [x_measured.min(), x_measured.max()]
y = np.interp(x, x_measured, y_measured)
ax6.plot(x,y, color= 'black')

plt.tight_layout(pad=2)
plt.show()
