import streamlit as st

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="PIOM Institutional Design Lab",
    layout="wide"
)

# ====================================
# HEADER
# ====================================

col1, col2 = st.columns([1,5])

with col1:
    st.image(
        "https://raw.githubusercontent.com/ulasanekonomi-collab/piom/main/Yuhka-Sundaya.jpg",
        width=120
    )

with col2:
    st.title("PIOM Institutional Design Lab")
    st.caption(
        "Experimental Laboratory for Political Economy and Institutional Engineering"
    )

# ====================================
# SIDEBAR
# ====================================

st.sidebar.title("PIOM Lab Flow")

menu = st.sidebar.radio(
    "Workflow",
    [
        "Problem Input",
        "Institutional Diagnosis",
        "Parameter Mapping",
        "Simulation Engine",
        "Resistance Analysis",
        "Design Recommendation",
        "Policy Output"
    ]
)

# ====================================
# PAGE CONTENT
# ====================================

if menu == "Problem Input":

    st.header("Problem Input")

    problem = st.text_area(
        "Describe institutional or political-economic problem"
    )

    st.info(
        "PIOM will transform the problem into institutional variables for simulation."
    )

elif menu == "Institutional Diagnosis":

    st.header("Institutional Diagnosis")

    st.write("Power structure")
    st.write("Institutional rules")
    st.write("Incentive system")
    st.write("Behavioral consequences")

elif menu == "Parameter Mapping":

    st.header("Parameter Mapping")

    st.slider("Benefit / Incentive", 0, 10, 5)
    st.slider("Transaction Cost", 0, 10, 5)
    st.slider("Information / Framing", 0, 10, 5)
    st.slider("Normative Support", 0, 10, 5)

elif menu == "Simulation Engine":

    st.header("Simulation Engine")

    st.markdown(
        """
        ## Behavioral Equation

        S = B + I + N - C
        """
    )

    st.success("Simulation engine will estimate probability of behavioral change.")

elif menu == "Resistance Analysis":

    st.header("Resistance Analysis")

    st.slider("Elite Resistance", 0, 10, 5)
    st.slider("Institutional Rigidity", 0, 10, 5)
    st.slider("Status Quo Dependency", 0, 10, 5)

elif menu == "Design Recommendation":

    st.header("Design Recommendation")

    st.write("Recommended institutional redesign:")
    st.write("- redesign incentive")
    st.write("- reduce transaction cost")
    st.write("- improve information framing")
    st.write("- coalition strategy")

elif menu == "Policy Output":

    st.header("Policy Output")

    st.success(
        "PIOM Institutional Design Lab generates policy-oriented institutional redesign."
    )
