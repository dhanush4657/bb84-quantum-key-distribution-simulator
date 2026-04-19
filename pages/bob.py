# pages/bob.py   (FULL FINAL VERSION)

import streamlit as st
import random
from core.qiskit_mode import measure_qubit

st.title("👨 Bob Receiving Station")

if "alice_qubits" not in st.session_state:
    st.warning("Complete Alice step first.")

else:
    qubits = st.session_state["alice_qubits"]
    n = len(qubits)

    st.markdown("## Incoming Quantum Transmission")
    st.code("   ".join(qubits))

    st.markdown("---")

    # ---------- Controls ----------
    c1, c2 = st.columns(2)

    with c1:
        basis_mode = st.radio(
            "Bob Basis Mode",
            ["Manual Entry", "Auto Random"],
            horizontal=True
        )

    with c2:
        noise_on = st.toggle("📡 Channel Noise")

    eve_on = st.toggle("😈 Enable Eve Attack")
    qiskit_on = st.toggle("⚛️ Qiskit Real Quantum Mode")

    # ---------- Basis Input ----------
    if basis_mode == "Manual Entry":
        bob_bases = st.text_input(
            f"Enter Bob Bases ({n} chars using Z/X)",
            placeholder="XXZXZ"
        )
    else:
        bob_bases = "".join(random.choice("ZX") for _ in range(n))
        st.info(f"Auto Generated Bob Bases: {bob_bases}")

    # ---------- Normal Simulation ----------
    def measure(qubit, basis):

        if qubit == "│0⟩":
            return 0 if basis == "Z" else random.randint(0,1)

        if qubit == "│1⟩":
            return 1 if basis == "Z" else random.randint(0,1)

        if qubit == "│+⟩":
            return 0 if basis == "X" else random.randint(0,1)

        if qubit == "│-⟩":
            return 1 if basis == "X" else random.randint(0,1)

    # ---------- Eve Attack ----------
    def eve_attack(q):
        eve_basis = random.choice(["Z", "X"])
        eve_bit = measure(q, eve_basis)

        if eve_basis == "Z":
            return "│0⟩" if eve_bit == 0 else "│1⟩"
        else:
            return "│+⟩" if eve_bit == 0 else "│-⟩"

    # ---------- Channel Noise ----------
    def apply_noise(q):
        options = ["│0⟩", "│1⟩", "│+⟩", "│-⟩"]

        if random.random() < 0.15:
            return random.choice(options)

        return q

    # ---------- Run ----------
    if st.button("📥 Receive & Measure"):

        bob_bases = bob_bases.strip().upper()

        if len(bob_bases) != n:
            st.error("Bob bases length mismatch.")

        elif any(ch not in "ZX" for ch in bob_bases):
            st.error("Use only Z or X.")

        else:
            transmitted = qubits[:]

            # Eve attack
            if eve_on:
                transmitted = [eve_attack(q) for q in transmitted]
                st.session_state["eve_used"] = True
            else:
                st.session_state["eve_used"] = False

            # Noise
            if noise_on:
                transmitted = [apply_noise(q) for q in transmitted]
                st.session_state["noise_used"] = True
            else:
                st.session_state["noise_used"] = False

            # ---------- Measurement ----------
            results = []

            for i, (q, b) in enumerate(zip(transmitted, bob_bases)):

                if qiskit_on:
                    bit = st.session_state["alice_bits"][i]
                    alice_basis = st.session_state["alice_bases"][i]

                    measured = measure_qubit(bit, alice_basis, b)
                    results.append(measured)

                else:
                    measured = measure(q, b)
                    results.append(measured)

            st.session_state["bob_bases"] = list(bob_bases)
            st.session_state["bob_results"] = results

            st.success("Measurement completed.")

            m1, m2, m3 = st.columns(3)

            with m1:
                st.metric("Bits Received", n)

            with m2:
                st.metric("Z Bases", bob_bases.count("Z"))

            with m3:
                st.metric("X Bases", bob_bases.count("X"))

            st.markdown("### 📄 Bob Output")

            st.info(f"Bases: {bob_bases}")
            st.info(f"Measured Bits: {''.join(map(str, results))}")

            if eve_on:
                st.error("⚠️ Eve Intercepted Transmission")

            if noise_on:
                st.warning("📡 Noise Applied")

            if qiskit_on:
                st.success("⚛️ Measured using Qiskit Quantum Circuits")