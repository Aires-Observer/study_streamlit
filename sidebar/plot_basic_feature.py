import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def plot_basic_feature_func():
    st.header("📈 图表可视化功能")
    
    # 生成示例数据
    @st.cache_data
    def generate_chart_data():
        # 从2024-01-01开始生成30天的日期数据，periods=30表示30天，freq='D'表示按天
        dates = pd.date_range('2024-01-01', periods=30, freq='D') # 一个DatetimeIndex对象
        data = {
            '日期': dates,
            '销售额': np.random.randint(1000, 5000, 30),
            '访问量': np.random.randint(100, 1000, 30)
        }
        return pd.DataFrame(data)
    
    df = generate_chart_data()
    
    # 折线图
    st.subheader("📉 折线图")
    st.line_chart(df.set_index('日期')['销售额'])
    # df.set_index('日期')['销售额']返回一个series，不影响原df，索引为日期，值为销售额

    # 柱状图
    st.subheader("📊 柱状图")
    st.bar_chart(df.set_index('日期')[['销售额', '访问量']])

    # 散点图
    st.subheader("🔍 散点图")
    fig_scatter = px.scatter(df, x='销售额', y='访问量', title='销售额 vs 访问量关系图')
    st.plotly_chart(fig_scatter)
    
    # Matplotlib 图表
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False # 设置中文字体支持

    st.subheader("🎨 Matplotlib 图表")
    fig, ax = plt.subplots()
    ax.hist(df['销售额'], bins=10, alpha=0.7)
    ax.set_xlabel('销售额')
    ax.set_ylabel('频次')
    ax.set_title('销售额分布图')
    st.pyplot(fig)
    
    # 地图数据
    st.subheader("🗺️ 地图可视化")
    map_data = pd.DataFrame({
        'lat': [39.9042, 31.2304, 23.1291, 22.3193],
        'lon': [116.4074, 121.4737, 113.2644, 114.1694],
        'city': ['北京', '上海', '广州', '深圳'],
        'size': [100, 150, 120, 130]
    }) # 必须有 'lat' 和 'lon' 列
    # st.map() 只需要经纬度列，其他列可以用于标记
    st.map(map_data[['lat', 'lon']])