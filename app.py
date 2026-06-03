import streamlit as st

from core.parser import extract_pdf_text
from core.analyser import analyze_contract
from core.risk_rules import run_rule_checks

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Clause Detective",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #F8FAFC;
}

.main-header {
    padding-bottom: 20px;
    border-bottom: 1px solid #CBD5E1;
    margin-bottom: 25px;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #1E3A5F;
    margin-bottom: 0px;
}

.subtitle {
    font-size: 18px;
    color: #64748B;
    margin-top: 0px;
}

.metric-container {
    background: white;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #E2E8F0;
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 8px;
    background-color: #2563EB;
    color: white;
    font-weight: 600;
    border: none;
}

.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="main-header">
    <div class="main-title">
        Clause Detective
    </div>
    <div class="subtitle">
        AI-Powered Contract Review Platform
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("Clause Detective")

    st.divider()

    st.markdown("### Platform Capabilities")

    st.write("• Contract Analysis")
    st.write("• Risk Assessment")
    st.write("• Missing Clause Detection")
    st.write("• AI Recommendations")
    st.write("• Contract Health Scoring")

# --------------------------------------------------
# OVERVIEW
# --------------------------------------------------

st.info(
    """
Upload a contract to identify legal risks, detect missing provisions,
and receive AI-generated recommendations for improvement.
"""
)

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Contract (PDF)",
    type=["pdf"]
)

# --------------------------------------------------
# MAIN WORKFLOW
# --------------------------------------------------

if uploaded_file:

    text = extract_pdf_text(uploaded_file)

    st.success("Contract uploaded successfully.")

    tab1, tab2 = st.tabs(
        [
            "Contract",
            "Analysis Report"
        ]
    )

    # ----------------------------------------------
    # CONTRACT TAB
    # ----------------------------------------------

    with tab1:

        st.subheader("Contract Content")

        st.text_area(
            "",
            text,
            height=500
        )

    # ----------------------------------------------
    # ANALYSIS TAB
    # ----------------------------------------------

    with tab2:

        if st.button("Analyze Contract"):

            with st.spinner("Running contract analysis..."):

                analysis = analyze_contract(text)

            rule_results = run_rule_checks(text)

            high_risk = sum(
                1 for item in rule_results
                if item["risk"] == "High"
            )

            medium_risk = sum(
                1 for item in rule_results
                if item["risk"] == "Medium"
            )

            score = max(
                100 - (high_risk * 15) - (medium_risk * 10),
                0
            )

            # ------------------------------------------
            # DASHBOARD METRICS
            # ------------------------------------------

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Contract Health",
                    f"{score}/100"
                )

            with col2:
                st.metric(
                    "High Risk Findings",
                    high_risk
                )

            with col3:
                st.metric(
                    "Medium Risk Findings",
                    medium_risk
                )

            st.progress(score / 100)

            st.divider()

            # ------------------------------------------
            # AI REPORT
            # ------------------------------------------

            st.subheader("AI Analysis Report")

            st.markdown(analysis)

            st.divider()

            # ------------------------------------------
            # RULE CHECKS
            # ------------------------------------------

            st.subheader("Rule-Based Findings")

            if rule_results:

                for item in rule_results:

                    if item["risk"] == "High":

                        st.error(
                            f"HIGH RISK — {item['issue']}"
                        )

                    elif item["risk"] == "Medium":

                        st.warning(
                            f"MEDIUM RISK — {item['issue']}"
                        )

                    else:

                        st.info(
                            f"LOW RISK — {item['issue']}"
                        )

            else:

                st.success(
                    "No missing clauses detected."
                )
