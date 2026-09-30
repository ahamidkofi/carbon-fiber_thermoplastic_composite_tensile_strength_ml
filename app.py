import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Carbon Fiber Composite Tensile Strength Predictor",
    page_icon="🔬",
    layout="centered"
)


# --------------------------------------------------
# Load trained model
# --------------------------------------------------

model = joblib.load(
    "models/xgboost_tensile_strength_model.joblib"
)


# --------------------------------------------------
# Title and project description
# --------------------------------------------------

st.title("Carbon Fiber Thermoplastic Composite")
st.subheader("Tensile Strength Predictor")

st.write(
    "This research prototype predicts the tensile strength of "
    "carbon-fiber/polysulfone (PSU) thermoplastic composite specimens "
    "using experimentally measured material, processing, and specimen "
    "characteristics."
)


# --------------------------------------------------
# Material information
# --------------------------------------------------

st.info(
    "**PSU (Polysulfone):** a high-performance thermoplastic polymer "
    "used as the matrix material in the carbon-fiber composite. "
    "The source group represents the experimental group associated "
    "with the PSU solution concentration used during composite preparation."
)


# --------------------------------------------------
# Input section
# --------------------------------------------------

st.header("Specimen Information")

source_group = st.selectbox(
    "PSU Solution Concentration / Source Group (%)",
    [20, 30, 40],
    help=(
        "Select the experimental source group corresponding to the "
        "PSU (polysulfone) solution concentration used during "
        "composite preparation."
    )
)

fiber_concentration = st.number_input(
    "Carbon Fiber Concentration (%)",
    min_value=0.0,
    max_value=100.0,
    value=60.0,
    step=0.1,
    help=(
        "Carbon fiber concentration associated with the composite "
        "specimen."
    )
)

specimen_length = st.number_input(
    "Specimen Length (mm)",
    min_value=0.0,
    value=100.0,
    step=0.1,
    help=(
        "Length of the composite specimen used in the experiment."
    )
)

specimen_mass = st.number_input(
    "Specimen Mass (mg)",
    min_value=0.0,
    value=100.0,
    step=0.1,
    help=(
        "Measured mass of the composite specimen."
    )
)

composite_diameter = st.number_input(
    "Composite Diameter (mm)",
    min_value=0.0,
    value=1.0,
    step=0.01,
    help=(
        "Measured diameter of the composite specimen."
    )
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict Tensile Strength"):

    input_data = pd.DataFrame({
        "source_group_pct": [source_group],
        "fiber_concentration_pct": [fiber_concentration],
        "specimen_length_mm": [specimen_length],
        "specimen_mass_mg": [specimen_mass],
        "composite_diameter_mm": [composite_diameter]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Tensile Strength: {prediction:.2f} MPa"
    )

    st.caption(
        "This prediction is intended as a research screening estimate "
        "within the range represented by the experimental dataset."
    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Developed and deployed by Hamid Kofi Abdul | "
    "Machine Learning for Carbon-Fiber/Polysulfone Composites"
)