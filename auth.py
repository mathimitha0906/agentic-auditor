import streamlit as st
import hashlib
import json
import os

AUTH_FILE = "data/user_auth.json"


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def load_auth():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(AUTH_FILE):
        return None

    try:
        with open(AUTH_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def save_auth(username, password):
    os.makedirs("data", exist_ok=True)

    with open(AUTH_FILE, "w", encoding="utf-8") as f:
        json.dump(
            {
                "username": username,
                "password": hash_password(password)
            },
            f,
            indent=4
        )


def render_login():
    st.markdown("""
    <style>
    .login-box {
        max-width: 500px;
        margin: 70px auto;
        padding: 40px;
        background: linear-gradient(145deg,#0f1b2d,#081221);
        border: 1px solid #26364d;
        border-radius: 24px;
        text-align: center;
    }
    .login-title {
        font-size: 38px;
        font-weight: 850;
        margin-bottom: 8px;
    }
    .login-subtitle {
        color: #94a3b8;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="login-box">
        <div class="login-title">🛡️ Agentic Auditor</div>
        <div class="login-subtitle">
            Secure Multi-Agent Contract & Invoice Auditing
        </div>
    </div>
    """, unsafe_allow_html=True)

    auth = load_auth()

    if auth is None:
        st.info("First-time setup: create your Agentic Auditor password.")

        username = st.text_input("Username", value="admin")
        password = st.text_input("Create Password", type="password")
        confirm = st.text_input("Confirm Password", type="password")

        if st.button("Create Account", type="primary", use_container_width=True):
            if not username.strip():
                st.error("Username is required.")
            elif len(password) < 4:
                st.error("Password must contain at least 4 characters.")
            elif password != confirm:
                st.error("Passwords do not match.")
            else:
                save_auth(username.strip(), password)
                st.session_state.authenticated = True
                st.session_state.username = username.strip()
                st.rerun()

    else:
        username = st.text_input("Username", value=auth.get("username", "admin"))
        password = st.text_input("Password", type="password")

        if st.button("Login", type="primary", use_container_width=True):
            if (
                username == auth.get("username")
                and hash_password(password) == auth.get("password")
            ):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Invalid username or password.")


def render_sidebar():
    with st.sidebar:
        st.markdown("## 🛡️ Agentic Auditor")
        st.caption(f"Signed in as **{st.session_state.get('username', 'User')}**")

        st.divider()

        page = st.radio(
            "Navigation",
            [
                "📊 Dashboard",
                "🚀 New Audit",
                "📜 Audit History",
                "⚙️ Settings"
            ],
            index=1
        )

        st.divider()

        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.pop("username", None)
            st.rerun()

    return page


def render_dashboard(load_history):
    st.markdown("## 📊 Audit Dashboard")
    st.caption("Your contract and invoice audit overview")

    history = load_history()

    total = len(history)
    high = sum(1 for x in history if str(x.get("risk", "")).upper() == "HIGH")
    mismatch = sum(
        1 for x in history
        if str(x.get("financial_status", "")).upper() == "MISMATCH"
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Audits", total)
    c2.metric("High Risk Audits", high)
    c3.metric("Financial Mismatches", mismatch)

    st.markdown("### 🕘 Recent Audits")

    if not history:
        st.info("No audits yet. Start your first audit from New Audit.")
        return

    for audit in reversed(history[-5:]):
        st.markdown(
            f"""
            **{audit.get('invoice_file', 'Unknown Invoice')}**  
            Risk: `{audit.get('risk', 'REVIEW')}` ·
            Financial: `{audit.get('financial_status', 'REVIEW')}` ·
            {audit.get('saved_at', '')}
            """
        )
        st.divider()


def render_settings():
    st.markdown("## ⚙️ Settings")
    st.caption("Manage your Agentic Auditor account")

    auth = load_auth()

    if auth is None:
        st.error("Account configuration not found.")
        return

    st.markdown("### 👤 Account")

    st.text_input(
        "Username",
        value=auth.get("username", ""),
        disabled=True
    )

    st.markdown("### 🔑 Change Password")

    current = st.text_input("Current Password", type="password")
    new_password = st.text_input("New Password", type="password")
    confirm = st.text_input("Confirm New Password", type="password")

    if st.button("Update Password", type="primary"):
        if hash_password(current) != auth.get("password"):
            st.error("Current password is incorrect.")
        elif len(new_password) < 4:
            st.error("New password must contain at least 4 characters.")
        elif new_password != confirm:
            st.error("New passwords do not match.")
        else:
            save_auth(auth["username"], new_password)
            st.success("Password updated successfully.")
