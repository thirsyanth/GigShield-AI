import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="GigShield - Risk Prediction",
    page_icon="🛡️",
    layout="wide"
)


# ============================================================
# PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    color: #9ca3af;
    font-size: 17px;
    margin-bottom: 30px;
}

.section {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 16px;
    padding: 25px;
    margin-bottom: 25px;
}

.result-high {
    background: #451a1a;
    border: 1px solid #ef4444;
    border-radius: 18px;
    padding: 30px;
    text-align: center;
}

.result-low {
    background: #123326;
    border: 1px solid #22c55e;
    border-radius: 18px;
    padding: 30px;
    text-align: center;
}

.result-title {
    font-size: 32px;
    font-weight: 800;
}

.probability {
    font-size: 45px;
    font-weight: 800;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    if not MODEL_PATH.exists():

        return None

    return joblib.load(MODEL_PATH)


try:

    model = load_model()

except Exception as e:

    st.error("❌ Could not load the trained model.")

    st.code(str(e))

    st.info(
        "Make sure the scikit-learn version used to load the model "
        "matches the version used during training."
    )

    st.stop()


if model is None:

    st.error(
        "❌ best_model.pkl was not found."
    )

    st.code(
        str(MODEL_PATH)
    )

    st.stop()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🛡️ GigShield Risk Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Predict whether a delivery is likely to experience
    work disruption using the trained Random Forest model.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MODEL STATUS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Model",
        "Random Forest"
    )

with col2:

    st.metric(
        "Test Accuracy",
        "91.7%"
    )

with col3:

    st.metric(
        "Disruption Recall",
        "87.76%"
    )


st.divider()


# ============================================================
# DELIVERY PARTNER
# ============================================================

st.markdown(
    "### 👤 Delivery Partner Information"
)

with st.container(border=True):

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        age = st.number_input(
            "Delivery Person Age",
            min_value=18,
            max_value=70,
            value=30
        )

    with col2:

        rating = st.number_input(
            "Delivery Person Rating",
            min_value=1.0,
            max_value=5.0,
            value=4.7,
            step=0.1
        )

    with col3:

        vehicle_condition = st.number_input(
            "Vehicle Condition",
            min_value=0,
            max_value=5,
            value=2
        )

    with col4:

        multiple_deliveries = st.number_input(
            "Multiple Deliveries",
            min_value=0,
            max_value=5,
            value=1
        )


# ============================================================
# ENVIRONMENT
# ============================================================

st.markdown(
    "### 🌦️ Environmental Conditions"
)

with st.container(border=True):

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        weather = st.selectbox(
            "Weather Conditions",
            [
                "Sunny",
                "Cloudy",
                "Fog",
                "Stormy",
                "Sandstorms",
                "Windy"
            ]
        )

    with col2:

        traffic = st.selectbox(
            "Road Traffic Density",
            [
                "Low",
                "Medium",
                "High",
                "Jam"
            ]
        )

    with col3:

        festival = st.selectbox(
            "Festival",
            [
                "No",
                "Yes"
            ]
        )

    with col4:

        city = st.selectbox(
            "City",
            [
                "Urban",
                "Metropolitian",
                "Semi-Urban"
            ]
        )


# ============================================================
# ORDER INFORMATION
# ============================================================

st.markdown(
    "### 🍔 Order Information"
)

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        order_type = st.selectbox(
            "Type of Order",
            [
                "Snack",
                "Meal",
                "Drinks",
                "Buffet"
            ]
        )

    with col2:

        vehicle_type = st.selectbox(
            "Type of Vehicle",
            [
                "motorcycle",
                "scooter",
                "electric_scooter",
                "bicycle"
            ]
        )


# ============================================================
# TIME INFORMATION
# ============================================================

st.markdown(
    "### 🕐 Delivery Timing"
)

with st.container(border=True):

    col1, col2, col3 = st.columns(3)

    with col1:

        day_of_week = st.selectbox(
            "Order Day of Week",
            [
                0,
                1,
                2,
                3,
                4,
                5,
                6
            ],
            index=5
        )

    with col2:

        month = st.selectbox(
            "Order Month",
            [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12
            ],
            index=2
        )

    with col3:

        order_hour = st.slider(
            "Order Hour",
            min_value=0,
            max_value=23,
            value=19
        )


# ============================================================
# DISTANCE
# ============================================================

st.markdown(
    "### 📍 Delivery Distance"
)

with st.container(border=True):

    distance = st.number_input(
        "Distance (km)",
        min_value=1.0,
        max_value=21.0,
        value=5.0,
        step=0.1
    )


st.divider()


# ============================================================
# PREDICT BUTTON
# ============================================================

predict = st.button(
    "🚀 Predict Work Disruption Risk",
    use_container_width=True,
    type="primary"
)


# ============================================================
# PREDICTION
# ============================================================

if predict:

    input_data = pd.DataFrame({

        "Delivery_person_Age": [float(age)],

        "Delivery_person_Ratings": [float(rating)],

        "Weatherconditions": [weather],

        "Road_traffic_density": [traffic],

        "Vehicle_condition": [float(vehicle_condition)],

        "Type_of_order": [order_type],

        "Type_of_vehicle": [vehicle_type],

        "multiple_deliveries": [float(multiple_deliveries)],

        "Festival": [festival],

        "City": [city],

        "Order_DayOfWeek": [float(day_of_week)],

        "Order_Month": [float(month)],

        "Order_Hour": [float(order_hour)],

        "Distance_km": [float(distance)]
    })


    try:

        prediction = model.predict(
            input_data
        )[0]

        probability = model.predict_proba(
            input_data
        )[0][1]

        probability_percent = probability * 100


        st.markdown(
            "## 📊 Prediction Result"
        )


        # ====================================================
        # HIGH RISK
        # ====================================================

        if prediction == 1:

            st.markdown(
                f"""
                <div class="result-high">

                <div class="result-title">
                ⚠️ HIGH DISRUPTION RISK
                </div>

                <br>

                <div class="probability">
                {probability_percent:.2f}%
                </div>

                <p>
                Probability of work disruption
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.warning(
                "The model predicts that this delivery "
                "has a high probability of work disruption."
            )

            st.markdown(
                "### 💡 Recommended Action"
            )

            st.write(
                """
                Consider checking traffic conditions,
                weather conditions, delivery distance and
                vehicle readiness before accepting or
                completing the delivery.
                """
            )


        # ====================================================
        # LOW RISK
        # ====================================================

        else:

            st.markdown(
                f"""
                <div class="result-low">

                <div class="result-title">
                ✅ NORMAL / LOW DISRUPTION RISK
                </div>

                <br>

                <div class="probability">
                {probability_percent:.2f}%
                </div>

                <p>
                Probability of work disruption
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.success(
                "The model predicts a relatively low "
                "probability of work disruption."
            )


        # ====================================================
        # INPUT SUMMARY
        # ====================================================

        st.markdown(
            "### 📋 Input Summary"
        )

        summary = pd.DataFrame({

            "Feature": [
                "Age",
                "Rating",
                "Weather",
                "Traffic",
                "Vehicle Condition",
                "Order Type",
                "Vehicle Type",
                "Multiple Deliveries",
                "Festival",
                "City",
                "Day of Week",
                "Month",
                "Order Hour",
                "Distance"
            ],

            "Value": [
                age,
                rating,
                weather,
                traffic,
                vehicle_condition,
                order_type,
                vehicle_type,
                multiple_deliveries,
                festival,
                city,
                day_of_week,
                month,
                order_hour,
                f"{distance:.2f} km"
            ]
        })


        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )


    except Exception as e:

        st.error(
            "❌ Prediction failed."
        )

        st.code(
            str(e)
        )

        st.info(
            "The input columns must exactly match the "
            "features used during model training."
        )