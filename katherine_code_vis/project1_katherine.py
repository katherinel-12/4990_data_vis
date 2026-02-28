import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D # for 3D plotting 

# --- 1. The data ---
# Coordinates of the bars' anchor points (bottom-left corner)
# xpos = [1, 4, 3, 1]
# ypos = [8, 1, 4, 2]
xpos = [1, 3]
ypos = [1, 3]
zpos = np.zeros(2) # Start height at 0

# Dimensions of the bars (width, depth, height)
dx = [1, 3]  # Width of each bar
dy = [1, 3] # Depth of each bar
dz = [4, 7] # Height (value) of each bar

# --- 2. The figure and 3D axes ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # Add subplot with 3D projection

# --- 3. Plot the 3D bars ---
# The bar3d function takes (x, y, z, dx, dy, dz)
# colors = ['#8a3ffc', '#ff7eb6', '#6fdc8c', '#bae6ff']
colors = ['#8a3ffc', '#6fdc8c']
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, shade=True)

# V1 = 1 * 1 * 4 = 4 
# V2 = 3 * 3 * 7 = 63 
# Answer: Ratio difference: 15.75

# --- 4. Customize the plot ---
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
ax.set_title('3D Bar Chart')

# Remove the grid lines 
ax.grid(False)

# Remove ticks and numbers
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Tilt and rotate the 3D view for better visibility
ax.view_init(elev=10, azim=-75)

# --- 5. Display the plot ---
plt.show()

''''''

# # --- 1. The data ---
# # Coordinates of each bubble (x and y positions)
# x = np.array([2, 1, 5, 8, 9])
# y = np.array([8, 6, 2, 5, 4])

# # Underlying data values (used to determine bubble size)
# values = np.array([507, 258, 602, 467, 128])

# # Scale values to bubble areas (Matplotlib expects sizes in points^2)
# sizes = values * 7  # Scaling factor for visibility

# # --- 2. Create the figure ---
# plt.figure()

# # --- 3. Plot the bubbles ---
# # The scatter function takes (x, y) positions and size (s)
# plt.scatter(x, y, s=sizes) 

# Answer: The largest bubble is about 4.7x larger than the smallest bubble.

# # --- 4. Customize the plot ---
# plt.title("Bubble Chart")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")

# # Set axis limits from 0 to 10
# plt.xlim(0, 10)
# plt.ylim(0, 10)

# # Remove ticks and numbers for a cleaner look
# plt.xticks([])
# plt.yticks([])

# # # Optional: Add labels to each bubble
# labelsList = np.array(["A", "B", "C", "D", "E"])
# for i in range(len(x)):
#     plt.text(x[i], y[i], str(labelsList[i]), ha='center', va='center')

# # --- 5. Display the plot ---
# plt.show()

''''''

# --- Define slopes and x-ranges ---
x0 = np.array([2, 8])
y0 = -1.2 * x0 + 5  
# height = 7.2 

x1 = np.array([1, 7])
y1 = 0.8 * x1 - 5
# height = 4.8

x2 = np.array([3, 9])
y2 = 1.5 * x2 - 9.2
# height = 9.0

x3 = np.array([0, 6])
y3 = (-0.5) * x3 - 1.2
# height = 3.0

x4 = np.array([4, 10])
y4 = 0.2 * x4 + 1 
# height = 1.2

# Answer: The tallest line is about 7.5x taller than the shortest line 
# in terms of vertical change (Δy)

# --- Plot all lines ---
plt.figure(figsize=(8,6))
plt.plot(x0, y0, label="Line A")
plt.plot(x1, y1, label="Line B")
plt.plot(x2, y2, label="Line C")
plt.plot(x3, y3, label="Line D")
plt.plot(x4, y4, label="Line E")
# --- Customize ---
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Line Chart")
plt.legend()

# Remove ticks and numbers for a cleaner look
plt.xticks([])
plt.yticks([])

plt.show()