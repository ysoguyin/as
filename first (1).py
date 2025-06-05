import streamlit as st   # 导入Streamlit并用st代表它
import pandas as pd   # 导入Pandas并用pd代替
import time

st.title('学生 张三-档案') # 创建标题
st.header("✉:基本信息")  # 创建章节
# 创建学生信息文本
st.text('''
学生ID:230511701XX
注册时间：2023.09|精神状态：良好
安全等级：安全
''')
st.subheader('📖:技能')  # 创建章节
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="c", value="60%", delta="10%")
c2.metric(label="python", value="50%", delta="6%")
c3.metric(label="java", value="10%", delta="0", delta_color="off")

st.header("streamlit学习进度") # 创建章节
progress_text_1='streamlit课程进度'
# 创建进度条
my_bar=st.progress(0,text=progress_text_1)
time.sleep(0.5)
for percent in range(20):
    time.sleep(0.1)
    my_bar.progress(percent+1,text=f'{progress_text_1},当前进度{percent}%:hourglass:')


st.header("🔖：任务日志",anchor='任务日志') # 创建章节
# 定义数据，方便创建数据框
data = {
    '任务':['学生档案管理','课程管理','数据图表'],
    '进度':['✅:green[完成]','🕐进行中','❌未完成'],
    '难度':['⭐⭐','⭐⭐⭐','⭐⭐⭐⭐'],
}
# 定义数据框所用的索引
index = pd.Series(['2023', '2024','2025'], name='时间')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)
st.table(df)

st.header("🎌：代码成果",anchor='代码成果')
st.subheader('代码展示')

# 创建要显示的Python代码块的内容
python_code='''
def matrix_breach():
      while True:
            if detect_vulnerability():
                exploit()
                return  "ABCDEFG HIJKLMM"
            else:
                 stealth_evade()
'''
# 创建一个代码块，用于展示python_code的内容
# 并设置language为True，即该代码块语法高亮
st.code(python_code, line_numbers=True)
# 代码说明
st.caption(':green[>> SYSTEM MESSAGE:]下一个任务目标已解锁...')
st.caption(':green[>> TARGET:]课程管理系统')
st.caption(':green[>> SYSTEM MESSAGE:]2025-6-05-11:00:24')
st.caption('系统状态:在线 连接状态:已加密')

