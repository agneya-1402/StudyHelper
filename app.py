import streamlit as st
from google import genai
import PyPDF2

st.set_page_config(page_title="Study Helper - Atharva College", layout="centered")

# Sidebar  
st.sidebar.header("📘 Study Helper Instructions")
st.sidebar.markdown(
    "1. Enter your Gemini API key. You can get one from [AI Studio API Key](https://aistudio.google.com/apikey).  "
    "\n2. Select your branch, year, semester, subject, and modules.  \n"
    "3. (Optional) Upload your syllabus and past question papers in PDF.  \n"
    "4. Click **Generate Important Questions** to get 30 key questions.  \n"
)

# Main Title 
st.title("📘 Study Helper - Atharva College of Engineering")

# Inputs 
api_key = st.text_input("🔑 Your Gemini API Key", type="password")

branch = st.selectbox(
    "📚 Branch", 
    ["CMPN", "IT", "EXTC", "ECS", "Electrical", "Other"]
)
if branch == "Other":
    branch = st.text_input("📚 Enter Your Branch Name")

year    = st.selectbox("🎓 Year", ["FE", "SE", "TE", "BE"])
sem     = st.selectbox("🗓️ Semester", [str(i) for i in range(1,9)])
subject = st.text_input("📝 Subject")
modules = st.text_area("📦 Modules (comma-separated)")

syllabus_pdf       = st.file_uploader("📄 Syllabus PDF (optional)", type="pdf")
question_paper_pdf = st.file_uploader("📄 Previous Year Papers (optional)", type="pdf")

# PDF Text Extraction 
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

# Generate
def generate_questions(prompt: str, key: str) -> str:
    client = genai.Client(api_key=key)
    resp = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return resp.text

if st.button("🔍 Generate Important Questions"):
    if not api_key or not subject.strip() or not branch.strip():
        st.warning("Please enter your Gemini API key, branch, and subject.")
        st.stop()

    st.info("⏳ Extracting texts…")
    syllabus_text = extract_text_from_pdf(syllabus_pdf) if syllabus_pdf else ""
    question_paper_text = extract_text_from_pdf(question_paper_pdf) if question_paper_pdf else ""

    prompt = f"""
    You are an expert Mumbai University engineering professor. Based on:
    • Branch: {branch}  
    • Year: {year}, Sem: {sem}  
    • Subject: "{subject}"  
    • Modules: {modules}

    Syllabus (if provided):
    {syllabus_text}

    Previous papers (if provided):
    {question_paper_text}

    Generate the **30 most important and frequently repeating exam questions** as bullet points only.
    """

    try:
        st.info("⏳ Generating questions via Gemini...")
        questions = generate_questions(prompt, api_key)
        st.success("✅ Here are your 30 questions:")
        st.markdown(questions)
        st.text_area("📋 Copy All Questions", questions, height=300)
    except Exception as e:
        st.error(f"❌ Generation Failed!: {e}")
