import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="GigShield - About",
    page_icon="ℹ️",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("ℹ️ About GigShield")

st.subheader(
    "Machine Learning-Based Income Disruption Risk Prediction "
    "for Gig Workers"
)

st.write(
    """
    GigShield is a machine learning capstone project focused on
    predicting potential work disruption for gig delivery workers.
    
    The system analyzes delivery-related operational conditions
    and uses a trained Random Forest classifier to estimate
    disruption risk.
    """
)

st.divider()

# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------

st.header("📌 Project Overview")

overview = {
    "Project Name": "GigShield",
    "ML Project": "Machine Learning-Based Income Disruption Risk Prediction for Gig Workers",
    "Problem Domain": "Gig Economy / Delivery Operations",
    "Machine Learning Task": "Binary Classification",
    "Final Model": "Random Forest",
    "Dataset Records": "45,593",
    "Input Features": "14",
    "Target": "Work Disruption",
    "Disruption Threshold": "Delivery Time > 32 minutes"
}

for key, value in overview.items():

    st.write(
        f"**{key}:** {value}"
    )

# --------------------------------------------------
# DATASET
# --------------------------------------------------

st.header("📊 Dataset Information")

st.write(
    """
    The project uses a food-delivery operational dataset containing
    delivery personnel information, order information, location
    information, weather conditions, traffic conditions and
    delivery time.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Records",
        "45,593"
    )

with col2:
    st.metric(
        "Input Features",
        "14"
    )

with col3:
    st.metric(
        "Target Classes",
        "2"
    )

st.write("### Selected Features")

features = [
    "Delivery_person_Age",
    "Delivery_person_Ratings",
    "Weatherconditions",
    "Road_traffic_density",
    "Vehicle_condition",
    "Type_of_order",
    "Type_of_vehicle",
    "multiple_deliveries",
    "Festival",
    "City",
    "Order_DayOfWeek",
    "Order_Month",
    "Order_Hour",
    "Distance_km"
]

st.dataframe(
    {
        "Feature": features,
        "Description": [
            "Age of delivery person",
            "Worker delivery rating",
            "Weather condition",
            "Road traffic density",
            "Vehicle condition",
            "Order category",
            "Vehicle category",
            "Number of multiple deliveries",
            "Festival status",
            "City category",
            "Day of week",
            "Order month",
            "Order hour",
            "Restaurant-to-delivery distance"
        ]
    },
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# TARGET VARIABLE
# --------------------------------------------------

st.header("🎯 Target Variable")

st.write(
    """
    Work_Disruption is a binary classification target created
    using a delivery-time threshold of 32 minutes.
    """
)

target_col1, target_col2 = st.columns(2)

with target_col1:

    st.success(
        """
        ### Class 0 — Normal

        Delivery time ≤ 32 minutes

        Records: **34,324**

        Percentage: **75.28%**
        """
    )

with target_col2:

    st.error(
        """
        ### Class 1 — Disruption

        Delivery time > 32 minutes

        Records: **11,269**

        Percentage: **24.72%**
        """
    )

# --------------------------------------------------
# MACHINE LEARNING MODELS
# --------------------------------------------------

st.header("🤖 Machine Learning Models")

models = {
    "Logistic Regression": {
        "Accuracy": "84.68%",
        "Precision": "64.43%",
        "Recall": "84.87%",
        "F1 Score": "73.25%",
        "ROC-AUC": "92.49%"
    },

    "Random Forest": {
        "Accuracy": "91.70%",
        "Precision": "80.44%",
        "Recall": "87.76%",
        "F1 Score": "83.94%",
        "ROC-AUC": "97.09%"
    },

    "Gradient Boosting": {
        "Accuracy": "92.44%",
        "Precision": "85.62%",
        "Recall": "83.45%",
        "F1 Score": "84.52%",
        "ROC-AUC": "97.22%"
    }
}

for model_name, metrics in models.items():

    st.subheader(model_name)

    cols = st.columns(5)

    metric_names = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC"
    ]

    for col, metric_name in zip(
        cols,
        metric_names
    ):

        with col:

            st.metric(
                metric_name,
                metrics[metric_name]
            )

# --------------------------------------------------
# MODEL SELECTION
# --------------------------------------------------

st.header("🏆 Final Model Selection")

st.write(
    """
    Gradient Boosting achieved the highest overall accuracy
    at 92.44%. However, Random Forest achieved 87.76% recall
    for the disruption class.
    
    Random Forest was selected as the operational model for
    this capstone because identifying disruption cases is an
    important project objective.
    """
)

st.info(
    """
    Final deployed model: **Random Forest**

    Test Accuracy: **91.70%**

    Disruption Recall: **87.76%**

    ROC-AUC: **97.09%**
    """
)

# --------------------------------------------------
# TECHNOLOGY STACK
# --------------------------------------------------

st.header("💻 Technology Stack")

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:

    st.subheader("🐍 Programming")

    st.markdown(
        """
        - Python
        - Pandas
        - NumPy
        """
    )

with tech_col2:

    st.subheader("🤖 Machine Learning")

    st.markdown(
        """
        - Scikit-learn
        - Logistic Regression
        - Random Forest
        - Gradient Boosting
        """
    )

with tech_col3:

    st.subheader("🌐 Application")

    st.markdown(
        """
        - Streamlit
        - Matplotlib
        - Joblib
        """
    )

# --------------------------------------------------
# PROJECT WORKFLOW
# --------------------------------------------------

st.header("⚙️ Complete Project Workflow")

st.code(
    """
Raw Dataset
     ↓
Data Cleaning
     ↓
Missing Value Handling
     ↓
Date & Time Feature Engineering
     ↓
Distance Calculation
     ↓
Delivery-Time Analysis
     ↓
Disruption Threshold = 32 Minutes
     ↓
Binary Target Creation
     ↓
Feature Selection
     ↓
Train / Test Split
     ↓
Preprocessing Pipeline
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Random Forest Selection
     ↓
Model Serialization
     ↓
Streamlit Deployment
     ↓
Risk Prediction
    """,
    language="text"
)

# --------------------------------------------------
# LIMITATIONS
# --------------------------------------------------

st.header("⚠️ Project Limitations")

st.markdown(
    """
    - The current system uses historical delivery data.
    - The model predicts delivery disruption rather than
      directly measuring worker income loss.
    - Real-time weather and traffic APIs are not currently
      integrated.
    - The current prototype does not process real insurance
      claims or payments.
    - Model predictions depend on the quality of the input data.
    - The 32-minute threshold is dataset-based.
    """
)

# --------------------------------------------------
# FUTURE ENHANCEMENTS
# --------------------------------------------------

st.header("🚀 Future Enhancements")

future = [
    "Real-time weather API integration",
    "Real-time traffic data",
    "GPS-based worker monitoring",
    "Fraud and GPS spoofing detection",
    "Dynamic risk-based insurance pricing",
    "Automated claim validation",
    "UPI payment integration",
    "Worker dashboard",
    "Policy management",
    "Real-time notifications"
]

for item in future:
    st.write(f"🔹 {item}")

# --------------------------------------------------
# PROJECT SUMMARY
# --------------------------------------------------

st.divider()

st.header("📝 Project Summary")

st.success(
    """
    GigShield demonstrates how machine learning can be used
    to identify potential delivery work disruption for gig
    workers.

    The system converts operational delivery information into
    a machine learning risk prediction and presents the result
    through an interactive Streamlit interface.
    """
)

st.caption(
    "GigShield | Machine Learning Capstone Project"
)