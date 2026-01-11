import sys
from pathlib import Path

import streamlit as st

# --- Make it possible to import from app/core ---
CORE_PATH = Path(__file__).resolve().parents[1] / "core"
sys.path.append(str(CORE_PATH))

from mapping import analyze_findings  # noqa: E402


st.set_page_config(page_title="GRC Risk Dashboard", layout="wide")

st.title("GRC Risk Dashboard")
st.caption("Shows inherent vs residual risk after applying control effectiveness estimates.")


# --- Load data ---
df = analyze_findings()

# Basic checks
if df.empty:
    st.error("No data found. Check your data/controls.csv and data/findings.csv files.")
    st.stop()

# --- Executive summary metrics ---
col1, col2, col3 = st.columns(3)

max_residual = float(df["residual_risk"].max())
avg_residual = float(df["residual_risk"].mean())
top_control = df.loc[df["residual_risk"].idxmax(), "control"]

col1.metric("Highest Residual Risk", f"{max_residual:.2f}")
col2.metric("Average Residual Risk", f"{avg_residual:.2f}")
col3.metric("Top Risk Control", str(top_control))

st.divider()

# --- Controls for filtering ---
st.subheader("Filter & Prioritize")

min_risk = st.slider(
    "Show only items with residual risk ≥",
    min_value=0.0,
    max_value=float(df["residual_risk"].max()),
    value=0.0,
    step=0.1,
)

filtered = df[df["residual_risk"] >= min_risk].copy()

left, right = st.columns([2, 1])

with left:
    st.subheader("Top Residual Risks (What to fix first)")
    st.dataframe(
        filtered[["asset_id", "finding", "control", "inherent_risk", "residual_risk"]],
        use_container_width=True,
    )

with right:
    st.subheader("Residual Risk Distribution")
    st.bar_chart(filtered.set_index("asset_id")["residual_risk"])

st.divider()

# --- Interpretation help (GRC meaning) ---
st.subheader("How to Read This (GRC Meaning)")
st.markdown(
    """
- **Inherent risk** = risk before controls (severity × asset criticality).  
- **Residual risk** = remaining risk after controls reduce it.  
- **The top row is your first priority** because it’s the highest remaining business risk.
"""
)

# --- Quick “Executive notes” generator ---
st.subheader("Executive Notes (Auto Summary)")
top3 = df.sort_values("residual_risk", ascending=False).head(3)
notes = []
for _, row in top3.iterrows():
    notes.append(
        f"- **{row['asset_id']}**: {row['finding']} "
        f"(Control: {row['control']}) → Residual risk **{row['residual_risk']:.2f}**"
    )

st.markdown("\n".join(notes))
