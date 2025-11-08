import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
from analytics_dashboard import render_analytics_dashboard

# Page configuration
st.set_page_config(
    page_title="Financial Risk Calculator - Traders & Brokers",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📊 Financial Risk Calculator - Traders & Brokers")
st.markdown("Comprehensive risk assessment tools for traders and forex broker operations")

# Sidebar for navigation
st.sidebar.header("Calculator Sections")
section = st.sidebar.radio(
    "Select Section:",
    ["Trader Models", "Broker Models", "Product Metrics"]
)

st.sidebar.markdown("---")

# Tool selection based on section
if section == "Trader Models":
    st.sidebar.header("Trader Tools")
    tool = st.sidebar.radio(
        "Select Tool:",
        ["Position Sizing", "Portfolio Risk", "Value at Risk (VaR)", "Risk/Reward Analysis"]
    )
elif section == "Broker Models":
    st.sidebar.header("Broker Tools")
    tool = st.sidebar.radio(
        "Select Tool:",
        ["Margin & Leverage", "Swap/Rollover Rates", "Pip Value & Commission",
         "Net Exposure & Hedging", "Client Position Monitor", "A-Book vs B-Book"]
    )
else:  # Product Metrics
    st.sidebar.header("Analytics Dashboard")
    tool = st.sidebar.radio(
        "Select View:",
        ["Business Metrics", "User Engagement", "Customer Success", "ROI Analysis"]
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

# ========== TRADER MODELS ==========
if section == "Trader Models":
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

# ========== BROKER MODELS ==========
else:  # section == "Broker Models"
    # Tool 1: Margin & Leverage Calculator
    if tool == "Margin & Leverage":
        st.header("Margin & Leverage Calculator")
        st.markdown("Calculate margin requirements and leverage exposure for client positions")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Account Details")
            account_equity = st.number_input(
                "Account Equity ($)",
                min_value=0.0,
                value=10000.0,
                step=100.0
            )

            leverage = st.selectbox(
                "Account Leverage",
                options=[1, 10, 20, 30, 50, 100, 200, 500],
                index=5
            )

            margin_call_level = st.slider(
                "Margin Call Level (%)",
                min_value=50,
                max_value=150,
                value=100,
                step=10
            )

            stop_out_level = st.slider(
                "Stop Out Level (%)",
                min_value=10,
                max_value=100,
                value=50,
                step=5
            )

        with col2:
            st.subheader("Position Details")

            currency_pair = st.selectbox(
                "Currency Pair",
                options=["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF", "NZD/USD", "USD/CAD"]
            )

            position_size = st.number_input(
                "Position Size (lots)",
                min_value=0.01,
                max_value=100.0,
                value=1.0,
                step=0.01
            )

            lot_size = st.selectbox(
                "Lot Type",
                options=["Standard (100k)", "Mini (10k)", "Micro (1k)"],
                index=0
            )

            current_price = st.number_input(
                "Current Price",
                min_value=0.0001,
                value=1.1000,
                step=0.0001,
                format="%.4f"
            )

        if st.button("Calculate Margin Requirements", type="primary"):
            # Lot size conversion
            lot_multiplier = {"Standard (100k)": 100000, "Mini (10k)": 10000, "Micro (1k)": 1000}
            contract_size = lot_multiplier[lot_size]

            # Calculate position value
            position_value = position_size * contract_size * current_price

            # Calculate required margin
            required_margin = position_value / leverage

            # Calculate free margin
            used_margin = required_margin
            free_margin = account_equity - used_margin

            # Calculate margin level
            margin_level = (account_equity / used_margin * 100) if used_margin > 0 else 0

            # Calculate max position size
            max_position_value = account_equity * leverage
            max_lots = max_position_value / (contract_size * current_price)

            # Calculate margin call and stop out thresholds
            margin_call_equity = (margin_call_level / 100) * used_margin
            stop_out_equity = (stop_out_level / 100) * used_margin

            st.success("### Margin Analysis Results")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Required Margin", f"${required_margin:,.2f}")
            with col2:
                st.metric("Free Margin", f"${free_margin:,.2f}")
            with col3:
                st.metric("Margin Level", f"{margin_level:.1f}%")
            with col4:
                st.metric("Max Lots Available", f"{max_lots:.2f}")

            # Risk thresholds
            st.subheader("Risk Thresholds")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Margin Call Threshold", f"${margin_call_equity:,.2f}")
                if margin_level <= margin_call_level:
                    st.error("⚠️ MARGIN CALL TRIGGERED")

            with col2:
                st.metric("Stop Out Threshold", f"${stop_out_equity:,.2f}")
                if margin_level <= stop_out_level:
                    st.error("🛑 STOP OUT - POSITIONS CLOSING")

            with col3:
                loss_to_margin_call = account_equity - margin_call_equity
                st.metric("Loss Until Margin Call", f"${loss_to_margin_call:,.2f}")

            # Create detailed summary table
            summary_data = {
                "Metric": [
                    "Position Value",
                    "Account Equity",
                    "Used Margin",
                    "Free Margin",
                    "Margin Level",
                    "Leverage",
                    "Max Position Size"
                ],
                "Value": [
                    f"${position_value:,.2f}",
                    f"${account_equity:,.2f}",
                    f"${used_margin:,.2f}",
                    f"${free_margin:,.2f}",
                    f"{margin_level:.1f}%",
                    f"{leverage}:1",
                    f"{max_lots:.2f} lots"
                ]
            }

            st.subheader("Position Summary")
            st.dataframe(pd.DataFrame(summary_data), use_container_width=True, hide_index=True)

            # Visualization
            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=['Account Equity', 'Used Margin', 'Free Margin', 'Margin Call Level', 'Stop Out Level'],
                y=[account_equity, used_margin, free_margin, margin_call_equity, stop_out_equity],
                marker_color=['blue', 'orange', 'green', 'yellow', 'red'],
                text=[f'${account_equity:,.0f}', f'${used_margin:,.0f}', f'${free_margin:,.0f}',
                      f'${margin_call_equity:,.0f}', f'${stop_out_equity:,.0f}'],
                textposition='outside'
            ))

            fig.update_layout(
                title="Margin Breakdown",
                yaxis_title="Amount ($)",
                showlegend=False,
                height=400
            )

            st.plotly_chart(fig, use_container_width=True)

    # Tool 2: Swap/Rollover Rates Calculator
    elif tool == "Swap/Rollover Rates":
        st.header("Swap/Rollover Rates Calculator")
        st.markdown("Calculate overnight financing charges for positions held past 5pm EST")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Position Details")

            currency_pair = st.selectbox(
                "Currency Pair",
                options=["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF", "NZD/USD", "USD/CAD", "EUR/GBP"],
                key="swap_pair"
            )

            position_type = st.radio(
                "Position Type",
                options=["Long (Buy)", "Short (Sell)"]
            )

            position_size = st.number_input(
                "Position Size (lots)",
                min_value=0.01,
                max_value=100.0,
                value=1.0,
                step=0.01,
                key="swap_lots"
            )

            lot_size = st.selectbox(
                "Lot Type",
                options=["Standard (100k)", "Mini (10k)", "Micro (1k)"],
                index=0,
                key="swap_lot_type"
            )

        with col2:
            st.subheader("Swap Rates")

            long_swap_rate = st.number_input(
                "Long Swap Rate (pips)",
                min_value=-50.0,
                max_value=50.0,
                value=-2.5,
                step=0.1,
                help="Swap charged for long positions (negative = cost, positive = credit)"
            )

            short_swap_rate = st.number_input(
                "Short Swap Rate (pips)",
                min_value=-50.0,
                max_value=50.0,
                value=0.8,
                step=0.1,
                help="Swap charged for short positions (negative = cost, positive = credit)"
            )

            broker_markup = st.slider(
                "Broker Markup (%)",
                min_value=0,
                max_value=50,
                value=10,
                help="Broker's markup on swap rates"
            )

            days_held = st.number_input(
                "Days Position Held",
                min_value=1,
                max_value=365,
                value=30
            )

        if st.button("Calculate Swap Charges", type="primary"):
            # Lot size conversion
            lot_multiplier = {"Standard (100k)": 100000, "Mini (10k)": 10000, "Micro (1k)": 1000}
            contract_size = lot_multiplier[lot_size]

            # Determine applicable swap rate
            base_swap_rate = long_swap_rate if position_type == "Long (Buy)" else short_swap_rate

            # Apply broker markup
            swap_with_markup = base_swap_rate * (1 + broker_markup/100)

            # Calculate pip value (simplified - assumes USD account)
            # For most pairs, 1 pip = $10 per standard lot
            pip_value = 10 * (contract_size / 100000) * position_size

            # Calculate daily swap charge
            daily_swap = swap_with_markup * pip_value

            # Calculate for holding period
            # Wednesday has triple swap (3-day rollover)
            wednesdays = days_held // 7
            regular_days = days_held - wednesdays
            total_swap_days = regular_days + (wednesdays * 3)

            total_swap_charge = daily_swap * total_swap_days

            # Annual projection
            annual_swap = daily_swap * (365 + (52 * 2))  # 365 days + 52 triple-swap Wednesdays

            # Broker revenue from markup
            base_daily_swap = base_swap_rate * pip_value
            broker_revenue_daily = daily_swap - base_daily_swap
            broker_revenue_total = broker_revenue_daily * total_swap_days

            st.success("### Swap Calculation Results")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Daily Swap", f"${daily_swap:,.2f}")
            with col2:
                st.metric(f"Total Swap ({days_held} days)", f"${total_swap_charge:,.2f}")
            with col3:
                st.metric("Annual Projection", f"${annual_swap:,.2f}")
            with col4:
                st.metric("Broker Revenue", f"${broker_revenue_total:,.2f}")

            # Detailed breakdown
            st.subheader("Swap Breakdown")

            swap_data = {
                "Description": [
                    "Position Size",
                    "Base Swap Rate",
                    "Swap with Markup",
                    "Pip Value",
                    "Daily Swap Charge",
                    "Total Swap Days",
                    "Total Swap Charge",
                    "Broker Daily Revenue",
                    "Broker Total Revenue"
                ],
                "Value": [
                    f"{position_size} {lot_size.split()[0]} lots",
                    f"{base_swap_rate:,.2f} pips",
                    f"{swap_with_markup:,.2f} pips",
                    f"${pip_value:,.2f}",
                    f"${daily_swap:,.2f}",
                    f"{total_swap_days} days",
                    f"${total_swap_charge:,.2f}",
                    f"${broker_revenue_daily:,.2f}",
                    f"${broker_revenue_total:,.2f}"
                ]
            }

            st.dataframe(pd.DataFrame(swap_data), use_container_width=True, hide_index=True)

            # Triple swap Wednesday info
            st.info(f"ℹ️ Calculation includes {wednesdays} triple-swap Wednesdays (3-day rollover)")

            if daily_swap < 0:
                st.warning(f"⚠️ This position costs ${abs(daily_swap):,.2f} per day in swap charges")
            else:
                st.success(f"✅ This position earns ${daily_swap:,.2f} per day in swap credits")

            # Visualization - Cumulative swap over time
            days_range = list(range(1, min(days_held + 1, 91)))  # Max 90 days for visualization
            cumulative_swaps = []

            for day in days_range:
                wed = day // 7
                reg = day - wed
                swap_days = reg + (wed * 3)
                cumulative_swaps.append(daily_swap * swap_days)

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=days_range,
                y=cumulative_swaps,
                mode='lines',
                fill='tozeroy',
                name='Cumulative Swap',
                line=dict(color='red' if daily_swap < 0 else 'green', width=2)
            ))

            fig.update_layout(
                title="Cumulative Swap Charges Over Time",
                xaxis_title="Days Held",
                yaxis_title="Cumulative Swap ($)",
                showlegend=True,
                height=400
            )

            st.plotly_chart(fig, use_container_width=True)

    # Tool 3: Pip Value & Commission Calculator
    elif tool == "Pip Value & Commission":
        st.header("Pip Value & Commission Calculator")
        st.markdown("Calculate pip values, spread costs, and broker revenue projections")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Position Details")

            currency_pair = st.selectbox(
                "Currency Pair",
                options=["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF", "NZD/USD", "USD/CAD", "EUR/GBP", "EUR/JPY", "GBP/JPY"],
                key="pip_pair"
            )

            account_currency = st.selectbox(
                "Account Currency",
                options=["USD", "EUR", "GBP"]
            )

            position_size = st.number_input(
                "Position Size (lots)",
                min_value=0.01,
                max_value=1000.0,
                value=1.0,
                step=0.01,
                key="pip_lots"
            )

            lot_size = st.selectbox(
                "Lot Type",
                options=["Standard (100k)", "Mini (10k)", "Micro (1k)"],
                index=0,
                key="pip_lot_type"
            )

            current_price = st.number_input(
                "Current Price",
                min_value=0.0001,
                value=1.1000,
                step=0.0001,
                format="%.4f",
                key="pip_price"
            )

        with col2:
            st.subheader("Broker Costs & Revenue")

            spread_pips = st.number_input(
                "Spread (pips)",
                min_value=0.0,
                max_value=100.0,
                value=1.5,
                step=0.1,
                help="Difference between bid and ask price"
            )

            commission_per_lot = st.number_input(
                "Commission per Lot (round-turn)",
                min_value=0.0,
                max_value=100.0,
                value=7.0,
                step=0.5,
                help="Total commission for opening and closing the position"
            )

            monthly_volume = st.number_input(
                "Client Monthly Volume (lots)",
                min_value=0.0,
                value=100.0,
                step=10.0,
                help="Average monthly trading volume for revenue projection"
            )

            pip_movement = st.slider(
                "Pip Movement (for P&L calc)",
                min_value=-500,
                max_value=500,
                value=50,
                step=10,
                help="Calculate P&L for a given pip movement"
            )

        if st.button("Calculate Pip Value & Costs", type="primary"):
            # Lot size conversion
            lot_multiplier = {"Standard (100k)": 100000, "Mini (10k)": 10000, "Micro (1k)": 1000}
            contract_size = lot_multiplier[lot_size]

            # Calculate pip value
            # For pairs with USD as quote currency (EUR/USD, GBP/USD, etc.)
            # 1 pip = 0.0001 for most pairs, 0.01 for JPY pairs
            is_jpy_pair = "JPY" in currency_pair
            pip_size = 0.01 if is_jpy_pair else 0.0001

            # Pip value = (pip size / current price) * contract size * position size
            # Simplified: For USD account and USD quote currency
            pip_value = (pip_size / current_price) * contract_size * position_size

            # For standard calculation: most pairs = $10 per pip per standard lot
            if not is_jpy_pair and account_currency == "USD":
                pip_value = 10 * (contract_size / 100000) * position_size
            elif is_jpy_pair and account_currency == "USD":
                pip_value = (0.01 / current_price) * contract_size * position_size

            # Calculate spread cost
            spread_cost = spread_pips * pip_value

            # Calculate total commission
            total_commission = commission_per_lot * position_size

            # Total trading cost
            total_cost = spread_cost + total_commission

            # P&L calculation
            pnl = pip_movement * pip_value
            net_pnl = pnl - total_cost if pip_movement > 0 else pnl - total_cost

            # Broker revenue projection
            monthly_spread_revenue = spread_pips * pip_value * monthly_volume
            monthly_commission_revenue = commission_per_lot * monthly_volume
            monthly_total_revenue = monthly_spread_revenue + monthly_commission_revenue
            annual_revenue = monthly_total_revenue * 12

            st.success("### Calculation Results")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Pip Value", f"${pip_value:,.2f}")
            with col2:
                st.metric("Spread Cost", f"${spread_cost:,.2f}")
            with col3:
                st.metric("Commission", f"${total_commission:,.2f}")
            with col4:
                st.metric("Total Trade Cost", f"${total_cost:,.2f}")

            # P&L Section
            st.subheader(f"P&L Analysis ({pip_movement:+d} pips)")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Gross P&L", f"${pnl:,.2f}")
            with col2:
                st.metric("Trading Costs", f"${total_cost:,.2f}")
            with col3:
                st.metric("Net P&L", f"${net_pnl:,.2f}")

            # Broker Revenue Projection
            st.subheader("Broker Revenue Projection")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Monthly Spread Revenue", f"${monthly_spread_revenue:,.2f}")
            with col2:
                st.metric("Monthly Commission Revenue", f"${monthly_commission_revenue:,.2f}")
            with col3:
                st.metric("Total Monthly Revenue", f"${monthly_total_revenue:,.2f}")
            with col4:
                st.metric("Annual Revenue", f"${annual_revenue:,.2f}")

            # Detailed cost breakdown table
            cost_data = {
                "Cost Component": [
                    "Position Size",
                    "Pip Value",
                    "Spread (pips)",
                    "Spread Cost",
                    "Commission per Lot",
                    "Total Commission",
                    "Total Trading Cost",
                    "Cost as % of Position"
                ],
                "Value": [
                    f"{position_size} {lot_size.split()[0]} lots",
                    f"${pip_value:,.2f} per pip",
                    f"{spread_pips} pips",
                    f"${spread_cost:,.2f}",
                    f"${commission_per_lot:,.2f}",
                    f"${total_commission:,.2f}",
                    f"${total_cost:,.2f}",
                    f"{(total_cost / (contract_size * position_size * current_price) * 100):.3f}%"
                ]
            }

            st.dataframe(pd.DataFrame(cost_data), use_container_width=True, hide_index=True)

            # Breakeven calculation
            breakeven_pips = total_cost / pip_value
            st.info(f"ℹ️ Position must move {breakeven_pips:.1f} pips in your favor to break even after costs")

            # Visualization - P&L at different pip movements
            pip_range = list(range(-200, 201, 10))
            pnl_values = [(p * pip_value) - total_cost for p in pip_range]

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=pip_range,
                y=pnl_values,
                mode='lines',
                fill='tozeroy',
                name='Net P&L',
                line=dict(color='blue', width=2),
                fillcolor='rgba(0,100,255,0.2)'
            ))

            fig.add_hline(y=0, line_dash="dash", line_color="black", annotation_text="Breakeven")
            fig.add_vline(x=breakeven_pips, line_dash="dot", line_color="red", annotation_text=f"BE: {breakeven_pips:.1f} pips")

            fig.update_layout(
                title="P&L Profile Across Pip Movements",
                xaxis_title="Pip Movement",
                yaxis_title="Net P&L ($)",
                showlegend=True,
                height=400
            )

            st.plotly_chart(fig, use_container_width=True)

    # Tool 4: Net Exposure & Hedging Calculator
    elif tool == "Net Exposure & Hedging":
        st.header("Net Exposure & Hedging Calculator")
        st.markdown("Calculate aggregate client positions and determine hedging requirements")

        st.subheader("Enter Client Positions")

        # Currency pair selection
        currency_pair = st.selectbox(
            "Currency Pair",
            options=["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF", "NZD/USD", "USD/CAD", "EUR/GBP", "GBP/JPY", "EUR/JPY"],
            key="exposure_pair"
        )

        num_clients = st.number_input("Number of Client Positions", min_value=1, max_value=50, value=5)

        client_positions = []

        for i in range(num_clients):
            with st.expander(f"Client {i+1}", expanded=(i<3)):
                col1, col2, col3 = st.columns(3)
                with col1:
                    client_id = st.text_input("Client ID", value=f"CLIENT{i+1:03d}", key=f"exp_client_{i}")
                with col2:
                    direction = st.selectbox("Direction", options=["Long", "Short"], key=f"exp_dir_{i}")
                with col3:
                    lots = st.number_input("Lots", min_value=0.01, max_value=100.0, value=1.0, step=0.01, key=f"exp_lots_{i}")

                client_positions.append({
                    "Client ID": client_id,
                    "Direction": direction,
                    "Lots": lots,
                    "Signed Lots": lots if direction == "Long" else -lots
                })

        col1, col2 = st.columns(2)

        with col1:
            current_price = st.number_input(
                "Current Market Price",
                min_value=0.0001,
                value=1.1000,
                step=0.0001,
                format="%.4f",
                key="exposure_price"
            )

            exposure_limit = st.number_input(
                "Broker Exposure Limit (lots)",
                min_value=0.0,
                value=10.0,
                step=1.0,
                help="Maximum net exposure broker is willing to carry"
            )

        with col2:
            lp_spread = st.number_input(
                "LP Spread Cost (pips)",
                min_value=0.0,
                value=0.5,
                step=0.1,
                help="Cost to hedge with liquidity provider"
            )

            pip_value_per_lot = st.number_input(
                "Pip Value per Lot ($)",
                min_value=0.0,
                value=10.0,
                step=0.1
            )

        if st.button("Calculate Net Exposure", type="primary"):
            df = pd.DataFrame(client_positions)

            # Calculate net exposure
            total_long = df[df['Direction'] == 'Long']['Lots'].sum()
            total_short = df[df['Direction'] == 'Short']['Lots'].sum()
            net_exposure = total_long - total_short

            # Determine hedge requirement
            if abs(net_exposure) > exposure_limit:
                hedge_required = abs(net_exposure) - exposure_limit
                hedge_direction = "Sell" if net_exposure > 0 else "Buy"
            else:
                hedge_required = 0
                hedge_direction = "None"

            # Calculate costs
            hedge_cost = hedge_required * lp_spread * pip_value_per_lot
            exposure_kept = min(abs(net_exposure), exposure_limit)

            # Risk calculation (if market moves 100 pips)
            risk_per_100_pips = exposure_kept * 100 * pip_value_per_lot

            st.success("### Net Exposure Analysis")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Total Long Positions", f"{total_long:.2f} lots")
            with col2:
                st.metric("Total Short Positions", f"{total_short:.2f} lots")
            with col3:
                st.metric("Net Exposure", f"{net_exposure:+.2f} lots", delta=f"{'Long' if net_exposure > 0 else 'Short' if net_exposure < 0 else 'Neutral'}")
            with col4:
                exposure_pct = (abs(net_exposure) / exposure_limit * 100) if exposure_limit > 0 else 0
                st.metric("Exposure vs Limit", f"{exposure_pct:.1f}%")

            # Hedging recommendation
            st.subheader("Hedging Recommendation")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Hedge Required", f"{hedge_required:.2f} lots")
            with col2:
                st.metric("Hedge Direction", hedge_direction)
            with col3:
                st.metric("Hedge Cost", f"${hedge_cost:,.2f}")

            if abs(net_exposure) > exposure_limit:
                st.warning(f"⚠️ Net exposure exceeds limit! Recommend hedging {hedge_required:.2f} lots via {hedge_direction}")
            else:
                st.success(f"✅ Net exposure within limits. No hedge required.")

            # Risk metrics
            st.subheader("Risk Metrics")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Exposure Kept on Books", f"{exposure_kept:.2f} lots")
            with col2:
                st.metric("Risk per 100 pips", f"${risk_per_100_pips:,.2f}")

            # Position breakdown table
            st.subheader("Client Position Breakdown")
            display_df = df[['Client ID', 'Direction', 'Lots']].copy()
            st.dataframe(display_df, use_container_width=True, hide_index=True)

            # Visualization - Long vs Short
            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=['Long Positions', 'Short Positions', 'Net Exposure', 'Exposure Limit'],
                y=[total_long, total_short, abs(net_exposure), exposure_limit],
                marker_color=['green', 'red', 'blue', 'orange'],
                text=[f'{total_long:.2f}', f'{total_short:.2f}', f'{abs(net_exposure):.2f}', f'{exposure_limit:.2f}'],
                textposition='outside'
            ))

            fig.update_layout(
                title="Position Exposure Analysis",
                yaxis_title="Lots",
                showlegend=False,
                height=400
            )

            st.plotly_chart(fig, use_container_width=True)

    # Tool 5: Client Position Monitor Dashboard
    elif tool == "Client Position Monitor":
        st.header("Client Position Monitor Dashboard")
        st.markdown("Real-time monitoring of all open client positions with risk flagging")

        st.subheader("Enter Client Positions")

        num_positions = st.number_input("Number of Open Positions", min_value=1, max_value=30, value=8)

        positions = []

        for i in range(num_positions):
            with st.expander(f"Position {i+1}", expanded=(i<3)):
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    client_id = st.text_input("Client ID", value=f"C{i+1:04d}", key=f"mon_client_{i}")
                    pair = st.selectbox("Pair", options=["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF"], key=f"mon_pair_{i}")

                with col2:
                    direction = st.selectbox("Direction", options=["Long", "Short"], key=f"mon_dir_{i}")
                    lots = st.number_input("Lots", min_value=0.01, value=1.0, step=0.01, key=f"mon_lots_{i}")

                with col3:
                    entry_price = st.number_input("Entry Price", min_value=0.0001, value=1.1000, step=0.0001, format="%.4f", key=f"mon_entry_{i}")
                    current_price = st.number_input("Current Price", min_value=0.0001, value=1.1050, step=0.0001, format="%.4f", key=f"mon_curr_{i}")

                with col4:
                    equity = st.number_input("Client Equity ($)", min_value=0.0, value=10000.0, step=100.0, key=f"mon_equity_{i}")
                    duration_hours = st.number_input("Duration (hours)", min_value=0, value=24, key=f"mon_dur_{i}")

                # Calculate P&L
                pip_movement = (current_price - entry_price) * 10000 if "JPY" not in pair else (current_price - entry_price) * 100
                if direction == "Short":
                    pip_movement = -pip_movement

                pip_value = 10 if "JPY" not in pair else (10 / current_price * 100)
                pnl = pip_movement * pip_value * lots

                # Calculate margin level (simplified)
                margin_used = (lots * 100000 * entry_price) / 100  # Assuming 100:1 leverage
                margin_level = (equity / margin_used * 100) if margin_used > 0 else 0

                positions.append({
                    "Client ID": client_id,
                    "Pair": pair,
                    "Direction": direction,
                    "Lots": lots,
                    "Entry": entry_price,
                    "Current": current_price,
                    "Pips": pip_movement,
                    "P&L": pnl,
                    "Equity": equity,
                    "Margin Level": margin_level,
                    "Duration (hrs)": duration_hours
                })

        if st.button("Analyze Positions", type="primary"):
            df = pd.DataFrame(positions)

            # Calculate aggregate metrics
            total_pnl = df['P&L'].sum()
            winning_positions = len(df[df['P&L'] > 0])
            losing_positions = len(df[df['P&L'] < 0])
            positions_at_risk = len(df[df['Margin Level'] < 150])

            st.success("### Position Summary")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Total Open Positions", len(df))
            with col2:
                st.metric("Aggregate Client P&L", f"${total_pnl:,.2f}")
            with col3:
                st.metric("Winning Positions", winning_positions)
            with col4:
                st.metric("At Risk (ML < 150%)", positions_at_risk)

            # Risk flagging
            st.subheader("Risk Alerts")

            # Flag positions near margin call
            margin_call_positions = df[df['Margin Level'] < 150]
            if len(margin_call_positions) > 0:
                st.warning(f"⚠️ {len(margin_call_positions)} position(s) approaching margin call threshold")
                for idx, row in margin_call_positions.iterrows():
                    st.error(f"🚨 {row['Client ID']} - {row['Pair']} - Margin Level: {row['Margin Level']:.1f}%")
            else:
                st.success("✅ All positions have healthy margin levels")

            # Flag large positions
            large_positions = df[df['Lots'] > 5]
            if len(large_positions) > 0:
                st.info(f"ℹ️ {len(large_positions)} large position(s) detected (>5 lots)")

            # Full position table
            st.subheader("All Open Positions")

            # Format display dataframe
            display_df = df.copy()
            display_df['P&L'] = display_df['P&L'].apply(lambda x: f"${x:,.2f}")
            display_df['Equity'] = display_df['Equity'].apply(lambda x: f"${x:,.0f}")
            display_df['Margin Level'] = display_df['Margin Level'].apply(lambda x: f"{x:.1f}%")
            display_df['Pips'] = display_df['Pips'].apply(lambda x: f"{x:+.1f}")

            st.dataframe(display_df, use_container_width=True, hide_index=True)

            # Visualization - P&L by client
            fig = go.Figure()

            colors = ['green' if pnl > 0 else 'red' for pnl in df['P&L']]

            fig.add_trace(go.Bar(
                x=df['Client ID'],
                y=df['P&L'],
                marker_color=colors,
                text=[f'${pnl:,.0f}' for pnl in df['P&L']],
                textposition='outside'
            ))

            fig.update_layout(
                title="Client P&L Overview",
                xaxis_title="Client ID",
                yaxis_title="P&L ($)",
                showlegend=False,
                height=400
            )

            st.plotly_chart(fig, use_container_width=True)

            # Pair concentration
            st.subheader("Position Concentration by Pair")
            pair_summary = df.groupby('Pair')['Lots'].sum().reset_index()
            pair_summary.columns = ['Currency Pair', 'Total Lots']

            fig2 = px.pie(pair_summary, values='Total Lots', names='Currency Pair', title='Position Distribution by Pair')
            st.plotly_chart(fig2, use_container_width=True)

    # Tool 6: A-Book vs B-Book Decision Tool
    else:  # A-Book vs B-Book
        st.header("A-Book vs B-Book Decision Tool")
        st.markdown("Analyze client profitability and determine optimal booking strategy")

        st.subheader("Enter Client Trading History")

        num_clients = st.number_input("Number of Clients to Analyze", min_value=1, max_value=20, value=6)

        clients = []

        for i in range(num_clients):
            with st.expander(f"Client {i+1}", expanded=(i<3)):
                col1, col2, col3 = st.columns(3)

                with col1:
                    client_id = st.text_input("Client ID", value=f"CLIENT{i+1:03d}", key=f"ab_client_{i}")
                    total_trades = st.number_input("Total Trades (30 days)", min_value=1, value=50, key=f"ab_trades_{i}")
                    winning_trades = st.number_input("Winning Trades", min_value=0, value=25, key=f"ab_wins_{i}")

                with col2:
                    avg_trade_size = st.number_input("Avg Trade Size (lots)", min_value=0.01, value=1.0, step=0.01, key=f"ab_size_{i}")
                    total_volume = st.number_input("Total Volume (lots)", min_value=0.0, value=50.0, step=1.0, key=f"ab_vol_{i}")
                    avg_hold_time = st.number_input("Avg Hold Time (hours)", min_value=0.1, value=24.0, step=0.1, key=f"ab_hold_{i}")

                with col3:
                    gross_pnl = st.number_input("Client Gross P&L ($)", value=1000.0, step=100.0, key=f"ab_pnl_{i}")
                    commission_paid = st.number_input("Commission Paid ($)", min_value=0.0, value=350.0, step=10.0, key=f"ab_comm_{i}")

                # Calculate metrics
                win_rate = (winning_trades / total_trades * 100) if total_trades > 0 else 0
                losing_trades = total_trades - winning_trades
                profit_factor = abs(gross_pnl / (commission_paid + 1)) if commission_paid > 0 else 0

                # Determine if toxic flow
                is_toxic = win_rate > 60 or avg_trade_size > 5 or avg_hold_time < 2
                is_profitable_to_broker = gross_pnl < 0  # Client is losing

                clients.append({
                    "Client ID": client_id,
                    "Total Trades": total_trades,
                    "Win Rate": win_rate,
                    "Avg Trade Size": avg_trade_size,
                    "Total Volume": total_volume,
                    "Avg Hold Time": avg_hold_time,
                    "Client P&L": gross_pnl,
                    "Commission Revenue": commission_paid,
                    "Toxic Flow": is_toxic,
                    "Profitable to Broker": is_profitable_to_broker
                })

        col1, col2 = st.columns(2)

        with col1:
            lp_commission_cost = st.number_input(
                "LP Commission Cost per Lot ($)",
                min_value=0.0,
                value=5.0,
                step=0.5,
                help="Cost to send trades to liquidity provider (A-Book)"
            )

        with col2:
            risk_tolerance = st.selectbox(
                "Broker Risk Tolerance",
                options=["Conservative", "Moderate", "Aggressive"],
                help="How much risk willing to take on B-Book positions"
            )

        if st.button("Analyze Clients & Generate Recommendations", type="primary"):
            df = pd.DataFrame(clients)

            # Calculate net broker revenue for each scenario
            df['A-Book Revenue'] = df['Commission Revenue'] - (df['Total Volume'] * lp_commission_cost)
            df['B-Book Revenue'] = df['Commission Revenue'] - df['Client P&L']  # Broker takes opposite side

            # Determine recommendation
            recommendations = []
            for idx, row in df.iterrows():
                if row['Toxic Flow']:
                    # Toxic flow should be A-Booked to avoid risk
                    recommendation = "A-Book"
                    reason = "Toxic flow - hedge with LP"
                elif row['Win Rate'] < 45:
                    # Losing clients can be B-Booked
                    if risk_tolerance in ["Moderate", "Aggressive"]:
                        recommendation = "B-Book"
                        reason = "Profitable client pattern"
                    else:
                        recommendation = "A-Book"
                        reason = "Conservative policy"
                elif row['Avg Trade Size'] > 5:
                    # Large positions should be hedged
                    recommendation = "A-Book"
                    reason = "Large position size risk"
                else:
                    # Default based on profitability
                    if row['B-Book Revenue'] > row['A-Book Revenue'] and not row['Toxic Flow']:
                        recommendation = "B-Book" if risk_tolerance != "Conservative" else "Hybrid"
                        reason = "More profitable to internalize"
                    else:
                        recommendation = "A-Book"
                        reason = "Better A-Book economics"

                recommendations.append(recommendation)

            df['Recommendation'] = recommendations

            # Summary metrics
            total_abook = len(df[df['Recommendation'] == 'A-Book'])
            total_bbook = len(df[df['Recommendation'] == 'B-Book'])
            total_hybrid = len(df[df['Recommendation'] == 'Hybrid'])

            total_abook_revenue = df[df['Recommendation'] == 'A-Book']['A-Book Revenue'].sum()
            total_bbook_revenue = df[df['Recommendation'] == 'B-Book']['B-Book Revenue'].sum()
            total_revenue = total_abook_revenue + total_bbook_revenue

            st.success("### Booking Strategy Recommendations")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("A-Book Clients", total_abook)
            with col2:
                st.metric("B-Book Clients", total_bbook)
            with col3:
                st.metric("Hybrid Clients", total_hybrid)
            with col4:
                st.metric("Projected Revenue", f"${total_revenue:,.2f}")

            # Revenue breakdown
            st.subheader("Revenue Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("A-Book Revenue", f"${total_abook_revenue:,.2f}")
            with col2:
                st.metric("B-Book Revenue", f"${total_bbook_revenue:,.2f}")

            # Client recommendations table
            st.subheader("Client-by-Client Recommendations")

            display_df = df[[
                'Client ID', 'Win Rate', 'Avg Trade Size', 'Total Volume',
                'Client P&L', 'Commission Revenue', 'Toxic Flow', 'Recommendation'
            ]].copy()

            display_df['Win Rate'] = display_df['Win Rate'].apply(lambda x: f"{x:.1f}%")
            display_df['Client P&L'] = display_df['Client P&L'].apply(lambda x: f"${x:,.0f}")
            display_df['Commission Revenue'] = display_df['Commission Revenue'].apply(lambda x: f"${x:,.0f}")
            display_df['Toxic Flow'] = display_df['Toxic Flow'].apply(lambda x: "⚠️ Yes" if x else "No")

            # Color code recommendations
            def highlight_recommendation(val):
                if val == 'A-Book':
                    return 'background-color: lightblue'
                elif val == 'B-Book':
                    return 'background-color: lightgreen'
                else:
                    return 'background-color: lightyellow'

            st.dataframe(display_df, use_container_width=True, hide_index=True)

            # Visualization - Client categorization
            st.subheader("Client Categorization")

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=df['Win Rate'],
                y=df['Avg Trade Size'],
                mode='markers+text',
                marker=dict(
                    size=df['Total Volume'] / 5,
                    color=[{'A-Book': 'blue', 'B-Book': 'green', 'Hybrid': 'orange'}[r] for r in df['Recommendation']],
                    showscale=False
                ),
                text=df['Client ID'],
                textposition='top center'
            ))

            fig.update_layout(
                title="Client Risk Profile (Size = Volume)",
                xaxis_title="Win Rate (%)",
                yaxis_title="Avg Trade Size (lots)",
                height=500
            )

            # Add risk zones
            fig.add_hline(y=5, line_dash="dash", line_color="red", annotation_text="Large Size Threshold")
            fig.add_vline(x=60, line_dash="dash", line_color="red", annotation_text="High Win Rate (Toxic)")

            st.plotly_chart(fig, use_container_width=True)

            # Booking strategy pie chart
            booking_summary = df['Recommendation'].value_counts().reset_index()
            booking_summary.columns = ['Strategy', 'Count']

            fig2 = px.pie(booking_summary, values='Count', names='Strategy',
                         title='Recommended Booking Distribution',
                         color='Strategy',
                         color_discrete_map={'A-Book': 'lightblue', 'B-Book': 'lightgreen', 'Hybrid': 'lightyellow'})
            st.plotly_chart(fig2, use_container_width=True)


# ========== PRODUCT METRICS ==========
if section == "Product Metrics":
    render_analytics_dashboard(tool)

# Footer
st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Risk Warning**: Trading involves substantial risk of loss.
    Past performance is not indicative of future results.
    Always use proper risk management.
    """
)
