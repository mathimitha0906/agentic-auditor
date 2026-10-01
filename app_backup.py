import streamlit as st
from core.orchestrator import run_full_audit
import re
import io

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Agentic Auditor",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 0%, rgba(37,99,235,.18), transparent 28%),
        radial-gradient(circle at 90% 10%, rgba(124,58,237,.16), transparent 25%),
        #050b16;
    color: #f8fafc;
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* HERO */

.hero {
    text-align: center;
    padding: 35px 20px 40px;
}

.hero-title {
    font-size: 52px;
    font-weight: 900;
    letter-spacing: -2px;
    margin-bottom: 10px;
}

.hero-subtitle {
    font-size: 20px;
    color: #94a3b8;
    margin-bottom: 20px;
}

.hero-badge {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 999px;
    background: rgba(37,99,235,.12);
    border: 1px solid rgba(96,165,250,.35);
    color: #60a5fa;
    font-size: 13px;
    font-weight: 800;
}

/* SECTION */

.section-title {
    font-size: 27px;
    font-weight: 850;
    margin: 25px 0 18px;
}

/* AGENT CARDS */

.agent-card {
    background: linear-gradient(
        145deg,
        rgba(15,27,45,.98),
        rgba(8,18,33,.98)
    );

    border: 1px solid #24344d;
    border-radius: 22px;
    padding: 26px;
    min-height: 235px;

    box-shadow:
        0 15px 40px rgba(0,0,0,.22);
}

.agent-icon {
    font-size: 40px;
    margin-bottom: 12px;
}

.agent-name {
    font-size: 21px;
    font-weight: 850;
}

.agent-description {
    color: #94a3b8;
    font-size: 14px;
    line-height: 1.6;
    margin-top: 10px;
}

.ready {
    margin-top: 20px;
    color: #4ade80;
    font-size: 12px;
    font-weight: 900;
}

/* WORKSPACE */

.workspace {
    margin-top: 38px;
    background: linear-gradient(
        145deg,
        rgba(11,23,40,.98),
        rgba(7,16,29,.98)
    );

    border: 1px solid #26364d;
    border-radius: 24px;
    padding: 30px;
}

.workspace-title {
    font-size: 28px;
    font-weight: 850;
}

.workspace-subtitle {
    color: #94a3b8;
    margin-top: 7px;
}

/* UPLOAD */

.upload-card {
    background: rgba(15,27,45,.95);
    border: 1px solid #26364d;
    border-radius: 20px;
    padding: 22px;
    min-height: 130px;
}

.upload-title {
    font-size: 20px;
    font-weight: 850;
}

.upload-description {
    color: #94a3b8;
    font-size: 14px;
    margin-top: 7px;
}

/* BUTTON */

.stButton > button {
    border-radius: 13px;
    font-weight: 850;
    min-height: 50px;
}

/* AUDIT HEADER */

.audit-header {
    margin-top: 42px;
    margin-bottom: 24px;
    padding: 28px;
    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            rgba(30,41,59,.95),
            rgba(15,23,42,.98)
        );

    border: 1px solid #334155;
}

.audit-header-title {
    font-size: 31px;
    font-weight: 900;
}

.audit-header-subtitle {
    color: #94a3b8;
    margin-top: 6px;
}

/* METRICS */

.metric-card {
    background: #0b1525;
    border: 1px solid #26364d;
    border-radius: 18px;
    padding: 22px;
    min-height: 125px;
}

.metric-label {
    color: #94a3b8;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
}

.metric-value {
    font-size: 28px;
    font-weight: 900;
    margin-top: 10px;
}

.risk-high,
.mismatch {
    color: #f87171;
}

.risk-medium {
    color: #fbbf24;
}

.risk-low,
.verified {
    color: #4ade80;
}

/* REPORT BOX */

.finding-box {
    background: #0b1525;
    border: 1px solid #26364d;
    border-radius: 19px;
    padding: 22px;
    margin-top: 22px;
}

.finding-title {
    font-size: 21px;
    font-weight: 850;
}

.finding-description {
    color: #94a3b8;
    line-height: 1.6;
    margin-top: 6px;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 60px;
    padding: 28px;
    border-top: 1px solid #172337;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-title">
        🛡️ Agentic Auditor
    </div>

    <div class="hero-subtitle">
        Multi-Agent AI for intelligent contract and invoice auditing
    </div>

    <div class="hero-badge">
        ✦ AI-Powered &nbsp;•&nbsp;
        Multi-Agent &nbsp;•&nbsp;
        Cross-Document Audit
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# AI AGENT NETWORK
# =========================================================

st.markdown(
    '<div class="section-title">🤖 AI Agent Network</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="agent-card">

        <div class="agent-icon">🛡️</div>

        <div class="agent-name">
            Compliance Officer
        </div>

        <div class="agent-description">
            Detects missing clauses, legal risks,
            ambiguous terms and compliance issues.
        </div>

        <div class="ready">
            ● READY
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown("""
    <div class="agent-card">

        <div class="agent-icon">💰</div>

        <div class="agent-name">
            Financial Auditor
        </div>

        <div class="agent-description">
            Verifies quantities, line items,
            tax calculations and invoice totals.
        </div>

        <div class="ready">
            ● READY
        </div>

    </div>
    """, unsafe_allow_html=True)


with col3:
    st.markdown("""
    <div class="agent-card">

        <div class="agent-icon">💬</div>

        <div class="agent-name">
            Client Communicator
        </div>

        <div class="agent-description">
            Converts technical findings into
            clear business-friendly recommendations.
        </div>

        <div class="ready">
            ● READY
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# AUDIT WORKSPACE
# =========================================================

st.markdown("""
<div class="workspace">

    <div class="workspace-title">
        📄 Audit Workspace
    </div>

    <div class="workspace-subtitle">
        Upload the contract and invoice separately.
        The AI system will compare both documents.
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# UPLOAD COLUMNS
# =========================================================

contract_col, invoice_col = st.columns(2)

with contract_col:

    st.markdown("""
    <div class="upload-card">

        <div class="upload-title">
            📄 Contract
        </div>

        <div class="upload-description">
            Upload the service agreement or contract.
        </div>

    </div>
    """, unsafe_allow_html=True)

    contract_file = st.file_uploader(
        "Upload Contract",
        type=["txt", "pdf"],
        key="contract_file",
        label_visibility="collapsed"
    )


with invoice_col:

    st.markdown("""
    <div class="upload-card">

        <div class="upload-title">
            🧾 Invoice
        </div>

        <div class="upload-description">
            Upload the corresponding invoice.
        </div>

    </div>
    """, unsafe_allow_html=True)

    invoice_file = st.file_uploader(
        "Upload Invoice",
        type=["txt", "pdf"],
        key="invoice_file",
        label_visibility="collapsed"
    )


# =========================================================
# FILE READER
# =========================================================

def read_file(uploaded_file):

    if uploaded_file is None:
        return ""

    filename = uploaded_file.name.lower()

    if filename.endswith(".txt"):

        return uploaded_file.read().decode(
            "utf-8",
            errors="ignore"
        )

    if filename.endswith(".pdf"):

        try:

            import PyPDF2

            reader = PyPDF2.PdfReader(uploaded_file)

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            return text

        except Exception as e:

            st.error(
                f"PDF reading failed: {e}"
            )

            return ""

    return ""


# =========================================================
# RESULT HELPERS
# =========================================================

def extract_risk(text):

    match = re.search(
        r"Overall Risk\s*:\s*(HIGH|MEDIUM|LOW)",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).upper()

    return "REVIEW"


def extract_financial_status(text):

    matches = re.findall(
        r"Financial Status\s*:\s*(VERIFIED|MISMATCH|INCOMPLETE)",
        text,
        re.IGNORECASE
    )

    if matches:
        return matches[-1].upper()

    return "REVIEW"


def count_issues(text):

    return len(
        re.findall(
            r"(?:^|\n)\s*\d+\.\s*\[",
            text or ""
        )
    )


def metric_class(value):

    value = value.upper()

    if value == "HIGH":
        return "risk-high"

    if value == "MEDIUM":
        return "risk-medium"

    if value in ["LOW", "VERIFIED"]:
        return "verified"

    if value == "MISMATCH":
        return "mismatch"

    return ""


# =========================================================
# AUDIT BUTTON
# =========================================================

if contract_file and invoice_file:

    st.success(
        "✅ Both documents uploaded successfully."
    )

    st.markdown("")

    start_audit = st.button(
        "🚀 START CROSS-DOCUMENT AI AUDIT",
        type="primary",
        use_container_width=True
    )

    if start_audit:

        contract_text = read_file(contract_file)
        invoice_text = read_file(invoice_file)

        if not contract_text.strip():

            st.error(
                "❌ Contract file is empty."
            )

        elif not invoice_text.strip():

            st.error(
                "❌ Invoice file is empty."
            )

        else:

            progress = st.progress(0)
            status = st.empty()

            try:

                status.info(
                    "🛡️ Compliance Officer is analysing..."
                )

                progress.progress(25)

                result = run_full_audit(
                    contract_text,
                    invoice_text
                )

                progress.progress(65)

                status.info(
                    "💰 Financial Auditor is verifying..."
                )

                progress.progress(80)

                status.info(
                    "💬 Client Communicator is preparing recommendations..."
                )

                progress.progress(95)

                progress.progress(100)

                status.success(
                    "✅ Multi-agent audit completed successfully."
                )

                st.session_state["audit_result"] = result

            except TypeError:

                try:

                    combined_text = (
                        "CONTRACT\n"
                        "====================\n"
                        + contract_text
                        + "\n\nINVOICE\n"
                        "====================\n"
                        + invoice_text
                    )

                    result = run_full_audit(
                        combined_text
                    )

                    progress.progress(100)

                    status.success(
                        "✅ Multi-agent audit completed successfully."
                    )

                    st.session_state["audit_result"] = result

                except Exception as e:

                    progress.empty()
                    status.empty()

                    st.error(
                        f"❌ Audit failed: {e}"
                    )

            except Exception as e:

                progress.empty()
                status.empty()

                st.error(
                    f"❌ Audit failed: {e}"
                )


elif contract_file:

    st.info(
        "🧾 Please upload the invoice also."
    )


elif invoice_file:

    st.info(
        "📄 Please upload the contract also."
    )


else:

    st.info(
        "📄 Upload a contract and 🧾 invoice "
        "to activate the cross-document AI audit."
    )


# =========================================================
# FINAL REPORT
# =========================================================

if "audit_result" in st.session_state:

    result = st.session_state["audit_result"]

    st.markdown("""
    <div class="audit-header">

        <div class="audit-header-title">
            📊 Final Audit Report
        </div>

        <div class="audit-header-subtitle">
            Cross-document analysis completed by the
            Agentic Auditor multi-agent network.
        </div>

    </div>
    """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # EXTRACT RESULTS
    # -----------------------------------------------------

    if isinstance(result, dict):

        compliance = result.get(
            "compliance",
            ""
        )

        financial = result.get(
            "financial",
            ""
        )

        communication = result.get(
            "communication",
            ""
        )

        summary = result.get(
            "summary",
            ""
        )

    else:

        compliance = ""
        financial = ""
        communication = ""
        summary = str(result)


    risk = extract_risk(
        str(compliance)
    )

    financial_status = extract_financial_status(
        str(financial)
    )

    issue_count = (
        count_issues(str(compliance))
        +
        count_issues(str(financial))
    )


    # -----------------------------------------------------
    # METRICS
    # -----------------------------------------------------

    m1, m2, m3 = st.columns(3)


    with m1:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    Overall Risk
                </div>

                <div class="metric-value {metric_class(risk)}">
                    {risk}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with m2:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    Financial Status
                </div>

                <div class="metric-value {metric_class(financial_status)}">
                    {financial_status}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with m3:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    Issues Detected
                </div>

                <div class="metric-value">
                    {issue_count}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # COMPLIANCE
    # =====================================================

    if compliance:

        st.markdown("""
        <div class="finding-box">

            <div class="finding-title">
                🛡️ Compliance Findings
            </div>

            <div class="finding-description">
                Contract risks, missing clauses,
                ambiguous terms and compliance observations.
            </div>

        </div>
        """, unsafe_allow_html=True)

        with st.expander(
            "View Compliance Officer Report",
            expanded=True
        ):

            st.markdown(
                compliance
            )


    # =====================================================
    # FINANCIAL
    # =====================================================

    if financial:

        st.markdown("""
        <div class="finding-box">

            <div class="finding-title">
                💰 Financial Verification
            </div>

            <div class="finding-description">
                Invoice calculations, tax verification,
                line-item checks and amount consistency.
            </div>

        </div>
        """, unsafe_allow_html=True)

        with st.expander(
            "View Financial Auditor Report",
            expanded=True
        ):

            st.markdown(
                financial
            )


    # =====================================================
    # COMMUNICATION
    # =====================================================

    if communication:

        st.markdown("""
        <div class="finding-box">

            <div class="finding-title">
                💬 Business Recommendations
            </div>

            <div class="finding-description">
                Clear business-friendly explanation
                of the audit findings.
            </div>

        </div>
        """, unsafe_allow_html=True)

        with st.expander(
            "View Client Communicator Report",
            expanded=True
        ):

            st.markdown(
                communication
            )


    # =====================================================
    # UNIFIED REPORT
    # =====================================================

    if summary:

        st.markdown("""
        <div class="finding-box">

            <div class="finding-title">
                📋 Unified Audit Report
            </div>

            <div class="finding-description">
                Consolidated output from the
                multi-agent audit workflow.
            </div>

        </div>
        """, unsafe_allow_html=True)

        with st.expander(
            "View Unified Report",
            expanded=False
        ):

            st.markdown(
                summary
            )


    # =====================================================
    # DOWNLOAD REPORT
    # =====================================================

    full_report = ""

    report_sections = [

        (
            "COMPLIANCE OFFICER REPORT",
            compliance
        ),

        (
            "FINANCIAL AUDITOR REPORT",
            financial
        ),

        (
            "CLIENT COMMUNICATOR REPORT",
            communication
        ),

        (
            "UNIFIED AUDIT REPORT",
            summary
        )

    ]


    for title, content in report_sections:

        if content:

            full_report += (
                "=" * 60
                + "\n"
                + title
                + "\n"
                + "=" * 60
                + "\n\n"
                + str(content)
                + "\n\n"
            )


    if full_report.strip():

        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )

        st.download_button(
            "📥 DOWNLOAD AUDIT REPORT",
            data=full_report,
            file_name="agentic_auditor_report.txt",
            mime="text/plain",
            use_container_width=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    🛡️ <b>Agentic Auditor</b>
    &nbsp; • &nbsp;
    Future of Work & Automation
    &nbsp; • &nbsp;
    HackNowa Global Hackathon 2026

    <br><br>

    Multi-Agent AI for intelligent business document auditing

</div>
""", unsafe_allow_html=True)