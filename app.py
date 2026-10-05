import streamlit as st
from core.orchestrator import run_full_audit
from audit_history import save_audit, load_history
import re
import io
import html

st.set_page_config(
    page_title="Agentic Auditor",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# STYLE
# =========================================================

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 10% 0%, rgba(37,99,235,.16), transparent 28%),
        radial-gradient(circle at 90% 10%, rgba(124,58,237,.13), transparent 25%),
        #050b16;
    color: #f8fafc;
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    text-align: center;
    padding: 28px 20px 35px;
}

.hero-title {
    font-size: 50px;
    font-weight: 850;
    letter-spacing: -1.5px;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 19px;
    color: #94a3b8;
    margin-bottom: 18px;
}

.hero-badge {
    display: inline-block;
    padding: 9px 18px;
    border-radius: 999px;
    background: rgba(37,99,235,.10);
    border: 1px solid rgba(96,165,250,.35);
    color: #60a5fa;
    font-size: 13px;
    font-weight: 700;
}

.section-title {
    font-size: 25px;
    font-weight: 800;
    margin: 25px 0 15px;
}

.agent-card {
    background: linear-gradient(145deg, rgba(15,27,45,.98), rgba(8,18,33,.98));
    border: 1px solid #24344d;
    border-radius: 20px;
    padding: 25px;
    min-height: 215px;
    box-shadow: 0 12px 35px rgba(0,0,0,.18);
}

.agent-icon {
    font-size: 36px;
    margin-bottom: 12px;
}

.agent-name {
    font-size: 20px;
    font-weight: 800;
}

.agent-description {
    color: #94a3b8;
    font-size: 14px;
    line-height: 1.55;
    margin-top: 10px;
}

.ready {
    margin-top: 18px;
    color: #4ade80;
    font-size: 12px;
    font-weight: 800;
}

.workspace {
    margin-top: 35px;
    background: linear-gradient(145deg, rgba(11,23,40,.98), rgba(7,16,29,.98));
    border: 1px solid #26364d;
    border-radius: 22px;
    padding: 28px;
}

.workspace-title {
    font-size: 26px;
    font-weight: 800;
}

.workspace-subtitle {
    color: #94a3b8;
    margin-top: 5px;
}

.upload-card {
    background: rgba(15,27,45,.9);
    border: 1px solid #26364d;
    border-radius: 18px;
    padding: 20px;
    min-height: 120px;
}

.upload-title {
    font-size: 19px;
    font-weight: 800;
}

.upload-description {
    color: #94a3b8;
    font-size: 14px;
    margin-top: 6px;
}

.audit-header {
    margin-top: 40px;
    margin-bottom: 22px;
    padding: 25px;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(30,41,59,.9), rgba(15,23,42,.95));
    border: 1px solid #334155;
}

.audit-header-title {
    font-size: 30px;
    font-weight: 850;
}

.audit-header-subtitle {
    color: #94a3b8;
    margin-top: 5px;
}

.metric-card {
    background: #0b1525;
    border: 1px solid #26364d;
    border-radius: 17px;
    padding: 20px;
    min-height: 125px;
}

.metric-label {
    color: #94a3b8;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
}

.metric-value {
    font-size: 27px;
    font-weight: 850;
    margin-top: 9px;
}

.risk-high, .mismatch {
    color: #f87171;
}

.risk-medium {
    color: #fbbf24;
}

.risk-low, .verified {
    color: #4ade80;
}

.finding-box {
    background: #0b1525;
    border: 1px solid #26364d;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 18px;
}

.finding-title {
    font-size: 21px;
    font-weight: 800;
}

.finding-description {
    color: #94a3b8;
    line-height: 1.6;
}

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 60px;
    padding: 25px;
    border-top: 1px solid #172337;
}

.stButton > button {
    border-radius: 12px;
    font-weight: 800;
    min-height: 48px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-title">🛡️ Agentic Auditor</div>
    <div class="hero-subtitle">
        Multi-Agent AI for intelligent contract and invoice auditing
    </div>
    <div class="hero-badge">
        ✦ AI-Powered &nbsp;•&nbsp; Multi-Agent &nbsp;•&nbsp; Cross-Document Audit
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# AGENT NETWORK
# =========================================================

st.markdown('<div class="section-title">🤖 AI Agent Network</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

agents = [
    ("🛡️", "Compliance Officer",
     "Detects missing clauses, legal risks, ambiguous terms and compliance issues."),
    ("💰", "Financial Auditor",
     "Verifies quantities, line items, tax calculations and invoice totals."),
    ("💬", "Client Communicator",
     "Converts technical findings into clear business-friendly recommendations.")
]

for column, (icon, name, description) in zip((c1, c2, c3), agents):
    with column:
        st.markdown(f"""
        <div class="agent-card">
            <div class="agent-icon">{icon}</div>
            <div class="agent-name">{name}</div>
            <div class="agent-description">{description}</div>
            <div class="ready">● READY</div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# WORKSPACE
# =========================================================

st.markdown("""
<div class="workspace">
    <div class="workspace-title">📄 Audit Workspace</div>
    <div class="workspace-subtitle">
        Upload the contract and invoice separately. The AI system will compare both documents.
    </div>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="upload-card">
        <div class="upload-title">📄 Contract</div>
        <div class="upload-description">Upload the service agreement or contract.</div>
    </div>
    """, unsafe_allow_html=True)

    contract_file = st.file_uploader(
        "Choose contract",
        type=["txt", "pdf"],
        key="contract_file"
    )

with c2:
    st.markdown("""
    <div class="upload-card">
        <div class="upload-title">🧾 Invoice</div>
        <div class="upload-description">Upload the corresponding invoice.</div>
    </div>
    """, unsafe_allow_html=True)

    invoice_file = st.file_uploader(
        "Choose invoice",
        type=["txt", "pdf"],
        key="invoice_file"
    )

# =========================================================
# FILE READER
# =========================================================

def read_file(uploaded_file):
    if uploaded_file is None:
        return ""

    name = uploaded_file.name.lower()

    if name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8", errors="ignore")

    if name.endswith(".pdf"):
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
            st.error(f"PDF reading failed: {e}")
            return ""

    return ""

# =========================================================
# HELPERS
# =========================================================

def extract_risk(text):
    match = re.search(
        r"Overall Risk\s*:\s*(HIGH|MEDIUM|LOW)",
        text,
        re.IGNORECASE
    )
    return match.group(1).upper() if match else "REVIEW"


def extract_financial_status(text):
    matches = re.findall(
        r"Financial Status\s*:\s*(VERIFIED|MISMATCH|INCOMPLETE)",
        text,
        re.IGNORECASE
    )
    return matches[-1].upper() if matches else "REVIEW"


def count_issues(text):
    return len(re.findall(r"(?:^|\n)\s*\d+\.\s*\[", text or ""))


def metric_class(value):
    value = value.upper()

    if value == "HIGH":
        return "risk-high"
    if value == "MEDIUM":
        return "risk-medium"
    if value in ("LOW", "VERIFIED"):
        return "verified"
    if value == "MISMATCH":
        return "mismatch"

    return ""

# =========================================================
# RUN AUDIT
# =========================================================

if contract_file and invoice_file:

    st.success("✅ Both documents uploaded successfully.")

    if st.button(
        "🚀 START CROSS-DOCUMENT AI AUDIT",
        type="primary",
        use_container_width=True
    ):

        contract_text = read_file(contract_file)
        invoice_text = read_file(invoice_file)

        if not contract_text.strip():
            st.error("❌ Contract file is empty.")
        elif not invoice_text.strip():
            st.error("❌ Invoice file is empty.")
        else:

            progress = st.progress(0)
            status = st.empty()

            try:
                status.info("🛡️ Compliance Officer is analysing...")
                progress.progress(25)

                result = run_full_audit(
                    contract_text,
                    invoice_text
                )

                progress.progress(100)
                status.success("✅ Multi-agent audit completed successfully.")

                st.session_state["audit_result"] = result
                                # Save audit to history
                save_audit({
                    "contract_file": contract_file.name,
                    "invoice_file": invoice_file.name,
                    "risk": extract_risk(str(result.get("compliance", ""))),
                    "financial_status": extract_financial_status(
                        str(result.get("financial", ""))
                    ),
                    "issue_count": (
                        count_issues(str(result.get("compliance", "")))
                        + count_issues(str(result.get("financial", "")))
                    ),
                    "result": result
                })

            except TypeError:

                # Compatibility fallback for an older one-argument orchestrator.
                combined = (
                    "CONTRACT\n"
                    "====================\n"
                    + contract_text
                    + "\n\nINVOICE\n"
                    "====================\n"
                    + invoice_text
                )

                try:
                    result = run_full_audit(combined)

                    progress.progress(100)
                    status.success("✅ Multi-agent audit completed successfully.")
                    st.session_state["audit_result"] = result

                except Exception as e:
                    progress.empty()
                    status.empty()
                    st.error(f"❌ Audit failed: {e}")

            except Exception as e:
                progress.empty()
                status.empty()
                st.error(f"❌ Audit failed: {e}")

elif contract_file:
    st.info("🧾 Please upload the invoice also.")

elif invoice_file:
    st.info("📄 Please upload the contract also.")

else:
    st.info("📄 Upload a contract and 🧾 invoice to activate the cross-document AI audit.")


# =========================================================
# PDF REPORT GENERATOR
# =========================================================

def clean_pdf_text(text):
    """Convert report text into PDF-safe plain text."""
    if not text:
        return ""

    text = str(text)

    # Keep the report readable with ReportLab's built-in fonts.
    replacements = {
        "₹": "Rs. ",
        "🛡️": "[Compliance]",
        "💰": "[Financial]",
        "💬": "[Communication]",
        "📋": "[Unified]",
        "📊": "[Audit]",
        "🚀": "",
        "✅": "[OK]",
        "❌": "[ERROR]",
        "⚠️": "[WARNING]",
        "—": "-",
        "–": "-",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "•": "-",
        "✦": "*",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove remaining non-ASCII characters that built-in PDF fonts
    # cannot reliably render.
    return text.encode("latin-1", errors="replace").decode("latin-1")


def build_pdf_report(compliance, financial, communication, summary):
    """
    Create a downloadable PDF audit report entirely in memory.
    Returns PDF bytes.
    """
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER
        from reportlab.lib.units import mm
        from reportlab.platypus import (
            SimpleDocTemplate,
            Paragraph,
            Spacer,
            PageBreak
        )
    except ImportError:
        return None

    buffer = io.BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="Agentic Auditor - Audit Report",
        author="Agentic Auditor"
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "AuditTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=27,
        alignment=TA_CENTER,
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        "AuditSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        spaceAfter=18
    )

    section_style = ParagraphStyle(
        "AuditSection",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=19,
        spaceBefore=12,
        spaceAfter=10
    )

    body_style = ParagraphStyle(
        "AuditBody",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=14,
        spaceAfter=7
    )

    story = []

    story.append(Paragraph("AGENTIC AUDITOR", title_style))
    story.append(
        Paragraph(
            "Multi-Agent AI for intelligent contract and invoice auditing",
            subtitle_style
        )
    )

    story.append(Paragraph("FINAL AUDIT REPORT", section_style))

    if compliance:
        story.append(Paragraph("Compliance Officer Report", section_style))
        for line in clean_pdf_text(compliance).splitlines():
            line = line.strip()
            if line:
                safe = html.escape(line)
                story.append(Paragraph(safe, body_style))

    if financial:
        story.append(Paragraph("Financial Auditor Report", section_style))
        for line in clean_pdf_text(financial).splitlines():
            line = line.strip()
            if line:
                safe = html.escape(line)
                story.append(Paragraph(safe, body_style))

    if communication:
        story.append(Paragraph("Client Communicator Report", section_style))
        for line in clean_pdf_text(communication).splitlines():
            line = line.strip()
            if line:
                safe = html.escape(line)
                story.append(Paragraph(safe, body_style))

    if summary:
        story.append(Paragraph("Unified Audit Report", section_style))
        for line in clean_pdf_text(summary).splitlines():
            line = line.strip()
            if line:
                safe = html.escape(line)
                story.append(Paragraph(safe, body_style))

    story.append(Spacer(1, 12))
    story.append(
        Paragraph(
            "Disclaimer: This AI-generated audit summary is for informational "
            "purposes and should be reviewed by an appropriate professional "
            "before making legal or financial decisions.",
            body_style
        )
    )

    document.build(story)

    return buffer.getvalue()


# =========================================================
# REPORT
# =========================================================

if "audit_result" in st.session_state:

    result = st.session_state["audit_result"]

    st.markdown("""
    <div class="audit-header">
        <div class="audit-header-title">📊 Final Audit Report</div>
        <div class="audit-header-subtitle">
            Cross-document analysis completed by the Agentic Auditor multi-agent network.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if isinstance(result, dict):
        compliance = result.get("compliance", "")
        financial = result.get("financial", "")
        communication = result.get("communication", "")
        summary = result.get("summary", "")
    else:
        compliance = ""
        financial = ""
        communication = ""
        summary = str(result)

    risk = extract_risk(str(compliance))
    financial_status = extract_financial_status(str(financial))
    issue_count = count_issues(str(compliance)) + count_issues(str(financial))

    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Overall Risk</div>
            <div class="metric-value {metric_class(risk)}">{risk}</div>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Financial Status</div>
            <div class="metric-value {metric_class(financial_status)}">
                {financial_status}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Issues Detected</div>
            <div class="metric-value">{issue_count}</div>
        </div>
        """, unsafe_allow_html=True)

    if compliance:
        st.markdown("""
        <div class="finding-box">
            <div class="finding-title">🛡️ Compliance Findings</div>
            <div class="finding-description">
                Contract risks, missing clauses, ambiguous terms and compliance observations.
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("View Compliance Officer Report", expanded=True):
            st.markdown(compliance)

    if financial:
        st.markdown("""
        <div class="finding-box">
            <div class="finding-title">💰 Financial Verification</div>
            <div class="finding-description">
                Invoice calculations, tax verification, line-item checks and amount consistency.
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("View Financial Auditor Report", expanded=True):
            st.markdown(financial)

    if communication:
        st.markdown("""
        <div class="finding-box">
            <div class="finding-title">💬 Business Recommendations</div>
            <div class="finding-description">
                Clear business-friendly explanation of the audit findings.
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("View Client Communicator Report", expanded=True):
            st.markdown(communication)

    if summary:
        st.markdown("""
        <div class="finding-box">
            <div class="finding-title">📋 Unified Audit Report</div>
            <div class="finding-description">
                Consolidated output from the multi-agent audit workflow.
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("View Unified Report", expanded=False):
            st.markdown(summary)

    full_report = ""

    sections = [
        ("COMPLIANCE OFFICER REPORT", compliance),
        ("FINANCIAL AUDITOR REPORT", financial),
        ("CLIENT COMMUNICATOR REPORT", communication),
        ("UNIFIED AUDIT REPORT", summary)
    ]

    for title, content in sections:
        if content:
            full_report += (
                "=" * 45 + "\n"
                + title + "\n"
                + "=" * 45 + "\n\n"
                + str(content)
                + "\n\n"
            )

    if full_report.strip():

        st.markdown("### 📥 Export Audit Report")

        pdf_data = build_pdf_report(
            compliance,
            financial,
            communication,
            summary
        )

        b1, b2 = st.columns(2)

        with b1:
            if pdf_data:
                st.download_button(
                    "📄 DOWNLOAD PDF REPORT",
                    data=pdf_data,
                    file_name="agentic_auditor_report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            else:
                st.error(
                    "ReportLab is not installed. Run: "
                    "pip install reportlab"
                )

        with b2:
            st.download_button(
                "📝 DOWNLOAD TEXT REPORT",
                data=full_report,
                file_name="agentic_auditor_report.txt",
                mime="text/plain",
                use_container_width=True
            )
# =========================================================
# AUDIT HISTORY
# =========================================================

st.markdown("---")

st.markdown("## 📚 Audit History")

history = load_history()

if not history:
    st.info("No previous audits found.")
else:
    for index, audit in enumerate(reversed(history)):
        st.markdown(
            f"### {audit.get('invoice_file', 'Unknown Invoice')}"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.write(
                f"**Contract:** {audit.get('contract_file', 'Unknown')}"
            )

        with col2:
            risk = audit.get("risk", "REVIEW")
            st.write(f"**Risk:** {risk}")

        with col3:
            financial_status = audit.get(
                "financial_status",
                "REVIEW"
            )
            st.write(
                f"**Financial:** {financial_status}"
            )

        with col4:
            st.write(
                f"**Date:** {audit.get('saved_at', 'Unknown')}"
            )

        with st.expander("View Previous Audit Report"):
            previous_result = audit.get("result", {})

            if isinstance(previous_result, dict):
                previous_compliance = previous_result.get(
                    "compliance", ""
                )
                previous_financial = previous_result.get(
                    "financial", ""
                )
                previous_communication = previous_result.get(
                    "communication", ""
                )
                previous_summary = previous_result.get(
                    "summary", ""
                )

                if previous_compliance:
                    st.markdown("#### Compliance Officer Report")
                    st.markdown(previous_compliance)

                if previous_financial:
                    st.markdown("#### Financial Auditor Report")
                    st.markdown(previous_financial)

                if previous_communication:
                    st.markdown("#### Client Communicator Report")
                    st.markdown(previous_communication)

                if previous_summary:
                    st.markdown("#### Unified Audit Report")
                    st.markdown(previous_summary)

            else:
                st.write(previous_result)

        st.markdown("---")
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
