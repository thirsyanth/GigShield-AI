import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="GigShield - ML Analytics",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 800;
}

.subtitle {
    color: #9ca3af;
    font-size: 17px;
    margin-bottom: 30px;
}

.metric-card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 16px;
    padding: 24px;
    text-align: center;
}

.metric-title {
    color: #9ca3af;
    font-size: 15px;
}

.metric-value {
    font-size: 32px;
    font-weight: 800;
    color: white;
}

.best-model {
    background: linear-gradient(
        135deg,
        #123326,
        #164e3b
    );
    border: 1px solid #22c55e;
    border-radius: 18px;
    padding: 28px;
    margin: 25px 0;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📊 Machine Learning Analytics</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Compare the supervised machine learning models developed
    for GigShield work disruption prediction.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MODEL RESULTS
# ============================================================

results = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Random Forest",
        "Gradient Boosting"
    ],

    "Accuracy": [
        0.8468,
        0.9170,
        0.9244
    ],

    "Precision": [
        0.6443,
        0.8044,
        0.8562
    ],

    "Recall": [
        0.8487,
        0.8776,
        0.8345
    ],

    "F1 Score": [
        0.7325,
        0.8394,
        0.8452
    ],

    "ROC-AUC": [
        0.9249,
        0.9709,
        0.9722
    ]
})


# ============================================================
# BEST MODEL
# ============================================================

st.markdown(
    """
    <div class="best-model">

    <h2>🏆 Selected Model: Random Forest</h2>

    <p>
    Random Forest was selected as the final deployed model
    because it provides a strong balance between accuracy,
    precision and disruption recall.
    </p>

    <b>Test Accuracy:</b> 91.7% &nbsp;&nbsp;

    <b>Disruption Recall:</b> 87.76%

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MODEL METRICS
# ============================================================

st.markdown("### 📈 Model Performance")


for _, row in results.iterrows():

    st.markdown(
        f"#### {row['Model']}"
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Accuracy",
            f"{row['Accuracy'] * 100:.2f}%"
        )

    with col2:
        st.metric(
            "Precision",
            f"{row['Precision'] * 100:.2f}%"
        )

    with col3:
        st.metric(
            "Recall",
            f"{row['Recall'] * 100:.2f}%"
        )

    with col4:
        st.metric(
            "F1 Score",
            f"{row['F1 Score'] * 100:.2f}%"
        )

    with col5:
        st.metric(
            "ROC-AUC",
            f"{row['ROC-AUC'] * 100:.2f}%"
        )


# ============================================================
# COMPARISON TABLE
# ============================================================

st.markdown("### 📋 Complete Model Comparison")

display_results = results.copy()

for column in [
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score",
    "ROC-AUC"
]:

    display_results[column] = (
        display_results[column] * 100
    ).round(2).astype(str) + "%"


st.dataframe(
    display_results,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# BAR CHART
# ============================================================

st.markdown("### 📊 Model Performance Comparison")


fig, ax = plt.subplots(
    figsize=(12, 6)
)

x = range(len(results))

width = 0.15

metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score",
    "ROC-AUC"
]

for i, metric in enumerate(metrics):

    values = results[metric]

    positions = [
        value + (i - 2) * width
        for value in x
    ]

    ax.bar(
        positions,
        values,
        width,
        label=metric
    )


ax.set_xticks(
    list(x)
)

ax.set_xticklabels(
    results["Model"]
)

ax.set_ylabel(
    "Score"
)

ax.set_ylim(
    0,
    1
)

ax.set_title(
    "Machine Learning Model Comparison"
)

ax.legend()

ax.grid(
    axis="y",
    alpha=0.2
)


st.pyplot(fig)

plt.close(fig)


# ============================================================
# CONFUSION MATRIX DATA
# ============================================================

st.markdown("### 🔢 Confusion Matrix Analysis")


st.info(
    """
    The confusion matrices show how accurately each model
    identifies Normal deliveries and Work Disruption cases.
    """
)


# ============================================================
# CONFUSION MATRICES
# ============================================================

matrices = {

    "Logistic Regression": [
        [5809, 1056],
        [341, 1913]
    ],

    "Random Forest": [
        [6384, 481],
        [276, 1978]
    ],

    "Gradient Boosting": [
        [6549, 316],
        [373, 1881]
    ]
}


selected_model = st.selectbox(
    "Select Model",
    list(matrices.keys())
)


matrix = matrices[selected_model]


fig, ax = plt.subplots(
    figsize=(7, 5)
)

image = ax.imshow(
    matrix
)

ax.set_title(
    f"{selected_model} - Confusion Matrix"
)

ax.set_xlabel(
    "Predicted Label"
)

ax.set_ylabel(
    "True Label"
)

ax.set_xticks([0, 1])

ax.set_yticks([0, 1])

ax.set_xticklabels([
    "Normal",
    "Disruption"
])

ax.set_yticklabels([
    "Normal",
    "Disruption"
])


for i in range(2):

    for j in range(2):

        ax.text(
            j,
            i,
            matrix[i][j],
            ha="center",
            va="center",
            fontsize=14
        )


st.pyplot(fig)

plt.close(fig)


# ============================================================
# MODEL INTERPRETATION
# ============================================================

st.markdown("### 🧠 Model Interpretation")


st.markdown("""
#### Logistic Regression

Logistic Regression achieved:

- **84.68% Accuracy**
- **64.43% Precision**
- **84.87% Recall**
- **73.25% F1 Score**
- **92.49% ROC-AUC**

It provides a useful baseline model but has lower
precision compared with the tree-based models.

---

#### Random Forest

Random Forest achieved:

- **91.70% Accuracy**
- **80.44% Precision**
- **87.76% Recall**
- **83.94% F1 Score**
- **97.09% ROC-AUC**

It provides a strong balance between identifying
disruptions and avoiding false alarms.

---

#### Gradient Boosting

Gradient Boosting achieved:

- **92.44% Accuracy**
- **85.62% Precision**
- **83.45% Recall**
- **84.52% F1 Score**
- **97.22% ROC-AUC**

It achieved the highest accuracy and ROC-AUC among
the three tested models.
""")


# ============================================================
# FINAL MODEL
# ============================================================

st.success(
    """
    🏆 Final deployed model: Random Forest

    The saved model is available as:
    models/best_model.pkl
    """
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "GigShield | Machine Learning-Based Income Disruption Risk Prediction"
)