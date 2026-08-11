import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="GigShield - About the Solution",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🛡️ GigShield")

st.subheader(
    "AI-Powered Parametric Income Protection Concept for Gig Workers"
)

st.write(
    """
    GigShield is a machine learning-based project designed to
    identify delivery work disruption risk for gig workers.
    
    The system uses operational delivery information to estimate
    the probability that a delivery may experience disruption.
    """
)

st.divider()

# --------------------------------------------------
# PROBLEM
# --------------------------------------------------

st.header("🎯 The Real-World Problem")

st.write(
    """
    Gig delivery workers depend on completing deliveries to earn
    their daily income. Their working conditions can be affected
    by factors such as:
    """
)

problem_col1, problem_col2, problem_col3 = st.columns(3)

with problem_col1:
    st.info(
        """
        ### 🌧️ Weather

        Storms, fog, sandstorms and other adverse weather
        conditions can make delivery operations difficult.
        """
    )

with problem_col2:
    st.info(
        """
        ### 🚦 Traffic

        Heavy traffic and road congestion can increase
        delivery completion time.
        """
    )

with problem_col3:
    st.info(
        """
        ### 📍 Distance

        Longer delivery distances can increase the time
        required to complete an order.
        """
    )

# --------------------------------------------------
# GIGSHIELD SOLUTION
# --------------------------------------------------

st.header("💡 Proposed Solution")

st.write(
    """
    GigShield uses a machine learning model to estimate
    delivery disruption risk before or during an operational
    decision process.
    """
)

st.markdown(
    """
    ### Core workflow

    **Delivery Conditions**
    
    ↓
    
    **Data Preprocessing**
    
    ↓
    
    **Random Forest Model**
    
    ↓
    
    **Disruption Probability**
    
    ↓
    
    **Risk Classification**
    
    ↓
    
    **Potential Income Protection Trigger**
    """
)

# --------------------------------------------------
# ML ROLE
# --------------------------------------------------

st.header("🤖 Role of Machine Learning")

st.write(
    """
    The machine learning component is the prediction engine
    of GigShield.
    """
)

ml_col1, ml_col2 = st.columns(2)

with ml_col1:

    st.subheader("Input Features")

    st.markdown(
        """
        The model uses 14 features:

        - Delivery person age
        - Delivery person rating
        - Weather conditions
        - Road traffic density
        - Vehicle condition
        - Type of order
        - Type of vehicle
        - Multiple deliveries
        - Festival status
        - City
        - Order day of week
        - Order month
        - Order hour
        - Delivery distance
        """
    )

with ml_col2:

    st.subheader("Prediction Output")

    st.markdown(
        """
        The trained Random Forest model produces:

        **Class 0**
        → Normal / Lower Disruption Risk

        **Class 1**
        → Predicted High Disruption Risk

        The model also provides a probability score representing
        the estimated likelihood of class 1.
        """
    )

# --------------------------------------------------
# PARAMETRIC INSURANCE CONCEPT
# --------------------------------------------------

st.header("🛡️ Parametric Protection Concept")

st.write(
    """
    In a parametric insurance design, predefined measurable
    conditions can be used as triggers rather than requiring
    traditional loss assessment for every individual claim.
    """
)

trigger_col1, trigger_col2 = st.columns(2)

with trigger_col1:

    st.subheader("Possible Trigger Signals")

    st.markdown(
        """
        - High disruption probability
        - Severe weather conditions
        - Heavy traffic conditions
        - Excessive delivery distance
        - Operational disruption conditions
        - Other verified external signals
        """
    )

with trigger_col2:

    st.subheader("Potential Response")

    st.markdown(
        """
        1. Detect disruption conditions
        2. Evaluate predefined eligibility rules
        3. Validate the event
        4. Trigger an eligible protection workflow
        5. Process compensation according to the policy
        """
    )

st.warning(
    """
    The current capstone implementation focuses on the
    machine learning risk prediction component. It does not
    implement real insurance underwriting, policy issuance,
    payment processing, or regulatory compliance.
    """
)

# --------------------------------------------------
# EXAMPLE
# --------------------------------------------------

st.header("📌 Example Scenario")

st.write(
    """
    Consider a delivery worker operating during a storm with
    heavy traffic, multiple deliveries and a relatively long
    delivery distance.
    """
)

example_col1, example_col2 = st.columns(2)

with example_col1:

    st.subheader("Input Situation")

    st.markdown(
        """
        🌧️ Stormy weather

        🚦 Jam traffic

        📍 15 km distance

        📦 2 multiple deliveries

        🎉 Festival = Yes
        """
    )

with example_col2:

    st.subheader("ML Result")

    st.error(
        """
        Predicted High Disruption Risk

        Example model probability:
        **85.22%**
        """
    )

st.write(
    """
    This example demonstrates how the ML component can be
    connected to a broader income-protection workflow.
    The probability is a model estimate and does not by itself
    establish an insurance claim.
    """
)

# --------------------------------------------------
# PROJECT ARCHITECTURE
# --------------------------------------------------

st.header("🏗️ GigShield System Architecture")

st.code(
    """
                Gig Worker
                    │
                    ▼
          Delivery Information
                    │
                    ▼
            Data Preprocessing
                    │
                    ▼
          Machine Learning Model
             Random Forest
                    │
                    ▼
          Disruption Probability
                    │
             ┌──────┴──────┐
             ▼             ▼
          Normal        Disruption
             │             │
             │             ▼
             │      Risk Assessment
             │             │
             │             ▼
             │     Protection Workflow
             │
             ▼
       Normal Operation
    """,
    language="text"
)

# --------------------------------------------------
# CURRENT IMPLEMENTATION
# --------------------------------------------------

st.header("✅ Current Capstone Implementation")

implemented_col1, implemented_col2 = st.columns(2)

with implemented_col1:

    st.success(
        """
        ### Completed

        ✅ Data preprocessing

        ✅ Feature engineering

        ✅ Disruption target creation

        ✅ Logistic Regression

        ✅ Random Forest

        ✅ Gradient Boosting

        ✅ Model evaluation

        ✅ Random Forest model deployment

        ✅ Streamlit prediction interface
        """
    )

with implemented_col2:

    st.info(
        """
        ### Future Extensions

        🔹 Real-time weather API

        🔹 GPS-based operational monitoring

        🔹 Fraud / GPS spoofing detection

        🔹 Dynamic insurance pricing

        🔹 Automated claim validation

        🔹 UPI payment integration

        🔹 Worker policy management

        🔹 Real-time notifications
        """
    )

# --------------------------------------------------
# FINAL MESSAGE
# --------------------------------------------------

st.divider()

st.success(
    """
    🛡️ GigShield combines machine learning and a
    parametric-protection concept to identify potential
    income-disrupting delivery conditions for gig workers.
    """
)

st.caption(
    "GigShield | Machine Learning Capstone Project"
)