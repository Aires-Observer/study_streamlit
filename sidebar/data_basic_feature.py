import streamlit as st
import numpy as np
import pandas as pd

def data_basic_feature_func():
    st.header("📊 数据展示功能")
    
    # 创建示例数据
    @st.cache_data # 使用缓存装饰器，避免重复计算
    # 第一次运行时需要加载数据并转换为 DataFrame，第二次直接从缓存中获取
    def create_sample_data():
        np.random.seed(42)
        data = {
            '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
            '年龄': np.random.randint(20, 60, 5),
            '薪资': np.random.randint(5000, 20000, 5),
            '部门': ['技术部', '销售部', '人事部', '财务部', '市场部']
        }
        return pd.DataFrame(data)

    # 调用创建的示例数据 
    df = create_sample_data()
    
    # 显示数据表
    st.subheader("📋 数据表格")
    st.dataframe(df)
    
    # 静态表格
    st.subheader("📄 静态表格")
    st.table(df)    
    
    # st.dataframe vs st.table
    # st.dataframe: 支持交互式操作，如排序、过滤、搜索、滚动
    # st.table: 静态表格，不支持交互式操作

    # 关键指标
    st.subheader("📈 关键指标")
    col1, col2, col3 = st.columns(3) # 创建三列布局
    with col1: # 设计指标卡片
        st.metric("平均年龄", f"{df['年龄'].mean():.1f}岁")
    with col2: # delta 参数显示变化量，正数显示为绿色向上的箭头，负数显示为红色向下的箭头
        st.metric("平均薪资", f"{df['薪资'].mean():.0f}元", delta=f"{df['薪资'].std():.0f}")
    with col3:
        st.metric("员工总数", len(df))
    
    # JSON 数据
    st.subheader("🔧 JSON 数据")
    sample_json = {
        "用户": "张三",
        "设置": {
            "主题": "深色模式",
            "语言": "中文",
            "通知": True
        }
    }
    st.json(sample_json) # 美观显示 JSON 数据，自动格式化和语法高亮