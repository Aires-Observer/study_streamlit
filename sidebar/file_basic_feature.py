import streamlit as st
import pandas as pd
import os

def file_basic_feature_func():
    st.header("📁 文件上传功能")
    
    uploaded_file = st.file_uploader("选择一个 CSV 文件", type=['csv'])
    
    if uploaded_file is not None:
        try:
            # 读取 CSV 文件
            df = pd.read_csv(uploaded_file)
            st.success(f"文件上传成功！共有 {len(df)} 行数据")
            
            # 显示文件信息
            st.write("文件信息:")
            st.write(f"- 文件名: {uploaded_file.name}")
            st.write(f"- 文件大小: {uploaded_file.size} 字节")
            
            # 显示数据
            st.subheader("数据预览")
            st.dataframe(df.head())
            
            # 数据摘要
            st.subheader("数据摘要")
            st.write(df.describe())
            
        except Exception as e:
            st.error(f"文件读取失败: {str(e)}")
    else:
        st.info("请上传一个 CSV 文件来查看数据")
        
    # 提供示例下载
    file_name = "test_data.csv"
    with open(os.path.join(os.path.dirname(__file__), file_name), "rb") as f:
        csv = f.read()
    st.download_button(
        label="下载示例 CSV 文件",
        data=csv, # 需要传入二进制字节流
        file_name=file_name,
        mime='text/csv' # 指定文件类型（MIME类型）
    )
    # 常见的 MIME 类型：
    # text/plain：纯文本文件
    # text/csv：CSV文件
    # application/pdf：PDF文件
    # image/png：PNG图片
    # application/zip：ZIP压缩包