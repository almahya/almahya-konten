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
<div class="foot"><span>Data per 22 November 2026</span><span style="color:#c8102e;font-weight:700">Belajar SKD+SKB: almahya.id</span><span>{page}/{total}</span></div></body></html>'''

T=7
s=[]
s.append(f'''<div style="text-align:center;margin-top:20px"><span style="display:inline-block;background:#ffd23f;color:#14234b;font-weight:800;font-size:36px;padding:10px 28px;border-radius:12px">FORMASI PRIORITAS CPNS 2026</span></div>
<h1 style="font-size:84px;margin-top:60px;line-height:1.12">BERAPA GAJI<br><span>POLISI HUTAN</span><br>&amp; <span>MANGGALA AGNI?</span></h1>
<div class="sub" style="font-size:36px;margin-top:34px">Rincian gaji pokok dan tunjangannya</div>
<div class="box" style="margin-top:70px;font-size:32px">Gaji pokok mengikuti skala PNS (PP 5/2024), ditambah <b>tunjangan jabatan fungsional</b></div>
<div style="text-align:center;font-size:32px;font-weight:700;color:#c8102e;margin-top:44px">Geser untuk rincian lengkapnya →</div>''')
s.append(f'''<h1>Komponen <span>Penghasilan</span></h1><div class="sub">Tidak hanya gaji pokok</div>
<div class="card"><div class="n r">1</div><div class="ct">Gaji pokok<small>Mengikuti golongan dan masa kerja, diatur PP 5/2024.</small></div></div>
<div class="card"><div class="n r">2</div><div class="ct">Tunjangan jabatan fungsional<small>Ditetapkan lewat Perpres, besarnya mengikuti jenjang jabatan.</small></div></div>
<div class="card"><div class="n">3</div><div class="ct">Tunjangan kinerja<small>Bergantung kebijakan instansi, kelas jabatan, dan penilaian kinerja.</small></div></div>
<div class="card"><div class="n">4</div><div class="ct">Tunjangan lain<small>Seperti tunjangan keluarga dan makan, sesuai syarat dan penugasan.</small></div></div>''')
s.append(f'''<h1>Gaji Pokok <span>per Golongan</span></h1><div class="sub">Skala PNS menurut PP 5/2024, per bulan</div>
<div class="card"><div class="n">I</div><div class="ct">Golongan I<small>Rp 1.685.700 – Rp 2.901.400</small></div></div>
<div class="card" style="border-color:#c8102e"><div class="n r">II</div><div class="ct">Golongan II<small>Rp 2.184.000 – Rp 4.125.600</small></div><div class="pill">Pemula, Terampil</div></div>
<div class="card" style="border-color:#c8102e"><div class="n r">III</div><div class="ct">Golongan III<small>Rp 2.785.700 – Rp 5.180.700</small></div><div class="pill">Mahir, Penyelia</div></div>
<div class="card"><div class="n">IV</div><div class="ct">Golongan IV<small>Rp 3.287.800 – Rp 6.373.200</small></div></div>
<div class="box" style="font-size:28px;margin-top:30px">Rentang tergantung masa kerja. Angka awal: II/a Rp 2.184.000 dan III/a Rp 2.785.700</div>''')
s.append(f'''<h1>Polisi Hutan: <span>Tunjangan Jabatan</span></h1><div class="sub">Jenjang keterampilan, Perpres 96/2022, per bulan</div>
<div class="card"><div class="n">1</div><div class="ct">Polhut Pemula</div><div class="pill">Rp 300.000</div></div>
<div class="card"><div class="n">2</div><div class="ct">Polhut Terampil</div><div class="pill">Rp 360.000</div></div>
<div class="card"><div class="n">3</div><div class="ct">Polhut Mahir</div><div class="pill">Rp 540.000</div></div>
<div class="card"><div class="n">4</div><div class="ct">Polhut Penyelia</div><div class="pill">Rp 976.000</div></div>
<div class="box" style="font-size:28px;margin-top:30px"><b>Simulasi</b> Polhut Pemula golongan II/a, masa kerja 0 tahun:<br>Rp 2.184.000 + Rp 300.000 = <b>Rp 2.484.000</b></div>''')
s.append(f'''<h1>Manggala Agni: <span>Gaji &amp; Jenjang</span></h1><div class="sub">Kategori keterampilan, Permenpan 54/2022</div>
<div class="card"><div class="n">1</div><div class="ct">Pemula<small>Golongan II/a, gaji pokok mulai Rp 2.184.000</small></div></div>
<div class="card"><div class="n">2</div><div class="ct">Terampil<small>Golongan II/b – II/d (rentang gol. II)</small></div></div>
<div class="card"><div class="n">3</div><div class="ct">Mahir<small>Golongan III/a – III/b, gaji pokok mulai Rp 2.785.700</small></div></div>
<div class="card"><div class="n">4</div><div class="ct">Penyelia<small>Golongan III/c – III/d (rentang gol. III)</small></div></div>
<div class="warn" style="font-size:27px;margin-top:28px">Tunjangan jabatan fungsional Manggala Agni diatur Perpres tersendiri. Nominalnya belum bisa kami pastikan, jadi tidak dicantumkan.</div>''')
s.append(f'''<h1>Catatan <span>Penting</span></h1><div class="sub">Sebelum menyimpulkan angka gaji</div>
<div class="card"><div class="n r">1</div><div class="ct">Tidak ada satu angka untuk semua<small>Gaji bergantung golongan, masa kerja, jenjang, dan instansi.</small></div></div>
<div class="card"><div class="n r">2</div><div class="ct">Angka di atas adalah simulasi<small>Belum termasuk tunjangan kinerja, tunjangan keluarga/makan, pajak, dan iuran.</small></div></div>
<div class="card"><div class="n r">3</div><div class="ct">CPNS menerima gaji pokok 80%<small>Sebelum diangkat menjadi PNS penuh. Contoh: 80% dari Rp 2.184.000 = Rp 1.747.200.</small></div></div>
<div class="card"><div class="n">4</div><div class="ct">Rincian resmi menunggu BKN<small>Kuota dan syarat tiap jabatan belum diumumkan resmi.</small></div></div>''')
s.append(f'''<h1 style="margin-top:6px;font-size:64px">Siap Daftar<br><span>Polhut atau Manggala Agni?</span></h1>
<div class="sub" style="font-size:34px">Belajar <b>SKD + SKB</b> sesuai formasimu:</div>
<div class="card" style="margin-top:28px"><div class="n r">1</div><div class="ct">www.almahya.id<small>SKD: latihan TIU, TWK, TKP, dan tryout CAT. Ada paket bundling SKD + SKB.</small></div></div>
<div class="card"><div class="n r">2</div><div class="ct">skb.almahya.id<small>Pilih formasi SKB: Manggala Agni (Terampil) atau Polisi Kehutanan (Pemula dan Terampil).</small></div></div>
<div class="card"><div class="n">@</div><div class="ct">Follow @andikaalmahya<small>Update CPNS &amp; ASN, tips SKD, dan strategi lulus.</small></div></div>
<div class="warn" style="margin-top:22px;font-size:21px;font-weight:500;padding:16px 22px">Sumber: Merdeka.com (14 Okt 2026), Perpres 96/2022, Kementerian PANRB (via Suara.com, Beritasatu), Tribunjatim. Info resmi mengacu pada pengumuman BKN dan KemenPANRB.</div>''')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for i,x in enumerate(s,1):
            await pg.set_content(wrap(x,i,T)); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"gaji/slide{i}.jpg",type="jpeg",quality=92)
        await b.close()
asyncio.run(main())
