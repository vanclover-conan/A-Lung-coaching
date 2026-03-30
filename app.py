import streamlit as st
from gtts import gTTS
import base64
from io import BytesIO

# --- CẤU HÌNH HỆ THỐNG ---
st.set_page_config(page_title="Bé Vui Học Lớp 1", page_icon="🎒", layout="centered")

def speak(text, lang='vi'):
    try:
        sound_file = BytesIO()
        tts = gTTS(text=text, lang=lang)
        tts.write_to_fp(sound_file)
        b64 = base64.b64encode(sound_file.getvalue()).decode()
        md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
        st.markdown(md, unsafe_allow_html=True)
    except:
        st.error("Không thể phát âm thanh lúc này.")

# --- GIAO DIỆN CHÍNH ---
st.sidebar.title("🌟 Bé Học Cùng Mẹ")
menu = st.sidebar.radio("Chọn bài học:", 
    ["Ghép Vần Tiếng Việt", "Toán Hình Ảnh", "Thời Trang Tiếng Anh"])

# --- MODULE 1: GHÉP VẦN TIẾNG VIỆT ---
if menu == "Ghép Vần Tiếng Việt":
    st.title("🅰️ Tập Ghép Vần Vui Nhộn")
    st.write("Bé hãy chọn phụ âm và nguyên âm để xem chúng tạo thành gì nhé!")

    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        phu_am = st.selectbox("Phụ âm", ["b", "c", "d", "đ", "h", "l", "m", "n"])
    with col2:
        nguyen_am = st.selectbox("Nguyên âm", ["a", "e", "ê", "i", "o", "ô", "u", "ư"])
    
    ket_qua = phu_am + nguyen_am
    
    with col3:
        st.markdown(f"<div style='font-size: 60px; color: #FF4B4B; border: 3px dashed #CCC; text-align: center;'>{phu_am} + {nguyen_am} = {ket_qua}</div>", unsafe_allow_html=True)
        if st.button("🔊 Bé nghe đọc vần này"):
            speak(f"{phu_am}, {nguyen_am}, {ket_qua}", 'vi')

# --- MODULE 2: TOÁN HÌNH ẢNH THẬT ---
elif menu == "Toán Hình Ảnh":
    st.title("🔢 Thử Thách Đếm Đồ Vật")
    
    # Danh sách hình ảnh minh họa thật (Sử dụng Unsplash - miễn phí và đẹp)
    images = {
        "Quả Táo": "https://images.unsplash.com/photo-1560806887-1e4cd0b6bccb?w=400",
        "Con Mèo": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=400",
        "Cái Bút": "https://images.unsplash.com/photo-1585336139118-89c7436b7285?w=400"
    }
    
    item_name = st.selectbox("Bé muốn đếm gì?", list(images.keys()))
    so_luong = st.slider("Mẹ chọn số lượng cho bé:", 1, 5)
    
    st.write(f"### Có bao nhiêu {item_name.lower()} ở đây?")
    
    cols = st.columns(so_luong)
    for i in range(so_luong):
        with cols[i]:
            st.image(images[item_name], use_container_width=True)
            
    dap_an = st.number_input("Bé điền số vào đây:", min_value=0, max_value=10, step=1)
    if st.button("Kiểm tra"):
        if dap_an == so_luong:
            st.success("Tuyệt quá! Bé đúng rồi! 🎉")
            st.balloons()
        else:
            st.warning("Bé đếm lại một lần nữa xem!")

# --- MODULE 3: THỜI TRANG TIẾNG ANH (Fashion English) ---
else:
    st.title("👗 My Fashion Show")
    st.write("Cùng học tên các loại trang phục bằng Tiếng Anh nhé!")

    clothes = {
        "Shirt": {"name": "Áo sơ mi 👕", "img": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400"},
        "Dress": {"name": "Váy liền 👗", "img": "https://images.unsplash.com/photo-1539008835757-c6117dd05b22?w=400"},
        "Hat": {"name": "Cái mũ 👒", "img": "https://images.unsplash.com/photo-1514327605112-b887c0e61c0a?w=400"},
        "Shoes": {"name": "Đôi giày 👟", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"},
        "Socks": {"name": "Đôi tất 🧦", "img": "https://images.unsplash.com/photo-1582966298431-99c6a1e863b9?w=400"}
    }
    
    selected_item = st.selectbox("Chọn trang phục:", list(clothes.keys()))
    
    col_img, col_info = st.columns([1, 1])
    with col_img:
        st.image(clothes[selected_item]["img"], caption=selected_item)
    with col_info:
        st.subheader(clothes[selected_item]["name"])
        if st.button(f"🔊 Listen: {selected_item}"):
            speak(selected_item, 'en')

st.sidebar.markdown("---")
st.sidebar.info("Mẹo: Mẹ có thể thay link ảnh trong code để có hình ảnh bé thích!")
