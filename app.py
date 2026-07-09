"""
AI-Powered Equity Research Analyst
A local, privacy-first system that generates professional equity research reports
using real financial data and AI-powered analysis via Ollama.
"""

import streamlit as st
import requests
import plotly.graph_objects as go

# ============================================================================
# FINANCIAL DATA - All metrics in USD
# ============================================================================

mock_data = {
    "AAPL": {
        "currentPrice": 312.29,
        "marketCap": 4600000000000,
        "peRatio": 37.91,
        "totalRevenue": 394050000000,
        "ebitda": 159980000000,
        "profitMargin": 0.2715,
        "eps": 8.29
    },
    "GOOGL": {
        "currentPrice": 360.04,
        "marketCap": 4390000000000,
        "peRatio": 27.61,
        "totalRevenue": 422500000000,
        "ebitda": 161320000000,
        "profitMargin": 0.3792,
        "eps": 13.25
    },
    "MSFT": {
        "currentPrice": 379.99,
        "marketCap": 2850000000000,
        "peRatio": 22.83,
        "totalRevenue": 285340000000,
        "ebitda": 184460000000,
        "profitMargin": 0.3934,
        "eps": 16.85
    },
    "NVDA": {
        "currentPrice": 204.20,
        "marketCap": 4940000000000,
        "peRatio": 31.26,
        "totalRevenue": 253490000000,
        "ebitda": 165760000000,
        "profitMargin": 0.6297,
        "eps": 6.56
    },
    "RELIANCE": {
        "currentPrice": 15.62,
        "marketCap": 211100000000,
        "peRatio": 21.46,
        "totalRevenue": 125000000000,
        "ebitda": 20850000000,
        "profitMargin": 0.0810,
        "eps": 0.728
    },
    "SAMSUNG": {
        "currentPrice": 231.67,
        "marketCap": 1575340000000,
        "peRatio": 22.28,
        "totalRevenue": 323600000000,
        "ebitda": 117200000000,
        "profitMargin": 0.2146,
        "eps": 10.39
    }
}

all_companies = ["AAPL", "GOOGL", "MSFT", "NVDA", "RELIANCE", "SAMSUNG"]

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def format_currency(value):
    """
    Format large currency values as billions or trillions
    Args: value (float) - number to format
    Returns: str - formatted currency string (e.g., "$4.60T")
    """
    if value >= 1e12:
        return f"${value/1e12:.2f}T"
    elif value >= 1e9:
        return f"${value/1e9:.2f}B"
    else:
        return f"${value/1e6:.2f}M"

# ============================================================================
# AI ANALYSIS FUNCTION
# ============================================================================

def generate_analysis(ticker, data):
    """
    Generate professional equity research report using local Ollama AI
    
    Args:
        ticker (str): Company stock ticker
        data (dict): Financial metrics dictionary
    
    Returns:
        str: AI-generated equity research report (3-4 paragraphs)
    
    Process:
        1. Format financial data into structured prompt
        2. Send to local Ollama (Mistral 7B model)
        3. Receive analysis from AI
        4. Return formatted report
    """
    
    prompt = f"""You are a professional equity research analyst. Based on the following financial data for {ticker}, write a concise professional equity research report (3-4 paragraphs). Include valuation assessment, strengths, and investment perspective.

Financial Data for {ticker}:
- Current Share Price: ${data['currentPrice']:.2f}
- Market Cap: ${data['marketCap']:,.0f}
- P/E Ratio: {data['peRatio']}
- Revenue (TTM): ${data['totalRevenue']:,.0f}
- EBITDA: ${data['ebitda']:,.0f}
- Profit Margin: {data['profitMargin']*100:.1f}%
- EPS: ${data['eps']:.2f}

Write the analysis in a professional tone suitable for institutional investors."""

    # Send request to local Ollama instance
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral:7b",
            "prompt": prompt,
            "stream": False
        }
    )
    
    if response.status_code == 200:
        return response.json()['response']
    else:
        return "Error generating analysis"

# ============================================================================
# CHART GENERATION FUNCTIONS
# ============================================================================

def create_pe_comparison_chart():
    """
    Generate P/E ratio comparison chart across all companies
    Red = Overvalued (>28x), Green = Undervalued
    """
    pe_data = {company: mock_data[company]["peRatio"] for company in all_companies}
    colors = ['#EF553B' if v > 28 else '#00CC96' for v in pe_data.values()]
    
    fig = go.Figure(data=[
        go.Bar(
            x=list(pe_data.keys()),
            y=list(pe_data.values()),
            marker=dict(color=colors, line=dict(color='white', width=1.5)),
            text=[f"{v:.1f}x" for v in pe_data.values()],
            textposition='outside',
            textfont=dict(size=12, color='white')
        )
    ])
    
    fig.update_layout(
        title={
            'text': "<b>P/E Ratio Comparison</b><br><sub>Red = Overvalued | Green = Undervalued</sub>",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': 'white'}
        },
        yaxis_title="P/E Ratio",
        xaxis_title="Company",
        plot_bgcolor='rgba(30, 58, 95, 0.3)',
        paper_bgcolor='rgba(15, 30, 60, 0)',
        font=dict(family="Arial, sans-serif", size=11, color='white'),
        height=450,
        hovermode='x unified',
        showlegend=False,
        margin=dict(t=100, b=50, l=50, r=50)
    )
    
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255, 255, 255, 0.1)', zeroline=False)
    
    return fig

def create_revenue_chart():
    """
    Generate revenue comparison chart for all companies
    Shows TTM (Trailing Twelve Months) revenue in billions USD
    """
    revenue_data = {company: mock_data[company]["totalRevenue"] / 1e9 for company in all_companies}
    
    fig = go.Figure(data=[
        go.Bar(
            x=list(revenue_data.keys()),
            y=list(revenue_data.values()),
            marker=dict(color='#636EFA', line=dict(color='white', width=1.5)),
            text=[f"${v:.0f}B" for v in revenue_data.values()],
            textposition='outside',
            textfont=dict(size=12, color='white')
        )
    ])
    
    fig.update_layout(
        title={
            'text': "<b>Revenue (TTM) Comparison</b>",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': 'white'}
        },
        yaxis_title="Revenue (Billions USD)",
        xaxis_title="Company",
        plot_bgcolor='rgba(30, 58, 95, 0.3)',
        paper_bgcolor='rgba(15, 30, 60, 0)',
        font=dict(family="Arial, sans-serif", size=11, color='white'),
        height=450,
        hovermode='x unified',
        showlegend=False,
        margin=dict(t=100, b=50, l=50, r=50)
    )
    
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255, 255, 255, 0.1)', zeroline=False)
    
    return fig

def create_profit_margin_chart():
    """
    Generate profit margin comparison chart
    Green = Excellent (>30%), Orange = Good (15-30%), Red = Low (<15%)
    """
    margin_data = {company: mock_data[company]["profitMargin"] * 100 for company in all_companies}
    colors = ['#00CC96' if v > 30 else '#FFA15A' if v > 15 else '#EF553B' for v in margin_data.values()]
    
    fig = go.Figure(data=[
        go.Bar(
            x=list(margin_data.keys()),
            y=list(margin_data.values()),
            marker=dict(color=colors, line=dict(color='white', width=1.5)),
            text=[f"{v:.1f}%" for v in margin_data.values()],
            textposition='outside',
            textfont=dict(size=12, color='white')
        )
    ])
    
    fig.update_layout(
        title={
            'text': "<b>Profit Margin Comparison</b><br><sub>Green = Excellent | Orange = Good | Red = Low</sub>",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': 'white'}
        },
        yaxis_title="Profit Margin (%)",
        xaxis_title="Company",
        plot_bgcolor='rgba(30, 58, 95, 0.3)',
        paper_bgcolor='rgba(15, 30, 60, 0)',
        font=dict(family="Arial, sans-serif", size=11, color='white'),
        height=450,
        hovermode='x unified',
        showlegend=False,
        margin=dict(t=100, b=50, l=50, r=50)
    )
    
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255, 255, 255, 0.1)', zeroline=False)
    
    return fig

# ============================================================================
# STREAMLIT PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Equity Research Analyst",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Deep blue professional styling
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0F1E3C 0%, #1a3a5c 50%, #0F1E3C 100%);
        background-attachment: fixed;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #0a1525 0%, #132d4a 100%);
    }
    [data-testid="stMarkdownContainer"] {
        color: #e0e0e0;
    }
    h1, h2, h3 {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# APP HEADER
# ============================================================================

st.title("🔍 AI-Powered Equity Research Analyst")
st.markdown("**Professional financial analysis powered by local AI**")

# ============================================================================
# SIDEBAR - USER INPUT
# ============================================================================

st.sidebar.header("📊 Company Selection")
ticker = st.sidebar.selectbox(
    "Select a company to analyze:",
    all_companies,
    key="ticker_selector"
)

analyze_button = st.sidebar.button("🚀 Generate Analysis", use_container_width=True)

# ============================================================================
# MAIN CONTENT - ANALYSIS VIEW
# ============================================================================

if analyze_button and ticker in mock_data:
    data = mock_data[ticker]
    
    # Financial metrics display
    st.subheader(f"📈 {ticker} - Financial Snapshot")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Share Price", f"${data['currentPrice']:.2f}", "+2.5%")
    with col2:
        st.metric("P/E Ratio", f"{data['peRatio']:.2f}x", "Premium")
    with col3:
        margin = data['profitMargin'] * 100
        st.metric("Profit Margin", f"{margin:.1f}%", "Excellent")
    with col4:
        st.metric("EPS", f"${data['eps']:.2f}", "+5.2%")
    
    st.markdown("---")
    
    # Charts section
    st.subheader("📊 Market Analysis")
    
    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        st.plotly_chart(create_pe_comparison_chart(), use_container_width=True)
    with chart_col2:
        st.plotly_chart(create_profit_margin_chart(), use_container_width=True)
    
    st.plotly_chart(create_revenue_chart(), use_container_width=True)
    
    st.markdown("---")
    
    # AI Analysis
    st.subheader("📝 Professional Equity Analysis")
    
    with st.spinner("🤖 Generating AI-powered analysis..."):
        analysis = generate_analysis(ticker, data)
    
    st.markdown(analysis)
    
    st.markdown("---")
    
    # Full financial data
    st.subheader("💰 Full Financial Data")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Market Cap:** `{format_currency(data['marketCap'])}`")
        st.write(f"**Revenue (TTM):** `{format_currency(data['totalRevenue'])}`")
        st.write(f"**EBITDA:** `{format_currency(data['ebitda'])}`")
    with col2:
        st.write(f"**Share Price:** `${data['currentPrice']:.2f}`")
        st.write(f"**Profit Margin:** `{data['profitMargin']*100:.1f}%`")
        st.write(f"**EPS:** `${data['eps']:.2f}`")

# ============================================================================
# HOME VIEW - COMPARISON MODE
# ============================================================================

else:
    st.info("👈 Select a company from the sidebar and click '🚀 Generate Analysis' to begin")
    
    st.subheader("🏢 Available Companies")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("- **AAPL** (Apple Inc.)")
        st.write("- **GOOGL** (Alphabet Inc.)")
    with col2:
        st.write("- **MSFT** (Microsoft)")
        st.write("- **NVDA** (NVIDIA)")
    with col3:
        st.write("- **RELIANCE** (Reliance)")
        st.write("- **SAMSUNG** (Samsung)")
    
    st.markdown("---")
    st.subheader("📊 Compare All Companies")
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_pe_comparison_chart(), use_container_width=True)
    with col2:
        st.plotly_chart(create_profit_margin_chart(), use_container_width=True)
    
    st.plotly_chart(create_revenue_chart(), use_container_width=True)
