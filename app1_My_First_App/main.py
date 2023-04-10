import streamlit as st

st.title('My first app')


st.write("""st.write()是Streamlit的瑞士军刀，
        你可以把任何东西丢给st.write()： 文本、数据、Matplotlib图表、Altair图表等等。
        别担心，Streamlit可以 自动识别数据类型并正确绘制。""")

st.markdown('## st.markdown - 显示markdown文本')

st.markdown('### 方法原型')
code = '''
streamlit.markdown(body, unsafe_allow_html=False)
'''
st.code(code, language='python')

st.markdown('''#### 调用参数：
- body：要显示的markdown文本，字符串。采用github增强语法，参考 https://github.github.com/gfm
- unsafe_allow_html： 是否允许出现html标签，布尔值，默认：false，表示所有的html标签都将转义。 注意，这是一个临时特性，在将来可能取消。
''')

st.markdown('### 示例代码')
code = '''
>>> st.markdown('Streamlit is **_really_ cool**.')
'''
st.code(code, language='python')

