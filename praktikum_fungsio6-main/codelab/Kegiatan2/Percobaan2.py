from PIL import Image

# TODO 0: Import beberapa library lain yang dibutuhkan
# (Tidak ada library tambahan yang diperlukan)

# TODO 1: Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)

# Ganti dengan path gambar background yang sesuai
background_image = Image.open(
    r"D:\Kuliah\semester 5\prak.fungsional\6\praktikum_fungsio6-main\images\UMM.jpg")

overlay_image = Image.open(
    r"D:\Kuliah\semester 5\prak.fungsional\6\praktikum_fungsio6-main\images\Logo.png")

# TODO 2: Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert("RGBA")

# TODO 3: (optional) Perkecil ukuran gambar overlay menggunakan method resize()
max_size = (300, 300)  # Ganti dengan ukuran yang diinginkan
overlay_image.thumbnail(max_size)

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2

# TODO 4: Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center))

# TODO 5: Simpan gambar hasil edit
background_image.save("images\percobaan_dua.jpg")

# TODO 6: Tampilkan
background_image.show()
