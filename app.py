import streamlit as st
from gtts import gTTS
import base64
from io import BytesIO

# --- HÀM PHÁT ÂM THANH ---
def speak(text, lang='vi'):
    sound_file = BytesIO()
    tts = gTTS(text=text, lang=lang)
    tts.write_to_fp(sound_file)
    b64 = base64.b64encode(sound_file.getvalue()).decode()
    md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
    st.markdown(md, unsafe_allow_html=True)

# --- DỮ LIỆU HÌNH ẢNH CHỮ CÁI & QUẢ ---
chu_cai_data = {
    "A": {"qua": "Quả Na", "img": "https://images.unsplash.com/photo-1591073113125-e46713c829ed?w=400"},
    "B": {"qua": "Quả Bơ", "img": "https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?w=400"},
    "C": {"qua": "Quả Cam", "img": "https://images.unsplash.com/photo-1547514701-42782101795e?w=400"},
    "D": {"qua": "Quả Dưa hấu", "img": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=400"},
    "Đ": {"qua": "Quả Đu đủ", "img": "https://images.unsplash.com/photo-1526470498-9ae7f97a99ee?w=400"},
    "L": {"qua": "Quả Lê", "img": "https://images.unsplash.com/photo-1514756331096-242f390ef2a5?w=400"},
    "M": {"qua": "Quả Măng cụt", "img": "https://images.unsplash.com/photo-1525385354411-301f26202301?w=400"},
    "N": {"qua": "Quả Nho", "img": "https://images.unsplash.com/photo-1537640538966-79f369b41e8f?w=400"},
    "O": {"qua": "Quả Ổi", "img": "https://images.unsplash.com/photo-1536511110591-7758a9417b67?w=400"}
}

st.title("🅰️ Bé Học Chữ Cái & Ghép Vần")

# --- PHẦN 1: NHẬN BIẾT CHỮ CÁI ---
st.subheader("1. Bé làm quen với chữ cái")
col1, col2 = st.columns([1, 1])

with col1:
    letter = st.selectbox("Chọn một chữ cái:", list(chu_cai_data.keys()))
    st.markdown(f"<h1 style='font-size: 100px; color: blue; text-align: center;'>{letter}</h1>", unsafe_allow_html=True)
    if st.button(f"🔊 Đọc chữ {letter}"):
        speak(f"Chữ {letter}", 'vi')

with col2:
    st.image(chu_cai_data[letter]["img"], caption=f"{letter} trong từ '{chu_cai_data[letter]['qua']}'")
    st.write(f"Đây là: **{chu_cai_data[letter]['qua']}**")

st.divider()

# --- PHẦN 2: GHÉP VẦN CÓ DẤU ---
st.subheader("2. Bé tập ghép vần và thanh điệu")
c1, c2 = st.columns(2)

with c1:
    pa = st.selectbox("Chọn phụ âm:", ["b", "c", "d", "đ", "l", "m", "n", "t", "v"])
with c2:
    na = st.selectbox("Chọn nguyên âm:", ["a", "o", "ô", "e", "ê", "i", "u", "ư"])

# Logic tạo bảng dấu
dau_thanh = {
    "Không dấu": "",
    "Dấu Sắc": "sắc",
    "Dấu Huyền": "huyền",
    "Dấu Hỏi": "hỏi",
    "Dấu Ngã": "ngã",
    "Dấu Nặng": "nặng"
}

# Hàm giả lập hiển thị từ có dấu (để bé dễ nhìn)
def get_word_with_tone(p, n, tone_name):
    # Đây là ví dụ minh họa, thực tế cần thư viện xử lý dấu tiếng Việt phức tạp hơn
    # Ở mức độ tiểu học, ta có thể liệt kê các trường hợp phổ biến
    tones = {
        "ba": ["ba", "bá", "bà", "bả", "bã", "bạ"],
        "ca": ["ca", "cá", "cà", "cả", "cã", "cạ"],
        "bo": ["bo", "bó", "bò", "bỏ", "bõ", "bọ"],
        # ... có thể mở rộng thêm các từ khác
    }
    base = p + n
    if base in tones:
        idx = list(dau_thanh.keys()).index(tone_name)
        return tones[base][idx]
    return base + " (" + tone_name + ")"

st.write(f"Bảng ghép vần của chữ: **{pa.upper()}** + **{na.upper()}**")

cols = st.columns(3)
for i, (name, tone) in enumerate(dau_thanh.items()):
    word = get_word_with_tone(pa, na, name)
    with cols[i % 3]:
        if st.button(f"{word}\n({name})"):
            speak(word, 'vi')
