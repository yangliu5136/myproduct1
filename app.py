import time

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tornado.gen import sleep

name = st.sidebar.text_input('name')
age = st.sidebar.slider(label='streamlit',min_value=0,max_value=10)

st.write(f'姓名{name},年龄{age}')

#缓存
@st.cache_data
def cache_data():
    file = pd.read_csv('./data_csv1.csv')
    st.write(file)

cache_data()

#上传文件

file1 = st.file_uploader('选择一个文件')
if file1 is not None:
    file2 = pd.read_csv(file1)
    st.write(file2)

# 显示散点图
fig , ax =plt.subplots()
ax.scatter([1,2,3],[1,2,3])
st.pyplot(fig)

#显示进度条
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i+1)
    time.sleep(0.1)
st.success('进度条结束')