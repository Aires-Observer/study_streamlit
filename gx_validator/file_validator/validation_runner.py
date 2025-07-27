import great_expectations as gx
import pandas as pd
from great_expectations.datasource.fluent import Datasource, DataAsset, BatchRequest
from great_expectations.validator.validator import Validator

# 避免streamlit的热重载反复注册自定义的期望
if not hasattr(gx, "_custom_expectations_registered"):
    from gx_validator.file_validator.custom_expectations.expect_column_values_to_match_date_format import ExpectColumnValuesToMatchDateFormat
    from gx_validator.file_validator.custom_expectations.expect_column_values_to_meet_date_condition import ExpectColumnValuesToMeetDateCondition
    gx._custom_expectations_registered = True

def validate_data(df: pd.DataFrame, validate_config: list[dict]) -> dict:
    context = gx.get_context()
    source_name = "test_pandas_data_source"
    data_source: Datasource = context.sources.add_or_update_pandas(name=source_name)
    data_asset: DataAsset = data_source.add_dataframe_asset(name="test_asset", dataframe=df)
    batch_request: BatchRequest = data_asset.build_batch_request()
    suite_name = "test_suite"
    context.add_or_update_expectation_suite(expectation_suite_name=suite_name)
    validator: Validator = context.get_validator(batch_request=batch_request, expectation_suite_name=suite_name)
    
    for config in validate_config:
        params = {k: v for k, v in config.items() if k != "expectation"}
        expectation = getattr(validator, config["expectation"])
        if expectation:
            expectation(**params)

    result_format = {
        "result_format": "COMPLETE", 
        "unexpected_index_column_names": ["index"],
        "return_unexpected_index_query": True,
    }
    results = validator.validate(result_format=result_format)
    return results.to_json_dict()