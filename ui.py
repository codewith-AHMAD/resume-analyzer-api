import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Resume Analyzer", layout="wide")

# ---- HEADER ----
st.markdown("<h1 style='text-align: center;'>📄 Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("---")

# ---- INPUT SECTION ----
col1, col2 = st.columns(2)

with col1:
    option = st.radio("Select Input Type", ["Text", "PDF"])

with col2:
    st.info("Analyze resumes using AI-powered backend 🚀")

st.markdown("---")

# ---- TEXT INPUT ----
if option == "Text":
    text = st.text_area("Paste Resume Text", height=200)

    if st.button("Analyze Resume"):
        if text.strip() == "":
            st.warning("Please enter some text")
        else:
            with st.spinner("Analyzing..."):
                response = requests.post(
                    f"{API_URL}/analyze",
                    json={"text": text}
                )

            if response.status_code == 200:
                data = response.json()

                st.success("Analysis Complete!")

                # ---- RESULTS ----
                col1, col2, col3 = st.columns(3)

                col1.metric("Score", data["score"])
                col2.metric("Skills Found", len(data["skills_found"]))
                col3.metric("Missing Skills", len(data["missing_skills"]))

                st.markdown("---")

                st.subheader("✅ Skills Found")
                st.write(data["skills_found"])

                st.subheader("⚠️ Missing Skills")
                st.write(data["missing_skills"])

                st.subheader("💡 Suggestions")
                for s in data["suggestions"]:
                    st.write(f"- {s}")

# ---- PDF INPUT ----
elif option == "PDF":
    file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    if file and st.button("Analyze PDF"):
        with st.spinner("Processing PDF..."):
            response = requests.post(
                f"{API_URL}/analyze-pdf",
                files={"file": file}
            )

        if response.status_code == 200:
            data = response.json()

            st.success("Analysis Complete!")

            col1, col2, col3 = st.columns(3)

            col1.metric("Score", data["score"])
            col2.metric("Skills Found", len(data["skills_found"]))
            col3.metric("Missing Skills", len(data["missing_skills"]))

            st.markdown("---")

            st.subheader("✅ Skills Found")
            st.write(data["skills_found"])

            st.subheader("⚠️ Missing Skills")
            st.write(data["missing_skills"])

            st.subheader("💡 Suggestions")
            for s in data["suggestions"]:
                st.write(f"- {s}")