import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 入門')

st.write("DataFrame")

left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ててて')
expander = st.beta_expander("問い合わせ内容")
expander.write("問い合わせ内容を書く")
# df = pd.DataFrame({
#     '1列目': [1,2,3,4],
#     '2列目': [10,20,30,40]
# })

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0),width=800,height=800)

"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
"""