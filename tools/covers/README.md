# Cover Reels almahya
Standar: setiap Reels diposting dengan `cover_url` (JPEG 1080x1920) buatan khusus, bukan frame pertama.
- Isi penting di tengah (y 330-1600) agar aman di grid profil 4:5.
- Susunan: pill kategori, kartu navy dengan angka/hook kuning besar + subjudul, headline 2 baris (kata kunci merah), presenter sesuai topik, tombol almahya.id.
- Generator: `make_covers.py` (edit daftar `items`, jalankan dengan Playwright + Chrome). Cover disimpan di folder postingan sebagai `cover.jpg`.
- Windsor `create_video_post`: `cover_url` = raw GitHub URL cover.jpg (tidak boleh bersamaan dengan `thumb_offset`).
- Cover Reels yang sudah tayang tidak bisa diganti via API; ganti manual di aplikasi (Edit > Edit cover).
