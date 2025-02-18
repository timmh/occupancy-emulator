
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import pandas as pd

df = pd.read_csv("simulation_results.csv")
df["n_sites_log10"] = np.log10(df["n_sites"])

st.title("Occupancy Emulator")

columns = list(df.columns)
x_axis = st.selectbox("X axis:", columns, index=columns.index("n_sites_log10"))
y_axis = st.selectbox("Y axis:", columns, index=columns.index("deployment_days_per_site"))
z_axis = st.selectbox("Z axis:", columns, index=columns.index("z_acc"))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

x_data = df[x_axis]
y_data = df[y_axis]
z_data = df[z_axis]

surf = ax.plot_trisurf(x_data, y_data, z_data, cmap=cm.jet, linewidth=0.1)

ax.set_xlabel(x_axis + (" (log)" if x_axis == "n_sites" else ""))
ax.set_ylabel(y_axis)
ax.set_zlabel(z_axis)
fig.colorbar(surf, shrink=0.5, aspect=5)

st.pyplot(fig)
