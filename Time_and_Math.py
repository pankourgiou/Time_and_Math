import numpy as np
import matplotlib.pyplot as plt
import datetime

def draw_math_clock():
    fig, ax = plt.subplots(figsize=(6, 6), dpi=100)

    # Set up the clock face
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')
    ax.set_facecolor('white')
    ax.axis('off')  # Hide axes

    # Draw clock border
    clock_circle = plt.Circle((0, 0), 1, edgecolor='black', facecolor='white', lw=3)
    ax.add_patch(clock_circle)

    # Mathematical expressions for each hour
    math_expressions = [
        r'$\frac{30}{5} \div \frac{19}{38}$',  # 12
        r'$\sin{\left(\frac{\pi}{2}\right)}$',  # 1
        r'$\frac{d}{dx}2x$',  # 2
        r'$\det{[5,7;1,2]}$',  # 3
        r'$\prod_{n=1}^{3} \frac{n+1}{n}$',  # 4
        r'$\sqrt{72^2 + 24^2}$',  # 5
        r'$3!$',  # 6
        r'$\frac{1}{4} x^{(8/2)}$',  # 7
        r'$2(2^2)$',  # 8
        r'$\int_0^3 x^2 dx$',  # 9
        r'$\sum_{n=1}^{4}n$',  # 10
        r'$\bigcup_{n=0}^{10} \{n\}$'  # 11
    ]

    # Place numbers at correct clock positions
    for i, expr in enumerate(math_expressions):
        angle = np.pi / 2 - i * (np.pi / 6)  # Convert to radians (12 at top, rest spaced evenly)
        x, y = 0.85 * np.cos(angle), 0.85 * np.sin(angle)  # Scale positions
        ax.text(x, y, expr, ha='center', va='center', fontsize=12, fontweight='bold')

    # Get current time
    now = datetime.datetime.now()
    hour = now.hour % 12 + now.minute / 60  # Adjust hour hand
    minute = now.minute + now.second / 60
    second = now.second

    # Calculate hand angles
    hour_angle = np.pi / 2 - (hour * 30) * (np.pi / 180)
    minute_angle = np.pi / 2 - (minute * 6) * (np.pi / 180)
    second_angle = np.pi / 2 - (second * 6) * (np.pi / 180)

    # Draw clock hands
    ax.plot([0, 0.5 * np.cos(hour_angle)], [0, 0.5 * np.sin(hour_angle)], color='black', lw=4)  # Hour hand
    ax.plot([0, 0.7 * np.cos(minute_angle)], [0, 0.7 * np.sin(minute_angle)], color='black', lw=3)  # Minute hand
    ax.plot([0, 0.9 * np.cos(second_angle)], [0, 0.9 * np.sin(second_angle)], color='red', lw=1)  # Second hand

    # Draw the center circle
    ax.scatter(0, 0, s=50, color='black', zorder=3)

    # Show the clock
    plt.show()

# Run the function to display the clock
draw_math_clock()

