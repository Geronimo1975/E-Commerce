import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styles to Streamlit app."""
    st.markdown("""
        <style>
        /* Main container styles */
        .main {
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        /* Header styles */
        .stTitle {
            color: #1E3A8A;
            font-size: 2.5em !important;
            font-weight: 700 !important;
            margin-bottom: 2rem !important;
            text-align: center;
        }

        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .stTabs [data-baseweb="tab"] {
            height: 50px;
            padding: 0 20px;
            background-color: white;
            border-radius: 5px;
            color: #1E3A8A;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .stTabs [data-baseweb="tab"]:hover {
            background-color: #F3F4F6;
            transform: translateY(-2px);
        }

        /* Product card styles */
        .product-card {
            background: white;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
        }

        /* Button styles */
        .stButton>button {
            width: 100%;
            height: 3em;
            background: #1E3A8A;
            color: white;
            border: none;
            border-radius: 5px;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background: #2563EB;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        /* Input field styles */
        .stNumberInput, .stTextInput {
            background: white;
            border-radius: 5px;
            border: 1px solid #E5E7EB;
            padding: 0.5rem;
            transition: all 0.3s ease;
        }

        .stNumberInput:focus, .stTextInput:focus {
            border-color: #2563EB;
            box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
        }

        /* Chart container styles */
        .chart-container {
            background: white;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Cart styles */
        .cart-item {
            background: white;
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 0.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }

        .cart-total {
            font-size: 1.25em;
            font-weight: 600;
            color: #1E3A8A;
            padding: 1rem;
            background: #F3F4F6;
            border-radius: 8px;
            margin-top: 1rem;
        }

        /* Form styles */
        .stForm {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Table styles */
        .dataframe {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .dataframe th {
            background: #1E3A8A;
            color: white;
            padding: 1rem;
            text-align: left;
        }

        .dataframe td {
            padding: 1rem;
            border-bottom: 1px solid #E5E7EB;
        }

        .dataframe tr:hover {
            background: #F3F4F6;
        }
        </style>
    """, unsafe_allow_html=True)