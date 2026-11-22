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
</style></head><body><div class="top"></div>{BRAND}<div class="tagr">INFO CPNS</div>
<div class="main">{inner}</div>
<div class="foot"><span>Data per 22 November 2026</span><span>{page}/{total}</span></div></body></html>'''

T=7
s=[]
s.append("""<h1 style="font-size:70px;margin-top:30px">INSTANSI YANG<br><span>SUDAH BERI KABAR</span><br>BUKA FORMASI<br>CPNS 2026</h1>
<div class="sub">Rangkuman pernyataan resmi pejabat per 22 November 2026</div>
<div style="margin-top:50px"><div class="big" style="font-size:120px">6.345</div><div class="bigl">formasi Kemenkeu + Mahkamah Agung (rencana)</div></div>
<div class="box" style="font-size:31px">Pendaftaran <b>belum dibuka</b>. Simak status tiap instansi di slide berikutnya.</div>""")
s.append("""<h1>Status <span>Saat Ini</span></h1><div class="sub">Baca dulu sebelum percaya info yang beredar</div>
<div class="card"><div class="n">1</div><div class="ct">150.000 sampai 158.000 formasi<small>Perkiraan Menteri PANRB, bukan kuota final dan masih dihitung ulang bersama instansi.</small></div></div>
<div class="card"><div class="n">2</div><div class="ct">Rincian dirilis BKN sekitar 20-23 November<small>Kepala BKN Zudan Arif Fakrulloh: "Insya Allah sekitar tanggal tersebut".</small></div></div>
<div class="card"><div class="n">3</div><div class="ct">Akun SSCASN sudah bisa dibuat<small>Registrasi akun di sscasn.bkn.go.id. Pendaftaran formasi belum dibuka.</small></div></div>
<div class="warn" style="font-size:28px">Angka per instansi di postingan ini adalah <b>pernyataan/rencana</b>, bisa berubah saat pengumuman resmi terbit.</div>""")
s.append("""<h1>Kementerian <span>Keuangan</span></h1><div class="sub">Dipastikan oleh Biro Komunikasi Kemenkeu</div>
<div style="margin-top:30px"><div class="big">1.915</div><div class="bigl">formasi CPNS 2026, bersifat umum</div></div>
<div class="card" style="margin-top:34px"><div class="n r">1</div><div class="ct">Jenjang pendidikan<small>SMA/SMK, D3, dan S1 (menurut pemberitaan detikFinance, 17 Nov 2026).</small></div></div>
<div class="card"><div class="n r">2</div><div class="ct">Tersebar di unit eselon I<small>Tidak khusus lulusan PKN STAN. Rincian jabatan belum diumumkan.</small></div></div>
<div class="warn" style="font-size:27px">Sumber: Kepala Biro Komunikasi dan Layanan Informasi Kemenkeu, Deni Surjantoro: "Formasinya 1.915, umum."</div>""")
s.append("""<h1>Mahkamah <span>Agung</span></h1><div class="sub">Pengumuman resmi direncanakan akhir November</div>
<div style="margin-top:20px"><div class="big">4.430</div><div class="bigl">formasi yang disiapkan</div></div>
<div class="card" style="margin-top:34px"><div class="n r" style="font-size:30px">1</div><div class="ct">1.600 calon hakim (cakim)<small>Peradilan Umum, Agama, dan TUN.</small></div></div>
<div class="card"><div class="n r" style="font-size:30px">2</div><div class="ct">2.830 CPNS lingkungan MA<small>Jabatan teknis dan pendukung peradilan. Rincian belum dirilis.</small></div></div>
<div class="warn" style="font-size:27px">Sumber: Plt. Sekretaris MA Sobandi (detikFinance, 6 Nov 2026). Status masih rencana, tunggu pengumuman resmi MA.</div>""")
s.append("""<h1>Formasi Lain <span>yang Disebut</span></h1><div class="sub">Sinyal dan prioritas pemerintah, belum ada angka final</div>
<div class="card"><div class="n">1</div><div class="ct">BRIN: periset<small>Sinyal dari Kepala BRIN (Des 2025): pemuliaan tanaman, nanoteknologi, genomik, antariksa, sains material.</small></div></div>
<div class="card"><div class="n">2</div><div class="ct">Polisi Hutan &amp; Manggala Agni<small>Disebut sebagai formasi prioritas (pemberitaan Katadata, 10 Nov 2026).</small></div></div>
<div class="card"><div class="n">3</div><div class="ct">Guru Sekolah Terintegrasi &amp; Sekolah Unggul Garuda<small>Termasuk prioritas, jumlah per formasi belum diumumkan.</small></div></div>
<div class="box" style="font-size:30px">Pantau terus kanal resmi <b>BKN</b> dan instansi tujuanmu untuk daftar lengkap.</div>""")
s.append("""<h1>SKD Saja <span>Tidak Cukup</span></h1><div class="sub">Kalau bisa dapat SKD dan SKB, kenapa pilih yang cuma SKD?</div>
<div class="card"><div class="n">1</div><div class="ct">SKD hanya gerbang pertama<small>Lolos passing grade SKD baru membuka jalan ke tahap berikutnya.</small></div></div>
<div class="card"><div class="n r">2</div><div class="ct">SKB ikut menentukan peringkat akhir<small>Pada seleksi CPNS 2024, nilai akhir gabungan SKD 40% dan SKB 60%. Ketentuan 2026 menunggu pengumuman resmi.</small></div></div>
<div class="card"><div class="n">3</div><div class="ct">Materi SKB beda tiap formasi<small>Kamu perlu latihan yang sesuai jabatan incaran, bukan hanya TWK, TIU, TKP.</small></div></div>
<div class="box" style="font-size:31px">Siapkan <b>SKD + SKB</b> sejak sekarang, jangan menunggu pengumuman.</div>""")
s.append("""<h1 style="margin-top:20px">Gabung <span>Almahya.id</span></h1>
<div class="sub">Dapatkan tryout SKD + SKB dalam satu tempat</div>
<div class="box" style="margin-top:40px;background:#c8102e;font-size:36px">Kalau bisa dapat SKD dan SKB,<br>kenapa pilih yang hanya SKD saja?</div>
<div class="box" style="margin-top:28px">Kunjungi <b>almahya.id</b><br>dan mulai tryout <b>SKD + SKB</b> sekarang</div>
<div class="box" style="margin-top:28px;font-size:30px">Simpan &amp; bagikan postingan ini. Follow <b>@andikaalmahya</b> untuk update CPNS &amp; ASN.</div>
<div class="warn" style="margin-top:28px;font-size:22px;font-weight:500;line-height:1.35">Sumber: detikFinance (17 Nov 2026), detikFinance (6 Nov 2026), Radar Semarang (16 Nov 2026), Katadata (10 Nov 2026), JawaPos (12 Des 2025). Info resmi mengacu pada BKN, KemenPANRB, dan instansi terkait.</div>""")
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for i,x in enumerate(s,1):
            await pg.set_content(wrap(x,i,T)); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"posts/2026-11-22-19-instansi-buka-formasi/slide{i}.jpg",type="jpeg",quality=92)
        await b.close()
asyncio.run(main())
