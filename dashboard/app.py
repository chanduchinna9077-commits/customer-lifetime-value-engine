import streamlit as st

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Customer Lifetime Value Engine",
    page_icon="💰",
    layout="wide"
)

# ==========================
# TITLE
# ==========================

st.title("💰 Customer Lifetime Value Engine")

st.markdown(
    "Predict High Value Customers and Generate Business Recommendations"
)

st.divider()

# ==========================
# CUSTOMER INPUTS
# ==========================

st.header("Customer Information")

col1, col2 = st.columns(2)

with col1:

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        value=12
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

with col2:

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )

predict_button = st.button(
    "🚀 Predict Customer Value"
)

# ==========================
# RESULTS
# ==========================

if predict_button:

    # Dummy Logic
    # Replace with real model later

    if total_charges > 2000:

        prediction = "High Value Customer"
        probability = 92

        segment = "VIP Customer"

        recommendation = """
        Offer Premium Membership

        Assign Dedicated Support

        Upsell Additional Services
        """

    elif total_charges > 1000:

        prediction = "Potential High Value Customer"
        probability = 70

        segment = "Regular Customer"

        recommendation = """
        Recommend Additional Services

        Send Loyalty Rewards

        Increase Engagement
        """

    else:

        prediction = "Low Value Customer"
        probability = 35

        segment = "At Risk Customer"

        recommendation = """
        Offer Retention Discount

        Send Re-engagement Campaign

        Schedule Customer Outreach
        """

    # ==========================
    # PREDICTION
    # ==========================

    st.divider()

    st.header("Prediction Result")

    if probability >= 80:

        st.success(prediction)

    elif probability >= 50:

        st.warning(prediction)

    else:

        st.error(prediction)

    st.metric(
        "Probability",
        f"{probability}%"
    )

    # ==========================
    # SEGMENT
    # ==========================

    st.divider()

    st.header("Customer Segment")

    st.info(segment)

    # ==========================
    # RECOMMENDATION
    # ==========================

    st.divider()

    st.header("Business Recommendation")

    st.warning(recommendation)

    # ==========================
    # EXPLAINABILITY
    # ==========================

    st.divider()

    st.header("Model Explainability")

    st.write(
        """
        Top Factors:

        • Customer Tenure

        • Monthly Charges

        • Total Charges

        • Service Usage

        • Contract Type
        """
    )