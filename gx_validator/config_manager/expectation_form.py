import streamlit as st    
from gx_validator.constant import Expectation
from gx_validator.constant import ExpectationParam

class ExpectationForm:
    def expect_column_values_to_not_be_null_from(columns: list):
        with st.form(Expectation.EXPECT_COLUMN_VALUES_TO_NOT_BE_NULL.value):
            select_columns = st.multiselect("*️⃣ 请选择验证字段", columns)
            mostly = st.slider("置信度", min_value=0.00, max_value=1.00, value=1.00, step=0.01)
            submit = st.form_submit_button("提交规则")
            if submit:
                for column in select_columns:
                    st.session_state.form_records.append({
                        ExpectationParam.EXPECTATION.value: Expectation.EXPECT_COLUMN_VALUES_TO_NOT_BE_NULL.value,
                        ExpectationParam.COLUMN.value: column,
                        ExpectationParam.MOSTLY.value: mostly
                    })
                st.rerun()

    def expect_column_values_to_be_between_from(columns: list):
        with st.form(Expectation.EXPECT_COLUMN_VALUES_TO_BE_BETWEEN.value):
            select_columns = st.multiselect("*️⃣ 请选择验证字段", columns)
            min_value_str = st.text_input("最小值")
            max_value_str = st.text_input("最大值")
            min_value = float(min_value_str) if min_value_str else None
            max_value = float(max_value_str) if max_value_str else None
            mostly = st.slider("置信度", min_value=0.00, max_value=1.00, value=1.00, step=0.01)
            submit = st.form_submit_button("提交规则")
            if submit:
                for column in select_columns:
                    config = {
                        ExpectationParam.EXPECTATION.value: Expectation.EXPECT_COLUMN_VALUES_TO_BE_BETWEEN.value,
                        ExpectationParam.COLUMN.value: column,
                        ExpectationParam.MINVALUE.value: min_value,
                        ExpectationParam.MAXVALUE.value: max_value,
                        ExpectationParam.MOSTLY.value: mostly
                    }
                    config = {k: v for k, v in config.items() if v is not None}
                    st.session_state.form_records.append(config)
                st.rerun()

    def expect_column_values_to_be_in_set_from(columns: list):
        with st.form(Expectation.EXPECT_COLUMN_VALUES_TO_BE_IN_SET.value):
            select_columns = st.multiselect("*️⃣ 请选择验证字段", columns)
            value_set = st.text_area("*️⃣ 请输入值集合（每个值换行）")
            mostly = st.slider("置信度", min_value=0.00, max_value=1.00, value=1.00, step=0.01)
            submit = st.form_submit_button("提交规则")
            if submit:
                for column in select_columns:
                    st.session_state.form_records.append({
                        ExpectationParam.EXPECTATION.value: Expectation.EXPECT_COLUMN_VALUES_TO_BE_IN_SET.value,
                        ExpectationParam.COLUMN.value: column,
                        ExpectationParam.VALUESET.value: [v.strip() for v in value_set.split("\n")],
                        ExpectationParam.MOSTLY.value: mostly
                    })
                st.rerun()

    def expect_column_values_to_not_be_in_set_from(columns: list):
        with st.form(Expectation.EXPECT_COLUMN_VALUES_TO_NOT_BE_IN_SET.value):
            select_columns = st.multiselect("*️⃣ 请选择验证字段", columns)
            value_set = st.text_area("*️⃣ 请输入值集合（每个值换行）")
            mostly = st.slider("置信度", min_value=0.00, max_value=1.00, value=1.00, step=0.01)
            submit = st.form_submit_button("提交规则")
            if submit:
                for column in select_columns:
                    st.session_state.form_records.append({
                        ExpectationParam.EXPECTATION.value: Expectation.EXPECT_COLUMN_VALUES_TO_NOT_BE_IN_SET.value,
                        ExpectationParam.COLUMN.value: column,
                        ExpectationParam.VALUESET.value: [v.strip() for v in value_set.split("\n")],
                        ExpectationParam.MOSTLY.value: mostly
                    })
                st.rerun()

    def expect_column_values_to_match_date_format_from(columns):
        with st.form(Expectation.EXPECT_COLUMN_VALUES_TO_MATCH_DATE_FORMAT.value):
            select_columns = st.multiselect("*️⃣ 请选择验证字段", columns)
            date_format = st.selectbox("请选择验证格式", ["YYYY-MM-DD", "YYYY-MM", "DD"])
            mostly = st.slider("置信度", min_value=0.00, max_value=1.00, value=1.00, step=0.01)
            submit = st.form_submit_button("提交规则")
            if submit:
                for column in select_columns:
                    st.session_state.form_records.append({
                        ExpectationParam.EXPECTATION.value: Expectation.EXPECT_COLUMN_VALUES_TO_MATCH_DATE_FORMAT.value,
                        ExpectationParam.COLUMN.value: column,
                        ExpectationParam.DATE_FORMAT.value: date_format,
                        ExpectationParam.MOSTLY.value: mostly
                    })
                st.rerun()

    def expect_column_values_to_meet_date_condition_from(columns):
        with st.form(Expectation.EXPECT_COLUMN_VALUES_TO_MEET_DATE_CONDITION.value):
            select_columns = st.multiselect("*️⃣ 请选择验证字段", columns)
            date = st.date_input("请选择日期")
            operator = st.selectbox("请选择比较符", ["==", ">", "<", ">=", "<="])
            mostly = st.slider("置信度", min_value=0.00, max_value=1.00, value=1.00, step=0.01)
            submit = st.form_submit_button("提交规则")
            if submit:
                for column in select_columns:
                    st.session_state.form_records.append({
                        ExpectationParam.EXPECTATION.value: Expectation.EXPECT_COLUMN_VALUES_TO_MEET_DATE_CONDITION.value,
                        ExpectationParam.COLUMN.value: column,
                        ExpectationParam.DATE.value: date.strftime("%Y-%m-%d"),
                        ExpectationParam.OPERATOR.value: operator,
                        ExpectationParam.MOSTLY.value: mostly
                    })
                st.rerun()  