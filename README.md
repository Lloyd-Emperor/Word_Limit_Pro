# 📄 Word Limit Pro

**Word Limit** is a simple and efficient Streamlit web application that allows users to upload essays in PDF or Word format and checks whether they meet the required word count range (250 to 3,000 words).

## 🚀 Features
- Supports **PDF (.pdf) and Word (.docx)** file uploads.
- Accurately counts the words in an uploaded document.
- Displays success or failure messages based on word count limits.
- User-friendly interface with a **Clear File** button for multiple file uploads.
- Works seamlessly on both **desktop and mobile**.

## 🛠️ Installation
Ensure you have Python installed, then follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Lloyd-Emperor/Word_Limit_Pro.git
   cd word-limit
   ```
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the app:**
   ```sh
   streamlit run word_count.py
   ```

## 📌 Usage
1. Upload a PDF or Word document.
2. The app will process the file and display the word count.
3. If the essay contains **less than 250 words**, it will show an unsuccessful message.
4. If the essay exceeds **3,000 words**, it will also show an unsuccessful message.
5. If the essay is within the valid range, it will display a success message.
6. Click the **Clear File** button to reset and upload a new document.

## 📷 Screenshots
![Word Limit Screenshot](screenshot.png)

## 🛡️ Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **Libraries:** PyPDF2, python-docx

## 📜 License
This project is open-source and available under the **MIT License**.

## 🤝 Contributing
Contributions are welcome! If you’d like to improve the app, feel free to fork the repo and submit a pull request.

## 📬 Contact
For any questions or feedback, reach out via email at **honourakhigbe@gmail.com** or open an issue on GitHub.

---
Made with ❤️ by [Akhigbe Honour]

