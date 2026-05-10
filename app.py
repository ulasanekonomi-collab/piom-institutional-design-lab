import streamlit as st
# =====================================
# SESSION STATE
# =====================================

if "problem" not in st.session_state:
    st.session_state.problem = ""

if "impact" not in st.session_state:
    st.session_state.impact = ""

if "bad_outcome" not in st.session_state:
    st.session_state.bad_outcome = ""
# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="PIOM Institutional Design Lab",
    layout="wide"
)

# =====================================
# SIDEBAR WORKFLOW
# =====================================

workflow = [
    "1. Problem Identification",
    "2. Institutional Diagnosis",
    "3. Root Cause Reflection",
    "4. Design Simulation",
    "5. Resistance Analysis",
    "6. Feasibility Projection",
    "7. Reflective Relevance",
    "8. Implementation Strategy",
    "9. Final Output"
]

st.sidebar.title("PIOM 2 Workflow")

selected_step = st.sidebar.radio(
    "Navigation",
    workflow
)

# =====================================
# HEADER
# =====================================

st.title("PIOM Institutional Design Lab")

st.markdown("""
Laboratorium desain kelembagaan untuk diagnosis,
simulasi, refleksi, dan rekayasa institusional.
""")

st.divider()

# =====================================
# MAIN PAGE
# =====================================

st.header(selected_step)

if selected_step == "1. Problem Identification":

    st.subheader("Describe the Problem")

    st.session_state.problem = st.text_area(
    "Apa masalah utama yang ingin dianalisis?",
    value=st.session_state.problem)

    st.session_state.impact = st.text_area(
    "Siapa yang terdampak?",
    value=st.session_state.impact)

    st.session_state.bad_outcome = st.text_area(
    "Outcome buruk apa yang muncul?",
    value=st.session_state.bad_outcome)

elif selected_step == "2. Institutional Diagnosis":

    st.subheader("Institutional Mapping")

    power_map = st.text_area(
        label="Siapa aktor dominan atau paling berpengaruh?",
        placeholder="contoh: pimpinan, elite birokrasi, vendor, kelompok senior"
    )

    institution_map = st.text_area(
        label="Aturan formal atau norma informal apa yang memperkuat masalah?",
        placeholder="contoh: SOP usang, budaya senioritas, aturan birokratis"
    )

    incentive_map = st.text_area(
        label="Insentif apa yang membuat perilaku bermasalah tetap bertahan?",
        placeholder="contoh: reward salah sasaran, keuntungan politik, kenyamanan status quo"
    )

    cost_map = st.text_area(
        label="Apa sumber transaction cost utama?",
        placeholder="contoh: koordinasi lambat, birokrasi panjang, data tidak terintegrasi"
    )

    behavior_map = st.text_area(
        label="Perilaku apa yang terus berulang dalam sistem?",
        placeholder="contoh: saling lempar tanggung jawab, keterlambatan, manipulasi laporan"
    )

    outcome_map = st.text_area(
        label="Outcome buruk apa yang terus diproduksi sistem?",
        placeholder="contoh: pelayanan lambat, konflik internal, distrust publik"
    )

elif selected_step == "3. Root Cause Reflection":

    st.subheader("Reflective Diagnosis")

    root_cause = st.text_area(
        label="Apa akar terdalam dari masalah ini?",
        placeholder="contoh: budaya patronase, ketakutan kehilangan posisi, struktur insentif yang salah"
    )

    reproduction = st.text_area(
        label="Mengapa masalah ini terus direproduksi dari waktu ke waktu?",
        placeholder="contoh: tidak ada hukuman, elite diuntungkan, organisasi terbiasa dengan pola lama"
    )

    blocked_change = st.text_area(
        label="Apa yang paling menghambat perubahan?",
        placeholder="contoh: resistensi elite, legitimasi budaya lama, ketergantungan sistem"
    )

    reflective_note = st.text_area(
        label="Refleksi kritis Anda terhadap sistem ini",
        placeholder="Apa yang sebenarnya sedang dipertahankan oleh sistem?"
    )

    st.info(
        "Tahap ini membantu pengguna memahami bahwa masalah kelembagaan biasanya diproduksi ulang oleh struktur insentif, relasi kekuasaan, dan budaya organisasi."
    )



elif selected_step == "4. Design Simulation":

    st.subheader("Simulation Engine")

    st.slider("Benefit / Incentive", 0, 10, 5)
    st.slider("Transaction Cost", 0, 10, 5)
    st.slider("Information / Framing", 0, 10, 5)
    st.slider("Normative Support", 0, 10, 5)

elif selected_step == "5. Resistance Analysis":

    st.subheader("Institutional Resistance")

    st.slider("Elite Resistance", 0, 10, 5)
    st.slider("Institutional Rigidity", 0, 10, 5)
    st.slider("Path Dependency", 0, 10, 5)

elif selected_step == "6. Feasibility Projection":

    st.subheader("Feasibility Analysis")

    st.info("Projection engine akan dikembangkan.")

elif selected_step == "7. Reflective Relevance":

    st.subheader("Problem–Design Alignment")

    st.write("""
    PIOM akan menjelaskan:
    - mengapa strategi relevan
    - akar masalah mana disentuh
    - masalah mana yang belum terselesaikan
    """)

elif selected_step == "8. Implementation Strategy":

    st.subheader("Implementation Strategy")

    st.write("""
    Strategi:
    - sequencing
    - coalition building
    - framing
    - institutional adaptation
    """)

elif selected_step == "9. Final Output":

    st.subheader("PIOM 2 Report")

    st.success("""
    PIOM 2 akan menghasilkan:
    - diagnosis
    - simulation
    - resistance profile
    - relevance reflection
    - implementation strategy
    """)
