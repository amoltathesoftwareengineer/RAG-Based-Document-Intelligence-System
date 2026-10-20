
import streamlit as st

from document_loader import extract_text_from_pdf
from text_splitter import split_text
from rag_pipeline import build_rag_index, retrieve_context


st.set_page_config(
    page_title="RAG Document Intelligence",
    page_icon="📚",
    layout="wide",
)

st.title("📚 RAG-Based Document Intelligence System")
st.write("Upload a PDF and ask questions about its contents.")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file is not None:
    try:
        with st.spinner("Reading document..."):
            text = extract_text_from_pdf(uploaded_file)

        chunks = split_text(text)

        if not chunks:
            st.error("No readable text was found in this document.")
            st.stop()

        st.success(f"Document processed: {len(chunks)} text chunks")

        if st.button("Build Search Index"):
            with st.spinner("Creating embeddings and search index..."):
                index, saved_chunks = build_rag_index(chunks)
                st.session_state["rag_index"] = index
                st.session_state["rag_chunks"] = saved_chunks
                st.success("Search index is ready.")

        question = st.text_input("Ask a question about your document")

        if st.button("Search Document"):
            if not question.strip():
                st.warning("Please enter a question.")
            elif "rag_index" not in st.session_state:
                st.warning("Click 'Build Search Index' first.")
            else:
                with st.spinner("Searching relevant passages..."):
                    result = retrieve_context(
                        question,
                        st.session_state["rag_index"],
                        st.session_state["rag_chunks"],
                    )

                st.subheader("Relevant passages")
                if result["context"]:
                    for number, passage in enumerate(
                        result["context"], start=1
                    ):
                        st.markdown(f"**Passage {number}**")
                        st.write(passage)
                else:
                    st.info("No relevant passages were found.")

    except Exception as exc:
        st.error(f"Unable to process the document: {exc}")
