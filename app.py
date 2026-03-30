import streamlit as st
import random

# Cấu hình trang chủ
st.set_page_config(page_title="Vững Bước Vào Lớp 1", page_icon="🎓", layout="wide")

# Giao diện Sidebar để chọn Module
st.sidebar.title("🌈 Góc Học Tập")
module = st.sidebar.selectbox("Bé muốn học gì nào?", ["Tiếng Việt", "Toán Học", "Tiếng Anh"])

# --- MODULE TIẾNG VIỆT ---
if module == "Tiếng Việt":
    st.header("🅰️ Bé học Chữ Cái & Ghép Vần")
    
    char_list = ['A', 'Ă', 'Â', 'B', 'C', 'D', 'Đ', 'E', 'Ê']
    col1, col2 = st.columns([1, 2])
    
    with col1:
        char = st.selectbox("Chọn một chữ cái:", char_list)
        st.title(f"Chữ: {char}")
    
    with col2:
        st.info("Hướng dẫn: Bé hãy nhìn hình và đọc to chữ cái nhé!")
        # Bạn có thể thay thế bằng link ảnh thực tế
        st.image(f"https://placehold.co/300x200?text=Hinh+Anh+Chu+{char}", caption=f"Đây là chữ {char}")

# --- MODULE TOÁN HỌC ---
elif module == "Toán Học":
    st.header("🔢 Bé học Đếm & Cộng Trừ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Trò chơi: Đếm táo")
        num_apples = random.randint(1, 5)
        st.write("🍎" * num_apples)
        answer = st.number_input("Có bao nhiêu quả táo?", min_value=0, max_value=10, step=1)
        if st.button("Kiểm tra"):
            if answer == num_apples:
                st.success("Giỏi quá! Đúng rồi! 🎉")
            else:
                st.error("Bé đếm lại thử xem nhé! 💪")

# --- MODULE TIẾNG ANH ---
else:
    st.header("🇬🇧 My First English")
    
    vocab = {
        "Apple": "Quả táo 🍎",
        "Cat": "Con mèo 🐱",
        "Sun": "Ông mặt trời ☀️",
        "Book": "Quyển sách 📚"
    }
    
    word = st.radio("Chọn từ vựng:", list(vocab.keys()))
    
    st.subheader(f"Từ này nghĩa là: {vocab[word]}")
    st.write(f"Cách đọc: **{word}**")
    
    if st.button("Nghe âm thanh (Giả lập)"):
        st.info(f"Đang phát âm thanh: {word}...") # Ở bản nâng cao sẽ dùng thư viện gTTS

# Footer khích lệ
st.divider()
st.caption("Chúc bé học tập thật vui và tự tin vào lớp 1! ❤️")
