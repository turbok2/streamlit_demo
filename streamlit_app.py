import streamlit as st
import requests
# from datetime import time, datetime/
import numpy as np
import altair as alt
import pandas as pd
from time import time
from pathlib import Path
# import pandas_profiling
# from streamlit_pandas_profiling import st_profile_report

# ---------------------------
# day 30

import streamlit as st

st.title('🖼️ yt-img-app')
st.header('YouTube 썸네일 이미지 추출기 앱')

with st.expander('이 앱에 대하여'):
  st.write('이 앱은 YouTube 동영상의 썸네일 이미지를 검색합니다.')

# 이미지 설정
st.sidebar.header('설정')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('이미지 품질 선택', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('YouTube URL 붙여넣기', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid

# YouTube 썸네일 이미지 표시
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube 동영상 썸네일 이미지 URL: ', yt_img)
else:
  st.write('☝️ URL을 입력해 계속하세요 ...')

# ---------------------------
# day 29 - 따라 해보기

# ---------------------------
# day 28
# import streamlit as st
# from streamlit_shap import st_shap
# import shap
# from sklearn.model_selection import train_test_split
# import xgboost
# import numpy as np
# import pandas as pd

# st.set_page_config(layout="wide")

# @st.experimental_memo
# def load_data():
#     return shap.datasets.adult()

# @st.experimental_memo
# def load_model(X, y):
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
#     d_train = xgboost.DMatrix(X_train, label=y_train)
#     d_test = xgboost.DMatrix(X_test, label=y_test)
#     params = {
#         "eta": 0.01,
#         "objective": "binary:logistic",
#         "subsample": 0.5,
#         "base_score": np.mean(y_train),
#         "eval_metric": "logloss",
#         "n_jobs": -1,
#     }
#     model = xgboost.train(params, d_train, 10, evals = [(d_test, "test")], verbose_eval=100, early_stopping_rounds=20)
#     return model

# st.title("`streamlit-shap`로 Streamlit 앱에서 SHAP 플롯 표시하기")

# with st.expander('앱에 대하여'):
#     st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap)는 [SHAP](https://github.com/slundberg/shap) 플롯을 [Streamlit](https://streamlit.io/)에서 표시하기 위한 래퍼를 제공하는 Streamlit 컴포넌트입니다.
#                     이 라이브러리는 저희 내부 직원인 [스네한 케크레](https://github.com/snehankekre)가 개발했으며, [Streamlit 문서화](https://docs.streamlit.io/) 웹사이트도 관리합니다.
#                 ''')

# st.header('입력 데이터')
# X, y = load_data()
# X_display, y_display = shap.datasets.adult(display=True)

# with st.expander('데이터에 대하여'):
#     st.write('예시 데이터셋으로 성인 인구 조사 데이터를 사용합니다.')
# with st.expander('X'):
#     st.dataframe(X)
# with st.expander('y'):
#     st.dataframe(y)

# st.header('SHAP 출력')

# # XGBoost 모델 훈련
# model = load_model(X, y)

# # SHAP 값 계산
# explainer = shap.Explainer(model, X)
# shap_values = explainer(X)

# with st.expander('워터폴 플롯'):
#     st_shap(shap.plots.waterfall(shap_values[0]), height=300)
# with st.expander('비스웜 플롯'):
#     st_shap(shap.plots.beeswarm(shap_values), height=300)

# explainer = shap.TreeExplainer(model)
# shap_values = explainer.shap_values(X)

# with st.expander('포스 플롯'):
#     st.subheader('첫 번째 데이터 인스턴스')
#     st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
#     st.subheader('첫 천 번째 데이터 인스턴스')
#     st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)


# ---------------------------
# day 27
# Streamlit Elements에서는 다음의 객체들이 필요합니다.
# 모든 사용 가능한 객체와 그 사용법은 여기에 나와 있습니다: https://github.com/okld/streamlit-elements#getting-started
# import json
# from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# st.set_page_config(layout="wide")

# with st.sidebar:
#     st.title("🗓️ #30DaysOfStreamlit")
#     st.header("Day 27 - Streamlit Elements")
#     st.write("Streamlit Elements를 사용하여 드래그 가능하고 크기 조절 가능한 대시보드 만들기.")
#     st.write("---")

#     # 미디어 플레이어에 대한 URL 정의.
#     media_url = st.text_input("미디어 URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")
    
# # 코드 편집기와 차트에 대한 기본 데이터 초기화.
# #
# # 이 튜토리얼에서는 Nivo Bump 차트에 필요한 데이터가 필요합니다.
# # 여기서 랜덤 데이터를 얻을 수 있습니다: https://nivo.rocks/bump/의 'data' 탭.
# #
# # 아래에서 보시다시피, 이 세션 상태 항목은 코드 편집기가 변경될 때 업데이트되며,
# # Nivo Bump 차트가 데이터를 그리기 위해 읽을 것입니다.

# if "data" not in st.session_state:
#     st.session_state.data = Path("data.json").read_text()
# #  기본 대시보드 레이아웃을 정의합니다.
# # 대시보드 그리드는 기본적으로 12개의 열을 가지고 있습니다.
# #
# # 사용 가능한 매개변수에 대한 자세한 정보:
# # https://github.com/react-grid-layout/react-grid-layout#grid-item-props
# layout = [
#     # 편집기 항목은 x=0, y=0 좌표에 위치하며, 12/6열을 차지하고 높이는 3입니다.
#     dashboard.Item("editor", 0, 0, 6, 3),
#     # 차트 항목은 x=6, y=0 좌표에 위치하며, 12/6열을 차지하고 높이는 3입니다.
#     dashboard.Item("chart", 6, 0, 6, 3),
#     # 미디어 항목은 x=0, y=3 좌표에 위치하며, 12/6열을 차지하고 높이는 4입니다.
#     dashboard.Item("media", 0, 2, 12, 4),
# ]
# # 요소를 표시할 프레임을 만듭니다.

# with elements("demo"):

#     # 위에서 지정한 레이아웃으로 새 대시보드를 만듭니다.
#     #
#     # draggableHandle은 대시보드 항목의 드래그 가능한 부분을 정의하는 CSS 쿼리 선택자입니다.
#     # 여기서는 'draggable' 클래스 이름을 가진 요소가 드래그 가능합니다.
#     #
#     # 대시보드 그리드에 사용 가능한 매개변수에 대한 자세한 정보:
#     # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
#     # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

#     with dashboard.Grid(layout, draggableHandle=".draggable"):

#         # 첫 번째 카드, 코드 편집기.
#         #
#         # 'key' 매개변수를 사용하여 올바른 대시보드 항목을 식별합니다.
#         #
#         # 카드 콘텐츠가 자동으로 사용 가능한 높이를 채우도록 하려면 CSS flexbox를 사용합니다.
#         # sx는 모든 Material UI 위젯에서 CSS 속성을 정의하는 데 사용할 수 있는 매개변수입니다.
#         #
#         # 카드, flexbox 및 sx에 대한 자세한 정보:
#         # https://mui.com/components/cards/
#         # https://mui.com/system/flexbox/
#         # https://mui.com/system/the-sx-prop/

#         with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

#             # 이 헤더를 드래그 가능하게 만들려면 위의 dashboard.Grid의 draggableHandle에 정의된 대로
#             # 클래스 이름을 'draggable'로 설정하기만 하면 됩니다.

#             mui.CardHeader(title="Editor", className="draggable")

#             # 여기서는 카드 콘텐츠가 사용자가 카드를 줄일 때 줄어들고 사용 가능한 모든 높이를 차지하도록 하기 위해
#             # flex를 1로, minHeight를 0으로 설정합니다.

#             with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

#                 # 여기에 우리의 Monaco 코드 편집기가 있습니다.
#                 #
#                 # 먼저, st.session_state.data에 초기화한 기본값을 설정합니다.
#                 # 두 번째로, 사용할 언어를 JSON으로 정의합니다.
#                 #
#                 # 그런 다음, 편집기 콘텐츠에 대한 변경 사항을 검색하려고 합니다.
#                 # Monaco 문서를 확인하면 onChange 속성이 함수를 사용한다는 것을 알 수 있습니다.
#                 # 이 함수는 변경이 이루어질 때마다 호출되며, 업데이트된 콘텐츠 값이 첫 번째 매개변수로 전달됩니다.
#                 # (cf. onChange: https://github.com/suren-atoyan/monaco-react#props)
#                 #
#                 # Streamlit Elements는 Streamlit의 세션 상태 항목으로 매개변수를 자동으로 전달하는 콜백을 만드는
#                 # 특별한 sync() 함수를 제공합니다.
#                 #
#                 # 예시
#                 # --------
#                 # 첫 번째 매개변수를 "data"라는 세션 상태 항목으로 전달하는 콜백을 생성
#                 # >>> editor.Monaco(onChange=sync("data"))
#                 # >>> print(st.session_state.data)
#                 #
#                 # 두 번째 매개변수를 "ev"라는 세션 상태 항목으로 전달하는 콜백을 생성
#                 # >>> editor.Monaco(onChange=sync(None, "ev"))
#                 # >>> print(st.session_state.ev)
#                 #
#                 # 두 매개변수 모두 세션 상태로 전달하는 콜백을 생성
#                 # >>> editor.Monaco(onChange=sync("data", "ev"))
#                 # >>> print(st.session_state.data)
#                 # >>> print(st.session_state.ev)
#                 #
#                 # onChange는 변경이 발생할 때마다 호출되므로, 단일 문자를 입력할 때마다
#                 # 전체 Streamlit 앱이 다시 실행되는 문제가 있습니다.
#                 #
#                 # 이 문제를 피하기 위해 다른 이벤트(예: 버튼 클릭)가 발생할 때까지 업데이트된 데이터를 보내도록
#                 # Streamlit Elements에게 지시할 수 있습니다. 이는 lazy()로 콜백을 감싸는 것으로 할 수 있습니다.
#                 #
#                 # Monaco에 사용 가능한 매개변수에 대한 자세한 정보:
#                 # https://github.com/suren-atoyan/monaco-react
#                 # https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneEditorConstructionOptions.html

#                 editor.Monaco(
#                     defaultValue=st.session_state.data,
#                     language="json",
#                     onChange=lazy(sync("data"))
#                 )

#             with mui.CardActions:

#                 # Monaco 편집기에는 lazy 콜백이 onChange에 바인딩되어 있으므로, Monaco의 내용을 변경해도
#                 # Streamlit은 직접 알림을 받지 못하고, 따라서 단일 문자를 입력할 때마다 다시 로드되지 않습니다.
#                 # 그래서 다른 비-lazy 이벤트가 업데이트를 트리거할 필요가 있습니다.
#                 #
#                 # 해결책은 클릭 시 콜백을 발생시키는 버튼을 생성하는 것입니다.
#                 # 콜백은 특별히 할 일이 없어도 됩니다. 빈 파이썬 함수를 생성하거나, 아무런 인수 없이 sync()를
#                 # 사용할 수 있습니다.
#                 #
#                 # 이제, 이 버튼을 클릭할 때마다 onClick 콜백이 발생하지만, 그 사이에 변경된 다른 모든 lazy
#                 # 콜백도 호출됩니다.

#                 mui.Button("변경 사항 적용", onClick=sync())

#         # 두 번째 카드, Nivo Bump 차트.
#         # 첫 번째 카드와 동일한 flexbox 구성을 사용하여 콘텐츠 높이를 자동으로 조정합니다.

#         with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

#             # 이 헤더를 드래그 가능하게 만들려면, 위의 dashboard.Grid의 draggableHandle에 정의된 대로
#             # 클래스 이름을 'draggable'로 설정하기만 하면 됩니다.

#             mui.CardHeader(title="차트", className="draggable")

#             # 위와 같이, 사용자가 카드 크기를 조절할 때 콘텐츠가 자동으로 늘어나고 줄어들도록 하기 위해
#             # flex를 1로, minHeight를 0으로 설정합니다.

#             with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

#                 # 여기서 Bump 차트를 그립니다.
#                 #
#                 # 이번 연습에서는 Nivo의 예제를 가져와 Streamlit Elements에서 작동하도록 조정할 수 있습니다.
#                 # Nivo의 예제는 여기 'code' 탭에서 찾을 수 있습니다: https://nivo.rocks/bump/
#                 #
#                 # 데이터는 딕셔너리 형식의 매개변수를 취하므로, `json.loads()`를 사용하여
#                 # JSON 데이터를 문자열에서 파이썬 딕셔너리로 변환해야 합니다.
#                 #
#                 # 다른 Nivo 차트에 대한 자세한 정보는 다음 주소에서 확인할 수 있습니다.
#                 # https://nivo.rocks/

#                 nivo.Bump(
#                     data=json.loads(st.session_state.data),
#                     colors={ "scheme": "spectral" },
#                     lineWidth=3,
#                     activeLineWidth=6,
#                     inactiveLineWidth=3,
#                     inactiveOpacity=0.15,
#                     pointSize=10,
#                     activePointSize=16,
#                     inactivePointSize=0,
#                     pointColor={ "theme": "background" },
#                     pointBorderWidth=3,
#                     activePointBorderWidth=3,
#                     pointBorderColor={ "from": "serie.color" },
#                     axisTop={
#                         "tickSize": 5,
#                         "tickPadding": 5,
#                         "tickRotation": 0,
#                         "legend": "",
#                         "legendPosition": "middle",
#                         "legendOffset": -36
#                     },
#                     axisBottom={
#                         "tickSize": 5,
#                         "tickPadding": 5,
#                         "tickRotation": 0,
#                         "legend": "",
#                         "legendPosition": "middle",
#                         "legendOffset": 32
#                     },
#                     axisLeft={
#                         "tickSize": 5,
#                         "tickPadding": 5,
#                         "tickRotation": 0,
#                         "legend": "ranking",
#                         "legendPosition": "middle",
#                         "legendOffset": -40
#                     },
#                     margin={ "top": 40, "right": 100, "bottom": 40, "left": 60 },
#                     axisRight=None,
#                 )

#         # 대시보드의 세 번째 요소, 미디어 플레이어.

#         with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
#             mui.CardHeader(title="미디어 플레이어", className="draggable")
#             with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

#                 # 이 요소는 ReactPlayer에 의해 구동되며, YouTube 외에도 많은 플레이어를 지원합니다.
#                 # 여기에서 확인할 수 있습니다: https://github.com/cookpete/react-player#props

#                 media.Player(url=media_url, width="100%", height="100%", controls=True)
        
# ---------------------------
# day 26
# st.title('Bored API 앱')

# selected_type = st.sidebar.selectbox('활동유형 선택',["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

# suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
# json_data = requests.get(suggested_activity_url)
# suggested_activity = json_data.json()

# c1, c2 = st.columns(2)
# with c1:
#     with st.expander('이 앱에 대하여'):
#         st.write('지루하신가요? **Bored API 앱**은 지루할 때 할 수 있는 활동을 제안합니다. 이 앱은 Bored API에 의해 구동됩니다.')
        
# with c2:
#     with st.expander('JSON 데이터'):
#         st.write(suggested_activity)

# st.header('제안된 활동')
# st.info(suggested_activity['activity'])

# col1, col2, col3 = st.columns(3)
# with col1:
#     st.metric(label='참가자 수', value=suggested_activity['participants'], delta='')
# with col2:
#     st.metric(label='활동유형', value=suggested_activity['type'], delta='')
# with col3:
#     st.metric(label='가격', value=suggested_activity['price'], delta='')
    
# ---------------------------
# day 25
# st.title('st.session_state')

# def lbs_to_kg():
#     st.session_state.kg = st.session_state.lbs/2.2046
# def kg_to_lbs():
#     st.session_state.lbs = st.session_state.kg*2.2046
    
# st.header('입력')    
# col1, spacer, col2 = st.columns([2,1,2])
# with col1:
#     pounds = st.number_input("파운드",key="lbs", on_change=lbs_to_kg)
# with col2:
#     kilogram = st.number_input("킬로그램",key="kg", on_change=kg_to_lbs)
    
# st.header('출력')    
# st.write("st.session_state 객체:",st.session_state)
# ---------------------------
# day 24
# st.title('st.cache')

# # using cache
# a0 = time()
# st.subheader('st.cache 사용')

# @st.cache_data()
# def load_data_a():
#     df = pd.DataFrame(
#         np.random.rand(2000000, 5),
#         columns=['a','b','c','d','e']                        
#     )
#     return df
    
# st.write(load_data_a())    
# a1 = time()
# st.info(a1-a0)

# # no cache
# b0 = time()
# st.subheader('st.cache 미사용')

# def load_data_b():
#     df = pd.DataFrame(
#         np.random.rand(2000000, 5),
#         columns=['a','b','c','d','e']                        
#     )
#     return df
    
# st.write(load_data_b())    
# b1 = time()
# st.info(b1-b0)


# ---------------------------
# day 23
# st.title('st.experimental_get_query_params')

# with st.expander('이 앱에 대하여'):
#     st.write("`st.experimental_get_query_params`는 사용자 브라우저의 URL에서 직접 쿼리 매개변수를 검색할 수 있데 해줍니다.")
    
# #1
# st.header('1. 지침')
# st.markdown('''
# 인터넷 브라우저의 URL 바에서 다음을 추가하세요:
# `?firstname=Jack&surname=Beanstalk`
# 기본 URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/` 뒤에 추가하여
# `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`가 되도록 합니다.            
#             ''')

# #2
# st.header('2. st.experimental_get_query_params의 내용')
# st.write(st.experimental_get_query_params())

# #3
# st.header('3. URL에서 정보 검색 및 표시')

# first_name =st.experimental_get_query_params()['firstname'][0]
# surname =st.experimental_get_query_params()['surname'][0]

# st.write(f'안녕하세요 **{first_name} {surname}**, 어떠세요?')
# ---------------------------
# day 22
# st.title('st.form')

# st.header('1. `with` 표기법 사용 예시')
# st.subheader('커피 머신')

# with st.form('my_form'):
#     st.subheader('**커피 주문하기**')
    
#     coffee_bean_val = st.selectbox('커피콩',['아라비카','오부스타'])
#     coffee_roast_val = st.selectbox('커피 로스팅', ['라이트', '미디엄', '다크'])
#     brewing_val = st.selectbox('추출 방법', ['에어로프레스', '드립', '프렌치 프레스', '모카 포트', '사이폰'])
#     serving_type_val = st.selectbox('서빙 형식', ['핫', '아이스', '프라페'])
#     milk_val = st.select_slider('우유 정도', ['없음', '낮음', '중간', '높음'])
#     owncup_val = st.checkbox('자신의 컵 가져오기')    
    
#     submitted = st.form_submit_button('제출')
    
#     if submitted:
#         st.markdown(f'''
#         ☕ 주문하신 내용:
#         - 커피콩: `{coffee_bean_val}`
#         - 커피 로스팅: `{coffee_roast_val}`
#         - 추출 방법: `{brewing_val}`
#         - 서빙 형식: `{serving_type_val}`
#         - 우유: `{milk_val}`
#         - 자신의 컵 가져오기: `{owncup_val}`                    
#                     ''')
#     else:
#         st.write('주문하세요.')
        
# st.header('2. 객체 표기법 예시')        
# form = st.form('my_form_2')
# form.subheader('**선택하기**')
# selected_val = form.slider('값 선택')
# form.form_submit_button('제출')

# st.write('선택된 값: ',selected_val)
# ---------------------------
# day 21
# st.title('st.progress')

# with st.expander('이 앱에 대하여'):
#     st.write('st.progress 명령어를 사용하여 Streamlit 앱에서 계산의 진행상태를 표시할 수 있습니다.')
    
# my_bar = st.progress(0)
# for percent_complete in range(100):
#     time.sleep(0.05)
#     my_bar.progress(percent_complete+1)
    
# st.balloons()    
# ---------------------------
 # day 19
# st.set_page_config(layout='wide')
# st.title('Streamlit 앱 레이아웃 구성하기')

# with st.expander('이 앱에 대하여'):
#     st.write('이 앱은 Streamlit 앱을 구성하는 다양한 방법을 보여줍니다.')
#     st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

# st.sidebar.header('입력')    
# user_name = st.sidebar.text_input('당신의 이름은 무엇인가요?')
# user_emoji = st.sidebar.selectbox('이모티콘 선택',['','😄', '😆', '😊', '😍', '😴', '😕', '😱'])
# user_food = st.sidebar.selectbox('가장 좋아하는 음식은?',['','Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

# st.header('출력')

# col1, col2, col3 = st.columns(3)
# with col1:
#     if user_name !='':
#         st.write(f'안녕하세요 {user_name}님!')
#     else:
#         st.write('**이름**을 입력해주세요!')

# with col2:
#     if user_emoji !='':
#         st.write(f'{user_emoji}는 당신 좋아하는 **이모티콘**입니다!')
#     else:
#         st.write('**이모티콘**을 입력해주세요!')

# with col3:
#     if user_food !='':
#         st.write(f'{user_food}는 당신 좋아하는 **음식**입니다!')
#     else:
#         st.write('가장 좋아하는 **음식**을 입력해주세요!')
        
# ---------------------------
# day 18
# st.title('st.file_uploader')

# st.subheader('CSV 입력')
# uploaded_file = st.file_uploader('파일 선택')

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.subheader('DataFrame')
#     st.write(df)
#     st.subheader('기술 통계')
#     st.write(df.describe())
# else:
#     st.write('CSV 파일을 업로드하세요.')
# ---------------------------
# day 17
# st.title('st.secrets')

# st.write(st.secrets['message'])

# ---------------------------
# day 16
# st.title('Streamlit 앱의 테마 사용자 정의하기')

# st.write('이 앱의 `.streamlit/config.toml` 파일 내용')

# st.code("""
# [theme]
# primaryColor="#F39C12"
# backgroundColor="#2E86C1"
# secondaryBackgroundColor="#AED6F1"
# textColor="#FFFFFF"
# font="monospace"
# """)

# number = st.sidebar.slider('숫자를 선택하세요: ',0,10,5)
# st.write('슬라이더 위젯에서 선택된 숫자: ',number)

# ---------------------------
# day 15

# st.header('st.latex')

# st.latex(r'''
#      a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#      \sum_{k=0}^{n-1} ar^k =
#      a \left(\frac{1-r^{n}}{1-r}\right)
#      ''')
# ---------------------------
# day 14 - fail

# st.header('`streamlit_pandas_profiling`')

# # df = pd.read_csv('penguins_cleaned.csv')
# df = pd.DataFrame({
#     'col1':[1,2,3,4],
#     'col2':[10,20,30,40]
# })
# st.write(df)


# pr = df.profile_report()
# st_profile_report(pr)

# ---------------------------
# day 12
# st.header('st.checkbox')
# st.write('주문하고 싶은 것이 무엇인가요?')

# icecream = st.checkbox('아이스크림')
# coffee = st.checkbox('커피')
# cola = st.checkbox('콜라')

# if icecream:
#     st.write("좋아요! 여기 더 많은 아이스크림")
# if coffee:
#     st.write("좋아요! 여기 더 많은 커피")
# if cola:
#     st.write("좋아요! 여기 더 많은 콜라")    
# ---------------------------
# day 11
# st.header('st.multiselect')

# option = st.multiselect(
#     '가장 좋아하는 색상은 무엇인가요?',
#     ['초록','노랑','빨강','파랑'],
#     ['노랑','빨강']
# )
# st.write('당신이 선택한 색상은 ',option)

# ---------------------------
# day 10
# st.header('st.selectbox')

# option = st.selectbox(
#     '가장 좋아하는 색상은 무엇인가요?',
#     ('파랑','빨강','초록')
# )
# st.write('당신이 좋아하는 색상은 ',option)

# ---------------------------
# day 9
# st.header('라인 차트')
# chart_data = pd.DataFrame(
#     np.random.randn(20,3),
#     columns=['a','b','c']
# )

# st.line_chart(chart_data)

# ---------------------------
# day 8
# st.header('st.slider')

# #1
# st.subheader('slider')
# age = st.slider("당신의 나이는?", 0,130, 25)
# st.write("나는 ",age,"살입니다.")

# #2
# st.subheader('범위 slider')
# values = st.slider("값의 범위를 선택하세요.", 0.0, 100.0, (25.0, 75.0))
# st.write("값: ",values)

# #3
# st.subheader('시간 범위 slider')
# appointment = st.slider("약속을 예약하세요:",
#                         value=(time(11,30), time(12,45)),
#                         format="HH:mm")
# st.write("예약된 시간: ",appointment)

# #4
# st.subheader('날짜 및 시간 slider')
# start_time = st.slider("언제 시작하시겠습니까?",
#                        value=datetime(2020,1,1,9,30),
#                        format="MM/DD/YY - hh:mm")
# st.write("값: ",start_time)

#---------------------------
# day 1-7
# st.header('st.write')

# # 1
# st.write("Hello, *World!* :sunglasses:")

# # 2 
# st.write(1234)

# # 3
# df = pd.DataFrame({
#     'col1':[1,2,3,4],
#     'col2':[10,20,30,40]
# })
# st.write(df)

# # 4
# st.write('아래는 DataFrame입니다.', df, '위는  dataframe입니다.')

# # 5
# df2 = pd.DataFrame(
#     np.random.randn(200,3),
#     columns=["a",'b','c']
# )
# c = alt.Chart(df2).mark_circle().encode(
#     x='a', y='b', size='c', color='c', tooltip=['a','b','c']
# )
# st.write(c)