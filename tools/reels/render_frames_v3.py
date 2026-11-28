import sys,os
from playwright.sync_api import sync_playwright
k,n,out,*ts=sys.argv[1:]
k=int(k);n=int(n)
os.makedirs(out,exist_ok=True)
FPS=30;TOT=65.72
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox","--allow-file-access-from-files"])
    pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto("file:///home/claude/reel/g2/index.html");pg.wait_for_timeout(800)
    if ts:
        for t in ts[0].split(','):
            pg.evaluate(f"render({t})");pg.screenshot(path=f"{out}{t}.jpg",type="jpeg",quality=88)
    else:
        for i in range(k,int(FPS*TOT),n):
            pg.evaluate(f"render({i/FPS})");pg.screenshot(path=f"{out}/f{i:05d}.jpg",type="jpeg",quality=88)
    b.close()
