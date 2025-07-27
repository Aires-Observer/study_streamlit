import streamlit as st

def text_basic_feature_func():
    st.header("📝 文本标题功能")

    # streamlit格式
    st.title("streamlit格式的一级标题")
    st.header("streamlit格式的二级标题")
    st.subheader("streamlit格式的三级标题")
    st.write("streamlit格式的普通文本")

    # markdown格式
    st.markdown("# markdown格式的一级标题")
    st.markdown("## markdown格式的二级标题")
    st.markdown("### markdown格式的三级标题")
    st.markdown("markdown格式的普通文本")
    st.markdown("**粗体文本** 和 *斜体文本*")
    st.markdown("`行内代码`")

    # 三引号格式
    """三引号格式的普通文本"""

    # 代码展示
    st.code("""
            # Python 代码示例
            def hello_streamlit():
                return "Hello, Streamlit!"
            """,
            language='python')
    
    st.markdown("""
                ```python
                # Python 代码示例
                def hello_streamlit():
                    return "Hello, Streamlit!"
                ```
                """)  # 使用 markdown 格式展示代码

    # LaTeX 数学公式
    st.latex(r"""
             \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)
             """)
    
    st.markdown(r"""
                $$\sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)$$
                """)  # 使用 markdown 格式展示 LaTeX 公式