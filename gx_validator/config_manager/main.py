import streamlit as st    
from gx_validator.constant import Expectation, EXPECTATION_PARAM_MAPPING
from gx_validator.config_manager.expectation_form import ExpectationForm

class ConfigManager:
    def __init__(self, columns: list):
        self.columns = columns

    def run(self):
        st.subheader("⚙️ 校验规则")
        # 初始化
        if "form_records" not in st.session_state:
            st.session_state.form_records = []
            st.session_state.config_submitted = False

        self._show_records()
        # 如果未提交配置，显示新建规则下拉框
        if not st.session_state.config_submitted:
            options = ["请选择规则"] + [k.value for k in Expectation]
            rule_type = st.selectbox("➕ 新建规则", options, key="rule_type")
            if rule_type != "请选择规则":
                self._show_form(rule_type)
            if st.session_state.form_records and st.button("提交配置"):
                st.session_state.config_submitted = True
                st.rerun()
        # 如果已提交配置，显示提交成功并返回配置给调用者
        else:
            st.success("✅ 配置提交成功！")
            return st.session_state.form_records

    def _show_form(self, rule_type: str):
        rule_form = {
            Expectation.EXPECT_COLUMN_VALUES_TO_NOT_BE_NULL.value: ExpectationForm.expect_column_values_to_not_be_null_from,
            Expectation.EXPECT_COLUMN_VALUES_TO_BE_BETWEEN.value: ExpectationForm.expect_column_values_to_be_between_from,
            Expectation.EXPECT_COLUMN_VALUES_TO_BE_IN_SET.value: ExpectationForm.expect_column_values_to_be_in_set_from,
            Expectation.EXPECT_COLUMN_VALUES_TO_NOT_BE_IN_SET.value: ExpectationForm.expect_column_values_to_not_be_in_set_from,
            Expectation.EXPECT_COLUMN_VALUES_TO_MATCH_DATE_FORMAT.value: ExpectationForm.expect_column_values_to_match_date_format_from,
            Expectation.EXPECT_COLUMN_VALUES_TO_MEET_DATE_CONDITION.value: ExpectationForm.expect_column_values_to_meet_date_condition_from,
        }
        if rule_type in rule_form:
            rule_form[rule_type](self.columns)

    def _show_records(self):
        if st.session_state.form_records:
            with st.expander("📚 提交记录", expanded=True):
                for i, record in enumerate(st.session_state.form_records, 1):
                    new_record = {}
                    for k, v in record.items():
                        new_key = EXPECTATION_PARAM_MAPPING.get(k, k)
                        new_record[new_key] = v
                    st.write(f"{i}. {new_record}")