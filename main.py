import requests

# Real financial data for 6 companies
mock_data = {
    "AAPL": {
        "currentPrice": 312.29,
        "marketCap": "4600000000000",
        "peRatio": "37.91",
        "totalRevenue": "394050000000",
        "ebitda": "159980000000",
        "profitMargin": "0.2715",
        "eps": "8.29"
    },
    "GOOGL": {
        "currentPrice": 360.04,
        "marketCap": "4390000000000",
        "peRatio": "27.61",
        "totalRevenue": "422500000000",
        "ebitda": "161320000000",
        "profitMargin": "0.3792",
        "eps": "13.25"
    },
    "MSFT": {
        "currentPrice": 379.99,
        "marketCap": "2850000000000",
        "peRatio": "22.83",
        "totalRevenue": "285340000000",
        "ebitda": "184460000000",
        "profitMargin": "0.3934",
        "eps": "16.85"
    },
    "NVDA": {
        "currentPrice": 204.20,
        "marketCap": "4940000000000",
        "peRatio": "31.26",
        "totalRevenue": "253490000000",
        "ebitda": "165760000000",
        "profitMargin": "0.6297",
        "eps": "6.56"
    },
    "RELIANCE": {
        "currentPrice": 1280.90,
        "marketCap": "17310000000000",
        "peRatio": "21.46",
        "totalRevenue": "10250000000000",
        "ebitda": "1710000000000",
        "profitMargin": "0.0810",
        "eps": "59.70"
    },
    "SAMSUNG": {
        "currentPrice": 278000,
        "marketCap": "1890410000000",
        "peRatio": "22.28",
        "totalRevenue": "388340000000",
        "ebitda": "140630000000",
        "profitMargin": "0.2146",
        "eps": "12462"
    }
}

def generate_analysis(ticker, data):
    """Use Ollama to generate professional analysis"""
    
    prompt = f"""You are a professional equity research analyst. Based on the following financial data for {ticker}, write a concise professional equity research report (3-4 paragraphs). Include valuation assessment, strengths, and investment perspective.

Financial Data for {ticker}:
- Current Share Price: {data['currentPrice']}
- Market Cap: {data['marketCap']}
- P/E Ratio: {data['peRatio']}
- Revenue (TTM): {data['totalRevenue']}
- EBITDA: {data['ebitda']}
- Profit Margin: {data['profitMargin']}
- EPS: {data['eps']}

Write the analysis in a professional tone suitable for institutional investors."""

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

ticker = input("Enter stock ticker (AAPL, GOOGL, MSFT, NVDA, RELIANCE, or SAMSUNG): ").upper()

if ticker in mock_data:
    data = mock_data[ticker]
    
    print(f"\n=== {ticker} Stock Data ===")
    print(f"Share Price: {data['currentPrice']}")
    print(f"Market Cap: {data['marketCap']}")
    print(f"P/E Ratio: {data['peRatio']}")
    print(f"Revenue: {data['totalRevenue']}")
    print(f"EBITDA: {data['ebitda']}")
    print(f"Profit Margin: {data['profitMargin']}")
    print(f"EPS: {data['eps']}")
    
    print("\nGenerating AI Analysis...")
    analysis = generate_analysis(ticker, data)
    
    print(f"\n=== Professional Equity Analysis ===\n{analysis}")
else:
    print(f"Ticker {ticker} not found")
