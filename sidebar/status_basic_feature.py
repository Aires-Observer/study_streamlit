import streamlit as st

def status_basic_feature_func():
    st.header("💾 状态管理功能")
    
    # 会话状态
    # st.session_state 用于存储会话级别的状态，类似一个字典存储变量
    # 可以在不同的交互中保持状态并对状态进行操作
    if 'counter' not in st.session_state:
        st.session_state.counter = 0
    
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    
    # 定义回调函数，用于在特定事件发生后自动执行
    def increment():
        st.session_state.counter += 1
    
    def decrement():
        st.session_state.counter -= 1
    
    def reset():
        st.session_state.counter = 0
    
    # 显示当前值
    st.subheader(f"🔢 计数器当前值: {st.session_state.counter}")
    
    # 按钮操作
    col1, col2, col3 = st.columns(3)
    with col1: # use_container_width=True 确保按钮宽度占满列
        st.button("➕ 增加", on_click=increment, use_container_width=True)
    with col2:
        st.button("➖ 减少", on_click=decrement, use_container_width=True)
    with col3:
        st.button("🔄 重置", on_click=reset, use_container_width=True)

    # 表单示例
    st.subheader("📝 表单")

    # 初始化记录列表及提交状态
    if "form_records" not in st.session_state:
        st.session_state.form_records = []
        st.session_state.form_submitted = False

    if not st.session_state.form_submitted:
        _show_form()
    else:
        if st.button("➕ 新建表单"):
            st.session_state.form_submitted = False
            st.rerun()
            
    _show_records()

def _show_form():
    with st.form("my_form"):
        name = st.text_input("姓名")
        sex = st.selectbox("性别", ["男", "女"])
        age = st.number_input("年龄", min_value=0)
        submit = st.form_submit_button("提交")
        if submit:
            st.session_state.form_records.append({
                "name": name,
                "sex": sex,
                "age": age
            })
            st.success("✅ 提交成功！")
            st.session_state.form_submitted = True
            st.rerun()

def _show_records():
    if st.session_state.form_records:
        with st.expander("📚 提交记录", expanded=True):
            for i, record in enumerate(st.session_state.form_records, 1):
                st.write(f"{i}. 姓名: {record['name']}, 性别: {record['sex']}, 年龄: {record['age']}")

    