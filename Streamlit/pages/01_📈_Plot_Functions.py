"""
Module 1 — Plot Functions
==========================
Master line plots, labels, legends, grids, axis limits, and custom ticks.
"""

import streamlit as st
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.styles import inject_custom_css, hero, step_header
from utils.helpers import show_code, show_explanation

st.set_page_config(page_title="Plot Functions", page_icon="📈", layout="wide")
inject_custom_css()
hero("📈 Plot Functions", "Line plots, labels, legends, grids & axis controls — the Matplotlib fundamentals")

# ═══════════════════════════════════════════════════════
# STEP 1 — Basic Line & Bar Plot
# ═══════════════════════════════════════════════════════
step_header(1, "Basic Line & Bar Plot")

show_explanation(
    "The simplest Matplotlib workflow: pass <code>x</code> and <code>y</code> lists to "
    "<code>plt.plot()</code> for a line or <code>plt.bar()</code> for bars, then call <code>plt.show()</code>."
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("##### 📉 Line Plot")
    x = [1, 2, 3, 4]
    y = [10, 20, 15, 25]
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    ax1.plot(x, y, color="#f59e0b", marker="o", linewidth=2)
    ax1.set_title("Basic Line Plot", fontweight="bold")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)

with col2:
    st.markdown("##### 📊 Bar Plot")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.bar(x, y, color="#d97706", edgecolor="white", linewidth=0.5)
    ax2.set_title("Basic Bar Plot", fontweight="bold")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)

show_code("""import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y)    # Line graph
plt.bar(x, y)     # Bar graph
plt.show()""")


# ═══════════════════════════════════════════════════════
# STEP 2 — Labels, Legends & Grid Customization
# ═══════════════════════════════════════════════════════
step_header(2, "Labels, Legends & Grid Customization")

show_explanation(
    "Add context to your plots with <code>plt.xlabel()</code>, <code>plt.ylabel()</code>, "
    "<code>plt.title()</code>. Use <code>plt.legend()</code> for series labels, "
    "<code>plt.grid()</code> for reference lines, and <code>plt.xlim() / plt.ylim()</code> "
    "to control the visible range."
)

a = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri']
b = [10, 15, 7, 21, 13]

st.markdown("##### 🎨 Customize Your Plot")

c1, c2, c3 = st.columns(3)
line_color = c1.color_picker("Line color", "#22c55e", key="lc")
line_style = c2.selectbox("Line style", ["solid", "dashed", "dashdot", "dotted"], key="ls")
marker = c3.selectbox("Marker", ["o", "s", "^", "D", "*", "None"], key="mk")

c4, c5 = st.columns(2)
show_grid = c4.checkbox("Show grid", value=True, key="sg")
show_legend = c5.checkbox("Show legend", value=True, key="sl")

fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.plot(a, b, color=line_color, linestyle=line_style, linewidth=2,
         marker=marker if marker != "None" else None, label="Week 1 Sales")
ax3.set_title("Sample Data for Week 1 Sales", fontweight="bold", fontsize=14)
ax3.set_xlabel("Day of the Week")
ax3.set_ylabel("Sales per Day")
if show_grid:
    ax3.grid(True, alpha=0.3, linestyle=":")
if show_legend:
    ax3.legend(loc="upper left", fontsize=10)
plt.tight_layout()
st.pyplot(fig3)
plt.close(fig3)

show_code("""a = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri']
b = [10, 15, 7, 21, 13]

plt.plot(a, b)
plt.title("Sample data for Week 1 Sales")
plt.xlabel('Day of the Week')
plt.ylabel('Sales per Day')
plt.show()""")


# ═══════════════════════════════════════════════════════
# STEP 3 — Advanced Line Plot (Full Customization)
# ═══════════════════════════════════════════════════════
step_header(3, "Advanced Line Plot — Full Customization")

show_explanation(
    "Control every aspect: <code>color</code>, <code>linestyle</code>, <code>linewidth</code>, "
    "<code>marker</code>, <code>label</code>, <code>plt.legend(loc, fontsize)</code>, "
    "<code>plt.grid(color, linestyle, linewidth)</code>, <code>plt.xlim()</code>, "
    "<code>plt.ylim()</code>, <code>plt.xticks()</code>."
)

month = [1, 2, 3, 4, 5]
sales = [1500, 3000, 2300, 5000, 4400]

c6, c7 = st.columns(2)
xlim_max = c6.slider("X-axis limit (max)", 3, 5, 5, key="xlm")
ylim_max = c7.slider("Y-axis limit (max)", 3000, 6000, 5500, step=500, key="ylm")

fig4, ax4 = plt.subplots(figsize=(10, 5))
ax4.plot(month, sales, color="green", linestyle="--", linewidth=2,
         marker="o", label="2025 Sales data")
ax4.set_xlabel("Months", fontsize=12)
ax4.set_ylabel("Sales per month", fontsize=12)
ax4.set_title("Monthly Sales Data Report", fontweight="bold", fontsize=14)
ax4.legend(loc="upper left", fontsize=10)
ax4.grid(color="blue", linestyle=":", linewidth=1, alpha=0.3)
ax4.set_xlim(1, xlim_max)
ax4.set_ylim(0, ylim_max)
ax4.set_xticks([1, 2, 3, 4, 5])
ax4.set_xticklabels(['M1', 'M2', 'M3', 'M4', 'M5'])
plt.tight_layout()
st.pyplot(fig4)
plt.close(fig4)

show_code("""month = [1, 2, 3, 4, 5]
sales = [1500, 3000, 2300, 5000, 4400]

plt.plot(month, sales, color="green", linestyle="--",
         linewidth=2, marker='o', label='2025 Sales data')
plt.xlabel('Months')
plt.ylabel('Sales per month')
plt.title('Monthly Sales Data Report')
plt.legend(loc='upper left', fontsize=10)
plt.grid(color='blue', linestyle=':', linewidth=1)
plt.xlim(1, 4)
plt.ylim(0, 5500)
plt.xticks([1,2,3,4,5], ['M1','M2','M3','M4','M5'])
plt.show()""")


# ═══════════════════════════════════════════════════════
# STEP 4 — Quick Reference
# ═══════════════════════════════════════════════════════
step_header(4, "Plot Functions — Quick Reference")

st.markdown("""
<div class="ref-card">
    <h4>🔧 Essential Plot Functions</h4>
    <ul>
        <li><code>plt.plot(x, y, color, linestyle, linewidth, marker, label)</code> — Line plot</li>
        <li><code>plt.xlabel('text')</code> / <code>plt.ylabel('text')</code> — Axis labels</li>
        <li><code>plt.title('Title')</code> — Chart title</li>
        <li><code>plt.legend(loc, fontsize)</code> — Legend placement</li>
        <li><code>plt.grid(color, linestyle, linewidth)</code> — Grid lines</li>
        <li><code>plt.xlim(min, max)</code> / <code>plt.ylim(min, max)</code> — Axis range</li>
        <li><code>plt.xticks(positions, labels)</code> — Custom tick marks</li>
        <li><code>plt.show()</code> — Render the infographic</li>
    </ul>
</div>
""", unsafe_allow_html=True)
