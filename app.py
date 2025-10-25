import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

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
    ["Trader Models", "Broker Models"]
)

st.sidebar.markdown("---")

# Tool selection based on section
if section == "Trader Models":
    st.sidebar.header("Trader Tools")
    tool = st.sidebar.radio(
        "Select Tool:",
        ["Position Sizing", "Portfolio Risk", "Value at Risk (VaR)", "Risk/Reward Analysis"]
    )
else:  # Broker Models
    st.sidebar.header("Broker Tools")
    tool = st.sidebar.radio(
        "Select Tool:",
        ["Margin & Leverage", "Swap/Rollover Rates", "Pip Value & Commission"]
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
    else:  # Pip Value & Commission
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

# Footer
st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Risk Warning**: Trading involves substantial risk of loss.
    Past performance is not indicative of future results.
    Always use proper risk management.
    """
)
