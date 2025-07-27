import streamlit as st

def layout_basic_feature_func():
    st.header("📐 布局和容器功能")
    
    # 列布局
    st.subheader("📚 列布局")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("第一列")
        st.button("按钮1")
    with col2:
        st.write("第二列")
        st.button("按钮2")
    with col3:
        st.write("第三列")
        st.button("按钮3")
    
    # 容器
    st.subheader("📦 容器")
    with st.container():
        st.write("这是一个容器内的内容")
        st.write("可以包含多个元素")
    
    # 展开器
    st.subheader("🔽 展开器")
    with st.expander("点击展开查看详细信息"):
        st.write("这里是隐藏的详细信息")
        st.write("只有点击展开器才能看到")
    
    # 标签页
    st.subheader("📑 标签页")
    tab1, tab2, tab3 = st.tabs(["标签1", "标签2", "标签3"])
    with tab1:
        st.write("这是标签1的内容")
    with tab2:
        st.write("这是标签2的内容")
    with tab3:
        st.write("这是标签3的内容")