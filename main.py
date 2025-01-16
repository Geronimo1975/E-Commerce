"""
Main entry point for the E-commerce Platform
"""
import streamlit as st
from inventory_management_system.streamlit.ecommerce_app import init_app

if __name__ == "__main__":
    init_app()
