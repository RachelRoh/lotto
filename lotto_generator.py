import streamlit as st
import random
import datetime
import time
from PIL import Image

st.title("🤞로또 생성기🤞")


# who = st.selectbox("누가 번호를 생성하나요?", ("성욱", "유정", "춘배", "덕배"))

# 선택지 목록에 안내 문구 추가
options = ("-- Please select --", "성욱", "유정", "춘배", "덕배")

# 라디오 선택 버튼
who = st.selectbox("누가 번호를 생성하나요?", options)


# 이미지 경로 매핑
image_paths = {
    "성욱": "seongwook.jpg",
    "유정": "youjeong.jpg",
    "춘배": "choonbae.jpg",
    "덕배": "duckbae.jpg",
}

if who != "-- Please select --":
    img = Image.open(image_paths[who])

    target_height = 100  # 픽셀
    ratio = target_height / img.height
    new_size = (int(img.width * ratio), target_height)
    resized_img = img.resize(new_size)

    match who:
        case "성욱":
            st.write(f"오늘의 럭키가이 {who} ✌️😉 ~~!! ")
            # st.image("images/seongwook.jpg", caption="성욱", use_container_width=True)
            rotated_img = resized_img.rotate(-90, expand=True)
        case "유정":
            st.write(f"오늘의 럭키걸 {who} ✌️😉 ~~!! ")
            # st.image("images/youjeong.jpg", caption="유정", use_container_width=True)
            rotated_img = resized_img.rotate(0, expand=True)
        case "춘배":
            st.write(f"오늘은 {who}/ᐠ｡ꞈ｡ᐟ\가 행운을~!")
            # st.image("images/choonbae.jpg", caption="춘배", use_container_width=True)
            rotated_img = resized_img.rotate(0, expand=True)
        case "덕배":
            st.write(f"오늘은 {who}🐶가 행운을~!")
            # st.image("images/duckbae.jpg", caption="덕배", use_container_width=True)
            rotated_img = resized_img.rotate(-90, expand=True)
    st.image(rotated_img)


def generate_lotto():
    lotto = set()

    while len(lotto) < 6:
        number = random.randint(1, 45)
        lotto.add(number)

    lotto = list(lotto)
    lotto.sort()
    return lotto


# for i in range(5):
#     st.subheader(f"{i} > 박성욱❤️을 위한 번호 : :green[{generate_lotto()}]")
# st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%m')}")


agree = st.checkbox("당첨이 될거라 믿습니까? 🙏")
if agree:
    st.write("Sure, why not~! 🤑")

button = st.button("로또를 생성해 주세요!")


def count_down():
    countdown = st.empty()  # 화면에 값을 업데이트할 공간

    for i in range(5, 0, -1):  # 5부터 1까지
        countdown.markdown(
            f"<h1 style='text-align: center; color: red;'>{i}</h1>",
            unsafe_allow_html=True,
        )
        time.sleep(1)

    countdown.markdown(
        "<h1 style='text-align: center; color: green;'>🎉 짜잔!</h1>",
        unsafe_allow_html=True,
    )


if button:
    count_down()
    for i in range(1, 6):
        st.subheader(f" {i}.  당첨 번호 : :green[{generate_lotto()}]")
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
