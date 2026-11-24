from playwright.sync_api import sync_playwright
items=[
("01-tips-manajemen-waktu-skd","TIPS SKD","100 MENIT","110 soal SKD, atur waktumu","Jangan kehabisan<br><span class=r>WAKTU!</span>","point-up",120),
("02-cpns-2026-vs-2027","BERITA CPNS","2026<br>vs 2027","Tahun berapa kamu daftar?","Jangan salah<br><span class=r>STRATEGI!</span>","thinking",150),
("03-bundling-skd-skb","LENGKAP","SKD + SKB","Satu tempat belajar","Siap dua tahap<br><span class=r>SEKALIGUS</span>","point-down",140),
("04-hasil-rapat-menpanrb","BERITA CPNS","167.113","Kebutuhan ASN 2026 (rapat DPR)","Hasil rapat<br><span class=r>MENPAN-RB</span>","explain",190),
("05-tryout-nasional-1","GRATIS","TRYOUT<br>NASIONAL 1","Ukur kemampuanmu","Berani bersaing<br><span class=r>DENGAN PESERTA LAIN?</span>","fist-pump",125),
("06-polisi-kehutanan-2024","FORMASI","POLHUT","CPNS Kementerian LHK 2024","Syarat, formasi,<br><span class=r>PENEMPATAN</span>","checklist",190),
("07-pentingnya-skb","JANGAN LUPA","SKB 60%","bobot nilai akhir CPNS 2024","Jangan abaikan<br><span class=r>SKB!</span>","warning",190)]
T=open("/dev/stdin").read() if False else None
tpl='''<html><body style="margin:0;width:1080px;height:1920px;position:relative;font-family:Poppins;background:linear-gradient(180deg,#eef2fc 0%%,#fff 45%%,#fdeef0 100%%);overflow:hidden">
<div style="position:absolute;left:0;top:0;width:1080px;height:12px;background:#c8102e"></div>
<div style="position:absolute;left:70px;top:330px;font-weight:800;font-size:52px;color:#c8102e">almahya<span style="color:#14234b;font-weight:600;font-size:34px"> · CPNS &amp; ASN</span></div>
<div style="position:absolute;left:70px;top:440px;background:#c8102e;color:#fff;font-weight:800;font-size:62px;padding:14px 46px;border-radius:60px">● %(pill)s</div>
<div style="position:absolute;left:70px;top:590px;width:940px;height:420px;background:#14234b;border-radius:56px;color:#fff;text-align:center;display:flex;flex-direction:column;justify-content:center">
 <div style="font-weight:800;font-size:%(fs)dpx;line-height:1.05;color:#ffd23f">%(big)s</div>
 <div style="font-weight:600;font-size:44px;margin-top:22px;opacity:.9">%(sub)s</div></div>
<div style="position:absolute;left:70px;top:1050px;width:600px;font-weight:800;font-size:%(hs)dpx;line-height:1.1;color:#14234b">%(head)s</div>
<img src="file:///home/claude/presenter_png/%(pose)s.png" style="position:absolute;right:30px;top:1090px;height:520px">
<div style="position:absolute;left:70px;top:1490px;background:#ffd23f;color:#14234b;font-weight:800;font-size:44px;padding:14px 40px;border-radius:50px">almahya.id</div>
<style>.r{color:#c8102e}</style></body></html>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox","--allow-file-access-from-files"])
    pg=b.new_page(viewport={"width":1080,"height":1920})
    for slug,pill,big,sub,head,pose,fs in items:
        hs=80 if len(head.replace("<br>","").replace('<span class=r>','').replace('</span>',''))<26 else 66
        open("t.html","w").write(tpl%dict(pill=pill,big=big,sub=sub,head=head,pose=pose,fs=fs,hs=hs))
        pg.goto("file:///home/claude/covers/t.html"); pg.wait_for_timeout(400)
        pg.screenshot(path=f"cover-{slug}.jpg",type="jpeg",quality=92)
    b.close()
from PIL import Image
import glob
fs=sorted(glob.glob("cover-*.jpg")); W=Image.new("RGB",(270*7,480),"white")
for i,f in enumerate(fs): W.paste(Image.open(f).resize((270,480)),(i*270,0))
W.save("sheet.png"); print(len(fs))
