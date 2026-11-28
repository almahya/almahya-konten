# Template v3: Reel animasi ilustrasi (standar sejak 28 Nov 2026)

Contoh jadi: "Gagal login SSCASN? Tenang" (posts/ ... gagal-login). File: `template_v3_animasi.html` (scene HTML digerakkan waktu), `render_frames_v3.py` (Playwright: `python3 render_frames_v3.py <k> <n> <outdir> [t1,t2,..]`; mode still bila waktu diberikan).

Cara pakai:
1. Salin ke folder kerja, ganti path aset `file:///home/claude/reel/g2/...` (foto, poster, kartun) dan presenter `file:///home/claude/presenter_png/<pose>.png` (ada di repo: tools/presenter).
2. Isi `scene(a,b)` sesuai jeda audio (silencedetect -30dB d=0.1; batas scene di jeda), `SUB=[[start,end,'teks'],...]` per frasa.
3. Ganti TOT di render_frames_v3.py = durasi audio. Render 2 proses paralel (`0 2` dan `1 2`), lalu ffmpeg libx264 crf 23, loudnorm -15, aac.
4. Cek stills sebelum render penuh (contact sheet), safe area: konten y 290-1320, subtitle y 1340-1530.

Pustaka ilustrasi di template (SVG berbasis waktu): LOGIN (laptop + spinner + error), CROWD (antrean orang + server sibuk), GEARS (roda gigi + kunci pas), TYPING (orang mengetik + progress bar), ikon IC.clock/broom/lock/help/warn, BOOK (simpan), SHARE (bagikan). Tambah ilustrasi baru dengan pola yang sama: string SVG + fungsi `ticks.push(t=>...)` yang mengatur transform/atribut.
