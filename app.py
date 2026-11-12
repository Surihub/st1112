import streamlit as st

st.title("11/12 실습")

# 초기화
if "saved_a1" not in st.session_state:
    st.session_state.saved_a1 = ""
if "saved_a2" not in st.session_state:
    st.session_state.saved_a2 = ""



with st.form("forms1"):
    a1 = st.number_input("a1")
    s1 = st.form_submit_button("제출 1")

if s1:
    st.session_state.saved_a1 = a1 

with st.form("forms2"):
    a2 = st.number_input("a2")
    s2 = st.form_submit_button("제출 2")

if s2:
    st.session_state.saved_a2 = a2  

a1 = st.session_state.saved_a1
a2 = st.session_state.saved_a2

st.write("기억된 a1:", a1)
st.write("기억된 a2:", a2)
st.write(a1+a2)



# with st.expander("기사 원문 보기"):
#     st.write("""[데이터넷] 2027년에는 사이버 공격의 초점이 데이터 탈취에서 기업의 의사결정 조작으로 확대될 것으로 예상된다.

#             구글 클라우드의 ‘2027년 보안 전망(Security Forecast for 2027)’에서는 “AI 에이전트가 계약 협상과 재고 관리, 자본 배분 등 핵심 업무를 자율적으로 수행하면서 공격자들도 데이터가 저장된 시스템을 넘어 기업의 의사결정 과정과 이를 뒷받침하는 데이터, 소프트웨어 공급망을 표적으로 삼기 시작했다”고 경고했다.

#             크리스 베츠(Chris Betz) 구글 클라우드 CISO는 “2027년 기업용 소프트웨어는 가격 결정, 공급업체 계약 협상, 자본 배분, 공급망 재편 등을 실시간으로 수행하는 자율형 에이전트의 집합체로 변화할 것”이라며 “이러한 에이전트가 의존하는 데이터와 기술 기반을 보호하는 것이 중요하다”고 밝혔다.

#             출처 : 데이터넷(https://www.datanet.co.kr)""")



# st.write("dddddd")
# st.write("""내용내용""")

# a, b, c = st.tabs( ["문제1" ,"문제2" ,"문제3"])
# with a:
#     st.write("문제1")
#     st.subheader("1. 식 전개하기")
#     st.latex(r"(x+y)^2")

#     with st.form("forms1"):
#         answer1 = st.radio("전개한 식을 선택해주세요.",
#         [r"$x^2+2x+1$", r"$x^2-2xy+y^2$",
#         r"$x^2+2xy+y^2$", r"$x^2+xy+y^2$"],
#         index=None,)

#         st.session_state.answer1 = answer1
#         submit_button1 = st.form_submit_button("제출")

#     if submit_button1:
#         answer1 = st.session_state.answer1
#         if answer1 == r"$x^2+2xy+y^2$":
#             st.success("정답입니다!")
#         elif answer1 == r"$x^2-2xy+y^2$":
#             st.warning("앗! 부호를 다시 살펴볼까요?")
#         elif answer1 == r"$x^2+xy+y^2$":
#             st.warning("앗! 두번째 항을 다시 살펴볼까요!")
#         else:
#             st.warning("앗! y는 어디로 갔나요!!")




# with b:


#     st.subheader("2. 일차방정식 풀기")
#     st.latex(r"2x+3=7")

#     with st.form("forms2"):
#         answer2 = st.radio("x의 값을 선택해주세요.",
#         [r"$x=2$", r"$x=5$", r"$x=-2$", r"$x=4$"],
#         index=None,)
#         submit_button2 = st.form_submit_button("제출")

#     if submit_button2:
#         if answer2 == r"$x=2$":
#             st.success("정답입니다! 양변에서 3을 빼고 2로 나누면 x=2입니다.")
#         elif answer2 == r"$x=5$":
#             st.warning("앗! 3을 빼야 하는데 더한 것 같아요.")
#         elif answer2 == r"$x=-2$":
#             st.warning("앗! 양변에서 3을 뺄 때 부호를 다시 확인해보세요.")
#         elif answer2 == r"$x=4$":
#             st.warning("앗! 2x=4에서 양변을 2로 나눠야 해요.")
#         else:
#             st.warning("답을 선택해주세요.")

# with c:
#     st.write("문제3")







# with st.form("forms3"):

#     answer3 = st.text_input("식을 입력해주세요.")
#     submit_button3 = st.form_submit_button("제출")

# if submit_button3:
