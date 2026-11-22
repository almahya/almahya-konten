import asyncio
from playwright.async_api import async_playwright
BRAND='<div class="brand"><span class="b1">almahya</span><span class="b2">_cpns</span></div>'
def wrap(inner,page,total):
    return f'''<html><head><style>
*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:Poppins;background:#fff;color:#14234b;position:relative;overflow:hidden}}
.top{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#c8102e,#14234b)}}
.brand{{position:absolute;top:50px;left:70px;font-size:40px;font-weight:800}}
.b1{{color:#c8102e}}.b2{{color:#14234b}}
.tagr{{position:absolute;top:56px;right:70px;font-size:26px;font-weight:600;color:#fff;background:#c8102e;padding:8px 22px;border-radius:30px}}
.main{{position:absolute;top:150px;left:70px;right:70px;bottom:130px}}
h1{{font-size:62px;line-height:1.15;font-weight:800;color:#c8102e;text-align:center}}
h1 span{{color:#14234b}}
.sub{{text-align:center;font-size:32px;font-weight:600;color:#14234b;margin-top:14px}}
.foot{{position:absolute;bottom:42px;left:70px;right:70px;font-size:24px;color:#5b6785;display:flex;justify-content:space-between;border-top:2px solid #e6e9f2;padding-top:18px}}
.card{{border:3px solid #e3b8be;border-radius:22px;padding:26px 30px;margin-top:22px;display:flex;align-items:center;gap:26px;background:#fff;box-shadow:0 6px 0 #f3dde0}}
.n{{flex:0 0 78px;height:78px;border-radius:50%;background:#14234b;color:#fff;font-weight:800;font-size:38px;display:flex;align-items:center;justify-content:center}}
.n.r{{background:#c8102e}}
.ct{{flex:1;font-size:32px;font-weight:700;line-height:1.28}}
.ct small{{display:block;font-weight:500;font-size:27px;color:#46537a;margin-top:6px;line-height:1.35}}
.pill{{flex:0 0 auto;background:#c8102e;color:#fff;font-weight:700;font-size:28px;padding:10px 22px;border-radius:14px;white-space:nowrap}}
.pill.b{{background:#14234b}}
.big{{font-size:150px;font-weight:800;color:#c8102e;line-height:1;text-align:center}}
.bigl{{text-align:center;font-size:40px;font-weight:700;margin-top:6px}}
.box{{background:#14234b;color:#fff;border-radius:26px;padding:34px 40px;font-size:34px;line-height:1.4;font-weight:600;text-align:center;margin-top:30px}}
.box b{{color:#ffd23f}}
.warn{{background:#fff4f5;border:3px dashed #c8102e;border-radius:22px;padding:28px 32px;margin-top:22px;font-size:31px;line-height:1.4;font-weight:600}}
</style></head><body><div class="top"></div>{BRAND}<div class="tagr">TIPS SKD</div>
<div class="main">{inner}</div>
<div class="foot"><span>Edukasi SKD · evergreen</span><span>{page}/{total}</span></div></body></html>'''

T=7
s=[]
s.append("""<h1 style="font-size:76px;margin-top:40px">5 KESALAHAN<br><span>FATAL SAAT SKD</span></h1>
<div class="sub">Yang sering bikin skor jeblok padahal sudah belajar</div>
<div style="margin-top:70px"><div class="big">110</div><div class="bigl">soal dalam 100 menit</div></div>
<div class="box">Rata-rata cuma <b>±54 detik</b> per soal. Strategi waktu itu penentu.</div>
<div style="text-align:center;font-size:32px;font-weight:700;color:#c8102e;margin-top:46px">Geser, cek kamu pernah salah di mana →</div>""")
s.append("""<h1>Kenali Dulu <span>Struktur SKD</span></h1><div class="sub">Dasar sebelum menyusun strategi</div>
<div class="card"><div class="n">1</div><div class="ct">TWK: 30 soal<small>Benar bernilai 5, salah 0. Nilai maksimal 150.</small></div></div>
<div class="card"><div class="n">2</div><div class="ct">TIU: 35 soal<small>Benar bernilai 5, salah 0. Nilai maksimal 175.</small></div></div>
<div class="card"><div class="n">3</div><div class="ct">TKP: 45 soal<small>Setiap opsi bernilai 1 sampai 5, tidak ada yang 0. Nilai maksimal 225.</small></div></div>
<div class="box" style="font-size:32px">Total <b>110 soal</b>, nilai maksimal <b>550</b>. Kosong tidak ada gunanya, isi semua.</div>""")
s.append("""<h1>Kesalahan <span>#1 dan #2</span></h1><div class="sub">Soal dan waktu</div>
<div class="card"><div class="n r">1</div><div class="ct">Terjebak lama di satu soal TIU<small>Soal hitungan rumit bisa menghabiskan 3 menit. Lewati dulu, kembali di akhir.</small></div></div>
<div class="card"><div class="n r">2</div><div class="ct">Tidak punya patokan waktu<small>Tanpa target per subtes, TKP yang mudah malah terburu-buru di menit terakhir.</small></div></div>
<div class="warn"><b>Contoh patokan (bisa disesuaikan):</b><br>TKP 30 menit ≈ 40 detik/soal<br>TWK 25 menit ≈ 50 detik/soal<br>TIU 45 menit ≈ 77 detik/soal<br>Total 100 menit.</div>""")
s.append("""<h1>Kesalahan <span>#3 dan #4</span></h1><div class="sub">Cara menjawab</div>
<div class="card"><div class="n r">3</div><div class="ct">Menjawab TKP pakai "versi ideal di kepala"<small>TKP menilai sikap kerja sebagai ASN: melayani, kolaboratif, taat aturan, solutif. Pilih respons yang paling konstruktif.</small></div></div>
<div class="card"><div class="n r">4</div><div class="ct">Menghafal tanpa memahami di TWK<small>Pancasila, UUD 1945, NKRI, Bhinneka Tunggal Ika, dan integritas muncul sebagai kasus. Pahami nilai dan penerapannya, bukan sekadar bunyi pasal.</small></div></div>
<div class="box" style="font-size:31px">Di TKP, jawaban skor 5 hampir selalu <b>proaktif, sesuai aturan, dan mengutamakan pelayanan publik</b>.</div>""")
s.append("""<h1>Kesalahan <span>#5</span></h1><div class="sub">Latihan yang salah arah</div>
<div class="card"><div class="n r">5</div><div class="ct">Latihan soal tanpa simulasi CAT<small>Mengerjakan santai tanpa timer tidak melatih ritme ujian yang sebenarnya.</small></div></div>
<div class="warn" style="margin-top:30px"><b>Perbaikannya:</b><br>• Latihan 110 soal utuh dengan timer 100 menit<br>• Catat soal yang salah dan penyebabnya<br>• Ulangi materi lemah, bukan semua materi<br>• Simulasi minimal seminggu sekali menjelang tes</div>
<div class="box" style="font-size:31px">Evaluasi hasil simulasi lebih berharga daripada <b>mengerjakan 1000 soal tanpa dicatat</b>.</div>""")
s.append("""<h1>Rencana <span>Belajar 7 Hari</span></h1><div class="sub">Siap diterapkan mulai hari ini</div>
<div class="card"><div class="n">1</div><div class="ct">Hari 1-2: TWK<small>Pancasila, UUD 1945, sejarah, nasionalisme, integritas.</small></div></div>
<div class="card"><div class="n">2</div><div class="ct">Hari 3-4: TIU<small>Numerik, verbal, dan figural dengan target waktu.</small></div></div>
<div class="card"><div class="n">3</div><div class="ct">Hari 5: TKP<small>Pola respons ASN: pelayanan publik, jejaring kerja, sosial budaya.</small></div></div>
<div class="card"><div class="n r">4</div><div class="ct">Hari 6-7: simulasi + evaluasi<small>Kerjakan 110 soal, lalu analisis kesalahan.</small></div></div>""")
s.append("""<h1 style="margin-top:50px">Simpan &amp;<br><span>Bagikan</span></h1>
<div class="sub">ke temanmu yang lagi persiapan CPNS 2026</div>
<div class="box" style="margin-top:50px">Follow <b>@andikaalmahya</b><br>untuk tips SKD, update CPNS &amp; ASN,<br>dan strategi lulus</div>
<div class="box" style="margin-top:30px;background:#c8102e;font-size:32px">Kesalahan mana yang paling sering kamu alami? Tulis nomornya di komentar!</div>
<div class="warn" style="margin-top:34px;font-size:25px;font-weight:500">Struktur dan penilaian SKD mengacu pada ketentuan seleksi CPNS KemenPANRB/BKN. Contoh pembagian waktu adalah saran belajar, bukan aturan resmi.</div>""")
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for i,x in enumerate(s,1):
            await pg.set_content(wrap(x,i,T)); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"posts/2026-11-22-12-edukasi-kesalahan-skd/slide{i}.jpg",type="jpeg",quality=92)
        await b.close()
asyncio.run(main())
