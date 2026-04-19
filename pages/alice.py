import streamlit as st
import random

st.title("👩 Alice Control Center")

st.markdown("## Create Quantum Transmission")

mode = st.radio(
    "Select Input Mode",
    ["Manual Entry", "Auto Random"],
    horizontal=True
)

# ---------- Qubit Mapping ----------
def to_qubit(bit, basis):
    if basis == "Z" and bit == "0":
        return "│0⟩"
    if basis == "Z" and bit == "1":
        return "│1⟩"
    if basis == "X" and bit == "0":
        return "│+⟩"
    if basis == "X" and bit == "1":
        return "│-⟩"

# ---------- MANUAL MODE ----------
if mode == "Manual Entry":

    col1, col2 = st.columns(2)

    with col1:
        bits = st.text_input("Enter Bit String", placeholder="10110")

    with col2:
        bases = st.text_input("Enter Bases (Z/X)", placeholder="XZXXZ")

# ---------- AUTO MODE ----------
else:
    n = st.slider("Number of Bits", 4, 100, 10)

    bits = "".join(random.choice("01") for _ in range(n))
    bases = "".join(random.choice("ZX") for _ in range(n))

    st.info(f"Generated Bits: {bits}")
    st.info(f"Generated Bases: {bases}")

# ---------- GENERATE ----------
if st.button("🚀 Generate Transmission"):

    bits = bits.strip()
    bases = bases.strip().upper()

    if len(bits) == 0 or len(bits) != len(bases):
        st.error("Bits and Bases length must match.")

    elif any(ch not in "01" for ch in bits):
        st.error("Bits must contain only 0 and 1.")

    elif any(ch not in "ZX" for ch in bases):
        st.error("Bases must contain only Z or X.")

    else:
        qubits = [to_qubit(b, ba) for b, ba in zip(bits, bases)]

        st.session_state["alice_bits"] = [int(x) for x in bits]
        st.session_state["alice_bases"] = list(bases)
        st.session_state["alice_qubits"] = qubits

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Total Bits", len(bits))

        with c2:
            st.metric("Z Bases", bases.count("Z"))

        with c3:
            st.metric("X Bases", bases.count("X"))

        st.success("Quantum transmission prepared.")

        st.markdown("### 📡 Qubits Ready to Send")
        st.code("   ".join(qubits))