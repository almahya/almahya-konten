import json,sys
from playwright.sync_api import sync_playwright
times=json.load(open("times2.json")); total=times[-1][1]; N=int(total*30)
part,parts,out=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
fl=[float(x) for x in sys.argv[4].split(",")] if len(sys.argv)>4 else None
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":1080,"height":1920}); pg.goto("file:///home/claude/reel/reel2.html"); pg.wait_for_timeout(500)
    if fl:
        for k,t in enumerate(fl):
            pg.evaluate(f"setT({t})"); pg.screenshot(path=f"{out}{k}.png")
    else:
        for f in range(part,N,parts):
            pg.evaluate(f"setT({min(f/30,total-0.001)})"); pg.screenshot(path=f"{out}/f{f:05d}.jpg",type="jpeg",quality=90)
    b.close()
