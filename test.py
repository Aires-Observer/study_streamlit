import streamlit as st
from sidebar import *
import os
from gx_validator.main import gx_validator_func

current_dir = os.path.dirname(os.path.abspath(__file__))

# 设置页面配置
st.set_page_config(
    page_title = "Streamlit 学习示例标签页",
    page_icon = "🚀", # 标签页的图标
    layout = "wide",
    initial_sidebar_state = "expanded"
)

# layout: 控制页面布局宽度
#     - wide: 页面宽度占满浏览器窗口 
#       - 适合数据表格、图表展示、仪表盘应用
#       - 适合需要复杂用户界面时    
#     - centered: 页面居中，适合博客类型
#       - 适合内容展示、文章阅读、博客和简单表单
#       - 适合以文字内容为主的应用
#       - 适合移动端友好的设计

# initial_sidebar_state: 控制侧边栏初始状态
#     - expanded: 侧边栏默认展开
#     - collapsed: 侧边栏默认折叠
#     - auto: 根据屏幕宽度自动决定，通常桌面端展开，移动端收起

with open (os.path.join(current_dir, "style.css"), "r", encoding="utf-8") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    # 使用markdown是需要全局注入样式，st.html 只会在当前容器内生效
    # unsafe_allow_html=True 允许渲染CSS、HTML等内容并且支持嵌入JavaScript

# 固定页眉
# st.html("""
#         <div class="fixed-header">
#             <h2>Streamlit 学习平台</h2>
#         </div>
#         """)

# 固定页脚
st.html("""
        <div class="fixed-footer">
            <p>📧 support@example.com | 📱 123-456-7890 | © 2025</p>
        </div>
        """)

# 包装主内容
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# 设置侧边栏及对应页面功能
PAGES = {
    "文本标题": text_basic_feature_func,
    "输入组件": input_basic_feature_func,
    "数据展示": data_basic_feature_func,
    "图表可视化": plot_basic_feature_func,
    "布局和容器": layout_basic_feature_func,
    "状态管理": status_basic_feature_func,
    "文件上传": file_basic_feature_func,
}

st.sidebar.title("📋 侧边栏导航")

# 侧边栏一级分类
main_options = ["基础功能", "数据校验"]
main_choice = st.sidebar.selectbox("选择主功能", main_options)

# 侧边栏二级分类
sub_pages = {
    "基础功能": list(PAGES.keys()),
    "数据校验": ["Pandas"]
}
sub_choice = st.sidebar.selectbox("选择子功能", sub_pages[main_choice])

# 根据选择加载对应页面
if sub_choice in PAGES:
    PAGES[sub_choice]()  # 根据选择切换主内容
elif sub_choice == "Pandas":
    gx_validator_func()

# 侧边栏页脚
st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 侧边栏页脚")
st.sidebar.markdown("""
                    - 每个功能都有示例代码
                    - [Streamlit 官方文档](https://docs.streamlit.io)
                    """)

# 页面固定内容，会紧跟在侧边栏加载的功能页面之后
st.markdown("---")
st.markdown("### 🚀 页脚：如何运行这个应用？")
st.code("""
        # 1. 安装依赖
        pip install -r requirements.txt

        # 2. 运行应用
        streamlit run test.py

        # 3. 在浏览器中查看应用
        # 通常会自动打开 http://localhost:8501
        """, language='bash')