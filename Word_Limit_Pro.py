import streamlit as st
import PyPDF2
import docx

def count_words(text):
    return len(text.split())

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + " "
    return text.strip()

def read_docx(file):
    doc = docx.Document(file)
    text = " ".join([para.text for para in doc.paragraphs])
    return text.strip()

# UI Setup
st.set_page_config(page_title="Essay Validator", page_icon="📄", layout="centered")
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .css-1d391kg {text-align: center;}
    </style>
    """, unsafe_allow_html=True)

st.title("📄 Essay Word Count Validator")
st.write("Upload your essay as a PDF or Word document to check if it meets the word count requirement.  \n**Between 250 and 3,000 words.**")

# Session state to manage file upload clearing
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

# Only show file uploader if no file has been uploaded
if st.session_state.uploaded_file is None:
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx"], help="Only PDF and DOCX files are supported.")
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file  # Store file in session state

if st.session_state.uploaded_file is not None:
    file_extension = st.session_state.uploaded_file.name.split(".")[-1].lower()
    text = ""
    
    if file_extension == "pdf":
        text = read_pdf(st.session_state.uploaded_file)
    elif file_extension == "docx":
        text = read_docx(st.session_state.uploaded_file)
    else:
        st.error("❌ Unsupported file type. Please upload a PDF or Word document.")
    
    if text:
        word_count = count_words(text)
        st.markdown(f"### Word Count: **{word_count}**")
        
        if word_count < 250:
            st.error("❌ Unsuccessful - Essay is less than 250 words.")
        elif word_count > 3000:
            st.error("❌ Unsuccessful - Essay is more than 3000 words.")
        else:
            st.success("✅ Successful - Your essay meets the word count requirement!")
    else:
        st.error("⚠️ Failed to extract text. Ensure the document contains selectable text.")

    # Add a button to clear file uploader
    if st.button("Clear File"):
        st.session_state.uploaded_file = None
        st.rerun()
