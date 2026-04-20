# app.py  (REPLACE FULL FILE FOR PREMIUM UI)

import streamlit as st

st.set_page_config(
    page_title="BB84 Quantum Security System",
    page_icon=":material/shield_lock:",
    layout="wide"
)

st.markdown("""
<style>
.stApp{
background:linear-gradient(135deg,#020617,#0f172a,#111827);
color:white;
}

h1,h2,h3{
text-align:center;
color:#38bdf8 !important;
font-weight:800;
}

p,li,label{
color:#e5e7eb !important;
}

[data-testid="stSidebar"]{
background:#020617;
border-right:1px solid #1e293b;
}

div.stButton > button{
width:100%;
background:linear-gradient(90deg,#06b6d4,#2563eb);
color:white;
border:none;
padding:0.7rem;
border-radius:14px;
font-weight:700;
font-size:16px;
}

div.stButton > button:hover{
transform:scale(1.02);
}

[data-testid="stMetricValue"]{
color:#22c55e;
font-size:28px;
font-weight:800;
}

.block-container{
padding-top:2rem;
padding-bottom:2rem;
max-width:1200px;
}

div[data-testid="stDataFrame"]{
border-radius:16px;
overflow:hidden;
}
</style>
""", unsafe_allow_html=True)

st.title(":material/shield_lock: BB84 Quantum Key Distribution")
st.subheader("Elite Secure Communication Simulator")

st.markdown("---")

left_space, main, right_space = st.columns([1,5,1])

with main:
    c1, c2, c3 = st.columns(3)

    with c1:
        st.image("assets/alice.png", width=150)
        st.metric("Alice", "Sender")

    with c2:
        st.image("assets/bob.png", width=150)
        st.metric("Bob", "Receiver")

    with c3:
        st.image("assets/eve.png", width=150)
        st.metric("Eve", "Optional")

st.markdown("---")

st.markdown("""
### Protocol Workflow

✅ Alice creates secret bits and bases  
✅ Qubits are generated and transmitted  
✅ Bob guesses bases and measures states  
✅ Eve may intercept communication  
✅ Bases compared publicly  
✅ Error rate calculated  
✅ Shared secret key produced
""")

st.success("Use Sidebar → Alice, Bob, Results")