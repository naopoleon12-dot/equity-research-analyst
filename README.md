# 🔍 AI-Powered Equity Research Analyst

A local, privacy-first equity research system that combines financial data analysis with AI-powered insights. Generates professional investment reports in seconds using on-device AI models.

## 🎯 Project Overview

This system automates equity research analysis by:
1. **Fetching real financial data** for companies
2. **Analyzing metrics** with intelligent color-coding (red/green valuation signals)
3. **Generating professional reports** using local AI (Ollama + Mistral 7B)
4. **Visualizing comparisons** across multiple companies with professional charts

**All processing happens locally on your Mac. Zero data leaves your computer.**

## ✨ Key Features

- **6 Companies Supported:** AAPL, GOOGL, MSFT, NVDA, RELIANCE, SAMSUNG
- **Professional Charts:** P/E ratio, revenue, and profit margin comparisons
- **AI-Powered Analysis:** Generates detailed equity research reports using local AI
- **Color-Coded Metrics:** Red (bad) / Green (good) / Blue (neutral) visual indicators
- **Real Financial Data:** All figures in USD for fair comparison
- **Privacy-First:** Runs entirely on your machine using Ollama local models
- **Interactive Web UI:** Built with Streamlit for easy exploration

## 🛠️ Tech Stack

- **Python 3.14+** — Core language
- **Streamlit** — Web UI framework
- **Plotly** — Professional data visualization
- **Ollama (Mistral 7B)** — Local AI model for analysis
- **Requests** — HTTP library for API calls

## 📊 How It Works
User selects company →
Fetches financial metrics →
Sends to local Ollama AI →
AI generates professional report →
Displays with charts & analysis

## 🚀 Setup Instructions

### Prerequisites
- macOS with M-series chip (M5 Air or better)
- Python 3.10+
- Ollama installed and running (download from https://ollama.ai)

### Installation

1. **Clone or download this project**
```bash
   cd equity_analyst
```

2. **Create virtual environment**
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. **Install dependencies**
```bash
   pip install streamlit requests plotly
```

4. **Ensure Ollama is running**
   - Open Ollama app on your Mac
   - Verify Mistral 7B model is installed: `ollama list`
   - If not: `ollama pull mistral:7b`

5. **Start the application**
```bash
   streamlit run app.py
```

6. **Open in browser**
http://localhost:8501

## 📖 Usage

1. Select a company from the sidebar dropdown
2. Click "🚀 Generate Analysis"
3. View financial snapshot, charts, and AI-generated equity research report
4. Explore comparison charts on the home page

## 📁 Project Structure
equity_analyst/
├── app.py              # Main Streamlit application
├── main.py             # Terminal-based version
├── README.md           # This file
└── venv/               # Python virtual environment

## 📊 Financial Metrics Included

- **Share Price** — Current stock price
- **Market Cap** — Total market capitalization
- **P/E Ratio** — Price-to-earnings valuation multiple
- **Revenue (TTM)** — Trailing twelve-month revenue
- **EBITDA** — Operating profitability
- **Profit Margin** — Net profit margin percentage
- **EPS** — Earnings per share

## 🎨 Data Visualization

The system generates three types of charts:

1. **P/E Ratio Comparison** — Red (overvalued >28x) vs Green (undervalued)
2. **Revenue Comparison** — Total revenue across all companies
3. **Profit Margin Comparison** — Green (excellent >30%), Orange (good 15-30%), Red (low <15%)

## 🤖 AI Integration

Reports are generated using:
- **Model:** Ollama Mistral 7B (4.4 GB)
- **Running:** Entirely on your local machine
- **Purpose:** Professional equity research analysis
- **Output:** Institutional-grade investment insights

## 🔒 Privacy & Security

✅ All data processing happens locally
✅ No API calls to external services
✅ No data stored on cloud
✅ No user tracking
✅ Fully offline capable (except initial Ollama setup)

## 🚀 Future Enhancements

- Real-time data integration with Alpha Vantage API
- Additional financial metrics (debt ratios, ROE, etc.)
- Multi-model support (switch between AI models)
- Export reports to PDF
- Historical data tracking
- Industry comparison benchmarks

## 📚 What I Learned Building This

This project demonstrates:
- **Systems Design:** Integrating data retrieval, AI processing, and visualization
- **Finance Knowledge:** Understanding equity metrics and valuation analysis
- **AI/ML:** Working with local models, prompt engineering, API integration
- **Full-Stack Development:** Backend logic + frontend UI + data visualization
- **Python Proficiency:** Virtual environments, libraries, error handling

## 🎓 Why This Project Stands Out

Unlike simply using ChatGPT or Claude, this project shows:
1. **Custom Architecture** — Built an integrated system, not just a prompt
2. **Local AI** — Privacy-first approach using on-device models
3. **Data Integration** — Combines multiple data sources intelligently
4. **Professional Output** — Financial-grade visualizations and reports
5. **Scalability** — Foundation for adding more companies, metrics, and models

## 📝 License

Personal portfolio project. Feel free to use as reference or learning material.

## 👨‍💻 Author

Built by a Grade 12 CBSE student interested in finance and AI systems.
- **Background:** Equity research intern, DEFINE Finance Club co-founder
- **Goal:** Demonstrating practical AI + finance knowledge integration

---

**Want to run this yourself?**

Follow the Setup Instructions above. Takes 5 minutes.

**Questions?** Check the setup or examine the code comments in app.py.
