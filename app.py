import streamlit as st
from crewai import Crew, Task, Process
from agents import compliance_officer, financial_auditor, communication_specialist

st.set_page_config(page_title="Agentic Auditor", page_icon="💼", layout="wide")

st.title("💼 Agentic Auditor: AI-Powered SMB Compliance Officer")
st.write("First Prize Architecture Prototype - Future of Work & Automation Track")

# Text inputs layout
contract_data = st.text_area("📄 Paste Contract/Agreement Text here:", height=200)
invoice_data = st.text_area("📊 Paste Invoice details or Text here:", height=150)

if st.button("🚀 Run Comprehensive AI Audit", type="primary"):
    if not contract_data or not invoice_data:
        st.warning("Please fill both text areas to begin the automated audit.")
    else:
        with st.spinner("AI Agents are actively auditing your business documents..."):
            
            # Define tasks
            task1 = Task(
                description=f"Analyze this contract text for risks, missing clauses, or penalties:\n{contract_data}",
                expected_output="A structured report highlighting risks, liabilities, and required updates.",
                agent=compliance_officer
            )
            
            task2 = Task(
                description=f"Audit this invoice against standard compliance and math accuracy:\n{invoice_data}",
                expected_output="An itemized financial audit report showing calculations, errors, or tax notes.",
                agent=financial_auditor
            )
            
            task3 = Task(
                description="Based on the contract risks and invoice audit, draft a professional update email to the client.",
                expected_output="A ready-to-send professional email negotiating corrections politely.",
                agent=communication_specialist
            )
            
            # Run the multi-agent system
            crew = Crew(
                agents=[compliance_officer, financial_auditor, communication_specialist],
                tasks=[task1, task2, task3],
                process=Process.sequential
            )
            
            result = crew.kickoff()
            
            st.success("🎉 Audit Completed Successfully!")
            st.markdown("### 📋 Final Executive Report & Action Steps")
            st.write(str(result))
