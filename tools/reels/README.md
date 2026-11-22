# Alur Reels almahya (suara ElevenLabs)
1. Naskah (angka dieja, "almahya titik i d") -> user buat MP3 di ElevenLabs.
2. silencedetect (noise=-35dB:d=0.25) -> potong di jeda -> transcribe_segments.py (Whisper small sherpa-onnx, bahasa id) -> bandingkan dgn naskah.
3. Isi times (batas scene di titik tengah jeda) + subs (start,end,teks per frasa) di template_v2_info.py; jalankan -> reel2.html.
4. render_frames.py (2 proses paralel, 1080x1920, jpeg) -> ffmpeg libx264 crf20 + loudnorm -15 LUFS, aac.
5. Cek contact sheet (subtitle maks 3 baris, jangan menimpa footer), ffprobe, SendUserFile.
6. Push ke posts/<tanggal>-reels-<slug>/reel.mp4 + caption.txt, cek raw URL 200, Windsor create_video_post, catat di posts/log.md.
Template v1 = gaya tips (kartu+bar), v2 = gaya info (VS, status, checklist, CTA). Fallback suara: tts_piper_fallback.py (pip piper-tts, bukan sherpa).
