import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Spasm Severity Classifier",
    page_icon="🩺",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main { background-color: #f0f4f8; }

.header-box {
    background: linear-gradient(135deg, #1a3a5c 0%, #2563a8 100%);
    border-radius: 12px;
    padding: 28px 32px 20px;
    margin-bottom: 28px;
    color: white;
}
.header-box h1 { margin: 0 0 6px; font-size: 1.75rem; font-weight: 700; }
.header-box p  { margin: 0; opacity: 0.85; font-size: 0.95rem; }

.card {
    background: white;
    border-radius: 12px;
    padding: 24px 28px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.07);
}
.card h3 { margin-top: 0; color: #1a3a5c; font-size: 1rem; font-weight: 600; }

.score-bar-bg {
    background: #e2e8f0;
    border-radius: 999px;
    height: 12px;
    margin: 10px 0 6px;
    overflow: hidden;
}
.score-bar-fill {
    height: 12px;
    border-radius: 999px;
    transition: width 0.6s ease;
}

.result-mild     { background: linear-gradient(90deg,#22c55e,#16a34a); color:white; }
.result-moderate { background: linear-gradient(90deg,#f59e0b,#d97706); color:white; }
.result-severe   { background: linear-gradient(90deg,#ef4444,#b91c1c); color:white; }

.result-box {
    border-radius: 12px;
    padding: 24px 28px;
    margin-bottom: 20px;
    text-align: center;
}
.result-box h2 { margin: 4px 0 0; font-size: 2rem; font-weight: 700; }
.result-box p  { margin: 6px 0 0; opacity: 0.9; font-size: 0.95rem; }

.rec-box {
    background: #f8fafc;
    border-left: 4px solid #2563a8;
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    margin-top: 12px;
    font-size: 0.93rem;
    color: #334155;
}

.factor-row {
    display: flex;
    justify-content: space-between;
    padding: 6px 0;
    border-bottom: 1px solid #f1f5f9;
    font-size: 0.93rem;
    color: #475569;
}
.factor-row:last-child { border-bottom: none; }
.factor-val { font-weight: 600; color: #1a3a5c; }

.disclaimer {
    font-size: 0.8rem;
    color: #94a3b8;
    text-align: center;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-box">
    <h1>🩺 Muscle Spasm Severity Classifier</h1>
    <p>DPT Clinical Decision Support Tool &nbsp;·&nbsp; Quick assessment aid</p>
</div>
""", unsafe_allow_html=True)

# ── Scoring maps ──────────────────────────────────────────────────────────────
freq_map     = {"Low (occasional)"   : 1, "Medium (frequent)" : 2, "High (constant)"  : 3}
dur_map      = {"Short (<30 seconds)": 1, "Medium (30 s – 2 min)": 2, "Long (>2 minutes)": 3}
trigger_map  = {"Yes": 2, "No": 0}
intensity_map= {"Mild discomfort": 1, "Moderate pain": 2, "Severe / disabling pain": 3}

MAX_SCORE = 11  # max possible: 3+3+2+3

# ── Input card ────────────────────────────────────────────────────────────────
st.markdown('<div class="card"><h3>📋 Patient Assessment Inputs</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    frequency  = st.selectbox("Spasm Frequency",  list(freq_map.keys()),  help="How often do spasms occur?")
    trigger    = st.selectbox("Identifiable Trigger", list(trigger_map.keys()), help="Is there a known trigger (movement, cold, stress)?")
with col2:
    duration   = st.selectbox("Spasm Duration",   list(dur_map.keys()),   help="How long does each spasm last?")
    intensity  = st.selectbox("Pain Intensity",   list(intensity_map.keys()), help="Patient-reported pain level during spasm")

st.markdown('</div>', unsafe_allow_html=True)

# ── Calculate ─────────────────────────────────────────────────────────────────
score = freq_map[frequency] + dur_map[duration] + trigger_map[trigger] + intensity_map[intensity]
pct   = round((score / MAX_SCORE) * 100)

if score <= 4:
    severity = "Mild"
    css_cls  = "result-mild"
    bar_color= "#22c55e"
    emoji    = "🟢"
    rec      = "Monitor and reassure. Basic stretching, heat therapy, and lifestyle advice may suffice. Review if symptoms worsen."
elif score <= 7:
    severity = "Moderate"
    css_cls  = "result-moderate"
    bar_color= "#f59e0b"
    emoji    = "🟡"
    rec      = "Recommend targeted physiotherapy, trigger identification, and possible referral. Document and reassess in 1–2 weeks."
else:
    severity = "Severe"
    css_cls  = "result-severe"
    bar_color= "#ef4444"
    emoji    = "🔴"
    rec      = "Urgent evaluation recommended. Consider specialist referral, imaging if indicated, and pharmacological management. Closely monitor function and pain."

# ── Result card ───────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="result-box {css_cls}">
    <div style="font-size:1.1rem;font-weight:600;opacity:0.9">{emoji} Severity Classification</div>
    <h2>{severity}</h2>
    <p>Total Score: {score} / {MAX_SCORE} &nbsp;({pct}%)</p>
</div>
""", unsafe_allow_html=True)

# Score bar
st.markdown(f"""
<div class="card">
    <h3>📊 Score Breakdown</h3>
    <div class="score-bar-bg">
        <div class="score-bar-fill" style="width:{pct}%;background:{bar_color};"></div>
    </div>
    <div style="font-size:0.85rem;color:#64748b;margin-bottom:14px">{score} of {MAX_SCORE} points</div>
    <div class="factor-row"><span>Frequency</span><span class="factor-val">{freq_map[frequency]} pt</span></div>
    <div class="factor-row"><span>Duration</span><span class="factor-val">{dur_map[duration]} pt</span></div>
    <div class="factor-row"><span>Trigger present</span><span class="factor-val">{trigger_map[trigger]} pt</span></div>
    <div class="factor-row"><span>Pain intensity</span><span class="factor-val">{intensity_map[intensity]} pt</span></div>
    <div class="rec-box">💡 <b>Recommendation:</b> {rec}</div>
</div>
""", unsafe_allow_html=True)

# ── Reference table ───────────────────────────────────────────────────────────
with st.expander("📖 Scoring Reference Guide"):
    st.markdown("""
| Score Range | Classification | Action |
|-------------|---------------|--------|
| 2 – 4       | 🟢 Mild        | Monitor, conservative management |
| 5 – 7       | 🟡 Moderate    | Physiotherapy, reassess |
| 8 – 11      | 🔴 Severe      | Urgent evaluation, possible referral |
""")
    st.caption("Scoring factors: Frequency (1-3) + Duration (1-3) + Trigger (0 or 2) + Intensity (1-3)")

st.markdown('<p class="disclaimer">⚠️ This tool is an educational aid only and does not replace clinical judgment or formal diagnosis.</p>', unsafe_allow_html=True)