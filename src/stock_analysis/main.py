import os
import shutil
import time
import streamlit as st
from crew import StockAnalysisCrew
from tools.BingDownloader.bingimage import CompanyLogo
from markdown_pdf import MarkdownPdf, Section

st.set_page_config(layout="wide")

# Add image to Streamlit app
image_path = "src\stock_analysis\images\stocky3-b.png"

col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    st.write(" ")
with col2:
    st.image(image_path, width=400)
with col3:
    st.write(" ")

# Add custom CSS styles
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #D1F7FF;
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .title {
        font-size: 36px;
        color: #3366ff;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 24px;
        color: #666666;
        margin-bottom: 10px;
    }
    .button {
        background-color: #3366ff;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add custom styling to the app
st.markdown("<h1 class='title'>Stocky AI!!</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>Hi !! I'm Stocky, the AI Stock Researcher and Analyst! 😄</p>",
    unsafe_allow_html=True,
)

# Get user input for the topic
topic = st.text_input("Enter the Name of Company")

# Check if the topic is provided
if topic:
    logo = CompanyLogo(topic)
    time.sleep(5)
    company_logo = str(logo)

    col1, col2, col3 = st.columns([1, 0.5, 1])
    with col1:
        st.image(company_logo, caption=topic + " Company", width=200)
    with col2:
        st.write("")
    with col3:
        st.write("")
        st.write("")
        generate_report = st.button(
            f"Generate {topic} stock report", key="generate_report"
        )
        st.write("")

    if generate_report:
        with st.spinner(f"Generating {topic} stock report..."):
            inputs = {
                "query": "What is the company you want to analyze?",
                "company_stock": topic,
            }
            result = StockAnalysisCrew().crew().kickoff(inputs=inputs)

            st.markdown(
                "<h2 class='subtitle'>Stock Report</h2>", unsafe_allow_html=True
            )
            st.write(result)

            # Create PDF using markdown-pdf
            pdf = MarkdownPdf(toc_level=2)

            # Add title section
            pdf.add_section(Section(f"# {topic} Stock Analysis Report\n", toc=False))

            # Add logo section
            pdf.add_section(Section(f"![{topic} Logo]({company_logo})\n\n"))

            # Add report content section
            report_content = str(result).replace("**", "")
            pdf.add_section(Section(report_content))

            # Set PDF metadata
            pdf.meta["title"] = f"{topic} Stock Analysis Report"
            pdf.meta["author"] = "Stocky AI"

            # Save PDF
            pdf.save(f"{topic}_stock_report.pdf")

            # Add download button
            with open(f"{topic}_stock_report.pdf", "rb") as file:
                st.download_button(
                    label="Download Stock Report",
                    data=file.read(),
                    file_name=f"{topic}_stock_report.pdf",
                    mime="application/pdf",
                )

            # Cleanup
            shutil.rmtree("images/company")
            time.sleep(5)
            os.remove(f"{topic}_stock_report.pdf")

else:
    st.write("Please enter a Company Name to generate a stock report. Like Reliance ")
