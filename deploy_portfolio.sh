#!/bin/bash
# Deployment script untuk Portfolio App

echo "🚀 Deploying Supply Chain Portfolio App..."

# 1. Create separate directory
mkdir -p portfolio_app
cd portfolio_app

# 2. Copy files
cp ../portfolio_app.py .
cp ../requirements_portfolio.txt .

# 3. Create Streamlit config
echo "[server]
headless = true
port = 8502
enableCORS = false
" > .streamlit/config.toml

echo "✅ Portfolio app setup complete!"
echo "📁 Directory: portfolio_app/"
echo "📄 Main file: portfolio_app.py"
echo "📦 Requirements: requirements_portfolio.txt"

echo ""
echo "🔧 To run locally:"
echo "   streamlit run portfolio_app.py --server.port 8502"
echo ""
echo "🌐 To deploy to Streamlit Cloud:"
echo "   1. Push to GitHub"
echo "   2. Go to share.streamlit.io"
echo "   3. Connect repository"
echo "   4. Set main file: portfolio_app.py"
