from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan Pillow
# Ganti dengan path gambar yang sesuai
image = Image.open(
    r"D:\Kuliah\semester 5\prak.fungsional\6\praktikum_fungsio6-main\images/UMM.jpg")

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
brightness_factor = 2.5
contrast_factor = 1.2

enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(brightness_factor)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(contrast_factor)

# TODO 3: Simpan gambar hasil edit
final_image.save("images\percobaan_tiga.jpg")

# TODO 4: Tampilkan
final_image.show()
