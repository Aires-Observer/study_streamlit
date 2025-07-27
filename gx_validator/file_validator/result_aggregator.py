import pandas as pd
from gx_validator.constant import ResultFieldName

def each_error_line_strategy(detailed_result_df: pd.DataFrame) -> pd.DataFrame:
    result_df = detailed_result_df
    return result_df

def each_rule_column_line_strategy(detailed_result_df: pd.DataFrame) -> pd.DataFrame:
    result_df = detailed_result_df.groupby([ResultFieldName.EXPECTATION_TYPE.value, 
                                            ResultFieldName.COLUMN_NAME.value])\
                                    .size().reset_index(name="Count")
    return result_df

def each_rule_line_strategy(detailed_result_df: pd.DataFrame) -> pd.DataFrame:
    result_df = detailed_result_df.groupby([ResultFieldName.EXPECTATION_TYPE.value])\
                                    .size().reset_index(name="Count")
    return result_df

def each_source_record_strategy(detailed_result_df: pd.DataFrame) -> pd.DataFrame:
    result_df = detailed_result_df.groupby([ResultFieldName.INDEX.value])\
                                    .size().reset_index(name="Count")
    return result_df