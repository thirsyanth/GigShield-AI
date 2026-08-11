import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="GigShield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* HERO */

.hero {
    padding: 45px;
    border-radius: 24px;
    background: linear-gradient(
        135deg,
        #101a38,
        #162b59
    );
    border: 1px solid #263b73;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero-subtitle {
    color: #b9c7e6;
    font-size: 18px;
    max-width: 850px;
    line-height: 1.6;
}

/* CARDS */

.card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 18px;
    padding: 25px;
    min-height: 190px;
}

.card h3 {
    margin-bottom: 10px;
}

.card p {
    color: #9ca3af;
    line-height: 1.6;
}

/* STAT CARDS */

.stat-card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 16px;
    padding: 22px;
    text-align: center;
}

.stat-title {
    color: #9ca3af;
    font-size: 14px;
}

.stat-value {
    font-size: 30px;
    font-weight: 800;
}

/* RISK */

.risk-card {
    background: linear-gradient(
        135deg,
        #123326,
        #164e3b
    );
    border: 1px solid #22c55e;
    border-radius: 18px;
    padding: 28px;
}

/* SECTION */

.section-title {
    font-size: 30px;
    font-weight: 800;
    margin-top: 35px;
    margin-bottom: 20px;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #6b7280;
    padding: 30px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "# 🛡️ GigShield"
    )

    st.caption(
        "AI-Powered Income Protection"
    )

    st.divider()

    st.markdown(
        "### Navigation"
    )

    st.info(
        """
        Use the pages on the left to:

        🛡️ Predict disruption risk

        📊 Compare ML models

        📈 Analyze delivery risks

        ℹ️ Learn about GigShield
        """
    )

    st.divider()

    st.markdown(
        "**Model:** Random Forest"
    )

    st.markdown(
        "**Accuracy:** 91.7%"
    )

    st.markdown(
        "**Disruption Recall:** 87.76%"
    )


# ============================================================
# HERO SECTION
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🛡️ GigShield
</div>

<div class="hero-subtitle">

AI-powered work disruption risk prediction for
gig delivery workers.

GigShield analyzes delivery conditions such as
weather, traffic, distance, vehicle condition and
delivery timing to estimate the probability of
work disruption.

</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# QUICK STATS
# ============================================================

st.markdown(
    '<div class="section-title">📊 Project Overview</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown("""
    <div class="stat-card">

    <div class="stat-title">
    Dataset Records
    </div>

    <div class="stat-value">
    45,593
    </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="stat-card">

    <div class="stat-title">
    Disruption Rate
    </div>

    <div class="stat-value">
    24.72%
    </div>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="stat-card">

    <div class="stat-title">
    Model Accuracy
    </div>

    <div class="stat-value">
    91.7%
    </div>

    </div>
    """, unsafe_allow_html=True)


with col4:

    st.markdown("""
    <div class="stat-card">

    <div class="stat-title">
    Avg Delivery Time
    </div>

    <div class="stat-value">
    26.29 min
    </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# RISK PREDICTION CTA
# ============================================================

st.markdown(
    '<div class="section-title">🚨 Check Delivery Risk</div>',
    unsafe_allow_html=True
)


st.markdown("""
<div class="risk-card">

<h2>Predict Work Disruption Risk</h2>

<p>

Enter delivery partner, weather, traffic, order and
distance information to estimate the probability of
work disruption.

</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "🛡️ Go to Risk Prediction",
    use_container_width=True,
    type="primary"
):

    st.switch_page(
        "pages/1_Risk_Prediction.py"
    )


# ============================================================
# FEATURES
# ============================================================

st.markdown(
    '<div class="section-title">⚡ GigShield Intelligence</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown("""
    <div class="card">

    <h3>🌦️ Environmental Risk</h3>

    <p>

    Analyze weather conditions, road traffic,
    festivals and city characteristics that
    can influence delivery performance.

    </p>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">

    <h3>📍 Delivery Intelligence</h3>

    <p>

    Use delivery distance, order timing,
    vehicle condition and multiple-delivery
    information to estimate operational risk.

    </p>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="card">

    <h3>🤖 Machine Learning</h3>

    <p>

    Random Forest provides the deployed
    disruption prediction model with a
    test accuracy of 91.7%.

    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# HOW IT WORKS
# ============================================================

st.markdown(
    '<div class="section-title">🔄 How GigShield Works</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown("""
    <div class="card">

    <h3>01</h3>

    <h4>Enter Conditions</h4>

    <p>
    Provide delivery and environmental
    information.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">

    <h3>02</h3>

    <h4>Feature Processing</h4>

    <p>
    GigShield processes numerical and
    categorical delivery features.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="card">

    <h3>03</h3>

    <h4>AI Prediction</h4>

    <p>
    The Random Forest model calculates
    disruption probability.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col4:

    st.markdown("""
    <div class="card">

    <h3>04</h3>

    <h4>Risk Decision</h4>

    <p>
    The system displays the predicted
    disruption risk.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# PROJECT RESULTS
# ============================================================

st.markdown(
    '<div class="section-title">🏆 Machine Learning Results</div>',
    unsafe_allow_html=True
)


results = {
    "Logistic Regression": {
        "Accuracy": "84.68%",
        "F1": "73.25%",
        "ROC-AUC": "92.49%"
    },

    "Random Forest": {
        "Accuracy": "91.70%",
        "F1": "83.94%",
        "ROC-AUC": "97.09%"
    },

    "Gradient Boosting": {
        "Accuracy": "92.44%",
        "F1": "84.52%",
        "ROC-AUC": "97.22%"
    }
}


for model_name, values in results.items():

    with st.expander(
        f"📊 {model_name}"
    ):

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Accuracy",
                values["Accuracy"]
            )

        with col2:

            st.metric(
                "F1 Score",
                values["F1"]
            )

        with col3:

            st.metric(
                "ROC-AUC",
                values["ROC-AUC"]
            )


# ============================================================
# FINAL MODEL
# ============================================================

st.success(
    """
    🏆 Deployed Model: Random Forest

    The Random Forest model is stored in
    `models/best_model.pkl` and is used by the
    Risk Prediction page.
    """
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown("""
<div class="footer">

<b>🛡️ GigShield</b>

<br>

AI-Powered Work Disruption Risk Intelligence

<br><br>

Machine Learning • Risk Prediction • Gig Worker Protection

</div>
""", unsafe_allow_html=True)