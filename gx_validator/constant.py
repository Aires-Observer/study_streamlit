from enum import Enum

class ResultFieldName(Enum):
    EXPECTATION_TYPE = "Expectation Type"
    COLUMN_NAME = "Column Name"
    VALIDATION_RESULT = "Validation Result"
    INDEX = "Index"
    UNEXPECTED_VALUE = "Unexpected Value"

class Expectation(Enum):
    EXPECT_COLUMN_VALUES_TO_NOT_BE_NULL = "expect_column_values_to_not_be_null"
    EXPECT_COLUMN_VALUES_TO_BE_BETWEEN = "expect_column_values_to_be_between"
    EXPECT_COLUMN_VALUES_TO_BE_IN_SET = "expect_column_values_to_be_in_set"
    EXPECT_COLUMN_VALUES_TO_NOT_BE_IN_SET = "expect_column_values_to_not_be_in_set"
    EXPECT_COLUMN_VALUES_TO_MATCH_DATE_FORMAT = "expect_column_values_to_match_date_format"
    EXPECT_COLUMN_VALUES_TO_MEET_DATE_CONDITION = "expect_column_values_to_meet_date_condition"

class ExpectationParam(Enum):
    EXPECTATION = "expectation"
    COLUMN = "column"
    MOSTLY = "mostly"
    MINVALUE = "min_value"
    MAXVALUE = "max_value"
    VALUESET = "value_set"
    DATE_FORMAT = "date_format"
    DATE = "date"
    OPERATOR = "operator"

EXPECTATION_PARAM_MAPPING = {
    ExpectationParam.EXPECTATION.value: "期望",
    ExpectationParam.COLUMN.value: "验证字段",
    ExpectationParam.MOSTLY.value: "置信度",
    ExpectationParam.MINVALUE.value: "最小值",
    ExpectationParam.MAXVALUE.value: "最大值",
    ExpectationParam.VALUESET.value: "值集合",
    ExpectationParam.DATE_FORMAT.value: "日期格式",
    ExpectationParam.DATE.value: "日期",
    ExpectationParam.OPERATOR.value: "比较符"
}
