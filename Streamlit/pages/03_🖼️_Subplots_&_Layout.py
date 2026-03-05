"""
Module 3 — Subplots & Layout Adjustments
==========================================
Multiple charts on one canvas, OOP figure/axes API, and saving publication-ready images.
"""

import streamlit as st
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import io
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.styles import inject_custom_css, hero, step_header
from utils.helpers import show_code, show_explanation

st.set_page_config(page_title="Subplots & Layout", page_icon="🖼️", layout="wide")
inject_custom_css()
hero("🖼️ Subplots & Layout Adjustments", "Multiple charts on one canvas · plt.subplot() · fig, ax · savefig()")


# ═══════════════════════════════════════════════════════
# STEP 1 — plt.subplot() — Quick Side-by-Side
# ═══════════════════════════════════════════════════════
step_header(1, "plt.subplot() — Quick Side-by-Side")

show_explanation(
    "Use <code>plt.subplot(nrows, ncols, index)</code> to place multiple plots on one canvas. "
    "Always call <code>plt.tight_layout()</code> just before <code>plt.show()</code> for automatic spacing."
)

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

fig1, (ax1a, ax1b) = plt.subplots(1, 2, figsize=(12, 5))
ax1a.plot(x, y, color="#f59e0b", marker="o", linewidth=2)
ax1a.set_title("Line Chart", fontweight="bold")
ax1a.grid(True, alpha=0.3)

ax1b.bar(x, y, color="#d97706", edgecolor="white")
ax1b.set_title("Bar Chart", fontweight="bold")

plt.tight_layout()
st.pyplot(fig1)
plt.close(fig1)

show_code("""import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.subplot(1, 2, 1)      # 1 row, 2 columns, 1st position
plt.plot(x, y)
plt.title('Line Chart')

plt.subplot(1, 2, 2)      # 1 row, 2 columns, 2nd position
plt.bar(x, y)
plt.title('Bar Chart')

plt.tight_layout()
plt.show()""")


# ═══════════════════════════════════════════════════════
# STEP 2 — fig, ax = plt.subplots() (OOP Approach)
# ═══════════════════════════════════════════════════════
step_header(2, "Object-Oriented Approach — fig, ax = plt.subplots()")

show_explanation(
    "The OOP approach gives more control: <code>fig, ax = plt.subplots(nrows, ncols, figsize)</code>. "
    "Access individual axes with <code>ax[i]</code>. Use <code>fig.suptitle()</code> to add a "
    "super-title above all subplots."
)

c1, c2 = st.columns(2)
fig_width = c1.slider("Figure width", 6, 16, 10, key="fw")
fig_height = c2.slider("Figure height", 3, 8, 5, key="fh")

color_left = st.color_picker("Left plot color", "#3b82f6", key="cl")
color_right = st.color_picker("Right plot color", "#22c55e", key="cr")

fig2, ax2 = plt.subplots(1, 2, figsize=(fig_width, fig_height))

ax2[0].plot(x, y, color=color_left, marker="o", linewidth=2)
ax2[0].set_title("Line Plot", fontweight="bold")
ax2[0].grid(True, alpha=0.3)

ax2[1].bar(x, y, color=color_right, edgecolor="white")
ax2[1].set_title("Bar Chart", fontweight="bold")

fig2.suptitle("Comparison of Bar and Line Graphs", fontsize=14, fontweight="bold")
plt.tight_layout()
st.pyplot(fig2)
plt.close(fig2)

show_code("""fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].plot(x, y, color='blue')
ax[0].set_title('Line Plot')

ax[1].bar(x, y, color='green')
ax[1].set_title('Bar Chart')

fig.suptitle('Comparison of Bar and Line Graphs')
plt.tight_layout()
plt.show()""")


# ═══════════════════════════════════════════════════════
# STEP 3 — Saving Figures
# ═══════════════════════════════════════════════════════
step_header(3, "Saving Figures — plt.savefig()")

show_explanation(
    "Use <code>plt.savefig('filename.png', dpi=300, bbox_inches='tight')</code> to export "
    "publication-ready images. <code>dpi</code> controls resolution and <code>bbox_inches='tight'</code> "
    "removes excess whitespace."
)

c3, c4, c5 = st.columns(3)
save_dpi = c3.slider("DPI (resolution)", 72, 600, 300, step=50, key="sd")
save_format = c4.selectbox("Format", ["png", "jpg", "svg", "pdf"], key="sf")
line_col = c5.color_picker("Line color", "#06b6d4", key="slc")

fig3, ax3 = plt.subplots(figsize=(8, 5))
ax3.plot([1, 2, 3, 4], [10, 20, 15, 25], color=line_col, marker="^", linewidth=2)
ax3.set_title("Simple Line Plot", fontweight="bold", fontsize=14)
ax3.set_xlabel("X Axis")
ax3.set_ylabel("Y Axis")
ax3.grid(True, alpha=0.3)
plt.tight_layout()
st.pyplot(fig3)

# ── Download button ──
buf = io.BytesIO()
fig3.savefig(buf, format=save_format, dpi=save_dpi, bbox_inches="tight")
buf.seek(0)
plt.close(fig3)

mime_map = {"png": "image/png", "jpg": "image/jpeg", "svg": "image/svg+xml", "pdf": "application/pdf"}
st.download_button(
    label=f"⬇️ Download as .{save_format} ({save_dpi} DPI)",
    data=buf,
    file_name=f"line_plot.{save_format}",
    mime=mime_map[save_format],
)

show_code(f"""plt.savefig('line_plot.{save_format}', dpi={save_dpi}, bbox_inches='tight')
plt.show()""")


# ═══════════════════════════════════════════════════════
# Quick Reference
# ═══════════════════════════════════════════════════════
step_header(4, "Subplots & Layout — Quick Reference")

st.markdown("""
<div class="ref-card">
    <h4>🔧 Essential Subplot Functions</h4>
    <ul>
        <li><code>plt.subplot(nrows, ncols, index)</code> — Place a plot at position <em>index</em></li>
        <li><code>fig, ax = plt.subplots(nrows, ncols, figsize=(w, h))</code> — OOP approach</li>
        <li><code>ax[i].plot(...)</code> / <code>ax[i].bar(...)</code> — Draw on a specific axis</li>
        <li><code>fig.suptitle('Title')</code> — Super-title above all subplots (<em>note: sup, not sub!</em>)</li>
        <li><code>plt.tight_layout()</code> — Automatic spacing adjustment (use before <code>show()</code>)</li>
        <li><code>plt.savefig('file.png', dpi=300, bbox_inches='tight')</code> — Export high-res image</li>
    </ul>
</div>
""", unsafe_allow_html=True)
