import streamlit as st
import pandas as pd
from enricher import enrich_companies

st.set_page_config(page_title="AI Lead Enrichment Bot", layout="wide")
st.title("AI-Powered Lead Enrichment Bot")
st.markdown("Upload a CSV of company names and get enriched data powered by **Gemini AI**.")

uploaded_file = st.file_uploader("Upload your companies CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Companies:")
    st.dataframe(df)

    if st.button("Run Enrichment"):
        with st.spinner("Processing companies... This may take a few minutes."):
            df.to_csv("input.csv", index=False)
            output_path = enrich_companies()

        st.success("Enrichment complete!")
        with open(output_path, "rb") as f:
            st.download_button("Download Enriched CSV", f, file_name=output_path)

        result_df = pd.read_csv(output_path)
        st.subheader("Enriched Data:")
        st.dataframe(result_df)