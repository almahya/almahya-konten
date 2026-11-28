from playwright.sync_api import sync_playwright
html='''<html><body style="margin:0;width:1080px;height:1920px;position:relative;font-family:Poppins;background:linear-gradient(180deg,#eef2fc 0%,#fff 45%,#fdeef0 100%);overflow:hidden">
<div style="position:absolute;left:0;top:0;width:1080px;height:12px;background:#c8102e"></div>
<div style="position:absolute;left:70px;top:300px;font-weight:800;font-size:52px;color:#c8102e">almahya<span style="color:#14234b;font-weight:600;font-size:34px"> · CPNS &amp; ASN</span></div>
<div style="position:absolute;left:70px;top:395px;background:#c8102e;color:#fff;font-weight:800;font-size:58px;padding:12px 44px;border-radius:60px">● UPDATE SSCASN · 28 NOV</div>
<div style="position:absolute;left:70px;top:540px;width:940px;height:600px;border-radius:44px;overflow:hidden;box-shadow:0 10px 30px #14234b40">
 <img src="file:///home/claude/covers/zudan.jpg" style="width:100%;height:100%;object-fit:cover;object-position:35% 20%">
 <div style="position:absolute;left:0;right:0;bottom:0;height:150px;background:linear-gradient(0deg,#14234bcc,#14234b00)"></div>
 <div style="position:absolute;left:36px;bottom:30px;background:#ffd23f;color:#14234b;font-weight:800;font-size:46px;padding:10px 34px;border-radius:50px">Prof. Zudan</div></div>
<div style="position:absolute;left:70px;top:1170px;width:940px;height:290px;background:#14234b;border-radius:56px;color:#fff;text-align:center;display:flex;flex-direction:column;justify-content:center">
 <div style="font-weight:800;font-size:92px;line-height:1.05;color:#ffd23f">SEKARANG 6 INSTANSI</div>
 <div style="font-weight:600;font-size:44px;margin-top:16px;opacity:.92">Mahkamah Agung 4.430 kebutuhan</div></div>
<div style="position:absolute;left:70px;top:1490px;background:#ffd23f;color:#14234b;font-weight:800;font-size:44px;padding:14px 40px;border-radius:50px">almahya.id</div>
</body></html>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox","--allow-file-access-from-files"])
    pg=b.new_page(viewport={"width":1080,"height":1920})
    open("t27.html","w").write(html)
    pg.goto("file:///home/claude/covers/t27.html");pg.wait_for_timeout(500)
    pg.screenshot(path="cover-27-update-sscasn-zudan.jpg",type="jpeg",quality=92)
    b.close()
