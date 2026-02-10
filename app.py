# ================================
# 🚀 MULYANTO - PREMIUM PORTFOLIO
# ================================
# Features:
# 1. Multi-page navigation
# 2. Interactive project demos
# 3. Live metrics dashboard
# 4. Professional branding
# 5. Mobile responsive
# ================================

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(
    page_title="Mulyanto | Supply Chain AI & Analytics",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =======================
# CUSTOM CSS PREMIUM
# =======================
st.markdown("""
<style>
    /* Professional Color Palette */
    :root {
        --primary: #6366F1;
        --secondary: #8B5CF6;
        --accent: #10B981;
        --dark: #1F2937;
        --light: #F9FAFB;
    }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
    }
    
    .project-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.08);
        border: 1px solid #E5E7EB;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(99, 102, 241, 0.15);
        border-color: var(--primary);
    }
    
    .skill-badge {
        background: linear-gradient(135deg, #E0E7FF 0%, #C7D2FE 100%);
        color: #4338CA;
        padding: 0.5rem 1rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.9rem;
        margin: 0.2rem;
        display: inline-block;
    }
    
    .impact-metric {
        background: linear-gradient(135deg, #D1FAE5 0%, #A7F3D0 100%);
        border-left: 5px solid #10B981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    /* Navigation */
    .st-emotion-cache-1v0mbdj {
        background: white !important;
        border-radius: 15px !important;
        padding: 10px !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05) !important;
    }
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.8s ease-out;
    }
</style>
""", unsafe_allow_html=True)

# =======================
# SIDEBAR NAVIGATION
# =======================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">🚀</div>
        <h2 style="color: #1F2937; margin: 0;">Mulyanto</h2>
        <p style="color: #6B7280; margin: 0;">Supply Chain AI & Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Skills", "Experience", "Contact"],
        icons=["house", "code-slash", "star", "briefcase", "envelope"],
        default_index=0,
        styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "#6366F1", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px"},
            "nav-link-selected": {"background-color": "#6366F1", "font-weight": "600"},
        }
    )

# =======================
# HOME PAGE
# =======================
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h1 class="main-header">Transforming Supply Chains with AI & Data</h1>', unsafe_allow_html=True)
        st.markdown("""
        <div class="fade-in">
            <p style="font-size: 1.2rem; color: #4B5563; line-height: 1.6;">
            Senior Demand Planning & Supply Chain Analytics professional with 10+ years experience 
            driving **80-90% forecast accuracy** and **70% operational efficiency** improvements 
            through AI-powered automation and real-time analytics.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick Stats
        st.markdown("""
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 2rem 0;">
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; font-weight: 800; color: #6366F1;">10+</div>
                <div style="color: #6B7280;">Years Experience</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; font-weight: 800; color: #10B981;">90%</div>
                <div style="color: #6B7280;">Forecast Accuracy</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; font-weight: 800; color: #8B5CF6;">70%</div>
                <div style="color: #6B7280;">Efficiency Gain</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Profile Image Placeholder
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 20px; padding: 2rem; color: white; text-align: center;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">👨‍💼</div>
            <h3 style="margin: 0;">Demand Planning Lead</h3>
            <p style="opacity: 0.9;">Supply Chain Analytics Specialist</p>
            
            <div style="margin-top: 2rem;">
                <button style="background: white; color: #6366F1; border: none; 
                        padding: 0.8rem 1.5rem; border-radius: 10px; font-weight: 600;
                        cursor: pointer; width: 100%;">
                    📥 Download CV
                </button>
            </div>
        </div>
        """, unsafe_allow_html=True)

# =======================
# PROJECTS PAGE
# =======================
elif selected == "Projects":
    st.title("🚀 Featured Projects")
    
    # PROJECT 1
    with st.container():
        st.markdown("""
        <div class="project-card">
            <div style="display: flex; justify-content: space-between; align-items: start;">
                <div>
                    <h2 style="color: #1F2937; margin: 0;">Integrated Supply Chain Command Center</h2>
                    <p style="color: #6B7280; margin: 0.5rem 0;">Python • Streamlit • Plotly • Google Sheets API</p>
                </div>
                <span style="background: #10B981; color: white; padding: 0.3rem 1rem; 
                            border-radius: 20px; font-size: 0.9rem; font-weight: 600;">LIVE</span>
            </div>
            
            <div class="impact-metric">
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;">
                    <div>
                        <div style="font-size: 1.5rem; font-weight: 800; color: #6366F1;">70%</div>
                        <div style="color: #6B7280; font-size: 0.9rem;">Faster Processing</div>
                    </div>
                    <div>
                        <div style="font-size: 1.5rem; font-weight: 800; color: #10B981;">90%</div>
                        <div style="color: #6B7280; font-size: 0.9rem;">Forecast Accuracy</div>
                    </div>
                    <div>
                        <div style="font-size: 1.5rem; font-weight: 800; color: #F59E0B;">$250K</div>
                        <div style="color: #6B7280; font-size: 0.9rem;">Cost Savings</div>
                    </div>
                </div>
            </div>
            
            <p style="color: #4B5563; line-height: 1.6;">
            A unified dashboard bridging Demand Forecasting, Inventory Optimization, and Financial 
            Profitability metrics with real-time visibility on stock health and expiry risks.
            </p>
            
            <div style="margin-top: 1.5rem;">
                <span class="skill-badge">Python Automation</span>
                <span class="skill-badge">Real-time Analytics</span>
                <span class="skill-badge">Inventory Optimization</span>
                <span class="skill-badge">FEFO/FIFO Logic</span>
            </div>
            
            <div style="margin-top: 1.5rem; display: flex; gap: 1rem;">
                <button style="background: #6366F1; color: white; border: none; 
                        padding: 0.7rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer;">
                    ▶️ Live Demo
                </button>
                <button style="background: white; color: #6366F1; border: 2px solid #6366F1; 
                        padding: 0.7rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer;">
                    📖 Case Study
                </button>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # PROJECT 2
    with st.container():
        st.markdown("""
        <div class="project-card">
            <div style="display: flex; justify-content: space-between; align-items: start;">
                <div>
                    <h2 style="color: #1F2937; margin: 0;">Universal Marketplace Order Processor</h2>
                    <p style="color: #6B7280; margin: 0.5rem 0;">Python • Shopee API • Tokopedia • Automation</p>
                </div>
                <span style="background: #10B981; color: white; padding: 0.3rem 1rem; 
                            border-radius: 20px; font-size: 0.9rem; font-weight: 600;">PRODUCTION</span>
            </div>
            
            <div style="background: #FEF3C7; border-left: 5px solid #F59E0B; padding: 1.5rem; border-radius: 12px; margin: 1rem 0;">
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
                    <div>
                        <div style="font-size: 1.5rem; font-weight: 800; color: #D97706;">70%</div>
                        <div style="color: #92400E; font-size: 0.9rem;">Time Reduction</div>
                    </div>
                    <div>
                        <div style="font-size: 1.5rem; font-weight: 800; color: #059669;">100%</div>
                        <div style="color: #065F46; font-size: 0.9rem;">Error Elimination</div>
                    </div>
                </div>
            </div>
            
            <p style="color: #4B5563; line-height: 1.6;">
            Automated order processing engine for multi-marketplace (Shopee, Tokopedia) that 
            standardized raw data, eliminated manual errors, and reduced processing time by 70%.
            </p>
            
            <div style="margin-top: 1.5rem;">
                <span class="skill-badge">API Integration</span>
                <span class="skill-badge">Data Parsing</span>
                <span class="skill-badge">Workflow Automation</span>
                <span class="skill-badge">Error Handling</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# =======================
# SKILLS PAGE
# =======================
elif selected == "Skills":
    st.title("🛠 Technical & Business Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Skills Radar Chart
        st.subheader("📊 Technical Expertise")
        
        categories = ['Python', 'Streamlit', 'Data Viz', 'SAP/ERP', 'Excel', 'SQL']
        values = [9, 8, 8, 7, 9, 7]
        
        fig = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            line_color='#6366F1',
            fillcolor='rgba(99, 102, 241, 0.3)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=False,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Business Competencies")
        
        competencies = {
            "Demand Forecasting": 9,
            "Inventory Optimization": 8,
            "S&OP Leadership": 8,
            "Cross-functional": 9,
            "Process Improvement": 8,
            "Financial Analysis": 7
        }
        
        for skill, level in competencies.items():
            st.markdown(f"""
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                    <span style="font-weight: 600;">{skill}</span>
                    <span style="color: #6366F1; font-weight: 600;">{level}/10</span>
                </div>
                <div style="height: 8px; background: #E5E7EB; border-radius: 4px; overflow: hidden;">
                    <div style="width: {level*10}%; height: 100%; background: linear-gradient(90deg, #6366F1, #8B5CF6);"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# =======================
# EXPERIENCE PAGE
# =======================
elif selected == "Experience":
    st.title("💼 Professional Journey")
    
    # Timeline
    experiences = [
        {
            "company": "PT. GENERO OMNICOM ASIA (ERHA SKINCARE)",
            "role": "Demand Planner Sr. Specialist",
            "period": "Oct 2022 - Present",
            "achievements": [
                "Improved forecast accuracy to 80-90% through advanced data analysis",
                "Developed Forecast & Inventory Control Dashboard using Python/Streamlit",
                "Mitigated overstock and stockout risks for expiry-constrained products"
            ]
        },
        {
            "company": "PT. DUTA INTI DAYA (WATSONS INDONESIA)",
            "role": "Supply Chain Supervisor",
            "period": "Jun 2020 - Oct 2022",
            "achievements": [
                "Optimized inventory levels reducing holding costs by 15%",
                "Streamlined centralized return processes improving efficiency by 25%"
            ]
        },
        # Add more experiences...
    ]
    
    for exp in experiences:
        with st.container():
            st.markdown(f"""
            <div style="background: white; border-radius: 15px; padding: 2rem; margin: 1rem 0; 
                        border-left: 5px solid #6366F1; box-shadow: 0 5px 20px rgba(0,0,0,0.05);">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <h3 style="color: #1F2937; margin: 0;">{exp['role']}</h3>
                        <p style="color: #6366F1; font-weight: 600; margin: 0.3rem 0;">{exp['company']}</p>
                    </div>
                    <span style="background: #E0E7FF; color: #4338CA; padding: 0.3rem 1rem; 
                                border-radius: 20px; font-weight: 600;">{exp['period']}</span>
                </div>
                
                <ul style="color: #4B5563; margin: 1rem 0; padding-left: 1.5rem;">
                    {"".join([f'<li style="margin-bottom: 0.5rem;">{ach}</li>' for ach in exp['achievements']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)

# =======================
# CONTACT PAGE
# =======================
elif selected == "Contact":
    st.title("📞 Let's Connect")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%); 
                    border-radius: 20px; padding: 3rem; color: white;">
            <h2 style="color: white;">Ready to Transform Your Supply Chain?</h2>
            <p style="opacity: 0.9; font-size: 1.1rem;">
            Let's discuss how data-driven insights and AI automation can optimize 
            your operations, reduce costs, and improve accuracy.
            </p>
            
            <div style="margin-top: 2rem;">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <span style="font-size: 1.5rem; margin-right: 1rem;">📧</span>
                    <div>
                        <div style="font-weight: 600;">Email</div>
                        <div>supply-chain@mulyanto.com</div>
                    </div>
                </div>
                
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <span style="font-size: 1.5rem; margin-right: 1rem;">📱</span>
                    <div>
                        <div style="font-weight: 600;">Phone</div>
                        <div>+62 857 8267 2208</div>
                    </div>
                </div>
                
                <div style="display: flex; align-items: center;">
                    <span style="font-size: 1.5rem; margin-right: 1rem;">🌐</span>
                    <div>
                        <div style="font-weight: 600;">Portfolio</div>
                        <div>supply-chain-dashboard-mulyanto.streamlit.app</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 5rem; margin-bottom: 1rem;">📊</div>
            <h3>Certifications</h3>
            
            <div style="background: white; border-radius: 12px; padding: 1.5rem; margin: 1rem 0; 
                        border: 2px solid #E5E7EB;">
                <div style="font-size: 2rem;">🎖️</div>
                <div style="font-weight: 600;">Supply Chain Analytics</div>
                <div style="color: #6B7280; font-size: 0.9rem;">Google/Coursera</div>
            </div>
            
            <div style="background: white; border-radius: 12px; padding: 1.5rem; margin: 1rem 0; 
                        border: 2px solid #E5E7EB;">
                <div style="font-size: 2rem;">🏆</div>
                <div style="font-weight: 600;">Python for Data Science</div>
                <div style="color: #6B7280; font-size: 0.9rem;">DataCamp</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# =======================
# FOOTER
# =======================
st.markdown("""
<hr style="margin: 3rem 0; border: none; height: 1px; background: #E5E7EB;">

<div style="text-align: center; color: #6B7280; padding: 2rem 0;">
    <p style="font-size: 0.9rem;">© 2024 Mulyanto | Supply Chain AI & Analytics Portfolio</p>
    <p style="font-size: 0.8rem; opacity: 0.7;">Built with ❤️ using Streamlit • Updated: Real-time</p>
</div>
""", unsafe_allow_html=True)
