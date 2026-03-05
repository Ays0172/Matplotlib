"""
Matplotlib Visualization Masterclass — Interactive Learning Platform
=====================================================================
Main entry point for the Streamlit multi-page application.
"""

import streamlit as st
import sys, os

# ── Make utils importable from any page ──
sys.path.insert(0, os.path.dirname(__file__))

from utils.styles import inject_custom_css, hero
from utils.helpers import create_metric_cards

# ── Page config ──
st.set_page_config(
    page_title="Matplotlib Masterclass",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_custom_css()

# ── Sidebar branding ──
with st.sidebar:
    st.markdown("## 📊 Matplotlib Masterclass")
    st.caption("Data Visualization with Python")
    st.divider()
    st.markdown(
        "**Modules**\n"
        "- 📈 Plot Functions\n"
        "- 📊 Charts\n"
        "- 🖼️ Subplots & Layout\n"
    )
    st.divider()
    st.caption("Use the sidebar pages ↑ to navigate.")

# ── Hero section ──
hero(
    "📊 Matplotlib Visualization Masterclass",
    "Line plots · Bar charts · Histograms · Scatter · Pie · Subplots — learn it all interactively.",
)

# ── Overview metrics ──
create_metric_cards([
    ("3", "Modules"),
    ("7", "Scripts"),
    ("3", "Notebooks"),
    ("10+", "Concepts"),
])

# ── Module cards ──
st.markdown("### 🗺️ Learning Roadmap")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="module-card">
        <h3>📈 Plot Functions</h3>
        <p>Master the fundamentals — line plots, labels, legends, grids, axis limits, and custom tick marks using <code>plt.plot()</code>.</p>
        <span class="badge">2 Scripts · 1 Notebook</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="module-card">
        <h3>🖼️ Subplots & Layout</h3>
        <p>Display multiple charts on one canvas with <code>plt.subplot()</code> and the OOP <code>fig, ax</code> approach. Save high-resolution figures.</p>
        <span class="badge">2 Scripts · 1 Notebook</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="module-card">
        <h3>📊 Charts</h3>
        <p>Build bar charts, histograms, scatter plots (single & multi-group), and pie charts — all with real-world sample data.</p>
        <span class="badge">5 Scripts · 1 Notebook</span>
    </div>
    """, unsafe_allow_html=True)

# ── Pipeline overview ──
st.markdown("### ⚡ What You'll Learn")
st.markdown("""
<div class="info-card">
    <strong>1. Plot Functions</strong> — Create and customise line plots with colors, markers, grids, legends, and axis controls.<br>
    <strong>2. Chart Types</strong> — Bar charts for comparison, histograms for distribution, scatter plots for correlation, pie charts for proportions.<br>
    <strong>3. Subplots & Layout</strong> — Combine multiple plots on a single canvas, use <code>tight_layout()</code>, and export publication-ready images.
</div>
""", unsafe_allow_html=True)

# ── Footer ──
st.divider()
st.markdown(
    "<center style='color:#64748b; font-size:0.85rem;'>"
    "Built with ❤️ using Streamlit · Matplotlib Visualization Masterclass"
    "</center>",
    unsafe_allow_html=True,
)
