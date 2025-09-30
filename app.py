import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Financial Risk Calculator",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📊 Financial Risk Calculator for Brokers")
st.markdown("Comprehensive risk assessment and position sizing tool")

# Sidebar for navigation
st.sidebar.header("Calculator Tools")
tool = st.sidebar.radio(
    "Select Tool:",
    ["Position Sizing", "Portfolio Risk", "Value at Risk (VaR)", "Risk/Reward Analysis"]
)

# Helper functions
def calculate_position_size(account_balance, risk_percentage, entry_price, stop_loss):
    """Calculate position size based on risk parameters"""
    risk_amount = account_balance * (risk_percentage / 100)
    price_risk = abs(entry_price - stop_loss)
    if price_risk == 0:
        return 0
    position_size = risk_amount / price_risk
    return position_size

def calculate_var(returns, confidence_level=0.95):
    """Calculate Value at Risk"""
    if len(returns) == 0:
        return 0
    return np.percentile(returns, (1 - confidence_level) * 100)

def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    """Calculate Sharpe Ratio"""
    if len(returns) == 0 or np.std(returns) == 0:
        return 0
    excess_returns = returns - (risk_free_rate / 252)
    return np.sqrt(252) * np.mean(excess_returns) / np.std(excess_returns)

# Tool 1: Position Sizing Calculator
if tool == "Position Sizing":
    st.header("Position Sizing Calculator")
    st.markdown("Calculate optimal position size based on risk management principles")
    
    col1, col2 = st.columns(2)
    
    with col1:
        account_balance = st.number_input(
            "Account Balance ($)",
            min_value=0.0,
            value=100000.0,
            step=1000.0
        )
        
        risk_percentage = st.slider(
            "Risk Per Trade (%)",
            min_value=0.1,
            max_value=5.0,
            value=1.0,
            step=0.1
        )
        
        entry_price = st.number_input(
            "Entry Price ($)",
            min_value=0.01,
            value=100.0,
            step=0.01
        )
    
    with col2:
        stop_loss = st.number_input(
            "Stop Loss Price ($)",
            min_value=0.01,
            value=95.0,
            step=0.01
        )
        
        target_price = st.number_input(
            "Target Price ($)",
            min_value=0.01,
            value=110.0,
            step=0.01
        )
    
    if st.button("Calculate Position Size", type="primary"):
        position_size = calculate_position_size(account_balance, risk_percentage, entry_price, stop_loss)
        risk_amount = account_balance * (risk_percentage / 100)
        position_value = position_size * entry_price
        
        price_risk = abs(entry_price - stop_loss)
        potential_profit = abs(target_price - entry_price)
        risk_reward_ratio = potential_profit / price_risk if price_risk > 0 else 0
        
        st.success("### Calculation Results")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Position Size", f"{position_size:.2f} shares")
        with col2:
            st.metric("Position Value", f"${position_value:,.2f}")
        with col3:
            st.metric("Risk Amount", f"${risk_amount:,.2f}")
        with col4:
            st.metric("Risk/Reward Ratio", f"1:{risk_reward_ratio:.2f}")
        
        # Visualization
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=['Stop Loss', 'Entry', 'Target'],
            y=[stop_loss, entry_price, target_price],
            mode='markers+lines+text',
            marker=dict(size=[15, 20, 15], color=['red', 'blue', 'green']),
            text=[f'${stop_loss}', f'${entry_price}', f'${target_price}'],
            textposition='top center',
            line=dict(color='gray', dash='dash')
        ))
        
        fig.update_layout(
            title="Trade Setup Visualization",
            xaxis_title="Trade Levels",
            yaxis_title="Price ($)",
            showlegend=False,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Tool 2: Portfolio Risk Assessment
elif tool == "Portfolio Risk":
    st.header("Portfolio Risk Assessment")
    st.markdown("Analyze overall portfolio risk and diversification")
    
    st.subheader("Enter Portfolio Positions")
    
    num_positions = st.number_input("Number of Positions", min_value=1, max_value=20, value=3)
    
    positions_data = []
    
    for i in range(num_positions):
        with st.expander(f"Position {i+1}", expanded=(i<3)):
            col1, col2, col3 = st.columns(3)
            with col1:
                symbol = st.text_input(f"Symbol", value=f"STOCK{i+1}", key=f"symbol_{i}")
            with col2:
                shares = st.number_input(f"Shares", min_value=0.0, value=100.0, key=f"shares_{i}")
            with col3:
                price = st.number_input(f"Price ($)", min_value=0.01, value=100.0, key=f"price_{i}")
            
            positions_data.append({
                "Symbol": symbol,
                "Shares": shares,
                "Price": price,
                "Value": shares * price
            })
    
    if st.button("Analyze Portfolio", type="primary"):
        df = pd.DataFrame(positions_data)
        total_value = df['Value'].sum()
        df['Weight (%)'] = (df['Value'] / total_value * 100).round(2)
        
        st.success("### Portfolio Summary")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Portfolio Value", f"${total_value:,.2f}")
        with col2:
            st.metric("Number of Positions", len(df))
        with col3:
            concentration = df['Weight (%)'].max()
            st.metric("Largest Position", f"{concentration:.1f}%")
        
        st.dataframe(df, use_container_width=True)
        
        # Pie chart
        fig = px.pie(df, values='Value', names='Symbol', title='Portfolio Allocation')
        st.plotly_chart(fig, use_container_width=True)

# Tool 3: Value at Risk (VaR)
elif tool == "Value at Risk (VaR)":
    st.header("Value at Risk (VaR) Calculator")
    st.markdown("Estimate potential portfolio losses using historical simulation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        portfolio_value = st.number_input(
            "Portfolio Value ($)",
            min_value=0.0,
            value=500000.0,
            step=10000.0
        )
        
        daily_volatility = st.slider(
            "Daily Volatility (%)",
            min_value=0.1,
            max_value=10.0,
            value=2.0,
            step=0.1
        )
    
    with col2:
        confidence_level = st.selectbox(
            "Confidence Level",
            options=[90, 95, 99],
            index=1
        )
        
        time_horizon = st.number_input(
            "Time Horizon (days)",
            min_value=1,
            max_value=30,
            value=1
        )
    
    if st.button("Calculate VaR", type="primary"):
        # Simulate returns
        np.random.seed(42)
        num_simulations = 10000
        daily_returns = np.random.normal(0, daily_volatility/100, num_simulations)
        
        # Calculate VaR
        var_percentage = np.percentile(daily_returns, 100 - confidence_level)
        var_amount = portfolio_value * abs(var_percentage) * np.sqrt(time_horizon)
        
        st.success("### VaR Results")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Value at Risk", f"${var_amount:,.2f}")
        with col2:
            st.metric("VaR as % of Portfolio", f"{(var_amount/portfolio_value*100):.2f}%")
        with col3:
            st.metric("Confidence Level", f"{confidence_level}%")
        
        st.info(f"With {confidence_level}% confidence, portfolio will not lose more than ${var_amount:,.2f} over {time_horizon} day(s)")
        
        # Distribution chart
        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=daily_returns * 100,
            nbinsx=50,
            name='Return Distribution'
        ))
        
        fig.add_vline(
            x=var_percentage * 100,
            line_dash="dash",
            line_color="red",
            annotation_text=f"VaR at {confidence_level}%"
        )
        
        fig.update_layout(
            title="Simulated Return Distribution",
            xaxis_title="Daily Return (%)",
            yaxis_title="Frequency",
            showlegend=True,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Tool 4: Risk/Reward Analysis
else:
    st.header("Risk/Reward Analysis")
    st.markdown("Evaluate trade opportunities based on risk/reward metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Trade Parameters")
        entry = st.number_input("Entry Price ($)", value=100.0, step=0.01)
        stop = st.number_input("Stop Loss ($)", value=95.0, step=0.01)
        target1 = st.number_input("Target 1 ($)", value=110.0, step=0.01)
        target2 = st.number_input("Target 2 ($)", value=120.0, step=0.01)
        
        win_rate = st.slider("Historical Win Rate (%)", 0, 100, 60)
    
    with col2:
        st.subheader("Position Details")
        shares = st.number_input("Number of Shares", value=100, step=1)
        commission = st.number_input("Commission per Trade ($)", value=5.0, step=0.1)
    
    if st.button("Analyze Trade", type="primary"):
        risk = abs(entry - stop)
        reward1 = abs(target1 - entry)
        reward2 = abs(target2 - entry)
        
        rr_ratio1 = reward1 / risk if risk > 0 else 0
        rr_ratio2 = reward2 / risk if risk > 0 else 0
        
        max_loss = (risk * shares) + (2 * commission)
        max_gain1 = (reward1 * shares) - (2 * commission)
        max_gain2 = (reward2 * shares) - (2 * commission)
        
        expected_value = (win_rate/100 * max_gain1) - ((100-win_rate)/100 * max_loss)
        
        st.success("### Analysis Results")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("R/R Ratio (Target 1)", f"1:{rr_ratio1:.2f}")
        with col2:
            st.metric("R/R Ratio (Target 2)", f"1:{rr_ratio2:.2f}")
        with col3:
            st.metric("Max Risk", f"${max_loss:,.2f}")
        with col4:
            st.metric("Expected Value", f"${expected_value:,.2f}")
        
        # Create scenario table
        scenarios = pd.DataFrame({
            'Scenario': ['Maximum Loss', 'Target 1', 'Target 2'],
            'Price': [stop, target1, target2],
            'P&L': [-max_loss, max_gain1, max_gain2],
            'Return %': [-(risk/entry)*100, (reward1/entry)*100, (reward2/entry)*100]
        })
        
        st.dataframe(scenarios, use_container_width=True)
        
        # Visualization
        fig = go.Figure()
        
        prices = [stop, entry, target1, target2]
        colors = ['red', 'gray', 'lightgreen', 'green']
        
        fig.add_trace(go.Bar(
            x=['Stop Loss', 'Entry', 'Target 1', 'Target 2'],
            y=prices,
            marker_color=colors,
            text=[f'${p:.2f}' for p in prices],
            textposition='outside'
        ))
        
        fig.update_layout(
            title="Trade Levels",
            yaxis_title="Price ($)",
            showlegend=False,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Risk Warning**: Trading involves substantial risk of loss. 
    Past performance is not indicative of future results. 
    Always use proper risk management.
    """
)
