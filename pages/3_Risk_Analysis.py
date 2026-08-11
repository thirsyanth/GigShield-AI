import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="GigShield - Risk Analysis",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
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

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 35px;
    margin-bottom: 18px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📊 GigShield Risk Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Explore the delivery conditions associated with work disruption
    in the GigShield dataset.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

DATA_PATH = DATA_DIR / "train.csv"


# ============================================================
# LOAD DATASET
# ============================================================

if not DATA_PATH.exists():

    st.error("❌ Dataset could not be found.")

    st.info(
        f"""
        Please make sure the dataset exists at:

        `{DATA_PATH}`

        The file must be named:

        `train.csv`
        """
    )

    st.stop()


try:

    df = pd.read_csv(DATA_PATH)

except Exception as e:

    st.error("❌ Error while loading train.csv")

    st.exception(e)

    st.stop()


st.success(
    f"✅ Dataset loaded successfully: {DATA_PATH.name}"
)


# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

# Very important:
# Remove leading/trailing spaces from column names.

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)


# ============================================================
# SHOW ORIGINAL COLUMNS FOR DEBUGGING
# ============================================================

# This will help if the dataset has a slightly different
# column name.

with st.expander("🔧 Dataset Column Information"):

    st.write(
        "Columns detected in train.csv:"
    )

    st.write(
        list(df.columns)
    )


# ============================================================
# FIND DELIVERY TIME COLUMN
# ============================================================

delivery_time_column = None


possible_time_columns = [
    "Time_taken(min)",
    "Time_taken (min)",
    "Time_taken",
    "Delivery_Time",
    "Delivery Time"
]


for column in possible_time_columns:

    if column in df.columns:

        delivery_time_column = column

        break


# ============================================================
# FALLBACK: SEARCH COLUMN NAME
# ============================================================

if delivery_time_column is None:

    for column in df.columns:

        column_lower = column.lower()

        if (
            "time" in column_lower
            and "taken" in column_lower
        ):

            delivery_time_column = column

            break


# ============================================================
# CREATE DELIVERY TIME
# ============================================================

if delivery_time_column is not None:

    # Convert everything to string first
    # and extract the numeric part.

    df["Delivery_Time"] = (
        df[delivery_time_column]
        .astype(str)
        .str.extract(
            r"([-+]?\d*\.?\d+)",
            expand=False
        )
    )

    df["Delivery_Time"] = pd.to_numeric(
        df["Delivery_Time"],
        errors="coerce"
    )

else:

    df["Delivery_Time"] = np.nan


# ============================================================
# VALIDATE DELIVERY TIME
# ============================================================

valid_delivery_times = (
    df["Delivery_Time"]
    .notna()
    .sum()
)


# ============================================================
# DELIVERY TIME DEBUG
# ============================================================

with st.expander("⏱️ Delivery Time Debug Information"):

    st.write(
        "Detected delivery-time column:"
    )

    st.code(
        str(delivery_time_column)
    )

    st.write(
        "Valid delivery-time values:"
    )

    st.write(
        f"{valid_delivery_times:,} / {len(df):,}"
    )

    if delivery_time_column is not None:

        st.write(
            "Original values:"
        )

        st.dataframe(
            df[
                [delivery_time_column, "Delivery_Time"]
            ].head(10),
            use_container_width=True
        )


# ============================================================
# DISTANCE CALCULATION
# ============================================================

def calculate_distance(row):

    try:

        lat1 = float(
            row["Restaurant_latitude"]
        )

        lon1 = float(
            row["Restaurant_longitude"]
        )

        lat2 = float(
            row["Delivery_location_latitude"]
        )

        lon2 = float(
            row["Delivery_location_longitude"]
        )

        # Invalid coordinate check

        if (
            abs(lat1) > 90
            or abs(lat2) > 90
            or abs(lon1) > 180
            or abs(lon2) > 180
        ):

            return np.nan


        # Convert degrees to radians

        lat1 = np.radians(lat1)
        lon1 = np.radians(lon1)

        lat2 = np.radians(lat2)
        lon2 = np.radians(lon2)


        # Haversine formula

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (
            np.sin(dlat / 2) ** 2
            +
            np.cos(lat1)
            * np.cos(lat2)
            * np.sin(dlon / 2) ** 2
        )

        c = 2 * np.arcsin(
            np.sqrt(a)
        )

        earth_radius = 6371

        return earth_radius * c


    except Exception:

        return np.nan


# ============================================================
# CREATE DISTANCE
# ============================================================

location_columns = [
    "Restaurant_latitude",
    "Restaurant_longitude",
    "Delivery_location_latitude",
    "Delivery_location_longitude"
]


if all(
    column in df.columns
    for column in location_columns
):

    df["Distance_km"] = df.apply(
        calculate_distance,
        axis=1
    )

else:

    df["Distance_km"] = np.nan


# ============================================================
# REMOVE INVALID DISTANCES
# ============================================================

df.loc[
    df["Distance_km"] > 50,
    "Distance_km"
] = np.nan


# ============================================================
# CREATE DISRUPTION TARGET
# ============================================================

DISRUPTION_THRESHOLD = 32


df["Work_Disruption"] = np.where(
    df["Delivery_Time"].notna(),
    (
        df["Delivery_Time"]
        > DISRUPTION_THRESHOLD
    ).astype(int),
    np.nan
)


# ============================================================
# DATASET OVERVIEW
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">📁 Dataset Overview</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


# Total deliveries

with col1:

    st.metric(
        "Total Deliveries",
        f"{len(df):,}"
    )


# Features

with col2:

    st.metric(
        "Features",
        f"{len(df.columns):,}"
    )


# Average delivery time

with col3:

    if valid_delivery_times > 0:

        avg_time = (
            df["Delivery_Time"]
            .dropna()
            .mean()
        )

        st.metric(
            "Average Delivery Time",
            f"{avg_time:.2f} min"
        )

    else:

        st.metric(
            "Average Delivery Time",
            "N/A"
        )


# Average distance

with col4:

    valid_distance = (
        df["Distance_km"]
        .dropna()
    )

    if len(valid_distance) > 0:

        avg_distance = (
            valid_distance.mean()
        )

        st.metric(
            "Average Distance",
            f"{avg_distance:.2f} km"
        )

    else:

        st.metric(
            "Average Distance",
            "N/A"
        )


# ============================================================
# DATASET PREVIEW
# ============================================================

st.markdown(
    '<div class="section-title">🔍 Dataset Preview</div>',
    unsafe_allow_html=True
)


preview_columns = [
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
    "Time_taken(min)",
    "Delivery_Time",
    "Distance_km",
    "Work_Disruption"
]


preview_columns = [
    column
    for column in preview_columns
    if column in df.columns
]


st.dataframe(
    df[preview_columns].head(10),
    use_container_width=True
)


# ============================================================
# DELIVERY TIME ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">⏱️ Delivery Time Analysis</div>',
    unsafe_allow_html=True
)


delivery_time = (
    df["Delivery_Time"]
    .dropna()
)


if len(delivery_time) > 0:

    mean_time = delivery_time.mean()

    median_time = delivery_time.median()

    percentile_75 = delivery_time.quantile(0.75)

    percentile_90 = delivery_time.quantile(0.90)


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Mean",
            f"{mean_time:.2f} min"
        )


    with col2:

        st.metric(
            "Median",
            f"{median_time:.0f} min"
        )


    with col3:

        st.metric(
            "75th Percentile",
            f"{percentile_75:.0f} min"
        )


    with col4:

        st.metric(
            "90th Percentile",
            f"{percentile_90:.0f} min"
        )


    # --------------------------------------------------------
    # Delivery time histogram
    # --------------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(12, 5)
    )


    ax.hist(
        delivery_time,
        bins=30
    )


    ax.axvline(
        DISRUPTION_THRESHOLD,
        linestyle="--",
        linewidth=2,
        label="Disruption Threshold = 32 min"
    )


    ax.set_title(
        "Distribution of Delivery Time"
    )

    ax.set_xlabel(
        "Delivery Time (Minutes)"
    )

    ax.set_ylabel(
        "Number of Deliveries"
    )

    ax.legend()

    ax.grid(
        alpha=0.2
    )


    st.pyplot(fig)

    plt.close(fig)


else:

    st.error(
        "❌ No valid delivery-time values were detected."
    )


# ============================================================
# WORK DISRUPTION ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">⚠️ Work Disruption Analysis</div>',
    unsafe_allow_html=True
)


valid_disruption = (
    df["Work_Disruption"]
    .dropna()
)


normal_count = (
    valid_disruption == 0
).sum()


disruption_count = (
    valid_disruption == 1
).sum()


total_valid = (
    normal_count
    +
    disruption_count
)


if total_valid > 0:

    disruption_rate = (
        disruption_count
        /
        total_valid
    ) * 100

else:

    disruption_rate = 0


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Normal Deliveries",
        f"{normal_count:,}"
    )


with col2:

    st.metric(
        "Disrupted Deliveries",
        f"{disruption_count:,}"
    )


with col3:

    st.metric(
        "Disruption Rate",
        f"{disruption_rate:.2f}%"
    )


# ============================================================
# DISRUPTION CHART
# ============================================================

if total_valid > 0:

    disruption_chart = pd.DataFrame(
        {
            "Delivery Status": [
                "Normal",
                "Disruption"
            ],
            "Deliveries": [
                normal_count,
                disruption_count
            ]
        }
    )


    st.bar_chart(
        disruption_chart.set_index(
            "Delivery Status"
        )
    )


# ============================================================
# WEATHER ANALYSIS
# ============================================================

if (
    "Weatherconditions" in df.columns
    and len(delivery_time) > 0
):

    st.markdown(
        '<div class="section-title">🌦️ Weather vs Delivery Time</div>',
        unsafe_allow_html=True
    )


    weather_analysis = (
        df.groupby(
            "Weatherconditions",
            dropna=True
        )["Delivery_Time"]
        .mean()
        .sort_values(
            ascending=False
        )
    )


    st.bar_chart(
        weather_analysis
    )


# ============================================================
# TRAFFIC ANALYSIS
# ============================================================

if (
    "Road_traffic_density" in df.columns
    and len(delivery_time) > 0
):

    st.markdown(
        '<div class="section-title">🚦 Traffic vs Delivery Time</div>',
        unsafe_allow_html=True
    )


    traffic_analysis = (
        df.groupby(
            "Road_traffic_density",
            dropna=True
        )["Delivery_Time"]
        .mean()
        .sort_values(
            ascending=False
        )
    )


    st.bar_chart(
        traffic_analysis
    )


# ============================================================
# DISTANCE ANALYSIS
# ============================================================

if (
    df["Distance_km"].notna().sum() > 0
    and len(delivery_time) > 0
):

    st.markdown(
        '<div class="section-title">📍 Distance vs Delivery Time</div>',
        unsafe_allow_html=True
    )


    distance_df = df[
        [
            "Distance_km",
            "Delivery_Time"
        ]
    ].dropna()


    if len(distance_df) > 10000:

        distance_plot = (
            distance_df
            .sample(
                10000,
                random_state=42
            )
        )

    else:

        distance_plot = distance_df


    fig, ax = plt.subplots(
        figsize=(12, 5)
    )


    ax.scatter(
        distance_plot["Distance_km"],
        distance_plot["Delivery_Time"],
        alpha=0.25
    )


    ax.axhline(
        DISRUPTION_THRESHOLD,
        linestyle="--",
        linewidth=2,
        label="32 min threshold"
    )


    ax.set_title(
        "Delivery Distance vs Delivery Time"
    )

    ax.set_xlabel(
        "Distance (km)"
    )

    ax.set_ylabel(
        "Delivery Time (minutes)"
    )

    ax.legend()

    ax.grid(
        alpha=0.2
    )


    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# CITY ANALYSIS
# ============================================================

if (
    "City" in df.columns
    and len(delivery_time) > 0
):

    st.markdown(
        '<div class="section-title">🏙️ City-wise Delivery Analysis</div>',
        unsafe_allow_html=True
    )


    city_analysis = (
        df.groupby(
            "City",
            dropna=True
        )["Delivery_Time"]
        .agg(
            [
                "mean",
                "median",
                "count"
            ]
        )
        .sort_values(
            "mean",
            ascending=False
        )
    )


    city_analysis.columns = [
        "Average Delivery Time",
        "Median Delivery Time",
        "Number of Deliveries"
    ]


    st.dataframe(
        city_analysis,
        use_container_width=True
    )


# ============================================================
# VEHICLE CONDITION
# ============================================================

if (
    "Vehicle_condition" in df.columns
    and len(delivery_time) > 0
):

    st.markdown(
        '<div class="section-title">🛵 Vehicle Condition Analysis</div>',
        unsafe_allow_html=True
    )


    vehicle_analysis = (
        df.groupby(
            "Vehicle_condition",
            dropna=True
        )["Delivery_Time"]
        .mean()
        .sort_index()
    )


    st.bar_chart(
        vehicle_analysis
    )


# ============================================================
# FESTIVAL ANALYSIS
# ============================================================

if (
    "Festival" in df.columns
    and len(delivery_time) > 0
):

    st.markdown(
        '<div class="section-title">🎉 Festival Impact</div>',
        unsafe_allow_html=True
    )


    festival_analysis = (
        df.groupby(
            "Festival",
            dropna=True
        )["Delivery_Time"]
        .mean()
        .sort_values(
            ascending=False
        )
    )


    st.bar_chart(
        festival_analysis
    )


# ============================================================
# ORDER TIME ANALYSIS
# ============================================================

if (
    "Time_Orderd" in df.columns
    and len(delivery_time) > 0
):

    st.markdown(
        '<div class="section-title">🕐 Order Time vs Delivery Time</div>',
        unsafe_allow_html=True
    )


    def extract_hour(value):

        try:

            text = str(value).strip()

            if ":" in text:

                return int(
                    text.split(":")[0]
                )

            return np.nan

        except Exception:

            return np.nan


    df["Order_Hour"] = (
        df["Time_Orderd"]
        .apply(extract_hour)
    )


    hour_analysis = (
        df[
            [
                "Order_Hour",
                "Delivery_Time"
            ]
        ]
        .dropna()
        .groupby(
            "Order_Hour"
        )["Delivery_Time"]
        .mean()
    )


    st.line_chart(
        hour_analysis
    )


# ============================================================
# KEY INSIGHTS
# ============================================================

st.markdown(
    '<div class="section-title">💡 Key Insights</div>',
    unsafe_allow_html=True
)


# ------------------------------------------------------------
# Average delivery time
# ------------------------------------------------------------

if len(delivery_time) > 0:

    st.info(
        f"""
        📦 The average delivery time is
        **{delivery_time.mean():.2f} minutes**.
        """
    )


# ------------------------------------------------------------
# Average distance
# ------------------------------------------------------------

if len(valid_distance) > 0:

    st.info(
        f"""
        📍 The average cleaned delivery distance is
        **{valid_distance.mean():.2f} km**.
        """
    )


# ------------------------------------------------------------
# Disruption
# ------------------------------------------------------------

if total_valid > 0:

    st.warning(
        f"""
        ⚠️ **{disruption_rate:.2f}%**
        of valid deliveries exceed the
        **{DISRUPTION_THRESHOLD}-minute disruption threshold**.
        """
    )


# ------------------------------------------------------------
# Weather insight
# ------------------------------------------------------------

if (
    "Weatherconditions" in df.columns
    and len(delivery_time) > 0
):

    if len(weather_analysis) > 0:

        worst_weather = (
            weather_analysis.index[0]
        )

        worst_weather_time = (
            weather_analysis.iloc[0]
        )

        st.info(
            f"""
            🌦️ The weather category associated
            with the highest average delivery time is
            **{worst_weather}**
            ({worst_weather_time:.2f} minutes).
            """
        )


# ------------------------------------------------------------
# Traffic insight
# ------------------------------------------------------------

if (
    "Road_traffic_density" in df.columns
    and len(delivery_time) > 0
):

    if len(traffic_analysis) > 0:

        worst_traffic = (
            traffic_analysis.index[0]
        )

        worst_traffic_time = (
            traffic_analysis.iloc[0]
        )

        st.info(
            f"""
            🚦 The traffic category with the highest
            average delivery time is
            **{worst_traffic}**
            ({worst_traffic_time:.2f} minutes).
            """
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "GigShield | Delivery Work Disruption Risk Intelligence"
)