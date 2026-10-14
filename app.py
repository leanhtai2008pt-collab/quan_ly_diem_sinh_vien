import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quan ly diem sinh vien", page_icon="📚", layout="wide")
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

data = {
    "Họ tên": [
        "Nguyễn Minh Anh", "Trần Quốc Bảo", "Lê Hoàng Nam",
        "Phạm Thu Hà", "Võ Gia Huy", "Đặng Ngọc Linh",
        "Bùi Thành Đạt", "Đỗ Khánh Vy", "Hồ Đức Thịnh",
        "Phan Mỹ Duyên"
    ],
    "Chuyên cần": [9.0, 8.5, 7.5, 10.0, 8.0, 9.5, 7.0, 8.5, 6.5, 9.0],
    "Giữa kỳ": [8.0, 7.0, 6.5, 9.0, 7.5, 8.5, 6.0, 8.0, 5.5, 9.0],
    "Cuối kỳ": [8.5, 7.5, 7.0, 9.5, 8.0, 9.0, 6.5, 8.5, 6.0, 9.5]
}

df = pd.DataFrame(data)

df["Tổng kết"] = (
    0.2 * df["Chuyên cần"]
    + 0.3 * df["Giữa kỳ"]
    + 0.5 * df["Cuối kỳ"]
)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

st.subheader("Bảng điểm 10 sinh viên")
st.dataframe(df, hide_index=True, use_container_width=True)

st.subheader("Thống kê kết quả")
diem_trung_binh = df["Tổng kết"].mean()
diem_cao_nhat = df["Tổng kết"].max()
diem_thap_nhat = df["Tổng kết"].min()
so_sinh_vien_dat = int((df["Tổng kết"] >= 5).sum())

col1, col2, col3, col4 = st.columns(4)
col1.metric("Điểm trung bình lớp", f"{diem_trung_binh:.2f}")
col2.metric("Điểm cao nhất", f"{diem_cao_nhat:.2f}")
col3.metric("Điểm thấp nhất", f"{diem_thap_nhat:.2f}")
col4.metric("Số sinh viên đạt", f"{so_sinh_vien_dat}/10")

st.write("**Sinh viên có điểm tổng kết cao nhất:**")
st.dataframe(df[df["Tổng kết"] == diem_cao_nhat], hide_index=True, use_container_width=True)

st.write("**Sinh viên có điểm tổng kết thấp nhất:**")
st.dataframe(df[df["Tổng kết"] == diem_thap_nhat], hide_index=True, use_container_width=True)

st.subheader("Tra cứu điểm theo sinh viên")
ten_sinh_vien = st.selectbox("Chọn một sinh viên:", df["Họ tên"])
sinh_vien = df[df["Họ tên"] == ten_sinh_vien].iloc[0]

st.write("**Thông tin điểm của sinh viên:**")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Chuyên cần", f'{sinh_vien["Chuyên cần"]:.1f}')
c2.metric("Giữa kỳ", f'{sinh_vien["Giữa kỳ"]:.1f}')
c3.metric("Cuối kỳ", f'{sinh_vien["Cuối kỳ"]:.1f}')
c4.metric("Tổng kết", f'{sinh_vien["Tổng kết"]:.2f}')
c5.metric("Xếp loại", sinh_vien["Xếp loại"])

st.subheader("Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Họ tên"], df["Tổng kết"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)
