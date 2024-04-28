import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return ("Underweight", 
                "Ayo, tingkatkan asupan makananmu dengan pilihan yang lebih banyak dan bernutrisi! Jadikan setiap suapan sebagai langkah cerdas menuju kesehatan yang lebih baik. Selalu ada ruang untuk lebih banyak kebaikan di piringmu!",
                "#3498db",
                [("Yoga", "Memperbaiki postur dan meningkatkan massa otot tanpa beban berlebih"),
                 ("Berenang", "Melatih semua grup otot tanpa risiko cedera"),
                 ("Berjalan cepat", "Meningkatkan kekuatan otot dengan risiko rendah")],
                "Setiap langkah kecil adalah kemajuan. Anda lebih kuat dari yang Anda pikir!")
    elif 18.5 <= bmi < 25:
        return ("Normal", 
                "Mari kita terus jaga semangat! Pertahankan pola makan sehat dan rutin berolahraga sebagai investasi terbaik untuk kesehatan jangka panjangmu. Ayo buat setiap hari sebagai langkah positif menuju versi terbaik dirimu!.",
                "#2ecc71",
                [("Berlari", "Membakar kalori dan meningkatkan kesehatan kardiovaskular"),
                 ("Berenang", "Cardio yang efektif dan rendah risiko"),
                 ("Latihan beban", "Membangun massa otot dan memperkuat tulang")],
                "Tetaplah konsisten dan nikmati prosesnya; Anda sedang melakukan hal-hal luar biasa untuk tubuh Anda!")
    elif 25 <= bmi < 30:
        return ("Overweight", 
                "Ayo, mulai kurangi asupan kalori dan tingkatkan aktivitas fisikmu! Setiap langkah kecil yang kamu ambil membawa dampak besar bagi kesehatan dan kesejahteraanmu. Bersama, kita bisa menjalani hidup yang lebih sehat dan penuh energi!",
                "#f39c12",
                [("Berjalan kaki cepat", "Cardio ringan untuk memulai dan membakar kalori"),
                 ("Berenang", "Mengurangi beban sendi saat berolahraga"),
                 ("Aerobik air", "Menyenangkan dan efektif untuk menurunkan berat badan")],
                "Setiap langkah adalah langkah ke arah yang benar. Terus bergerak maju!")
    else:
        return ("Obese", 
                "Mulai Hari Ini - Ingat, perjalanan seribu mil dimulai dengan satu langkah. Tak peduli seberapa kecil, langkah pertama Anda menuju kesehatan yang lebih baik adalah yang paling penting!",
                "#e74c3c",
                [("Berjalan kaki", "Mulai dengan sesuatu yang mudah dan bertahap"),
                 ("Latihan kekuatan", "Membantu membakar kalori bahkan saat istirahat"),
                 ("LIIT", "Latihan interval intensitas rendah untuk memulai tanpa risiko tinggi")],
                "Setiap hari membawa peluang baru untuk menjadi lebih baik. Jangan menyerah!")

def display_bmi_info(bmi):
    category, advice, color, exercises, motivation = interpret_bmi(bmi)
    st.success(f'BMI Anda adalah {bmi:.2f}.')
    st.metric(label="Kategori", value=category, delta_color="off", help=advice)
    st.caption(advice)
    st.markdown("**Saran Olahraga:**")
    exercise_table = { "Aktivitas": [], "Manfaat": [] }
    for exercise, benefit in exercises:
        exercise_table["Aktivitas"].append(exercise)
        exercise_table["Manfaat"].append(benefit)
    st.table(exercise_table)
    st.markdown("**Motivasi:**")
    st.markdown(motivation)

def main():
    st.header('Interactive BMI Calculator')
    st.markdown("<hr style='border: 2px solid blue; border-radius: 5px;'/>", unsafe_allow_html=True)

    st.write("## Anggota Kelompok:")
    st.markdown("""
    - **Elvio Aldwin Faqih** (2302521)
    - **Indana Zulfa** (2320531)
    - **Nayla Rahma** (2320540)
    - **Pramesthi Dewi Amelia** (2320543)
    - **Raden Kayla Syawal Sabira** (2320547)
    """, unsafe_allow_html=True)

    st.write("## Tentang Aplikasi Ini")
    st.write("""
    Aplikasi ini dirancang khusus untuk membantu Anda dengan cara yang mudah dan cepat
    dalam menghitung serta memahami nilai BMI (Body Mass Index) Anda. Cukup masukkan berat
    dan tinggi badan Anda, dan biarkan aplikasi ini melakukan sisanya. Aplikasi ini tidak hanya menghitung
    BMI Anda, tetapi juga memberikan penjelasan mendetail tentang kategori kesehatan yang sesuai dengan hasil pengukuran BMI Anda,
    saran olahraga yang cocok dalam bentuk tabel, serta kata-kata motivasi untuk membangun semangat Anda.
    """)

    bmi_categories = {
        "Kategori": ["Underweight", "Normal", "Overweight", "Obese"],
        "BMI Range": ["di bawah 18.5", "antara 18.5 dan 24.99", "antara 25 dan 29.99", "30 atau lebih"]
    }
    st.table(bmi_categories)

    with st.sidebar:
        name = st.text_input("Masukkan nama Anda:")
        weight = st.number_input("Masukkan berat Anda (dalam kg):", min_value=1.0, format="%.2f")
        height = st.number_input("Masukkan tinggi Anda (dalam cm):", min_value=1.0, format="%.2f")
    
    if st.sidebar.button('Hitung BMI'):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            display_bmi_info(bmi)
        else:
            st.error("Mohon masukkan data yang valid!")

if __name__ == '__main__':
    main()
