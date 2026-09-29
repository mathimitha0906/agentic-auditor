import streamlit as st
from pathlib import Path

from core.document_processor import extract_text_from_pdf
from agents.compliance_agent import run_compliance_audit
from agents.financial_agent import run_financial_audit


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Agentic Auditor",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f5f7fb;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Main title */

    .main-title {
        font-size: 48px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 5px;
    }

    .main-subtitle {
        font-size: 18px;
        color: #64748b;
        margin-bottom: 25px;
    }

    /* Cards */

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 5px 20px rgba(15,23,42,0.06);
        margin-bottom: 20px;
    }

    .card-title {
        font-size: 20px;
        font-weight: 700;
        color: #111827;
    }

    .card-text {
        color: #64748b;
        font-size: 14px;
        line-height: 1.6;
    }

    /* Agent cards */

    .agent-name {
        font-size: 19px;
        font-weight: 700;
        color: #111827;
    }

    .agent-description {
        color: #64748b;
        font-size: 14px;
        line-height: 1.5;
    }

    /* Section */

    .section {
        font-size: 26px;
        font-weight: 750;
        color: #111827;
        margin-top: 25px;
        margin-bottom: 18px;
    }

    /* Status */

    .status {
        color: #16a34a;
        font-weight: 700;
        font-size: 13px;
    }

    /* Footer */

    .footer {
        text-align: center;
        color: #94a3b8;
        padding-top: 40px;
        padding-bottom: 20px;
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🛡️ Agentic Auditor")

    st.caption(
        "AI-powered document intelligence"
    )

    st.divider()

    st.markdown("### ⚙️ Audit Configuration")

    document_type = st.selectbox(
        "Document Type",
        [
            "Auto Detect",
            "Contract",
            "Invoice",
            "Contract + Invoice",
        ],
    )

    st.divider()

    st.markdown("### 🤖 AI Agent Network")

    st.markdown("🛡️ **Compliance Officer**")
    st.caption("Legal risk & clause analysis")

    st.markdown("💰 **Financial Auditor**")
    st.caption("Invoice & calculation verification")

    st.markdown("💬 **Client Communicator**")
    st.caption("Business-friendly recommendations")

    st.divider()

    st.caption(
        "HackNowa Global Hackathon 2026"
    )

    st.caption(
        "Future of Work & Automation"
    )


# ============================================================
# HERO
# ============================================================

st.markdown(
    '<div class="main-title">🛡️ Agentic Auditor</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="main-subtitle">'
    'Multi-Agent AI for intelligent contract and invoice auditing'
    '</div>',
    unsafe_allow_html=True,
)

st.info(
    "✦ AI-Powered   •   Multi-Agent   •   Automated Audit"
)


# ============================================================
# AGENT NETWORK
# ============================================================

st.markdown(
    '<div class="section">🤖 AI Agent Network</div>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
        <div class="card">

        <div style="font-size:35px;">🛡️</div>

        <div class="agent-name">
        Compliance Officer
        </div>

        <br>

        <div class="agent-description">
        Detects missing clauses, legal risks,
        ambiguous terms and compliance issues.
        </div>

        <br>

        <div class="status">
        ● READY
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col2:

    st.markdown(
        """
        <div class="card">

        <div style="font-size:35px;">💰</div>

        <div class="agent-name">
        Financial Auditor
        </div>

        <br>

        <div class="agent-description">
        Verifies quantities, line items,
        tax calculations and invoice totals.
        </div>

        <br>

        <div class="status">
        ● READY
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col3:

    st.markdown(
        """
        <div class="card">

        <div style="font-size:35px;">💬</div>

        <div class="agent-name">
        Client Communicator
        </div>

        <br>

        <div class="agent-description">
        Converts technical findings into
        clear business-friendly recommendations.
        </div>

        <br>

        <div class="status">
        ● READY
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# AUDIT WORKSPACE
# ============================================================

st.markdown(
    '<div class="section">📄 Audit Workspace</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="card">

    <div class="card-title">
    Upload your business document
    </div>

    <div class="card-text">
    Upload a contract, invoice or business document
    for multi-agent AI analysis.
    </div>

    </div>
    """,
    unsafe_allow_html=True,
)


uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf", "txt"],
)


# ============================================================
# PROCESS DOCUMENT
# ============================================================

document_text = ""


if uploaded_file is not None:

    st.success(
        f"📎 {uploaded_file.name} uploaded successfully"
    )

    extension = Path(
        uploaded_file.name
    ).suffix.lower()

    try:

        if extension == ".pdf":

            document_text = extract_text_from_pdf(
                uploaded_file
            )

        elif extension == ".txt":

            document_text = uploaded_file.read().decode(
                "utf-8"
            )

    except Exception as error:

        st.error(
            f"Document processing error: {error}"
        )


# ============================================================
# DOCUMENT INFORMATION
# ============================================================

if document_text.strip():

    st.markdown(
        '<div class="section">📊 Document Intelligence</div>',
        unsafe_allow_html=True,
    )

    word_count = len(
        document_text.split()
    )

    char_count = len(
        document_text
    )

    m1, m2, m3 = st.columns(3)

    with m1:

        st.metric(
            "Document Status",
            "READY",
        )

    with m2:

        st.metric(
            "Words Detected",
            word_count,
        )

    with m3:

        st.metric(
            "File Type",
            extension.upper().replace(".", ""),
        )

    with st.expander(
        "👁️ Preview Document"
    ):

        st.text_area(
            "Document Content",
            document_text,
            height=250,
            label_visibility="collapsed",
        )

    st.divider()

    # ========================================================
    # START AUDIT
    # ========================================================

    st.markdown(
        '<div class="section">⚡ AI Audit Engine</div>',
        unsafe_allow_html=True,
    )

    start_audit = st.button(
        "🚀 START MULTI-AGENT AI AUDIT",
        type="primary",
        use_container_width=True,
    )

    if start_audit:

        # ----------------------------------------------------
        # COMPLIANCE
        # ----------------------------------------------------

        with st.spinner(
            "🛡️ Compliance Officer is analyzing the document..."
        ):

            compliance_result = run_compliance_audit(
                document_text
            )

        st.success(
            "🛡️ Compliance analysis completed"
        )

        # ----------------------------------------------------
        # FINANCIAL
        # ----------------------------------------------------

        with st.spinner(
            "💰 Financial Auditor is verifying calculations..."
        ):

            financial_result = run_financial_audit(
                document_text
            )

        st.success(
            "💰 Financial verification completed"
        )

        # ----------------------------------------------------
        # RESULTS
        # ----------------------------------------------------

        st.divider()

        st.markdown(
            '<div class="section">📊 Audit Results</div>',
            unsafe_allow_html=True,
        )

        tab1, tab2, tab3 = st.tabs(
            [
                "🛡️ Compliance",
                "💰 Financial",
                "💬 Communication",
            ]
        )

        with tab1:

            st.subheader(
                "🛡️ Compliance Officer"
            )

            st.markdown(
                compliance_result
            )

        with tab2:

            st.subheader(
                "💰 Financial Auditor"
            )

            st.markdown(
                financial_result
            )

        with tab3:

            st.subheader(
                "💬 Client Communication"
            )

            st.info(
                "Client Communicator will be connected "
                "to the final orchestration layer next."
            )

        # ----------------------------------------------------
        # DOWNLOAD
        # ----------------------------------------------------

        st.divider()

        report = f"""
AGENTIC AUDITOR
MULTI-AGENT AI AUDIT REPORT

Document:
{uploaded_file.name}

Document Type:
{document_type}

========================================

COMPLIANCE AUDIT

{compliance_result}

========================================

FINANCIAL AUDIT

{financial_result}

========================================

Generated by Agentic Auditor
HackNowa Global Hackathon 2026
"""

        st.download_button(
            "📥 Download Audit Report",
            report,
            file_name="agentic_audit_report.txt",
            mime="text/plain",
            use_container_width=True,
        )


# ============================================================
# EMPTY STATE
# ============================================================

else:

    st.markdown(
        '<div class="section">🚀 Ready to Audit</div>',
        unsafe_allow_html=True,
    )

    st.info(
        "📄 Upload a PDF or TXT contract/invoice above "
        "to activate the AI agent network."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
    🛡️ Agentic Auditor
    &nbsp;•&nbsp;
    Future of Work & Automation
    &nbsp;•&nbsp;
    HackNowa Global Hackathon 2026
    </div>
    """,
    unsafe_allow_html=True,
)