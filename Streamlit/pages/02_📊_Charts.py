"""
Module 2 — Charts
==================
Bar charts, histograms, scatter plots (single & multi-group), and pie charts.
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

st.set_page_config(page_title="Charts", page_icon="📊", layout="wide")
inject_custom_css()
hero("📊 Chart Types", "Bar · Histogram · Scatter · Pie — the essential chart gallery")


# ═══════════════════════════════════════════════════════
# STEP 1 — Bar Chart
# ═══════════════════════════════════════════════════════
step_header(1, "Bar Chart — Category Comparison")

show_explanation(
    "Use <code>plt.bar(x, height)</code> for vertical bars or "
    "<code>plt.barh()</code> for horizontal bars. Great for comparing categories."
)

product = ['A', 'B', 'C', 'D']
sales = [1000, 1500, 800, 1200]

c1, c2, c3 = st.columns(3)
bar_color = c1.color_picker("Bar color", "#f97316", key="bc")
bar_width = c2.slider("Bar width", 0.2, 0.9, 0.6, step=0.1, key="bw")
horizontal = c3.checkbox("Horizontal bars", value=False, key="bh")

fig1, ax1 = plt.subplots(figsize=(8, 5))
if horizontal:
    ax1.barh(product, sales, color=bar_color, height=bar_width, edgecolor="white")
    ax1.set_xlabel("Sales")
    ax1.set_ylabel("Product")
else:
    ax1.bar(product, sales, color=bar_color, width=bar_width, edgecolor="white", label="Sales 2025")
    ax1.set_xlabel("Product")
    ax1.set_ylabel("Sales")
    ax1.legend()
ax1.set_title("Product Sales Comparison", fontweight="bold", fontsize=14)
plt.tight_layout()
st.pyplot(fig1)
plt.close(fig1)

show_code("""product = ['A', 'B', 'C', 'D']
sales = [1000, 1500, 800, 1200]

plt.bar(product, sales, color='orange', label='Sales 2025')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title("Product Sales Comparison")
plt.legend()
plt.show()""")


# ═══════════════════════════════════════════════════════
# STEP 2 — Histogram
# ═══════════════════════════════════════════════════════
step_header(2, "Histogram — Distribution of Continuous Data")

show_explanation(
    "Histograms show the <strong>distribution</strong> of continuous data by dividing it into "
    "ranges (bins). Use <code>plt.hist(data, bins)</code>. The height of each bar = "
    "number of data points in that range."
)

scores = [45, 67, 77, 58, 67, 92, 82, 74, 81, 66, 39, 57, 48, 75, 59,
          79, 88, 63, 63, 65, 78, 10, 96, 57, 36, 57, 85, 75, 34, 67,
          97, 18, 7, 76, 35, 56, 87, 75, 45, 56, 38, 56, 97, 87, 35,
          65, 88, 72, 42, 85, 92]

c4, c5 = st.columns(2)
num_bins = c4.slider("Number of bins", 3, 20, 5, key="hb")
hist_color = c5.color_picker("Histogram color", "#9333ea", key="hc")

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.hist(scores, bins=num_bins, color=hist_color, edgecolor="black", alpha=0.85)
ax2.set_xlabel("Score Range", fontsize=12)
ax2.set_ylabel("Number of Students", fontsize=12)
ax2.set_title("Score Distribution of Students", fontweight="bold", fontsize=14)
plt.tight_layout()
st.pyplot(fig2)
plt.close(fig2)

show_code("""scores = [45, 67, 77, 58, 67, 92, 82, 74, ...]

plt.hist(scores, bins=5, color='purple', edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.title("Score Distribution of Students")
plt.show()""")


# ═══════════════════════════════════════════════════════
# STEP 3 — Scatter Plots
# ═══════════════════════════════════════════════════════
step_header(3, "Scatter Plots — Correlation & Comparison")

show_explanation(
    "Use <code>plt.scatter(x, y)</code> to visualise the relationship between two variables. "
    "Add <code>marker</code>, <code>color</code>, and <code>label</code> for clarity."
)

tab1, tab2 = st.tabs(["📍 Single Scatter", "📍📍 Multi-Group Scatter"])

with tab1:
    hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
    exam_scores = [50, 55, 60, 65, 70, 75, 80, 85]

    scatter_color = st.color_picker("Dot color", "#ef4444", key="sc")
    scatter_marker = st.selectbox("Marker style", ["^", "o", "s", "D", "*"], key="sm")

    fig3, ax3 = plt.subplots(figsize=(8, 5))
    ax3.scatter(hours_studied, exam_scores, color=scatter_color,
                marker=scatter_marker, s=100, label="Student data", edgecolors="white")
    ax3.set_xlabel("Hours Studied", fontsize=12)
    ax3.set_ylabel("Exam Scores", fontsize=12)
    ax3.set_title("Correlation: Hours Studied vs Marks Scored", fontweight="bold", fontsize=14)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig3)
    plt.close(fig3)

    show_code("""hours = [1,2,3,4,5,6,7,8]
scores = [50,55,60,65,70,75,80,85]

plt.scatter(hours, scores, color='red', marker='^', label='Student data')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Correlation btw hours studied and marks scored')
plt.legend()
plt.grid(True)
plt.show()""")

with tab2:
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    ax4.scatter([1, 2, 3], [50, 60, 70], color="blue", marker="o", s=100, label="Class A", edgecolors="white")
    ax4.scatter([1, 2, 3], [60, 98, 80], color="green", marker="^", s=100, label="Class B", edgecolors="white")
    ax4.set_xlabel("Hours Studied", fontsize=12)
    ax4.set_ylabel("Exam Scores", fontsize=12)
    ax4.set_title("Comparison of Two Classes", fontweight="bold", fontsize=14)
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig4)
    plt.close(fig4)

    show_code("""plt.scatter([1,2,3], [50,60,70], color='blue', marker='o', label='Class A')
plt.scatter([1,2,3], [60,98,80], color='green', marker='^', label='Class B')

plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Comparison of two classes')
plt.legend()
plt.grid(True)
plt.show()""")


# ═══════════════════════════════════════════════════════
# STEP 4 — Pie Chart
# ═══════════════════════════════════════════════════════
step_header(4, "Pie Chart — Proportions")

show_explanation(
    "Use <code>plt.pie(values, labels, autopct)</code> to show proportions. "
    "Best for a small number of categories — avoid clutter!"
)

regions = ['North', 'South', 'East', 'West']
revenue = [3000, 2000, 1700, 2300]

c6, c7 = st.columns(2)
explode_idx = c6.selectbox("Explode slice", ["None"] + regions, key="pe")
show_pct = c7.checkbox("Show percentages", value=True, key="pp")

explode = [0.08 if r == explode_idx else 0 for r in regions]
colors = ['#fbbf24', '#38bdf8', '#4ade80', '#fb7185']

fig5, ax5 = plt.subplots(figsize=(7, 7))
ax5.pie(
    revenue,
    labels=regions,
    autopct='%1.1f%%' if show_pct else None,
    colors=colors,
    explode=explode,
    shadow=True,
    startangle=90,
    textprops={"fontsize": 12},
)
ax5.set_title("Revenue Contribution by Region", fontweight="bold", fontsize=14)
plt.tight_layout()
st.pyplot(fig5)
plt.close(fig5)

show_code("""regions = ['North', 'South', 'East', 'West']
revenue = [3000, 2000, 1700, 2300]

plt.pie(revenue, labels=regions, autopct='%1.1f%%',
        colors=['gold','skyblue','lightgreen','coral'])
plt.title('Revenue Contribution by Region')
plt.show()""")
