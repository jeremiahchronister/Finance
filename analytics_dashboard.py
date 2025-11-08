"""
Product Metrics & Analytics Dashboard for Forex Risk Calculator Platform
"""
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px


def generate_sample_data():
    """Generate realistic sample data for analytics dashboard"""

    # Monthly data for the past 24 months
    months = pd.date_range(end=datetime.now(), periods=24, freq='M')

    # Business Metrics
    broker_growth = [5, 5, 8, 12, 15, 18, 22, 25, 30, 35, 42, 50, 58, 65, 72, 80, 88, 95, 100, 105, 108, 110, 112, 115]
    mrr_data = [14.5, 14.5, 23, 35, 44, 53, 64, 73, 87, 102, 122, 145, 168, 189, 209, 232, 256, 276, 290, 305, 314, 319, 325, 334]  # in thousands
    churn_rate = [0, 0, 4, 3.5, 3.2, 3.0, 2.8, 2.7, 2.6, 2.5, 2.5, 2.4, 2.4, 2.3, 2.3, 2.2, 2.2, 2.1, 2.5, 2.3, 2.2, 2.1, 2.2, 2.0]

    # User Engagement Metrics
    mau_data = [4000, 4000, 6400, 9600, 12000, 14400, 17600, 20000, 24000, 28000, 33600, 40000, 46400, 52000, 57600, 64000, 70400, 76000, 80000, 84000, 86400, 88000, 89600, 92000]
    calculations_per_day = [x / 30 * 10 for x in mau_data]  # Avg 10 calcs per user per month
    dau_data = [x * 0.15 for x in mau_data]  # 15% stickiness

    # Customer Success Metrics
    churn_reduction = [0, 0, 18, 20, 22, 23, 24, 25, 24, 25, 26, 24, 25, 23, 24, 26, 25, 24, 24, 25, 23, 24, 25, 26]
    nps_scores = [0, 0, 45, 48, 50, 52, 53, 52, 54, 53, 52, 54, 55, 54, 52, 53, 54, 52, 52, 51, 53, 54, 52, 53]

    return {
        'months': months,
        'broker_count': broker_growth,
        'mrr': mrr_data,
        'churn_rate': churn_rate,
        'mau': mau_data,
        'calculations_per_day': calculations_per_day,
        'dau': dau_data,
        'churn_reduction': churn_reduction,
        'nps': nps_scores
    }


def render_business_metrics():
    """Render business metrics dashboard"""
    st.header("Business Metrics Dashboard")
    st.markdown("Track revenue, growth, and broker acquisition metrics")

    data = generate_sample_data()
    df = pd.DataFrame(data)

    # Current metrics (latest month)
    current_brokers = data['broker_count'][-1]
    current_mrr = data['mrr'][-1]
    current_arr = current_mrr * 12
    current_churn = data['churn_rate'][-1]

    # Previous month for comparison
    prev_brokers = data['broker_count'][-2]
    prev_mrr = data['mrr'][-2]
    prev_churn = data['churn_rate'][-2]

    # Calculate deltas
    broker_delta = ((current_brokers - prev_brokers) / prev_brokers * 100) if prev_brokers > 0 else 0
    mrr_delta = ((current_mrr - prev_mrr) / prev_mrr * 100) if prev_mrr > 0 else 0
    churn_delta = current_churn - prev_churn

    # KPI Cards
    st.subheader("Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Active Brokers",
            value=f"{current_brokers}",
            delta=f"{broker_delta:+.1f}% MoM"
        )

    with col2:
        st.metric(
            label="Monthly Recurring Revenue",
            value=f"${current_mrr:.0f}K",
            delta=f"{mrr_delta:+.1f}% MoM"
        )

    with col3:
        st.metric(
            label="Annual Recurring Revenue",
            value=f"${current_arr/1000:.2f}M",
            delta=f"{mrr_delta:+.1f}% MoM"
        )

    with col4:
        st.metric(
            label="Monthly Churn Rate",
            value=f"{current_churn:.1f}%",
            delta=f"{churn_delta:+.1f}pp",
            delta_color="inverse"
        )

    # Revenue Growth Chart
    st.subheader("Revenue Growth Trajectory")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['months'],
        y=df['mrr'],
        name='MRR',
        mode='lines+markers',
        line=dict(color='#1f77b4', width=3),
        fill='tozeroy',
        fillcolor='rgba(31, 119, 180, 0.2)'
    ))

    # Add ARR target line
    arr_target = [290] * len(df['months'])  # Month 24 target
    fig.add_trace(go.Scatter(
        x=df['months'],
        y=arr_target,
        name='Target MRR',
        mode='lines',
        line=dict(color='red', width=2, dash='dash')
    ))

    fig.update_layout(
        title="Monthly Recurring Revenue (MRR) Over Time",
        xaxis_title="Month",
        yaxis_title="MRR ($K)",
        hovermode='x unified',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    # Broker Growth Chart
    st.subheader("Broker Customer Growth")

    fig2 = go.Figure()

    fig2.add_trace(go.Bar(
        x=df['months'],
        y=df['broker_count'],
        name='Active Brokers',
        marker=dict(color='#2ca02c')
    ))

    # Add milestones
    fig2.add_hline(y=25, line_dash="dash", line_color="orange",
                   annotation_text="Q4 2025 Target (25)")
    fig2.add_hline(y=100, line_dash="dash", line_color="red",
                   annotation_text="Month 24 Target (100)")

    fig2.update_layout(
        title="Active Broker Accounts",
        xaxis_title="Month",
        yaxis_title="Number of Brokers",
        height=400
    )

    st.plotly_chart(fig2, use_container_width=True)

    # Revenue by Tier (Mock Data)
    st.subheader("Revenue Breakdown by Tier")

    col1, col2 = st.columns(2)

    with col1:
        # Pie chart of revenue by tier
        tier_data = pd.DataFrame({
            'Tier': ['Standard', 'Professional', 'Enterprise'],
            'Revenue': [203, 133, 51.2],
            'Brokers': [70, 25, 5]
        })

        fig3 = px.pie(
            tier_data,
            values='Revenue',
            names='Tier',
            title='MRR by Tier (Month 24)',
            color='Tier',
            color_discrete_map={'Standard': '#1f77b4', 'Professional': '#ff7f0e', 'Enterprise': '#2ca02c'}
        )

        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        # Bar chart of brokers by tier
        fig4 = px.bar(
            tier_data,
            x='Tier',
            y='Brokers',
            title='Broker Distribution by Tier',
            color='Tier',
            color_discrete_map={'Standard': '#1f77b4', 'Professional': '#ff7f0e', 'Enterprise': '#2ca02c'}
        )

        fig4.update_layout(showlegend=False)

        st.plotly_chart(fig4, use_container_width=True)

    # Churn Analysis
    st.subheader("Churn Rate Analysis")

    fig5 = go.Figure()

    fig5.add_trace(go.Scatter(
        x=df['months'],
        y=df['churn_rate'],
        mode='lines+markers',
        name='Monthly Churn Rate',
        line=dict(color='red', width=2)
    ))

    # Add target churn line
    fig5.add_hline(y=3.0, line_dash="dash", line_color="green",
                   annotation_text="Target: <3%")

    fig5.update_layout(
        title="Monthly Broker Churn Rate",
        xaxis_title="Month",
        yaxis_title="Churn Rate (%)",
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)


def render_user_engagement():
    """Render user engagement metrics"""
    st.header("User Engagement Metrics")
    st.markdown("Track platform usage, calculations, and trader activity")

    data = generate_sample_data()
    df = pd.DataFrame(data)

    # Current metrics
    current_mau = data['mau'][-1]
    current_dau = data['dau'][-1]
    current_calcs = data['calculations_per_day'][-1]

    # Previous month
    prev_mau = data['mau'][-2]
    prev_dau = data['dau'][-2]
    prev_calcs = data['calculations_per_day'][-2]

    # Deltas
    mau_delta = ((current_mau - prev_mau) / prev_mau * 100) if prev_mau > 0 else 0
    dau_delta = ((current_dau - prev_dau) / prev_dau * 100) if prev_dau > 0 else 0
    calcs_delta = ((current_calcs - prev_calcs) / prev_calcs * 100) if prev_calcs > 0 else 0

    # Stickiness ratio
    stickiness = (current_dau / current_mau * 100) if current_mau > 0 else 0

    # KPI Cards
    st.subheader("Engagement KPIs")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Monthly Active Users (MAU)",
            value=f"{current_mau:,.0f}",
            delta=f"{mau_delta:+.1f}% MoM"
        )

    with col2:
        st.metric(
            label="Daily Active Users (DAU)",
            value=f"{current_dau:,.0f}",
            delta=f"{dau_delta:+.1f}% MoM"
        )

    with col3:
        st.metric(
            label="Calculations/Day",
            value=f"{current_calcs:,.0f}",
            delta=f"{calcs_delta:+.1f}% MoM"
        )

    with col4:
        st.metric(
            label="Stickiness (DAU/MAU)",
            value=f"{stickiness:.1f}%",
            delta="Healthy" if stickiness >= 15 else "Needs Improvement",
            delta_color="normal" if stickiness >= 15 else "inverse"
        )

    # MAU Growth Chart
    st.subheader("Monthly Active Users Growth")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['months'],
        y=df['mau'],
        name='MAU',
        mode='lines+markers',
        line=dict(color='#1f77b4', width=3),
        fill='tozeroy',
        fillcolor='rgba(31, 119, 180, 0.2)'
    ))

    fig.add_hline(y=80000, line_dash="dash", line_color="red",
                  annotation_text="Month 24 Target (80K)")

    fig.update_layout(
        title="Monthly Active Users Over Time",
        xaxis_title="Month",
        yaxis_title="MAU",
        hovermode='x unified',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    # DAU vs MAU Comparison
    st.subheader("Daily vs Monthly Active Users")

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        x=df['months'],
        y=df['mau'],
        name='MAU',
        mode='lines',
        line=dict(color='#1f77b4', width=2)
    ))

    fig2.add_trace(go.Scatter(
        x=df['months'],
        y=df['dau'],
        name='DAU',
        mode='lines',
        line=dict(color='#ff7f0e', width=2)
    ))

    fig2.update_layout(
        title="DAU vs MAU Trend",
        xaxis_title="Month",
        yaxis_title="Users",
        hovermode='x unified',
        height=400
    )

    st.plotly_chart(fig2, use_container_width=True)

    # Calculations per Day
    st.subheader("Platform Usage (Calculations per Day)")

    fig3 = go.Figure()

    fig3.add_trace(go.Bar(
        x=df['months'],
        y=df['calculations_per_day'],
        name='Calculations/Day',
        marker=dict(color='#2ca02c')
    ))

    fig3.update_layout(
        title="Daily Calculation Volume",
        xaxis_title="Month",
        yaxis_title="Calculations per Day",
        height=400
    )

    st.plotly_chart(fig3, use_container_width=True)

    # User Segmentation
    st.subheader("User Segmentation by Activity")

    # Mock segmentation data
    segments = pd.DataFrame({
        'Segment': ['Power Users (15+ calcs/mo)', 'Active Users (6-14 calcs/mo)',
                   'Casual Users (1-5 calcs/mo)', 'Inactive (0 calcs)'],
        'Users': [18400, 36800, 27600, 9200],  # MAU = 92000
        'Percentage': [20, 40, 30, 10]
    })

    col1, col2 = st.columns(2)

    with col1:
        fig4 = px.pie(
            segments,
            values='Users',
            names='Segment',
            title='User Distribution by Activity Level',
            hole=0.4
        )
        st.plotly_chart(fig4, use_container_width=True)

    with col2:
        fig5 = px.bar(
            segments,
            x='Segment',
            y='Users',
            title='Users by Activity Segment',
            color='Segment'
        )
        fig5.update_layout(showlegend=False, xaxis_tickangle=-45)
        st.plotly_chart(fig5, use_container_width=True)


def render_customer_success():
    """Render customer success metrics"""
    st.header("Customer Success Metrics")
    st.markdown("Track broker impact, trader outcomes, and satisfaction scores")

    data = generate_sample_data()
    df = pd.DataFrame(data)

    # Current metrics
    current_churn_reduction = data['churn_reduction'][-1]
    current_nps = data['nps'][-1]

    # Targets
    target_churn_reduction = 25  # 20-30% range
    target_nps = 50

    # KPI Cards
    st.subheader("Success KPIs")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Broker Churn Reduction",
            value=f"{current_churn_reduction}%",
            delta=f"Target: 20-30%",
            delta_color="normal" if 20 <= current_churn_reduction <= 30 else "off"
        )

    with col2:
        st.metric(
            label="Broker NPS Score",
            value=f"{current_nps}",
            delta=f"Target: ≥50",
            delta_color="normal" if current_nps >= 50 else "inverse"
        )

    with col3:
        st.metric(
            label="Trader 90-Day Survival",
            value="48%",
            delta="+13pp vs industry (35%)",
            delta_color="normal"
        )

    with col4:
        st.metric(
            label="Support Ticket Reduction",
            value="56%",
            delta="Target: 30%",
            delta_color="normal"
        )

    # Churn Reduction Impact Chart
    st.subheader("Broker Client Churn Reduction Impact")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['months'],
        y=df['churn_reduction'],
        name='Churn Reduction',
        mode='lines+markers',
        line=dict(color='#2ca02c', width=3),
        fill='tozeroy',
        fillcolor='rgba(44, 160, 44, 0.2)'
    ))

    # Target range
    fig.add_hrect(y0=20, y1=30, fillcolor="green", opacity=0.1, line_width=0,
                  annotation_text="Target Range (20-30%)", annotation_position="top right")

    fig.update_layout(
        title="% Reduction in Broker's 90-Day Trader Churn",
        xaxis_title="Month",
        yaxis_title="Churn Reduction (%)",
        hovermode='x unified',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    # NPS Trend
    st.subheader("Broker Net Promoter Score (NPS) Trend")

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        x=df['months'],
        y=df['nps'],
        name='NPS',
        mode='lines+markers',
        line=dict(color='#ff7f0e', width=3)
    ))

    fig2.add_hline(y=50, line_dash="dash", line_color="green",
                   annotation_text="Target NPS: 50")

    # NPS zones
    fig2.add_hrect(y0=0, y1=30, fillcolor="red", opacity=0.1, line_width=0,
                   annotation_text="Needs Improvement", annotation_position="bottom left")
    fig2.add_hrect(y0=30, y1=50, fillcolor="yellow", opacity=0.1, line_width=0,
                   annotation_text="Good", annotation_position="bottom left")
    fig2.add_hrect(y0=50, y1=100, fillcolor="green", opacity=0.1, line_width=0,
                   annotation_text="Excellent", annotation_position="bottom left")

    fig2.update_layout(
        title="Broker Net Promoter Score Over Time",
        xaxis_title="Month",
        yaxis_title="NPS",
        hovermode='x unified',
        height=400
    )

    st.plotly_chart(fig2, use_container_width=True)

    # Case Study Results
    st.subheader("Pilot Broker Case Studies")

    case_studies = pd.DataFrame({
        'Broker': ['Apex Forex', 'Global Markets FX', 'TradePro', 'ForexEdge', 'SwiftTrade'],
        'Clients': [2500, 8500, 1200, 3500, 5000],
        'Baseline Churn': [65, 70, 62, 68, 64],  # %
        'Post-Platform Churn': [48, 52, 45, 50, 47],  # %
        'Churn Reduction': [26, 26, 27, 26, 27],  # %
        'Support Tickets Reduced': [56, 48, 62, 52, 58]  # %
    })

    st.dataframe(
        case_studies.style.format({
            'Clients': '{:,}',
            'Baseline Churn': '{:.0f}%',
            'Post-Platform Churn': '{:.0f}%',
            'Churn Reduction': '{:.0f}%',
            'Support Tickets Reduced': '{:.0f}%'
        }).background_gradient(subset=['Churn Reduction'], cmap='Greens'),
        use_container_width=True,
        hide_index=True
    )

    # Trader Survival by Calculator Usage
    st.subheader("Trader Outcomes by Platform Engagement")

    usage_outcomes = pd.DataFrame({
        'Usage Segment': ['Never Used', 'Used 1-5x', 'Used 6-15x', 'Used 16+x'],
        '90-Day Survival Rate': [32, 42, 55, 68],
        'Avg Account Balance Change': [-10, 0, 5, 12]
    })

    col1, col2 = st.columns(2)

    with col1:
        fig3 = px.bar(
            usage_outcomes,
            x='Usage Segment',
            y='90-Day Survival Rate',
            title='Trader Survival Rate by Calculator Usage',
            color='90-Day Survival Rate',
            color_continuous_scale='Greens',
            text='90-Day Survival Rate'
        )
        fig3.update_traces(texttemplate='%{text}%', textposition='outside')
        fig3.update_layout(showlegend=False, xaxis_tickangle=-45)
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        fig4 = px.bar(
            usage_outcomes,
            x='Usage Segment',
            y='Avg Account Balance Change',
            title='Account Balance Change by Calculator Usage',
            color='Avg Account Balance Change',
            color_continuous_scale='RdYlGn',
            text='Avg Account Balance Change'
        )
        fig4.update_traces(texttemplate='%{text}%', textposition='outside')
        fig4.update_layout(showlegend=False, xaxis_tickangle=-45)
        st.plotly_chart(fig4, use_container_width=True)


def render_roi_analysis():
    """Render ROI analysis for brokers"""
    st.header("ROI Analysis for Brokers")
    st.markdown("Calculate return on investment for broker partners")

    st.subheader("Broker ROI Calculator")

    col1, col2 = st.columns(2)

    with col1:
        broker_clients = st.number_input(
            "Number of Active Clients",
            min_value=100,
            max_value=20000,
            value=2000,
            step=100
        )

        baseline_churn = st.slider(
            "Baseline 90-Day Churn Rate (%)",
            min_value=50,
            max_value=80,
            value=65,
            step=1
        )

        cac = st.number_input(
            "Client Acquisition Cost ($)",
            min_value=100,
            max_value=1000,
            value=600,
            step=50
        )

    with col2:
        support_tickets_month = st.number_input(
            "Risk-Related Support Tickets/Month",
            min_value=0,
            max_value=2000,
            value=240,
            step=10
        )

        cost_per_ticket = st.number_input(
            "Cost per Support Ticket ($)",
            min_value=5,
            max_value=50,
            value=15,
            step=1
        )

        avg_client_ltv = st.number_input(
            "Average Client LTV ($)",
            min_value=100,
            max_value=2000,
            value=600,
            step=50
        )

    # Calculate ROI
    st.subheader("ROI Analysis Results")

    # Assumptions
    churn_reduction_pct = 25  # 25% reduction
    support_reduction_pct = 56  # 56% reduction
    platform_cost_annual = 34800  # $2,900/mo

    # Calculations
    churned_clients_baseline = broker_clients * (baseline_churn / 100)
    churned_clients_with_platform = churned_clients_baseline * (1 - churn_reduction_pct / 100)
    clients_saved = churned_clients_baseline - churned_clients_with_platform

    churn_savings = clients_saved * cac
    support_savings_annual = support_tickets_month * 12 * cost_per_ticket * (support_reduction_pct / 100)
    total_annual_value = churn_savings + support_savings_annual

    roi = ((total_annual_value - platform_cost_annual) / platform_cost_annual * 100)

    # Display results
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Annual Platform Cost",
            value=f"${platform_cost_annual:,.0f}"
        )

    with col2:
        st.metric(
            label="Annual Value Delivered",
            value=f"${total_annual_value:,.0f}"
        )

    with col3:
        st.metric(
            label="Return on Investment",
            value=f"{roi:.1f}x",
            delta=f"${total_annual_value - platform_cost_annual:,.0f} net benefit"
        )

    # Breakdown
    st.subheader("Value Breakdown")

    value_breakdown = pd.DataFrame({
        'Value Source': ['Churn Reduction', 'Support Cost Savings'],
        'Annual Value': [churn_savings, support_savings_annual]
    })

    col1, col2 = st.columns(2)

    with col1:
        fig = px.pie(
            value_breakdown,
            values='Annual Value',
            names='Value Source',
            title='Annual Value by Source',
            hole=0.4,
            color_discrete_sequence=['#2ca02c', '#1f77b4']
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = px.bar(
            value_breakdown,
            x='Value Source',
            y='Annual Value',
            title='Annual Value Comparison',
            text='Annual Value',
            color='Value Source',
            color_discrete_sequence=['#2ca02c', '#1f77b4']
        )
        fig2.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
        fig2.update_layout(showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)

    # Detailed breakdown
    st.markdown("#### Detailed Calculations")

    breakdown_details = pd.DataFrame({
        'Metric': [
            'Baseline Churned Clients (annual)',
            'Churned Clients with Platform',
            'Clients Saved',
            'Value of Saved Clients (CAC × Clients Saved)',
            'Support Tickets Reduced (annual)',
            'Support Cost Savings',
            'Total Annual Value',
            'Platform Cost',
            'Net Benefit',
            'ROI Multiple'
        ],
        'Value': [
            f"{churned_clients_baseline:,.0f}",
            f"{churned_clients_with_platform:,.0f}",
            f"{clients_saved:,.0f}",
            f"${churn_savings:,.0f}",
            f"{support_tickets_month * 12 * support_reduction_pct / 100:,.0f}",
            f"${support_savings_annual:,.0f}",
            f"${total_annual_value:,.0f}",
            f"$({platform_cost_annual:,.0f})",
            f"${total_annual_value - platform_cost_annual:,.0f}",
            f"{roi:.1f}x"
        ]
    })

    st.dataframe(breakdown_details, use_container_width=True, hide_index=True)

    # Sensitivity Analysis
    st.subheader("Sensitivity Analysis")

    churn_reduction_range = np.arange(15, 36, 1)
    roi_range = []

    for cr in churn_reduction_range:
        clients_saved_temp = churned_clients_baseline * (cr / 100)
        churn_savings_temp = clients_saved_temp * cac
        total_value_temp = churn_savings_temp + support_savings_annual
        roi_temp = ((total_value_temp - platform_cost_annual) / platform_cost_annual)
        roi_range.append(roi_temp)

    fig3 = go.Figure()

    fig3.add_trace(go.Scatter(
        x=churn_reduction_range,
        y=roi_range,
        mode='lines',
        fill='tozeroy',
        line=dict(color='#2ca02c', width=3),
        fillcolor='rgba(44, 160, 44, 0.2)'
    ))

    fig3.add_vline(x=25, line_dash="dash", line_color="red",
                   annotation_text="Expected: 25%")

    fig3.update_layout(
        title="ROI Sensitivity to Churn Reduction %",
        xaxis_title="Churn Reduction (%)",
        yaxis_title="ROI Multiple",
        height=400
    )

    st.plotly_chart(fig3, use_container_width=True)


def render_analytics_dashboard(selected_view):
    """Main function to render analytics dashboard based on selected view"""

    if selected_view == "Business Metrics":
        render_business_metrics()
    elif selected_view == "User Engagement":
        render_user_engagement()
    elif selected_view == "Customer Success":
        render_customer_success()
    elif selected_view == "ROI Analysis":
        render_roi_analysis()
