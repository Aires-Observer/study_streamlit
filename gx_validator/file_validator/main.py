from gx_validator.file_validator.validation_runner import validate_data
from gx_validator.file_validator.result_executor import extract_raw_gx_result_info
from gx_validator.file_validator.result_aggregator import each_error_line_strategy, \
    each_rule_column_line_strategy, each_rule_line_strategy, each_source_record_strategy
import streamlit as st
import pandas as pd

class FileValidator:
    def __init__(self, df: pd.DataFrame, validate_config: list[dict]):
        self.df = df
        self.validate_config = validate_config

    def run(self):
        # 用validation_started控制点击开始验证后按钮消失并输出验证结果
        if "validation_started" not in st.session_state:
            st.session_state.validation_started = False

        if not st.session_state.validation_started:
            if st.button("开始验证"):
                st.session_state.validation_started = True
                st.rerun()
        else:
            try:
                results = validate_data(self.df, self.validate_config)
                st.success("✅ 数据验证成功！")
                self._show_results(results)
            except Exception as e:
                st.error(f"❌ 文件验证失败: {str(e)}")

    def _show_results(self, results: dict):
        detailed_result_df = extract_raw_gx_result_info(results)
        st.header("📝 验证结果")
        st.subheader("1️⃣ Each Rule Line")
        st.dataframe(each_rule_line_strategy(detailed_result_df))
        st.subheader("2️⃣ Each Rule Column Line")
        st.dataframe(each_rule_column_line_strategy(detailed_result_df))
        st.subheader("3️⃣ Each Source Record")
        st.dataframe(each_source_record_strategy(detailed_result_df))
        st.subheader("4️⃣ Each Error Line")
        st.dataframe(each_error_line_strategy(detailed_result_df))
        st.subheader("5️⃣ GX结果明细")
        st.json(results, expanded=1)