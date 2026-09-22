import tkinter as tk
import psutil
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from collections import deque

# Set up the data strcture for the graph
max_data_points = 60 # Show the last 60 seconds
time_data = deque(maxlen=max_data_points)
cpu_data = deque(maxlen=max_data_points)

# Initiliaze the data deques with zeros
for i in range(max_data_points):
    time_data.append(i)
    cpu_data.append(0)

def update():
    #Update the text label
    current_cpu = psutil.cpu_percent()
    cpu_label.config(text=f"CPU Usage: {current_cpu:.1f}%")
    mem_label.config(text=f"Memory Usage: {psutil.virtual_memory().percent:.1f}%")
    
    # Update the data for the graph
    cpu_data.append(current_cpu)

    # Schedule the next update
    root.after(1000, update)

def update_graph(frame):
    # This function is called by the matplotlib animation
    # Update the graph data
    line.set_data(time_data, cpu_data)

    # Adjust the x-axis to scroll with the data
    if len(time_data) >= max_data_points:
        ax.set_xlim(time_data[0], time_data[-1])

    # Ensure the y-axis always shows 0-100%
    ax.set_ylim(0, 100)

    return line, 

# Create the main window
root = tk.Tk()
root.title("Advanced System Monitor")
root.geometry("800x600") # Make window larger to fit the graph

# Create text labels
cpu_label = tk.Label(root, font=('Helvetica', 14))
mem_label = tk.Label(root, font=('Helvetica', 14))
cpu_label.pack(padx=20, pady=10)
mem_label.pack(padx=20, pady=10)

# Create matplotlib figure and axis
fig, ax = plt.subplots(figsize=(8,4))
ax.set_title('CPU Usage Over Time: by Professor Christian')
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('CPU Usage (%)')
ax.grid(True, alpha=0.3)

# Create the initial empty line
line, = ax.plot(time_data, cpu_data, 'r-', linewidth=2)
ax.set_ylim(0, 100)

# Embded the matplotlib figure in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Create the animation
ani = FuncAnimation(fig, update_graph, interval=1000, blit=True, cache_frame_data=False)

# Start the update cycle for the labels
update()

#print("Professor Christian")
# start the GUI event loop
root.mainloop()
