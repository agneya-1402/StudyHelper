## Study Helper - Atharva College of Engineering

A Streamlit web application that generates the 30 most important and frequently repeating exam questions based on the Mumbai University syllabus and past question papers, powered by Google Gemini (gemini-2.0-flash).

---

## Try it Out



### Features

* **Gemini API Integration**: Uses Google Gemini Flash model (`gemini-2.0-flash`) for content generation.
* **Custom Inputs**: Select branch (with ‘Other’ option), year, semester, subject, and modules.
* **PDF Upload**: Optionally upload syllabus and past question papers in PDF format.
* **Question Generation**: Generates 30 key exam questions as bullet points.
* **Copy Function**: Copy all generated questions with a single click.
* **Sidebar Guidance**: Step-by-step instructions and link to acquire a Gemini API key.

### Requirements

* Python 3.8+
* Streamlit
* google-genai (Google Gemini client)
* PyPDF2

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/agneya-1402/StudyHelper.git
   cd StudyHelper
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install streamlit google-genai PyPDF2
   ```

### Usage

1. **Run the app**

   ```bash
   streamlit run app.py
   ```

2. **Sidebar Instructions**

   * Enter your Gemini API key (get one at [AI Studio API Key](https://aistudio.google.com/apikey)).
   * Select or enter your branch, year, semester, subject, and modules.
   * (Optional) Upload syllabus and previous question papers in PDF.
   * Click **Generate Important Questions**.

3. **View Results**

   * The app displays 30 generated questions.
   * Use the **Copy All Questions** box to copy for your notes.

### Contributing

Contributions are welcome! Please fork the repo, create a feature branch, and open a pull request.

### License

This project is licensed under the MIT License. Feel free to use, modify, and distribute.
