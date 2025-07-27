import os
import streamlit as st
import pandas as pd
from streamlit.runtime.uploaded_file_manager import UploadedFile

class FileManager:
    def __init__(self, uploaded_file: UploadedFile):
        self.uploaded_file = uploaded_file

    def show_example_download_button(self):
        file_name = "test_data.csv"
        file_dir = os.path.dirname(__file__)
        with open(os.path.join(file_dir, file_name), "rb") as f:
            csv = f.read()
        st.download_button(label="下载示例 CSV 文件", data=csv, file_name=file_name, mime='text/csv')

    def show_file_info_and_preview(self):
        if self.uploaded_file is not None:
            df = pd.read_csv(self.uploaded_file)
            st.success(f"✅ 文件上传成功！共有 {len(df)} 行数据")
            st.write("文件信息:")
            st.write(f"- 文件名: {self.uploaded_file.name}")
            st.write(f"- 文件大小: {self._format_size(self.uploaded_file.size)}")
            st.subheader("数据预览")
            st.dataframe(df.head(30))
            return df
        return None

    def _format_size(self, size: int) -> str:
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024