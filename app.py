import streamlit as st
import time
import base64
from datetime import datetime

st.set_page_config(page_title="NIDHI Loan Assistant", page_icon="🏦", layout="wide")

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); }
    .block-container { padding: 2rem; max-width: 100%; }
    .glass-container { background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(20px); border: 1px solid rgba(148, 163, 184, 0.1); border-radius: 16px; padding: 1.5rem; margin-bottom: 1rem; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2); }
    .gradient-text { background: linear-gradient(90deg, #8b5cf6, #06b6d4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .user-bubble { background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%); color: #ffffff !important; border-radius: 18px 18px 4px 18px; padding: 14px 18px; margin: 10px 0; margin-left: auto; max-width: 75%; box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3); }
    .user-bubble * { color: #ffffff !important; }
    .bot-bubble { background: rgba(51, 65, 85, 0.8) !important; color: #f1f5f9 !important; border-radius: 18px 18px 18px 4px; padding: 14px 18px; margin: 10px 0; max-width: 75%; border-left: 4px solid #8b5cf6; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); }
    .bot-bubble * { color: #f1f5f9 !important; }
    .chat-container { max-height: 550px; overflow-y: auto; padding: 10px; margin-bottom: 1rem; }
    .chat-container::-webkit-scrollbar { width: 6px; }
    .chat-container::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.05); border-radius: 10px; }
    .chat-container::-webkit-scrollbar-thumb { background: rgba(139, 92, 246, 0.5); border-radius: 10px; }
    .typing-indicator { display: flex; gap: 6px; padding: 16px; background: rgba(51, 65, 85, 0.6); border-radius: 18px; width: fit-content; margin: 10px 0; }
    .typing-dot { width: 8px; height: 8px; background: #8b5cf6; border-radius: 50%; animation: typing 1.4s infinite; }
    .typing-dot:nth-child(2) { animation-delay: 0.2s; }
    .typing-dot:nth-child(3) { animation-delay: 0.4s; }
    @keyframes typing { 0%, 60%, 100% { transform: translateY(0); opacity: 0.7; } 30% { transform: translateY(-10px); opacity: 1; } }
    .stButton > button { background: linear-gradient(135deg, #8b5cf6 0%, #06b6d4 100%); color: white !important; border: none; padding: 10px 20px; border-radius: 10px; font-weight: 600; width: 100%; transition: all 0.3s ease; }
    .stButton > button:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(139, 92, 246, 0.4); }
    .stTextInput input, .stNumberInput input { background: rgba(51, 65, 85, 0.6) !important; border: 1px solid rgba(148, 163, 184, 0.2) !important; border-radius: 10px !important; color: #f1f5f9 !important; padding: 12px 16px !important; }
    .stTextInput input:focus, .stNumberInput input:focus { border-color: #8b5cf6 !important; box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2) !important; }
    .stRadio label { color: #e2e8f0 !important; font-weight: 500; }
    .stRadio [role="radiogroup"] label { background: rgba(51, 65, 85, 0.5) !important; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 8px; padding: 10px 16px; color: #e2e8f0 !important; transition: all 0.3s ease; }
    .stRadio [role="radiogroup"] label:hover { background: rgba(139, 92, 246, 0.15) !important; border-color: rgba(139, 92, 246, 0.4); }
    .stRadio [role="radiogroup"] label[data-checked="true"] { background: rgba(139, 92, 246, 0.25) !important; border-color: #8b5cf6; }
    .progress-bar { height: 8px; background: rgba(51, 65, 85, 0.6); border-radius: 4px; overflow: hidden; margin: 8px 0; }
    .progress-fill { height: 100%; background: linear-gradient(90deg, #8b5cf6, #06b6d4); border-radius: 4px; transition: width 0.5s ease; }
    #MainMenu, footer, header { visibility: hidden; }
    .stFileUploader { background: rgba(51, 65, 85, 0.4); border: 2px dashed rgba(139, 92, 246, 0.3); border-radius: 12px; padding: 20px; }
    .stFileUploader:hover { border-color: rgba(139, 92, 246, 0.6); background: rgba(139, 92, 246, 0.05); }
    .section-header { font-size: 18px; font-weight: 600; color: #f1f5f9 !important; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; }
    .info-card { background: rgba(51, 65, 85, 0.4); border: 1px solid rgba(148, 163, 184, 0.1); border-radius: 12px; padding: 16px; margin-bottom: 12px; transition: all 0.3s ease; }
    .info-card:hover { background: rgba(51, 65, 85, 0.6); border-color: rgba(139, 92, 246, 0.3); transform: translateY(-2px); }
    h1, h2, h3, h4, h5, h6, p, span, div, label { color: #e2e8f0 !important; }
    a[download] { display: inline-block; background: linear-gradient(135deg, #8b5cf6 0%, #06b6d4 100%); color: white !important; padding: 10px 20px; border-radius: 10px; text-decoration: none; font-weight: 600; }
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
    </style>
    """, unsafe_allow_html=True)

def init_session_state():
    defaults = {
        'messages': [
            {"role": "agent", "text": "Hello there! 👋 I'm NIDHI, your AI Loan Assistant. I'm here to help you secure a personal loan with the best possible terms. How can I assist you today?", "timestamp": datetime.now().isoformat()},
            {"role": "agent", "text": "You can simply tell me how much you need, or ask about interest rates, EMI calculations, or required documents.", "timestamp": datetime.now().isoformat()}
        ],
        'progress': {"Document Check": 0, "Credit Score": 0, "Eligibility": 0, "Approval": 0},
        'loan_amount': 100000,
        'user_info': {"name": "Aarav Sharma", "pan": "ABCDE1234F", "pre_approved": "₹200,000", "credit_score": 780, "monthly_income": "₹85,000"},
        'selected_file': None,
        'needs_salary_slip': False,
        'process_steps': {
            "Document Check": {"status": "pending", "description": "Verify PAN & documents"},
            "Credit Score": {"status": "pending", "description": "Check credit history"},
            "Eligibility": {"status": "pending", "description": "Calculate eligibility"},
            "Approval": {"status": "pending", "description": "Final approval"}
        },
        'sanction_text': None
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

LOAN_DOC_THRESHOLD = 100000

def format_time(timestamp):
    try:
        return datetime.fromisoformat(timestamp).strftime("%I:%M %p")
    except:
        return ""

def simulate_typing(duration=1.0):
    placeholder = st.empty()
    placeholder.markdown('<div class="typing-indicator"><div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div></div>', unsafe_allow_html=True)
    time.sleep(duration)
    placeholder.empty()

def add_message(role, text):
    st.session_state.messages.append({"role": role, "text": text, "timestamp": datetime.now().isoformat()})

def update_progress(step, value):
    st.session_state.progress[step] = value

def update_process_step(step, status, description=None):
    if description:
        st.session_state.process_steps[step]["description"] = description
    st.session_state.process_steps[step]["status"] = status

def process_loan_request(amount):
    # Get user info
    user_info = st.session_state.user_info
    credit_score = user_info['credit_score']
    pre_approved = int(user_info["pre_approved"].replace('₹', '').replace(',', ''))
    monthly_income = int(user_info["monthly_income"].replace('₹', '').replace(',', ''))
    
    # Fix 1: CREDIT SCORE CHECK (First diamond in flowchart)
    simulate_typing(0.5)
    if credit_score < 700:
        update_process_step("Eligibility", "partial", "❌ Credit score below 700")
        add_message("agent", f"❌ Unfortunately, your credit score ({credit_score}/900) does not meet the minimum eligibility criteria of 700.")
        return {"success": False}
    
    # Fix 2: DOCUMENT CHECK - Always verify documents first
    add_message("agent", "📋 Starting document verification...")
    for i in range(0, 101, 20):
        update_progress("Document Check", i)
        time.sleep(0.15)
    update_process_step("Document Check", "completed", "✅ Documents verified")
    add_message("agent", "✅ PAN and documents verified successfully")
    
    # Fix 3: CREDIT SCORE PROGRESS (Separate step)
    add_message("agent", "📊 Checking credit score...")
    for i in range(0, 101, 25):
        update_progress("Credit Score", i)
        time.sleep(0.2)
    update_process_step("Credit Score", "completed", f"✅ Credit score: {credit_score}/900")
    add_message("agent", f"✅ Credit score check completed: {credit_score}/900 (Above threshold ✓)")
    
    # Fix 4: ELIGIBILITY CALCULATION with explicit pre-approved logic
    add_message("agent", "🧮 Calculating eligibility...")
    for i in range(0, 101, 25):
        update_progress("Eligibility", i)
        time.sleep(0.2)
    
    # FIXED LOGIC: Aligned with flowchart diamonds
    if amount <= pre_approved:
        # Instant approval path
        emi = int(amount * 0.033)
        update_process_step("Eligibility", "completed", f"✅ Eligible for ₹{amount:,} (Instant)")
        
        # Fix 5: EMI CHECK (Last diamond in flowchart)
        if emi > 0.5 * monthly_income:
            update_process_step("Eligibility", "partial", "⚠️ EMI > 50% income")
            add_message("agent", f"❌ EMI (₹{emi:,}) exceeds 50% of your monthly income (₹{monthly_income:,}). Loan cannot be approved.")
            return {"success": False}
        
        add_message("agent", f"✅ **Instant Approval Eligible!**")
        
    elif amount <= pre_approved * 2:
        # Needs salary slip path
        if not st.session_state.selected_file:
            update_process_step("Eligibility", "partial", f"⏳ Needs salary slip")
            add_message("agent", f"📄 Your requested amount (₹{amount:,}) requires salary slip verification. Please upload your latest salary slip.")
            st.session_state.needs_salary_slip = True
            return {"needs_salary_slip": True, "amount": amount}
        
        # Salary slip already uploaded, continue
        emi = int(amount * 0.033)
        update_process_step("Eligibility", "completed", f"✅ Eligible for ₹{amount:,}")
        
        # Fix 5: EMI CHECK (Last diamond in flowchart)
        if emi > 0.5 * monthly_income:
            update_process_step("Eligibility", "partial", "⚠️ EMI > 50% income")
            add_message("agent", f"❌ EMI (₹{emi:,}) exceeds 50% of your monthly income (₹{monthly_income:,}). Loan cannot be approved.")
            return {"success": False}
        
        add_message("agent", f"✅ **Salary Slip Verified - Eligible!**")
        
    else:
        # Amount exceeds policy limits
        update_process_step("Eligibility", "partial", "❌ Amount exceeds limit")
        add_message("agent", f"❌ Requested amount (₹{amount:,}) exceeds maximum permissible limit (₹{pre_approved * 2:,}).")
        add_message("agent", f"**Recommendation:** Reduce amount to ₹{pre_approved * 2:,} or lower for consideration.")
        return {"success": False}
    
    # APPROVAL PROCESSING
    add_message("agent", "✅ Processing final approval...")
    for i in range(0, 101, 33):
        update_progress("Approval", i)
        time.sleep(0.3)
    update_process_step("Approval", "completed", "✅ Loan approved")
    
    # Success message with proper details
    add_message("agent", f"""✅ **Loan Approved!**

**Loan Details:**
• Amount: ₹{amount:,}
• Interest Rate: 12.5% p.a.
• Tenure: 36 months
• Monthly EMI: ₹{emi:,}
• EMI/Income Ratio: {emi/monthly_income*100:.1f}%

**Policy Compliance:**
✓ Credit Score: {credit_score}/900 (≥700)
✓ Amount within limits
✓ EMI ≤ 50% of income

Would you like me to generate the sanction letter?""")
    
    # Sanction letter text
    sanction_text = f"""NIDHI LOAN ASSISTANT - SANCTION LETTER

Customer Name: {user_info['name']}
PAN Number: {user_info['pan']}
Monthly Income: {user_info['monthly_income']}
Credit Score: {credit_score}/900

Sanctioned Amount: ₹{amount:,}
Interest Rate: 12.5% per annum
Loan Tenure: 36 months
Monthly EMI: ₹{emi:,}

**Approval Criteria Met:**
1. Credit Score: {credit_score} (Minimum: 700) ✓
2. Amount within {2 if amount > pre_approved else 1}× pre-approved limit ✓
3. EMI/Income Ratio: {emi/monthly_income*100:.1f}% (Maximum: 50%) ✓

Approval Date: {datetime.now().strftime("%d %B %Y")}
Validity: 30 days from approval

Terms & Conditions:
1. This sanction is subject to verification of original documents.
2. Final disbursement upon completion of all formalities.
3. Processing charges as applicable.

Generated by NIDHI AI Loan Assistant - Agentic Decision Flow"""
    
    return {"success": True, "amount": amount, "sanction_text": sanction_text, "emi": emi}

def extract_amount(text):
    import re
    text = text.replace(',', '').replace('₹', '')
    lakh_match = re.search(r'(\d+(?:\.\d+)?)\s*(lakh|lac)', text, re.IGNORECASE)
    if lakh_match:
        return int(float(lakh_match.group(1)) * 100000)
    thousand_match = re.search(r'(\d+)\s*(thousand|k)', text, re.IGNORECASE)
    if thousand_match:
        return int(float(thousand_match.group(1)) * 1000)
    number_match = re.search(r'(\d{4,7})', text)
    if number_match:
        return int(number_match.group(1))
    return None

def create_download_link(text, filename):
    b64 = base64.b64encode(text.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{filename}">📥 Download {filename}</a>'

def main():
    load_css()
    init_session_state()
    
    col1, _, col3 = st.columns([3, 3, 1])
    with col1:
        st.markdown("""<div style="display: flex; align-items: center; gap: 16px;">
            <div style="width: 56px; height: 56px; background: linear-gradient(135deg, #8b5cf6, #06b6d4); border-radius: 12px; 
                 display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 24px;">N</div>
            <div><h1 class="gradient-text" style="font-size: 26px; margin: 0;">NIDHI Loan Assistant</h1>
            <p style="color: #94a3b8; margin: 0; font-size: 14px;">AI-Powered Personal Loan Assistant</p></div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div style="background: rgba(34, 197, 94, 0.15); border: 1px solid rgba(34, 197, 94, 0.3); padding: 8px 16px; 
             border-radius: 20px; display: flex; align-items: center; gap: 8px; justify-content: center; margin-top: 10px;">
            <div style="width: 8px; height: 8px; background: #22c55e; border-radius: 50%; animation: pulse 2s infinite;"></div>
            <span style="color: #22c55e; font-weight: 600;">Live</span></div>""", unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
    
    col_left, col_center, col_right = st.columns([1.2, 2.5, 1.3])
    
    with col_left:
        st.markdown('<div class="glass-container"><div class="section-header">👤 Your Profile</div>', unsafe_allow_html=True)
        user_info = st.session_state.user_info
        st.markdown(f"""<div class="info-card"><div style="color: #94a3b8; font-size: 12px;">Full Name</div>
            <div style="font-weight: 600; color: #f1f5f9 !important;">{user_info['name']}</div></div>
            <div class="info-card"><div style="color: #94a3b8; font-size: 12px;">PAN Number</div>
            <div style="font-weight: 600; font-family: monospace; color: #f1f5f9 !important;">{user_info['pan']}</div></div>
            <div class="info-card"><div style="color: #94a3b8; font-size: 12px;">Monthly Income</div>
            <div style="font-weight: 600; color: #10b981 !important;">{user_info['monthly_income']}</div></div>
            <div class="info-card"><div style="color: #94a3b8; font-size: 12px;">Credit Score</div>
            <div style="display: flex; gap: 8px;"><span style="font-weight: 800; font-size: 22px; color: #22c55e !important;">{user_info['credit_score']}</span>
            <span style="color: #64748b;">/ 900</span></div></div></div>""", unsafe_allow_html=True)
        
        st.markdown('<div class="glass-container"><div class="section-header">⚡ Quick Actions</div>', unsafe_allow_html=True)
        for action_text, action_msg in [("Apply for ₹1,50,000", "I need a loan of ₹1,50,000"), ("Check EMI Options", "What are the EMI options?"), 
                                         ("Interest Rates", "What is the interest rate?"), ("Required Documents", "What documents do I need?")]:
            if st.button(action_text, key=f"action_{action_text}", use_container_width=True):
                add_message("user", action_msg)
                amount = extract_amount(action_msg)
                if amount:
                    st.session_state.loan_amount = amount
                    result = process_loan_request(amount)
                    if result.get("sanction_text"):
                        st.session_state.sanction_text = result["sanction_text"]
                else:
                    simulate_typing(0.6)
                    if "emi" in action_msg.lower():
                        emi = int(st.session_state.loan_amount * 0.033)
                        add_message("agent", f"""**EMI Options for ₹{st.session_state.loan_amount:,}:**

• **24 months:** ₹{int(st.session_state.loan_amount * 0.05):,}/month
• **36 months:** ₹{emi:,}/month (Recommended)
• **48 months:** ₹{int(st.session_state.loan_amount * 0.027):,}/month""")
                    elif "interest" in action_msg.lower():
                        add_message("agent", """**Interest Rate Details:**

• **Existing Customers:** 10.99% - 12.5% p.a.
• **New Customers:** 11.5% - 14.5% p.a.
• **Special Offers:** Starting at 10.5% for salaried professionals""")
                    elif "document" in action_msg.lower():
                        add_message("agent", f"""**Required Documents:**

**Basic (≤ ₹{LOAN_DOC_THRESHOLD:,}):** PAN, Aadhaar, Bank Statement
**Additional (> ₹{LOAN_DOC_THRESHOLD:,}):** Salary Slips, Form 16/ITR""")
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_center:
        st.markdown('<div class="glass-container"><div class="section-header">💬 Loan Assistant Chat</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"""<div style="display: flex; justify-content: flex-end;">
                    <div class="user-bubble"><div style="font-weight: 600; margin-bottom: 4px;">You</div>{msg['text']}
                    <div style="text-align: right; font-size: 11px; color: rgba(255,255,255,0.6); margin-top: 6px;">{format_time(msg['timestamp'])}</div></div></div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""<div style="display: flex;">
                    <div class="bot-bubble"><div style="display: flex; gap: 8px; margin-bottom: 6px;">
                    <span>🤖</span><span style="font-weight: 600; color: #8b5cf6 !important;">NIDHI AI</span>
                    <span style="margin-left: auto; font-size: 11px; color: #94a3b8;">{format_time(msg['timestamp'])}</span></div>
                    {msg['text']}</div></div>""", unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)
        
        st.markdown('<div class="glass-container"><div class="section-header">📝 Send Message</div>', unsafe_allow_html=True)
        col_input, col_btn = st.columns([4, 1])
        with col_input:
            user_input = st.text_input("Message", placeholder="Example: 'I need a loan of ₹2 lakhs'", label_visibility="collapsed", key="chat_input")
        with col_btn:
            if st.button("Send", use_container_width=True):
                if user_input.strip():
                    add_message("user", user_input)
                    amount = extract_amount(user_input)
                    if amount:
                        st.session_state.loan_amount = amount
                        result = process_loan_request(amount)
                        if result.get("sanction_text"):
                            st.session_state.sanction_text = result["sanction_text"]
                    else:
                        simulate_typing(0.6)
                        if any(w in user_input.lower() for w in ["hi", "hello", "hey"]):
                            add_message("agent", "Hello! 👋 Welcome to NIDHI Loan Assistant. How can I help you today?")
                        elif "thank" in user_input.lower():
                            add_message("agent", "You're welcome! 😊 Feel free to ask if you need more assistance.")
                        else:
                            add_message("agent", "I can help you with personal loans up to ₹25 lakhs. Ask me about amounts, rates, EMI, or documents!")
                    st.rerun()
        
        st.markdown(f'<div style="margin-top: 20px;"><h4 style="font-size: 14px; margin-bottom: 10px;">📎 Upload Documents</h4>' +
                   f'<p style="color: #94a3b8; font-size: 13px;">Required for loans above ₹{LOAN_DOC_THRESHOLD:,}</p></div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload salary slip", type=['pdf', 'jpg', 'jpeg', 'png'], label_visibility="collapsed")
        if uploaded_file and uploaded_file != st.session_state.selected_file:
            st.session_state.selected_file = uploaded_file
            add_message("user", f"📎 Uploaded: {uploaded_file.name}")
            simulate_typing(1.0)
            add_message("agent", "🔍 Processing document...")
            time.sleep(1.5)
            add_message("agent", "✅ Salary slip verified successfully!")
            
            # Now process the loan with the uploaded salary slip
            if st.session_state.needs_salary_slip:
                result = process_loan_request(st.session_state.loan_amount)
                if result.get("success") and result.get("sanction_text"):
                    st.session_state.sanction_text = result["sanction_text"]
                st.session_state.needs_salary_slip = False
            st.rerun()
        if st.session_state.selected_file:
            st.success(f"✅ Document uploaded: {st.session_state.selected_file.name}")
        
        # Sanction letter download section
        if st.session_state.get('sanction_text'):
            st.markdown('<div style="margin-top: 20px; padding: 16px; background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.2); border-radius: 12px;">', unsafe_allow_html=True)
            st.markdown('<h4 style="color: #22c55e !important; margin-bottom: 10px;">📄 Sanction Letter Ready!</h4>', unsafe_allow_html=True)
            st.markdown(create_download_link(st.session_state.sanction_text, f"loan_sanction_{datetime.now().strftime('%Y%m%d')}.txt"), unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_right:
        st.markdown('<div class="glass-container"><div class="section-header">💰 Loan Details</div>', unsafe_allow_html=True)
        loan_options = ["₹1,00,000", "₹1,50,000", "₹2,00,000", "₹2,50,000", "₹5,00,000"]
        selected_option = st.radio("Select amount:", loan_options, key="loan_select", label_visibility="collapsed")
        selected_amount = int(selected_option.replace('₹', '').replace(',', ''))
        if selected_amount != st.session_state.loan_amount:
            st.session_state.loan_amount = selected_amount
            st.rerun()
        
        custom_amount = st.number_input("Custom amount:", min_value=10000, max_value=2500000, value=st.session_state.loan_amount, step=50000)
        if custom_amount != st.session_state.loan_amount:
            st.session_state.loan_amount = custom_amount
            st.rerun()
        
        emi_36, emi_24, emi_48 = int(st.session_state.loan_amount * 0.033), int(st.session_state.loan_amount * 0.05), int(st.session_state.loan_amount * 0.027)
        st.markdown(f"""<div style="margin-top: 20px;"><div style="color: #94a3b8; font-size: 13px;">Selected Amount</div>
            <div style="font-weight: 800; font-size: 26px; color: #8b5cf6 !important; margin: 8px 0;">₹{st.session_state.loan_amount:,}</div>
            <div style="color: #94a3b8; font-size: 13px; margin: 16px 0 10px;">Estimated EMI</div>
            <div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 10px; margin-bottom: 6px;">
            <span>24 months:</span> <span style="float: right; font-weight: 600;">₹{emi_24:,}/mo</span></div>
            <div style="background: rgba(139, 92, 246, 0.1); padding: 10px; border-radius: 10px; border: 1px solid rgba(139, 92, 246, 0.2); margin-bottom: 6px;">
            <span>36 months (Rec):</span> <span style="float: right; font-weight: 700;">₹{emi_36:,}/mo</span></div>
            <div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 10px;">
            <span>48 months:</span> <span style="float: right; font-weight: 600;">₹{emi_48:,}/mo</span></div>
            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.03); border-radius: 12px;">
            <div style="color: #94a3b8; font-size: 13px;">Interest Rate</div>
            <div style="font-weight: 800; font-size: 20px; color: #10b981 !important;">12.5% <span style="font-size: 13px; color: #94a3b8;">p.a.</span></div></div></div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="glass-container"><div class="section-header">📈 Application Status</div>', unsafe_allow_html=True)
        for step_name, step_info in st.session_state.process_steps.items():
            status_icons = {"completed": "✅", "partial": "⚠️", "pending": "⏳"}
            status_colors = {"completed": "#10b981", "partial": "#f59e0b", "pending": "#64748b"}
            icon = status_icons.get(step_info["status"], "⏳")
            color = status_colors.get(step_info["status"], "#64748b")
            st.markdown(f"""<div class="info-card"><div style="display: flex; gap: 10px;">
                <div style="font-size: 20px;">{icon}</div><div style="flex: 1;"><div style="font-weight: 600; margin-bottom: 2px;">{step_name}</div>
                <div style="font-size: 13px; color: {color};">{step_info['description']}</div></div></div>
                <div class="progress-bar" style="margin-top: 8px;">
                <div class="progress-fill" style="width: {st.session_state.progress[step_name]}%;"></div>
                </div>
                </div>""", unsafe_allow_html=True)
        
        # Reset button
        if st.button("🔄 Reset Application", use_container_width=True):
            for key in ['messages', 'progress', 'loan_amount', 'selected_file', 'needs_salary_slip', 'process_steps', 'sanction_text']:
                if key in st.session_state:
                    if key == 'messages':
                        st.session_state[key] = [
                            {"role": "agent", "text": "Hello there! 👋 I'm NIDHI, your AI Loan Assistant. I'm here to help you secure a personal loan with the best possible terms. How can I assist you today?", "timestamp": datetime.now().isoformat()},
                            {"role": "agent", "text": "You can simply tell me how much you need, or ask about interest rates, EMI calculations, or required documents.", "timestamp": datetime.now().isoformat()}
                        ]
                    elif key == 'progress':
                        st.session_state[key] = {"Document Check": 0, "Credit Score": 0, "Eligibility": 0, "Approval": 0}
                    elif key == 'loan_amount':
                        st.session_state[key] = 100000
                    elif key == 'selected_file':
                        st.session_state[key] = None
                    elif key == 'needs_salary_slip':
                        st.session_state[key] = False
                    elif key == 'process_steps':
                        st.session_state[key] = {
                            "Document Check": {"status": "pending", "description": "Verify PAN & documents"},
                            "Credit Score": {"status": "pending", "description": "Check credit history"},
                            "Eligibility": {"status": "pending", "description": "Calculate eligibility"},
                            "Approval": {"status": "pending", "description": "Final approval"}
                        }
                    elif key == 'sanction_text':
                        st.session_state[key] = None
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 30px; padding: 20px; color: #94a3b8; font-size: 12px; border-top: 1px solid rgba(148, 163, 184, 0.1);">
    <p>NIDHI Loan Assistant v1.0 • This is a demo application for educational purposes</p>
    <p>Interest rates and eligibility are subject to change based on credit assessment</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()