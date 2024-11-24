# Stocky AI - Stock Analysis Application 🚀

Stocky AI is an intelligent stock analysis application that helps users research and analyze companies using AI-powered insights. Built with Streamlit and powered by AI agents, it provides comprehensive stock analysis and research capabilities.

## Features ✨

- Company research and analysis powered by AI agents
- Real-time stock data analysis and visualization
- Automated PDF report generation with company logos and branding
- Clean and intuitive Streamlit web interface
- Multi-agent system for in-depth analysis:
  - Research Analyst: Gathers company information and news
  - Financial Analyst: Analyzes financial metrics and performance
  - Investment Advisor: Provides investment recommendations

## Getting Started 🛠️

1. Clone the repository:

   ```bash
   git clone https://github.com/shivatmax/STOCKY.git
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Required Python version:

   - Python >= 3.12 and <= 3.13

4. Main dependencies:

   - crewai[tools] >= 0.41.1
   - python-dotenv >= 1.0.1
   - html2text >= 2024.2.26
   - sec-api >= 1.0.20
   - setuptools >= 75.6.0

5. Set up environment variables:
   Create a `.env` file in the root directory with:
   ```bash
   SERPER_API_KEY=your_serper_api_key # https://serper.dev/ (free tier)
   SEC_API_API_KEY=your_sec_api_key # https://sec-api.io/ (free tier)
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage 📱

1. Start the application:

   ```bash
   streamlit run src/stock_analysis/main.py
   ```

2. Enter a company name in the search box

3. Click "Generate Stock Report" to analyze the company

4. View the comprehensive analysis and download the PDF report

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Thanks to the Streamlit team for the amazing framework
- OpenAI for providing the AI capabilities
- All contributors who help improve this project
