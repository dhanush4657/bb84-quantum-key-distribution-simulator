# pages/results.py   (FULL UPGRADE)

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Security Analysis Dashboard")

# ---------- Styling ----------
st.markdown("""
<style>
thead tr th, tbody tr td {
    text-align:center !important;
}
table {
    margin-left:auto !important;
    margin-right:auto !important;
}
</style>
""", unsafe_allow_html=True)

if "bob_results" not in st.session_state:
    st.warning("Complete Alice and Bob steps first.")
else:
    alice_bits = st.session_state["alice_bits"]
    alice_bases = st.session_state["alice_bases"]
    bob_bases   = st.session_state["bob_bases"]
    bob_bits    = st.session_state["bob_results"]

    eve_used   = st.session_state.get("eve_used", False)
    noise_used = st.session_state.get("noise_used", False)

    rows = []
    match_positions = []

    for i in range(len(alice_bits)):
        keep = alice_bases[i] == bob_bases[i]

        if keep:
            match_positions.append(i)

        rows.append({
            "Pos": i + 1,
            "Alice Bit": alice_bits[i],
            "Alice Basis": alice_bases[i],
            "Bob Basis": bob_bases[i],
            "Bob Bit": bob_bits[i],
            "Keep": "✅" if keep else "❌"
        })

    # ---------- Table ----------
    left, mid, right = st.columns([1,4,1])

    with mid:
        st.subheader("🔍 Basis Comparison Table")
        df = pd.DataFrame(rows)
        st.table(df)

    st.markdown("---")

    if len(match_positions) == 0:
        st.error("No matching bases found.")

    else:
        # ---------- Real Error ----------
        errors = 0

        for i in match_positions:
            if alice_bits[i] != bob_bits[i]:
                errors += 1

        rate = errors / len(match_positions)

        status = "✅ Secure Communication"
        if rate > 0.15:
            status = "⚠️ Eve / Noise Detected"

        # ---------- Final Keys ----------
        alice_key = "".join(str(alice_bits[i]) for i in match_positions)
        bob_key   = "".join(str(bob_bits[i]) for i in match_positions)

        # ---------- Metrics ----------
        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("Matching Bases", len(match_positions))

        with c2:
            st.metric("Errors", errors)

        with c3:
            st.metric("Error Rate", f"{rate*100:.2f}%")

        with c4:
            st.metric("Key Length", len(alice_key))

        st.info(status)

        # ---------- Charts ----------
        chart_df = pd.DataFrame({
            "Metric": ["Matching", "Errors", "Correct"],
            "Value": [
                len(match_positions),
                errors,
                len(match_positions) - errors
            ]
        })

        fig = px.bar(
            chart_df,
            x="Metric",
            y="Value",
            text="Value",
            title="Transmission Analytics"
        )

        fig.update_layout(height=450)

        st.plotly_chart(fig, use_container_width=True)

        # ---------- Eve / Noise ----------
        x1, x2 = st.columns(2)

        with x1:
            st.metric("Eve Mode", "ON 😈" if eve_used else "OFF ✅")

        with x2:
            st.metric("Noise Mode", "ON 📡" if noise_used else "OFF ✅")

        # ---------- Final Key ----------
        st.markdown("### 🔐 Final Secret Key")

        a, b = st.columns(2)

        with a:
            st.success(f"Alice Key: {alice_key}")

        with b:
            st.success(f"Bob Key: {bob_key}")

        # ---------- CSV Export ----------
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Results CSV",
            data=csv,
            file_name="bb84_results.csv",
            mime="text/csv"
        )

        if alice_key == bob_key and alice_key != "":
            st.balloons()