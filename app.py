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

    # INITIALIZE SESSION STATE
    if "power_map" not in st.session_state:
        st.session_state.power_map = ""

    if "institution_map" not in st.session_state:
        st.session_state.institution_map = ""

    if "incentive_map" not in st.session_state:
        st.session_state.incentive_map = ""

    if "cost_map" not in st.session_state:
        st.session_state.cost_map = ""

    if "behavior_map" not in st.session_state:
        st.session_state.behavior_map = ""

    if "outcome_map" not in st.session_state:
        st.session_state.outcome_map = ""

    # TEXT AREAS

    st.session_state.power_map = st.text_area(
        label="Siapa aktor dominan atau paling berpengaruh?",
        value=st.session_state.power_map,
        placeholder="contoh: pimpinan, elite birokrasi, vendor, kelompok senior"
    )

    st.session_state.institution_map = st.text_area(
        label="Aturan formal atau norma informal apa yang memperkuat masalah?",
        value=st.session_state.institution_map,
        placeholder="contoh: SOP usang, budaya senioritas, aturan birokratis"
    )

    st.session_state.incentive_map = st.text_area(
        label="Insentif apa yang membuat perilaku bermasalah tetap bertahan?",
        value=st.session_state.incentive_map,
        placeholder="contoh: reward salah sasaran, keuntungan politik, kenyamanan status quo"
    )

    st.session_state.cost_map = st.text_area(
        label="Apa sumber transaction cost utama?",
        value=st.session_state.cost_map,
        placeholder="contoh: koordinasi lambat, birokrasi panjang, data tidak terintegrasi"
    )

    st.session_state.behavior_map = st.text_area(
        label="Perilaku apa yang terus berulang dalam sistem?",
        value=st.session_state.behavior_map,
        placeholder="contoh: saling lempar tanggung jawab, keterlambatan, manipulasi laporan"
    )

    st.session_state.outcome_map = st.text_area(
        label="Outcome buruk apa yang terus diproduksi sistem?",
        value=st.session_state.outcome_map,
        placeholder="contoh: pelayanan lambat, konflik internal, distrust publik"
    )

elif selected_step == "3. Root Cause Reflection":

    st.subheader("Reflective Diagnosis")

    # INITIALIZE SESSION STATE

    if "root_cause" not in st.session_state:
        st.session_state.root_cause = ""

    if "reproduction" not in st.session_state:
        st.session_state.reproduction = ""

    if "blocked_change" not in st.session_state:
        st.session_state.blocked_change = ""

    if "reflective_note" not in st.session_state:
        st.session_state.reflective_note = ""

    # REFLECTIVE QUESTIONS

    st.session_state.root_cause = st.text_area(
        label="Apa akar terdalam dari masalah ini?",
        value=st.session_state.root_cause,
        placeholder="contoh: budaya patronase, struktur insentif salah, ketergantungan politik"
    )

    st.session_state.reproduction = st.text_area(
        label="Mengapa masalah ini terus direproduksi dari waktu ke waktu?",
        value=st.session_state.reproduction,
        placeholder="contoh: elite diuntungkan, organisasi terbiasa, tidak ada hukuman efektif"
    )

    st.session_state.blocked_change = st.text_area(
        label="Apa yang paling menghambat perubahan?",
        value=st.session_state.blocked_change,
        placeholder="contoh: resistensi elite, legitimasi budaya lama, ketakutan kehilangan posisi"
    )

    st.session_state.reflective_note = st.text_area(
        label="Refleksi kritis Anda terhadap sistem ini",
        value=st.session_state.reflective_note,
        placeholder="Apa yang sebenarnya sedang dipertahankan oleh sistem?"
    )

    st.info(
        """
        Tahap refleksi membantu pengguna memahami bahwa masalah kelembagaan
        biasanya diproduksi ulang oleh relasi kekuasaan, struktur insentif,
        budaya organisasi, dan resistensi terhadap perubahan.
        """
    )
    
elif selected_step == "4. Design Simulation":

    st.subheader("Institutional Design Simulation")

    # INITIALIZE SESSION STATE

    if "benefit_score" not in st.session_state:
        st.session_state.benefit_score = 5

    if "cost_score" not in st.session_state:
        st.session_state.cost_score = 5

    if "information_score" not in st.session_state:
        st.session_state.information_score = 5

    if "normative_score" not in st.session_state:
        st.session_state.normative_score = 5

    # SLIDERS

    st.session_state.benefit_score = st.slider(
        "Benefit / Incentive",
        0,
        10,
        5
    )

    st.session_state.cost_score = st.slider(
        "Transaction Cost",
        0,
        10,
        5
    )

    st.session_state.information_score = st.slider(
        "Information / Framing",
        0,
        10,
        5
    )

    st.session_state.normative_score = st.slider(
        "Normative / Moral Support",
        0,
       10,
       5
    )

    st.session_state.cost_score = st.slider(
        "Transaction Cost",
        0, 10,
        st.session_state.cost_score
    )

    st.session_state.information_score = st.slider(
        "Information / Framing",
        0, 10,
        st.session_state.information_score
    )

    st.session_state.normative_score = st.slider(
        "Normative / Moral Support",
        0, 10,
        st.session_state.normative_score
    )

    # BEHAVIORAL EQUATION

    behavior_score = (
        st.session_state.benefit_score
        + st.session_state.information_score
        + st.session_state.normative_score
        - st.session_state.cost_score
    )

    # NORMALIZATION

    normalized_score = behavior_score + 10

    probability_change = int(
    (normalized_score / 40) * 100
    )
    st.divider()

    st.subheader("Behavioral Projection")

    st.metric(
        "Probability of Behavioral Change",
        f"{probability_change}%"
    )

    # INTERPRETATION

    if probability_change <= 30:

        st.error(
            "Desain kelembagaan masih lemah dalam mendorong perubahan perilaku."
        )

    elif probability_change <= 70:

        st.warning(
            "Perubahan perilaku mungkin terjadi, tetapi masih membutuhkan dukungan institusional tambahan."
        )

    else:

        st.success(
            "Desain kelembagaan cukup kuat untuk mendorong perubahan perilaku."
        )

    st.info(
        """
        Simulasi ini membantu pengguna memahami bagaimana perubahan insentif,
        biaya transaksi, framing informasi, dan dukungan normatif
        dapat memengaruhi kemungkinan perubahan perilaku.
        """
    )

elif selected_step == "5. Resistance Analysis":

    st.subheader("Institutional Resistance Analysis")

    # AMBIL DATA DARI SIMULATION

    benefit = st.session_state.benefit_score
    cost = st.session_state.cost_score
    information = st.session_state.information_score
    normative = st.session_state.normative_score

    # RESISTANCE COMPONENTS

    incentive_resistance = 10 - benefit
    administrative_resistance = cost
    perception_resistance = 10 - information
    cultural_resistance = 10 - normative

    # TOTAL RESISTANCE

    resistance_score = (
        incentive_resistance
        + administrative_resistance
        + perception_resistance
        + cultural_resistance
    ) / 4

    st.metric(
        "Institutional Resistance Score",
        round(resistance_score, 2)
    )

    st.divider()

    st.subheader("Resistance Interpretation")

    # INTERPRETATION

    if resistance_score <= 3:

        st.success(
            "Resistensi kelembagaan relatif rendah dan sistem mulai mendukung perubahan."
        )

    elif resistance_score <= 6:

        st.warning(
            "Resistensi kelembagaan masih cukup kuat dan reformasi membutuhkan dukungan tambahan."
        )

    else:

        st.error(
            "Resistensi sistemik masih tinggi dan berpotensi menghambat implementasi perubahan."
        )

    st.divider()

    st.subheader("Institutional Reading")

    # DYNAMIC READING

    if incentive_resistance >= 7:

        st.write(
            "- Sistem masih memberi keuntungan pada perilaku lama."
        )

    if administrative_resistance >= 7:

        st.write(
            "- Hambatan birokrasi dan koordinasi masih tinggi."
        )

    if perception_resistance >= 7:

        st.write(
            "- Framing dan legitimasi perubahan masih lemah."
        )

    if cultural_resistance >= 7:

        st.write(
            "- Norma dan budaya kelembagaan belum mendukung perubahan."
        )

    st.info(
        """
        Resistance Analysis membantu pengguna memahami bahwa
        hambatan perubahan biasanya berasal dari kombinasi
        insentif lama, budaya organisasi, hambatan administratif,
        dan legitimasi perubahan yang belum kuat.
        """
    )

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
