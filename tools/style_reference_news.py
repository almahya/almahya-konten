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
<div class="foot"><span>Data per 20 November 2026</span><span>{page}/{total}</span></div></body></html>'''
T=6
s=[]
s.append(f'''<h1 style="font-size:78px;margin-top:40px">CPNS 2026<br><span>KAPAN DIBUKA?</span></h1>
<div class="sub">Update terbaru dari BKN, simak sebelum daftar</div>
<div style="margin-top:80px"><div class="big">158.000</div><div class="bigl">formasi disiapkan pemerintah</div></div>
<div class="box">Pengumuman resmi ditargetkan <b>pekan keempat November</b> (23–29 Nov 2026)</div>
<div style="text-align:center;font-size:32px;font-weight:700;color:#c8102e;margin-top:46px">Geser untuk detail lengkapnya →</div>''')
s.append(f'''<h1>Kronologi <span>Terbaru</span></h1><div class="sub">Dari pengumuman pemerintah sampai hari ini</div>
<div class="card"><div class="n r">1</div><div class="ct">6 November<small>Mensesneg menyampaikan pemerintah akan melakukan rekrutmen CPNS dan menargetkan prosesnya mulai November.</small></div></div>
<div class="card"><div class="n r">2</div><div class="ct">10–14 November<small>Kepala BKN menyebut pengumuman direncanakan sekitar 20 atau 23 November.</small></div></div>
<div class="card"><div class="n r">3</div><div class="ct">20 November<small>Hingga siang hari, BKN belum menerbitkan pengumuman resmi di situs maupun media sosialnya.</small></div></div>
<div class="card"><div class="n">4</div><div class="ct">23–29 November<small>Pekan keempat November, jadwal yang kini ditunggu untuk pengumuman pembukaan.</small></div></div>''')
s.append(f'''<h1>Fakta Kunci <span>CPNS 2026</span></h1><div class="sub">Yang sudah disampaikan pejabat</div>
<div class="card"><div class="n">1</div><div class="ct">Sekitar 158.000 formasi<small>Terutama untuk menggantikan PNS yang pensiun.</small></div><div class="pill">158 rb</div></div>
<div class="card"><div class="n">2</div><div class="ct">Anggaran sudah tersedia<small>Dirjen Anggaran Kemenkeu menyatakan dana rekrutmen telah disediakan.</small></div></div>
<div class="card"><div class="n">3</div><div class="ct">Pendaftaran via SSCASN<small>Portal resmi: sscasn.bkn.go.id. Pembuatan akun dilaporkan sudah bisa dilakukan.</small></div></div>
<div class="card"><div class="n">4</div><div class="ct">Proses sampai 2027<small>Seleksi diperkirakan berlangsung hingga paruh pertama 2027.</small></div></div>''')
s.append(f'''<h1>Yang Bisa Kamu <span>Siapkan Sekarang</span></h1><div class="sub">Jangan menunggu pengumuman baru bergerak</div>
<div class="card"><div class="n r">1</div><div class="ct">Buat akun SSCASN<small>Daftar dan aktifkan akun di sscasn.bkn.go.id lebih awal.</small></div></div>
<div class="card"><div class="n r">2</div><div class="ct">Siapkan dokumen<small>Umumnya: KTP, ijazah, transkrip nilai, pas foto, email dan nomor HP aktif.</small></div></div>
<div class="card"><div class="n r">3</div><div class="ct">Pelajari formasi<small>Cocokkan jurusan dan jabatan setelah rincian formasi resmi keluar.</small></div></div>
<div class="card"><div class="n r">4</div><div class="ct">Mulai latihan SKD<small>Latihan soal TWK, TIU, TKP dengan timer tiap hari.</small></div></div>''')
s.append(f'''<h1>Waspada <span>Hoaks CPNS</span></h1><div class="sub">Jangan sampai tertipu info palsu</div>
<div class="warn">BKN pernah menegaskan bahwa poster atau tautan yang mengklaim pendaftaran CPNS sudah dibuka, padahal belum ada pengumuman resmi, adalah hoaks.</div>
<div class="card" style="margin-top:34px"><div class="n">✓</div><div class="ct">Cek hanya di kanal resmi<small>sscasn.bkn.go.id<br>bkn.go.id<br>Instagram @bkngoidofficial</small></div></div>
<div class="card"><div class="n r">✗</div><div class="ct">Abaikan calo dan tautan asing<small>Pendaftaran CPNS tidak bisa diloloskan lewat pihak ketiga.</small></div></div>''')
s.append(f'''<h1 style="margin-top:60px">Simpan &amp;<br><span>Bagikan</span></h1>
<div class="sub">ke temanmu yang lagi nunggu info CPNS 2026</div>
<div class="box" style="margin-top:60px">Follow <b>@andikaalmahya</b><br>untuk update CPNS &amp; ASN, tips SKD,<br>dan strategi lulus</div>
<div class="warn" style="margin-top:50px;font-size:25px;font-weight:500">Sumber: CNBC Indonesia, detikJateng, Bisnis.com, Pojoksatu (data per 20–22 Nov 2026). Info resmi tetap mengacu pada pengumuman BKN dan KemenPANRB.</div>''')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for i,x in enumerate(s,1):
            await pg.set_content(wrap(x,i,T)); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"news1/slide{i}.jpg",type="jpeg",quality=92)
        await b.close()
asyncio.run(main())
