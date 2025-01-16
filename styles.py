import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styles to Streamlit app."""
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            border-radius: 5px;
            height: 3em;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .product-card {
            border: 1px solid #eee;
            padding: 1rem;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .product-card:hover {
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }
        .cart-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.5rem;
            border-bottom: 1px solid #eee;
        }
        .checkout-progress {
            display: flex;
            justify-content: space-between;
            margin: 2rem 0;
        }
        .progress-step {
            text-align: center;
            flex: 1;
            position: relative;
        }
        .progress-step::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 20px;
            height: 20px;
            background: #FF4B4B;
            border-radius: 50%;
            transform: translate(-50%, -50%);
        }
        </style>
    """, unsafe_allow_html=True)
