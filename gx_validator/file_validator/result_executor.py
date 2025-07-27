import pandas as pd
from gx_validator.constant import ResultFieldName

def extract_raw_gx_result_info(gx_result: dict) -> pd.DataFrame:
    raw_result_info = []
    for result in gx_result["results"]:
        try:
            expectation_config = result["expectation_config"]
            result_data = result["result"]
            column_name = expectation_config["kwargs"]["column"]
            raw_result = {
                ResultFieldName.EXPECTATION_TYPE.value: expectation_config["expectation_type"],
                ResultFieldName.COLUMN_NAME.value: column_name,
                ResultFieldName.VALIDATION_RESULT.value: result["success"],
                ResultFieldName.INDEX.value: [item["index"] for item in result_data["unexpected_index_list"]],
                ResultFieldName.UNEXPECTED_VALUE.value: [item[column_name] for item in result_data["unexpected_index_list"]]
            }
            raw_result_info.append(raw_result)
        except Exception as e:
            raise ValueError(f"Invalid GX result structure: {e}")
    flattened_result_info = _flatten_result_info(raw_result_info)
    detailed_result_df = pd.DataFrame(
        flattened_result_info,
        columns=[field.value for field in ResultFieldName]
    )
    return detailed_result_df
        
def _flatten_result_info(raw_result_info: list[dict]) -> list[list]:
    flattened_result_info = []
    for item in raw_result_info:
        expectation_type = item[ResultFieldName.EXPECTATION_TYPE.value]
        column_name = item[ResultFieldName.COLUMN_NAME.value]
        result = str(item[ResultFieldName.VALIDATION_RESULT.value])
        if item[ResultFieldName.INDEX.value]:
            for i, index in enumerate(item[ResultFieldName.INDEX.value]):
                unexpected_value = item[ResultFieldName.UNEXPECTED_VALUE.value][i]
                unexpected_value = None if unexpected_value is None else str(unexpected_value)
                flattened_result_info.append([expectation_type, column_name, result, index, unexpected_value])
        # else:
        #     flattened_result_info.append([expectation_type, column_name, result, None, None])
    return flattened_result_info