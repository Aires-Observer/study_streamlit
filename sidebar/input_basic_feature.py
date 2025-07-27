import streamlit as st
from datetime import date

def input_basic_feature_func():
    st.header("🎛️ 输入组件功能")

    # 文本输入，value 参数设置默认值
    name = st.text_input("请输入您的姓名：", value="张三")
    st.write(f"你好，{name}！")

    # 数字输入，可以设置最小值、最大值，超出范围会有自动提醒
    age = st.number_input("请输入您的年龄：", min_value=0, max_value=120, value=25)
    st.write(f"您今年 {age} 岁")

    # 滑块，设置范围和默认值，输入的值要么全为整数要么全为小数
    score = st.slider("选择一个分数", min_value=0.0, max_value=100.0, value=50.0, step=0.25)
    st.write(f"您选择的分数是：{score}")

    # 下拉单选框，提供多个选项供用户选择
    city = st.selectbox("选择您的城市", ["北京", "上海", "广州", "深圳"])
    st.write(f"您选择的城市是：{city}")

    # 下拉多选框，提供多个选项供用户选择
    hobbies = st.multiselect("选择您的爱好", ["读书", "运动", "音乐", "电影", "旅行"])
    if hobbies:
        st.write(f"您的爱好有：{', '.join(hobbies)}")

    # 单选按钮
    gender = st.radio("选择您的性别", ["男", "女", "其他"])
    st.write(f"您的性别是：{gender}")

    # 勾选框
    agree = st.checkbox("我同意服务条款")
    if agree:
        st.write("感谢您的同意！")

    # 日期选择
    selected_date = st.date_input("选择日期", date.today())
    st.write(f"您选择的日期是：{selected_date}")
    
    # 时间选择
    selected_time = st.time_input("选择时间")
    st.write(f"您选择的时间是：{selected_time}")