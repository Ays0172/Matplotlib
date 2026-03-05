"""Shared helper utilities for the Matplotlib Visualization Masterclass Streamlit app."""

import streamlit as st


def show_code(code: str, language: str = "python") -> None:
    """Display a code block with syntax highlighting."""
    st.code(code, language=language)


def show_explanation(text: str) -> None:
    """Render an explanation inside a styled info card."""
    st.markdown(
        f'<div class="info-card">{text}</div>',
        unsafe_allow_html=True,
    )


def create_metric_cards(metrics: list[tuple[str, str]]) -> None:
    """
    Render a row of mini metric cards.

    metrics: list of (value, label) tuples.
    """
    cards_html = "".join(
        f'<div class="metric-mini"><div class="value">{val}</div><div class="label">{lbl}</div></div>'
        for val, lbl in metrics
    )
    st.markdown(f'<div class="metric-row">{cards_html}</div>', unsafe_allow_html=True)
