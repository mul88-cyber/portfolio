import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import base64

# ======================================================
# KONFIGURASI HALAMAN
# ======================================================
st.set_page_config(
    page_title="Supply Chain Professional Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# CSS STYLING PREMIUM
# ======================================================
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        text-align: center;
        padding: 1rem;
    }
    
    .portfolio-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-top: 5px solid;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .portfolio-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }
    
    .card-blue { border-top-color: #667eea; }
    .card-green { border-top-color: #4CAF50; }
    .card-orange { border-top-color: #FF9800; }
    .card-purple { border-top-color: #9C27B0; }
    
    .skill-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1.2rem;
        border-radius: 25px;
        display: inline-block;
        margin: 0.3rem;
        font-size: 0.9rem;
        font-weight: 600;
        box-shadow: 0 4px 10px rgba(102, 126, 234, 0.3);
    }
    
    .achievement-item {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.2rem;
        border-radius: 12px;
        margin: 0.8rem 0;
        border-left: 5px solid #4CAF50;
        transition: all 0.3s ease;
    }
    
    .achievement-item:hover {
        transform: translateX(10px);
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
    }
    
    .cert-badge {
        background: white;
        border: 2px solid #4CAF50;
        padding: 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .metric-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        margin: 0.5rem;
    }
    
    .timeline-item {
        position: relative;
        padding-left: 2rem;
        margin: 1.5rem 0;
        border-left: 3px solid #667eea;
    }
    
    .timeline-dot {
        position: absolute;
        left: -0.5rem;
        top: 0;
        width: 1rem;
        height: 1rem;
        background: #667eea;
        border-radius: 50%;
    }
    
    /* Navigation */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        padding: 10px 0;
        background: #f8f9fa;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background: white;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 700;
        border: 2px solid transparent;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: 2px solid #5a67d8 !important;
    }
</style>
""", unsafe_allow_html=True)

# ======================================================
# DATA PORTFOLIO
# ======================================================

class SupplyChainPortfolio:
    def __init__(self):
        self.profile = {
            "name": "Mulyanto",
            "title": "Demand Planner & Supply Chain Analytics Professional",
            "tagline": "Transforming Data into Supply Chain Excellence",
            "experience": "8+ Years",
            "current_role": "Senior Demand Planner - D2C E-commerce",
            "location": "Indonesia",
            "contact": {
                "linkedin": "https://linkedin.com/in/...",
                "email": "mulyanto@example.com",
                "github": "https://github.com/..."
            },
            "summary": """Seasoned Supply Chain professional specializing in demand forecasting, 
            inventory optimization, and data-driven decision making. Proven track record in 
            improving forecast accuracy, reducing inventory costs, and implementing scalable 
            supply chain solutions across FMCG and E-commerce sectors.""",
            
            "specializations": [
                "Demand Forecasting & Planning",
                "Inventory Optimization",
                "S&OP Process Implementation",
                "Supply Chain Analytics",
                "Cost-to-Serve Optimization",
                "Dashboard & Reporting Automation",
                "Cross-functional Collaboration",
                "Process Improvement"
            ],
            
            "achievements": [
                {
                    "title": "Improved Forecast Accuracy",
                    "description": "Increased forecast accuracy from 65% to 85% through statistical modeling and process improvements",
                    "impact": "30% reduction in stockouts, 25% decrease in excess inventory",
                    "year": "2023"
                },
                {
                    "title": "Inventory Cost Reduction",
                    "description": "Implemented inventory optimization model reducing holding costs by 30%",
                    "impact": "Annual savings of $500K+ through better stock rotation",
                    "year": "2022"
                },
                {
                    "title": "S&OP Process Implementation",
                    "description": "Designed and implemented S&OP process across 5 departments",
                    "impact": "Improved cross-functional alignment, reduced planning cycle by 40%",
                    "year": "2021"
                },
                {
                    "title": "Dashboard Automation",
                    "description": "Developed comprehensive supply chain dashboard reducing manual reporting time by 70%",
                    "impact": "Freed up 20+ hours weekly for strategic analysis",
                    "year": "2023"
                },
                {
                    "title": "Safety Stock Optimization",
                    "description": "Optimized safety stock levels using statistical methods",
                    "impact": "15% reduction in warehouse space requirement",
                    "year": "2022"
                },
                {
                    "title": "Multi-channel Integration",
                    "description": "Integrated E-commerce and Reseller demand planning into single platform",
                    "impact": "Improved visibility, 25% better resource allocation",
                    "year": "2023"
                }
            ],
            
            "skills": {
                "technical": [
                    {"name": "Python (Pandas, NumPy)", "level": 95},
                    {"name": "SQL & Database Management", "level": 90},
                    {"name": "Statistical Forecasting", "level": 92},
                    {"name": "Google Sheets/Excel", "level": 95},
                    {"name": "Streamlit/Dash", "level": 88},
                    {"name": "Tableau/Power BI", "level": 85},
                    {"name": "Machine Learning Basics", "level": 80},
                    {"name": "API Integration", "level": 82}
                ],
                "business": [
                    {"name": "Demand Planning", "level": 96},
                    {"name": "Inventory Management", "level": 94},
                    {"name": "S&OP Process", "level": 90},
                    {"name": "Supply Chain Analytics", "level": 92},
                    {"name": "Stakeholder Management", "level": 88},
                    {"name": "Project Management", "level": 85},
                    {"name": "Cost Optimization", "level": 90},
                    {"name": "Process Improvement", "level": 87}
                ]
            },
            
            "certifications": [
                {
                    "name": "APICS CPIM",
                    "issuer": "Association for Supply Chain Management",
                    "year": "2022",
                    "credential": "Certified in Production & Inventory Management"
                },
                {
                    "name": "Six Sigma Green Belt",
                    "issuer": "International Association for Six Sigma",
                    "year": "2021",
                    "credential": "Process Improvement Methodology"
                },
                {
                    "name": "Google Data Analytics",
                    "issuer": "Google Career Certificates",
                    "year": "2023",
                    "credential": "Professional Certificate"
                },
                {
                    "name": "Supply Chain Fundamentals",
                    "issuer": "MITx MicroMasters",
                    "year": "2020",
                    "credential": "Supply Chain Management"
                }
            ],
            
            "projects": [
                {
                    "name": "Inventory Intelligence Dashboard",
                    "description": "End-to-end supply chain analytics dashboard for D2C company",
                    "technologies": ["Python", "Streamlit", "Plotly", "Google Sheets API"],
                    "features": [
                        "Real-time forecast accuracy tracking",
                        "Inventory health monitoring",
                        "Financial performance analysis",
                        "Multi-channel performance comparison"
                    ],
                    "impact": "Reduced manual reporting by 70%, improved decision making speed"
                },
                {
                    "name": "Demand Forecasting System",
                    "description": "Statistical forecasting system with machine learning integration",
                    "technologies": ["Python", "scikit-learn", "Facebook Prophet", "SQL"],
                    "features": [
                        "Multiple forecasting algorithms",
                        "Automated accuracy tracking",
                        "Exception-based alerting",
                        "What-if scenario analysis"
                    ],
                    "impact": "Improved forecast accuracy by 20 percentage points"
                },
                {
                    "name": "Inventory Optimization Model",
                    "description": "EOQ and safety stock optimization tool",
                    "technologies": ["Python", "Pandas", "Matplotlib", "Excel VBA"],
                    "features": [
                        "Economic Order Quantity calculator",
                        "Service level optimization",
                        "Stock-out probability analysis",
                        "Reorder point calculation"
                    ],
                    "impact": "Reduced inventory holding costs by 30%"
                }
            ],
            
            "experience_timeline": [
                {
                    "role": "Senior Demand Planner",
                    "company": "D2C E-commerce Company",
                    "period": "2022 - Present",
                    "achievements": [
                        "Led demand planning for 1000+ SKUs across multiple channels",
                        "Implemented S&OP process improving forecast accuracy to 85%",
                        "Reduced inventory costs by 30% through optimization models"
                    ]
                },
                {
                    "role": "Supply Chain Analyst",
                    "company": "FMCG Multinational",
                    "period": "2020 - 2022",
                    "achievements": [
                        "Developed inventory optimization dashboard used by 5 regional teams",
                        "Automated monthly reporting saving 15 hours per week",
                        "Improved fill rate from 85% to 95% through better forecasting"
                    ]
                },
                {
                    "role": "Logistics Coordinator",
                    "company": "Retail Chain",
                    "period": "2018 - 2020",
                    "achievements": [
                        "Managed inventory for 50+ stores",
                        "Reduced stockouts by 40% through improved replenishment",
                        "Implemented barcode system improving picking accuracy"
                    ]
                }
            ]
        }
    
    def generate_skill_chart(self, skill_type="technical"):
        """Generate radar chart for skills"""
        skills = self.profile['skills'][skill_type]
        
        categories = [s['name'] for s in skills]
        values = [s['level'] for s in skills]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=skill_type.capitalize(),
            line_color='#667eea' if skill_type == 'technical' else '#4CAF50',
            fillcolor='rgba(102, 126, 234, 0.2)' if skill_type == 'technical' else 'rgba(76, 175, 80, 0.2)'
        ))
        
        fig.update_layout(
            height=500,
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    tickfont=dict(size=10)
                ),
                angularaxis=dict(
                    tickfont=dict(size=11),
                    rotation=90
                )
            ),
            showlegend=False,
            title=f"{skill_type.capitalize()} Skills Assessment"
        )
        
        return fig
    
    def generate_impact_metrics(self):
        """Generate impact metrics cards"""
        metrics = [
            {"label": "Forecast Accuracy Improvement", "value": "+20%", "icon": "📈"},
            {"label": "Inventory Cost Reduction", "value": "30%", "icon": "💰"},
            {"label": "Reporting Time Saved", "value": "70%", "icon": "⏱️"},
            {"label": "Stockout Reduction", "value": "40%", "icon": "📦"},
            {"label": "Process Cycle Time", "value": "-40%", "icon": "⚡"},
            {"label": "Cross-functional Teams", "value": "5", "icon": "🤝"}
        ]
        return metrics

# Initialize portfolio
portfolio = SupplyChainPortfolio()

# ======================================================
# HEADER SECTION
# ======================================================
st.markdown(f'<h1 class="main-header">🚀 SUPPLY CHAIN PROFESSIONAL PORTFOLIO</h1>', unsafe_allow_html=True)

# Hero Section
col_hero1, col_hero2, col_hero3 = st.columns([2, 1, 1])

with col_hero1:
    st.markdown(f"""
    <div style="padding: 1rem 0;">
        <h2 style="color: #333; margin-bottom: 0.5rem;">{portfolio.profile['name']}</h2>
        <h3 style="color: #667eea; margin-top: 0;">{portfolio.profile['title']}</h3>
        <p style="font-size: 1.1rem; color: #666; line-height: 1.6;">{portfolio.profile['summary']}</p>
    </div>
    """, unsafe_allow_html=True)

with col_hero2:
    st.markdown(f"""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #667eea;">{portfolio.profile['experience']}</div>
        <div style="font-size: 0.9rem; color: #666;">Experience</div>
    </div>
    """, unsafe_allow_html=True)

with col_hero3:
    st.markdown(f"""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #4CAF50;">15+</div>
        <div style="font-size: 0.9rem; color: #666;">Projects Completed</div>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# NAVIGATION TABS
# ======================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏆 Core Competencies",
    "📊 Skills & Expertise",
    "💼 Professional Journey",
    "🚀 Key Projects",
    "📞 Contact & Connect"
])

# ======================================================
# TAB 1: CORE COMPETENCIES
# ======================================================
with tab1:
    col_comp1, col_comp2 = st.columns([2, 1])
    
    with col_comp1:
        st.markdown("""
        <div class="portfolio-card card-blue">
            <h3>🎯 Core Specializations</h3>
            <div style="margin-top: 1.5rem;">
        """, unsafe_allow_html=True)
        
        for spec in portfolio.profile['specializations']:
            st.markdown(f'<span class="skill-badge">{spec}</span>', unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
        
        # Impact Metrics
        st.markdown("### 📈 Professional Impact Metrics")
        
        metrics = portfolio.generate_impact_metrics()
        metric_cols = st.columns(3)
        
        for idx, metric in enumerate(metrics):
            with metric_cols[idx % 3]:
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">{metric['icon']}</div>
                    <div style="font-size: 1.8rem; font-weight: 800; color: #333;">{metric['value']}</div>
                    <div style="font-size: 0.9rem; color: #666;">{metric['label']}</div>
                </div>
                """, unsafe_allow_html=True)
    
    with col_comp2:
        st.markdown("""
        <div class="portfolio-card card-green">
            <h3>🏅 Certifications</h3>
            <div style="margin-top: 1rem;">
        """, unsafe_allow_html=True)
        
        for cert in portfolio.profile['certifications']:
            st.markdown(f"""
            <div style="margin: 1rem 0; padding: 1rem; background: #F5F5F5; border-radius: 10px;">
                <div style="font-weight: 600; color: #333;">{cert['name']}</div>
                <div style="font-size: 0.9rem; color: #666;">{cert['issuer']}</div>
                <div style="font-size: 0.8rem; color: #888;">{cert['year']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)

# ======================================================
# TAB 2: SKILLS & EXPERTISE
# ======================================================
with tab2:
    st.markdown("### 🛠️ Technical & Business Competencies")
    
    col_skill1, col_skill2 = st.columns(2)
    
    with col_skill1:
        # Technical Skills Chart
        fig_tech = portfolio.generate_skill_chart("technical")
        st.plotly_chart(fig_tech, use_container_width=True)
        
        # Technical Skills List
        with st.expander("📋 Detailed Technical Skills", expanded=True):
            for skill in portfolio.profile['skills']['technical']:
                st.markdown(f"""
                <div style="margin: 0.5rem 0;">
                    <div style="display: flex; justify-content: space-between;">
                        <span>{skill['name']}</span>
                        <span style="font-weight: 600; color: #667eea;">{skill['level']}%</span>
                    </div>
                    <div style="height: 8px; background: #eee; border-radius: 4px; margin-top: 0.2rem;">
                        <div style="width: {skill['level']}%; height: 100%; background: #667eea; border-radius: 4px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    with col_skill2:
        # Business Skills Chart
        fig_business = portfolio.generate_skill_chart("business")
        st.plotly_chart(fig_business, use_container_width=True)
        
        # Business Skills List
        with st.expander("📋 Detailed Business Skills", expanded=True):
            for skill in portfolio.profile['skills']['business']:
                st.markdown(f"""
                <div style="margin: 0.5rem 0;">
                    <div style="display: flex; justify-content: space-between;">
                        <span>{skill['name']}</span>
                        <span style="font-weight: 600; color: #4CAF50;">{skill['level']}%</span>
                    </div>
                    <div style="height: 8px; background: #eee; border-radius: 4px; margin-top: 0.2rem;">
                        <div style="width: {skill['level']}%; height: 100%; background: #4CAF50; border-radius: 4px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# ======================================================
# TAB 3: PROFESSIONAL JOURNEY
# ======================================================
with tab3:
    col_journey1, col_journey2 = st.columns([2, 1])
    
    with col_journey1:
        st.markdown("### 📅 Career Timeline")
        
        for exp in portfolio.profile['experience_timeline']:
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <div>
                            <h4 style="margin: 0; color: #333;">{exp['role']}</h4>
                            <p style="margin: 0.3rem 0; color: #667eea; font-weight: 600;">{exp['company']}</p>
                        </div>
                        <span style="background: #E3F2FD; color: #1565C0; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">
                            {exp['period']}
                        </span>
                    </div>
                    <div style="margin-top: 1rem;">
                        <ul style="margin: 0; padding-left: 1.2rem;">
                            {"".join([f"<li>{ach}</li>" for ach in exp['achievements']])}
                        </ul>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col_journey2:
        st.markdown("### 🏆 Key Achievements")
        
        for idx, achievement in enumerate(portfolio.profile['achievements'][:4]):
            icon = "📈" if idx == 0 else "💰" if idx == 1 else "⚡" if idx == 2 else "🎯"
            
            st.markdown(f"""
            <div class="achievement-item">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <div style="font-size: 1.2rem;">{icon}</div>
                    <div style="font-weight: 600; color: #333;">{achievement['title']}</div>
                </div>
                <div style="font-size: 0.9rem; color: #666;">{achievement['description']}</div>
                <div style="margin-top: 0.5rem; padding: 0.5rem; background: #E8F5E9; border-radius: 5px; font-size: 0.85rem; color: #2E7D32;">
                    <strong>Impact:</strong> {achievement['impact']}
                </div>
                <div style="text-align: right; font-size: 0.8rem; color: #888; margin-top: 0.5rem;">
                    {achievement['year']}
                </div>
            </div>
            """, unsafe_allow_html=True)

# ======================================================
# TAB 4: KEY PROJECTS
# ======================================================
with tab4:
    st.markdown("### 🚀 Portfolio Projects")
    
    for project in portfolio.profile['projects']:
        col_proj1, col_proj2 = st.columns([3, 1])
        
        with col_proj1:
            st.markdown(f"""
            <div class="portfolio-card card-purple">
                <h3>{project['name']}</h3>
                <p style="color: #666; line-height: 1.6;">{project['description']}</p>
                
                <div style="margin: 1rem 0;">
                    <h4>✨ Key Features:</h4>
                    <ul>
                        {"".join([f"<li>{feature}</li>" for feature in project['features']])}
                    </ul>
                </div>
                
                <div style="margin: 1rem 0;">
                    <h4>🏆 Business Impact:</h4>
                    <p style="background: #E8F5E9; padding: 1rem; border-radius: 8px; color: #2E7D32;">
                        {project['impact']}
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_proj2:
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
                <h4>🛠️ Technologies</h4>
                <div style="margin-top: 1rem;">
            """, unsafe_allow_html=True)
            
            for tech in project['technologies']:
                st.markdown(f"""
                <div style="background: #F5F5F5; padding: 0.5rem 1rem; border-radius: 20px; 
                            margin: 0.3rem 0; text-align: center; font-size: 0.9rem;">
                    {tech}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div></div>", unsafe_allow_html=True)

# ======================================================
# TAB 5: CONTACT & CONNECT
# ======================================================
with tab5:
    col_contact1, col_contact2 = st.columns([2, 1])
    
    with col_contact1:
        st.markdown("""
        <div class="portfolio-card card-orange">
            <h3>📞 Let's Connect!</h3>
            <p style="font-size: 1.1rem; line-height: 1.6;">
                I'm passionate about leveraging data and analytics to solve complex supply chain challenges. 
                Whether you're looking for consulting, collaboration, or career opportunities, feel free to reach out!
            </p>
            
            <div style="margin: 2rem 0;">
                <h4>📍 Contact Information</h4>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                    <div style="padding: 1rem; background: #F5F5F5; border-radius: 10px;">
                        <div style="font-weight: 600;">Email</div>
                        <div style="color: #667eea;">{portfolio.profile['contact']['email']}</div>
                    </div>
                    <div style="padding: 1rem; background: #F5F5F5; border-radius: 10px;">
                        <div style="font-weight: 600;">Location</div>
                        <div>{portfolio.profile['location']}</div>
                    </div>
                </div>
            </div>
            
            <div>
                <h4>🔗 Professional Profiles</h4>
                <div style="display: flex; gap: 1rem; margin-top: 1rem;">
                    <a href="{portfolio.profile['contact']['linkedin']}" target="_blank" 
                       style="display: inline-block; padding: 0.8rem 1.5rem; background: #0077B5; 
                              color: white; border-radius: 25px; text-decoration: none; font-weight: 600;">
                        LinkedIn
                    </a>
                    <a href="{portfolio.profile['contact']['github']}" target="_blank"
                       style="display: inline-block; padding: 0.8rem 1.5rem; background: #333; 
                              color: white; border-radius: 25px; text-decoration: none; font-weight: 600;">
                        GitHub
                    </a>
                </div>
            </div>
        </div>
        """.format(**portfolio.profile), unsafe_allow_html=True)
    
    with col_contact2:
        st.markdown("""
        <div class="portfolio-card card-blue">
            <h3>📋 Quick Resume</h3>
            <p style="color: #666;">
                Download my detailed resume for comprehensive information about my experience, 
                skills, and achievements.
            </p>
            
            <div style="text-align: center; margin: 2rem 0;">
                <div style="font-size: 3rem; color: #667eea;">📄</div>
                <div style="font-weight: 600; margin: 1rem 0;">Download Resume</div>
                
                <div style="display: flex; gap: 1rem; justify-content: center;">
                    <button style="padding: 0.8rem 1.5rem; background: #667eea; color: white; 
                            border: none; border-radius: 25px; cursor: pointer;">
                        PDF Format
                    </button>
                </div>
            </div>
            
            <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee;">
                <h4>🎯 Availability</h4>
                <div style="background: #E8F5E9; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                    <div style="font-weight: 600; color: #2E7D32;">Open to Opportunities</div>
                    <div style="font-size: 0.9rem; color: #666;">
                        • Full-time roles<br>
                        • Consulting projects<br>
                        • Advisory positions
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ======================================================
# FOOTER
# ======================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p style="font-size: 1.1rem; font-weight: 600;">Transforming Supply Chains Through Data & Analytics</p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">
        © {year} {name} | Supply Chain Analytics Portfolio<br>
        Last updated: {date}
    </p>
</div>
""".format(
    year=datetime.now().year,
    name=portfolio.profile['name'],
    date=datetime.now().strftime('%B %Y')
), unsafe_allow_html=True)

# ======================================================
# SIDEBAR (Optional)
# ======================================================
with st.sidebar:
    st.markdown("### 👨‍💼 Quick Profile")
    
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem;">
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
        <div style="font-weight: 600; font-size: 1.2rem;">{portfolio.profile['name']}</div>
        <div style="color: #667eea; margin: 0.5rem 0;">{portfolio.profile['current_role']}</div>
        <div style="font-size: 0.9rem; color: #666;">{portfolio.profile['location']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Core Strengths")
    strengths = [
        "Data-Driven Decision Making",
        "Process Optimization",
        "Cross-functional Leadership",
        "Technical Implementation"
    ]
    
    for strength in strengths:
        st.markdown(f"✅ {strength}")
    
    st.markdown("---")
    
    st.markdown("### 🔗 Live Projects")
    
    if st.button("📊 Inventory Dashboard"):
        st.session_state.dashboard_link = "https://your-dashboard-app.streamlit.app"
    
    if st.button("📈 Forecasting System"):
        st.session_state.forecast_link = "https://your-forecast-app.streamlit.app"
