from gx_validator.file_manager import FileManager
from gx_validator.file_validator.main import FileValidator
from gx_validator.config_manager.main import ConfigManager
import streamlit as st

def gx_validator_func():
    st.header("📁 上传文件")
    uploaded_file = st.file_uploader("选择一个 CSV 文件", type=['csv'])
    file_manager = FileManager(uploaded_file)
    file_manager.show_example_download_button()
    original_df = file_manager.show_file_info_and_preview()
    if original_df is not None:
        columns = list(original_df.columns)
        validate_config = ConfigManager(columns).run()
        if validate_config:
            validation_executor = FileValidator(original_df, validate_config)
            validation_executor.run()