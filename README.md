# 📊 Data Visualization with Matplotlib — Essential Plots for Data Analysts

A beginner-friendly, hands-on guide for data analysts and Python enthusiasts to learn and demonstrate essential plotting skills using [Matplotlib](https://matplotlib.org/). Includes Python scripts, Jupyter notebooks, and an **interactive Streamlit app** to explore every chart type live.

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/matplotlib-visualization-masterclass.git
cd matplotlib-visualization-masterclass

# 2. Install dependencies
pip install -r Streamlit/requirements.txt

# 3. Launch the interactive app
cd Streamlit
streamlit run app.py
```

---

## 📁 Project Structure

```
Matplotlib/
├── README.md
├── matplotlib/
│   ├── intro.txt                          # Introduction to Matplotlib
│   ├── 1.py                              # First line & bar plot
│   ├── line_plot.png                      # Sample output image
│   ├── code_test.ipynb                    # Notebook playground
│   ├── plotfunctions/
│   │   ├── plotfunctions.txt              # Plot function reference
│   │   ├── line_plot.py                   # Customised line plot
│   │   └── test.ipynb
│   ├── Charts/
│   │   ├── intro.txt                      # Chart types overview
│   │   ├── bar_chart.py                   # Bar chart demo
│   │   ├── hitograms.py                   # Histogram demo
│   │   ├── scatteplots.py                 # Single scatter plot
│   │   ├── mult_scatterplot.py            # Multi-group scatter plot
│   │   ├── pie_chart.py                   # Pie chart demo
│   │   └── test.ipynb
│   └── Subplots & Layout Adjustments/
│       ├── intro.txt                      # Subplot concepts
│       ├── subplots.py                    # Subplot examples (4 demos)
│       ├── saving_images.py               # savefig() demo
│       ├── line_plot.png                  # Saved output
│       └── test.ipynb
└── Streamlit/                             # 🖥️ Interactive Streamlit App
    ├── app.py                             # Home page
    ├── requirements.txt
    ├── utils/
    │   ├── styles.py                      # Amber-themed CSS
    │   └── helpers.py                     # Shared helper functions
    └── pages/
        ├── 01_📈_Plot_Functions.py        # Line plots & customisation
        ├── 02_📊_Charts.py                # Bar, histogram, scatter, pie
        └── 03_🖼️_Subplots_&_Layout.py    # Subplots & savefig
```

---

## 📚 Modules

| # | Module | Topics | Scripts |
|---|--------|--------|---------|
| 1 | **Plot Functions** | Line plots, labels, legends, grids, axis limits, custom ticks | `1.py`, `line_plot.py` |
| 2 | **Charts** | Bar charts, histograms, scatter plots (single & multi-group), pie charts | 5 scripts |
| 3 | **Subplots & Layout** | `plt.subplot()`, OOP `fig, ax` approach, `tight_layout()`, `savefig()` | `subplots.py`, `saving_images.py` |

---

## 🖥️ Streamlit App Features

The interactive Streamlit app lets you **explore every concept live** without running scripts locally:

- **📈 Plot Functions** — Build and customise line plots with color pickers, style selectors, grid toggles, and axis sliders
- **📊 Charts** — Interactive bar charts, histograms (adjustable bins), scatter plots (single + multi-group tabs), and pie charts with explode/percentage toggles
- **🖼️ Subplots & Layout** — Side-by-side subplot demos, OOP figure API with figsize controls, and a download button for exported images

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.x** | Core language |
| **Matplotlib** | Plotting library |
| **NumPy** | Numerical operations |
| **Streamlit** | Interactive web app |
| **Jupyter Notebook** | Exploratory notebooks |

---

## 📋 Requirements

```
streamlit
matplotlib
numpy
pandas
```

Install all dependencies:

```bash
pip install -r Streamlit/requirements.txt
```

---

## 📄 License

This project is open source and available for learning purposes.
