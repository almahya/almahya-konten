import json
from scenes import SCENES
times=json.load(open("times.json"))
data=dict(times=times,subs=[s["sub"] for s in SCENES])
html=r'''<!doctype html><meta charset=utf-8><style>
*{box-sizing:border-box}
body{margin:0;width:1080px;height:1920px;font-family:Poppins;background:#fff;color:#14234b;overflow:hidden;position:relative}
body:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 85% 12%,#e9efff 0,transparent 45%),radial-gradient(circle at 10% 80%,#fdeceb 0,transparent 40%)}
.top{position:absolute;left:0;top:0;width:1080px;height:16px;background:linear-gradient(90deg,#14234b,#c8102e)}
#prog{position:absolute;left:0;top:16px;height:8px;background:#c8102e}
.brand{position:absolute;left:64px;top:140px;font-weight:800;font-size:48px}.brand b{color:#c8102e}
.tag{position:absolute;right:64px;top:146px;background:#c8102e;color:#fff;font-weight:700;font-size:30px;padding:10px 28px;border-radius:40px}
.scene{position:absolute;left:64px;top:270px;width:952px;height:860px;display:none}
.abs{position:absolute}
.title{position:absolute;left:0;top:0;width:952px;font-weight:800;font-size:54px;line-height:1.15}
.title span{color:#c8102e}
.card{position:absolute;background:#fff;border:3px solid #dfe5f2;border-radius:36px;box-shadow:0 14px 40px rgba(20,35,75,.12)}
.big{font-weight:800;line-height:1}
#sub{position:absolute;left:50px;width:980px;top:1190px;text-align:center;font-weight:800;font-size:56px;line-height:1.25;color:#fff;background:#14234b;border-radius:30px;padding:22px 30px;display:none}
.foot{position:absolute;left:0;width:1080px;top:1480px;text-align:center;font-weight:700;font-size:32px;color:#c8102e}
</style>
<div class=top></div><div id=prog></div>
<div class=brand>al<b>mahya</b></div><div class=tag>TIPS SKD</div>
<div id=stage></div><div id=sub></div><div class=foot>Belajar SKD+SKB: almahya.id</div>
<script>
const D=__DATA__;
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const ez=x=>1-Math.pow(1-clamp(x),3);
const bk=x=>{x=clamp(x);const c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const stage=document.getElementById('stage');
function mk(parent,css,html=''){const e=document.createElement('div');e.className='abs';e.style.cssText=css;e.innerHTML=html;parent.appendChild(e);return e}
function show(e,u,d,dy=40){const p=ez((u-d)/0.5);e.style.opacity=p;e.style.transform=`translateY(${(1-p)*dy}px) scale(${0.96+0.04*p})`}
const S=[];
function scene(){const s=document.createElement('div');s.className='scene';stage.appendChild(s);return s}
// 1
{const s=scene();
 const c1=mk(s,'left:0;top:20px;width:456px;height:360px','');c1.className='card';c1.style.position='absolute';
 c1.innerHTML='<div class="big" id=n1 style="font-size:170px;text-align:center;margin-top:50px;color:#14234b">0</div><div style="text-align:center;font-weight:700;font-size:48px;color:#c8102e;margin-top:10px">SOAL</div>';
 const c2=mk(s,'left:496px;top:20px;width:456px;height:360px','');c2.className='card';
 c2.innerHTML='<div class="big" id=n2 style="font-size:170px;text-align:center;margin-top:50px;color:#14234b">0</div><div style="text-align:center;font-weight:700;font-size:48px;color:#c8102e;margin-top:10px">MENIT</div>';
 const b=mk(s,'left:126px;top:440px;width:700px;height:170px;background:#14234b;border-radius:85px;color:#fff;text-align:center;padding-top:22px','<div style="font-size:30px;font-weight:600;opacity:.85">rata-rata cuma</div><div class=big style="font-size:64px">≈ 54 detik / soal</div>');
 const t=mk(s,'left:0;top:690px;width:952px;text-align:center;font-weight:800;font-size:50px;line-height:1.2','Tips <span style="color:#c8102e">manajemen waktu</span><br>SKD CPNS');
 S.push(u=>{show(c1,u,0.1);show(c2,u,0.4);
  document.getElementById('n1').textContent=Math.round(110*ez((u-0.3)/1.2));
  document.getElementById('n2').textContent=Math.round(100*ez((u-0.6)/1.2));
  show(b,u,4.2);show(t,u,7.0)})}
// 2
{const s=scene();
 mk(s,'','').remove();
 const ti=mk(s,'left:0;top:0;width:952px','');ti.className='title';ti.innerHTML='<span>TIPS 1</span> · Bagi waktu per subtes';
 const segs=[['TWK',25,'#14234b'],['TIU',40,'#c8102e'],['TKP',30,'#2f6fdc'],['Cek',5,'#9aa5bd']];
 const bar=mk(s,'left:0;top:150px;width:952px;height:80px;border-radius:40px;overflow:hidden;background:#eef1f8','');
 let x=0;const segEls=segs.map(g=>{const w=g[1]/100*952;const e=mk(bar,`left:${x}px;top:0;height:80px;width:${w}px;background:${g[2]}`);x+=w;return e});
 const rows=segs.map((g,i)=>{const r=mk(s,`left:0;top:${270+i*140}px;width:952px;height:120px`,'');r.className='card';r.style.position='absolute';
  r.innerHTML=`<div style="position:absolute;left:30px;top:36px;width:48px;height:48px;border-radius:24px;background:${g[2]}"></div><div style="position:absolute;left:105px;top:26px;font-weight:800;font-size:50px">${i==3?'Cek ulang':g[0]}</div><div style="position:absolute;right:40px;top:20px;font-weight:800;font-size:64px;color:${g[2]}">${g[1]} <span style="font-size:36px">menit</span></div>`;return r});
 const d=[3.0,4.9,6.9,9.2];
 S.push(u=>{show(ti,u,0.1);segEls.forEach((e,i)=>{e.style.opacity=clamp((u-d[i]+0.3)/0.3)});bar.style.opacity=ez(u/0.5);rows.forEach((r,i)=>show(r,u,d[i]-0.2,30))})}
// 3
{const s=scene();
 const ti=mk(s,'','');ti.className='title';ti.innerHTML='<span>TIPS 2</span> · Soal menguras waktu?';
 const q=mk(s,'left:0;top:150px;width:952px;height:330px','');q.className='card';
 q.innerHTML='<div style="position:absolute;left:40px;top:34px;font-weight:700;font-size:34px;color:#c8102e">SOAL No. 47</div>'+[0,1,2,3].map(i=>`<div style="position:absolute;left:40px;top:${96+i*46}px;width:${i==3?420:870}px;height:22px;border-radius:11px;background:#e3e8f3"></div>`).join('')+'<div style="position:absolute;right:36px;top:30px;font-weight:700;font-size:30px;color:#9aa5bd">hitungan panjang…</div>';
 const rg=mk(s,'left:0;top:530px;width:452px;height:120px;border-radius:30px;border:4px solid #14234b;background:#fff;font-weight:800;font-size:44px;padding:28px 0 0 36px','');
 rg.innerHTML='<span id=ck style="display:inline-block;width:48px;height:48px;border:4px solid #14234b;border-radius:10px;vertical-align:middle;margin-right:18px;text-align:center;line-height:40px;font-size:40px"></span>Ragu-ragu';
 const nx=mk(s,'left:490px;top:530px;width:462px;height:120px;border-radius:30px;background:#14234b;color:#fff;font-weight:800;font-size:44px;padding:30px 0 0 38px','Lanjut dulu →');
 const bk2=mk(s,'left:0;top:690px;width:952px;height:130px;border-radius:30px;background:#fdeceb;border:3px solid #c8102e;color:#c8102e;font-weight:800;font-size:46px;text-align:center;padding-top:32px','↺ Kembali lagi di akhir');
 S.push(u=>{show(ti,u,0.1);show(q,u,0.5);show(rg,u,2.2);show(nx,u,4.0);show(bk2,u,5.6);
  const on=u>3.0;document.getElementById('ck').textContent=on?'✓':'';rg.style.background=on?'#ffd23f':'#fff';})}
// 4
{const s=scene();
 const ti=mk(s,'','');ti.className='title';ti.innerHTML='<span>TIPS 3</span> · Jangan ada soal kosong';
 const cells=[];for(let i=0;i<110;i++){const r=Math.floor(i/11),c=i%11;cells.push(mk(s,`left:${c*87}px;top:${130+r*70}px;width:76px;height:60px;border-radius:12px;background:#e3e8f3`))}
 const ov=mk(s,'left:76px;top:360px;width:800px;height:210px;background:#fff;border:4px solid #1a9a52;border-radius:40px;box-shadow:0 20px 60px rgba(0,0,0,.2);text-align:center;padding-top:24px','<div class=big style="font-size:84px;color:#1a9a52">✓ 110 / 110</div><div style="font-weight:700;font-size:42px;margin-top:8px">semua terisi!</div>');
 S.push(u=>{show(ti,u,0.1);const n=Math.floor(110*clamp((u-2.6)/1.8));cells.forEach((e,i)=>{e.style.background=i<n?(i%2?'#14234b':'#2f4a8f'):'#e3e8f3';e.style.opacity=ez((u-0.3)/0.4)});show(ov,u,4.5,20)})}
// 5
{const s=scene();
 const ti=mk(s,'','');ti.className='title';ti.innerHTML='<span>TIPS 4</span> · Biasakan simulasi';
 const cl=mk(s,'left:176px;top:140px;width:600px;height:600px','');
 cl.innerHTML='<svg width=600 height=600 viewBox="0 0 600 600"><circle cx=300 cy=300 r=270 fill="#fff" stroke="#e3e8f3" stroke-width=36 /><circle id=arc cx=300 cy=300 r=270 fill=none stroke="#c8102e" stroke-width=36 stroke-linecap=round transform="rotate(-90 300 300)" stroke-dasharray="1696" stroke-dashoffset=0 /></svg><div id=clk class=big style="position:absolute;left:0;top:200px;width:600px;text-align:center;font-size:132px">100:00</div><div style="position:absolute;left:0;top:350px;width:600px;text-align:center;font-weight:700;font-size:46px;color:#c8102e">110 soal</div>';
 const t=mk(s,'left:0;top:775px;width:952px;text-align:center;font-weight:800;font-size:48px','Rutin = ritme jadi terbiasa');
 S.push(u=>{show(ti,u,0.1);show(cl,u,0.3);const p=clamp((u-2.8)/2.8);const sec=Math.round(6000*(1-p));
  document.getElementById('clk').textContent=String(Math.floor(sec/60)).padStart(2,'0')+':'+String(sec%60).padStart(2,'0');
  document.getElementById('arc').setAttribute('stroke-dashoffset',1696*p);show(t,u,4.8)})}
// 6
{const s=scene();
 const c=mk(s,'left:0;top:40px;width:952px;height:520px;background:#14234b;border-radius:48px;color:#fff;text-align:center;padding-top:60px','<div style="font-weight:600;font-size:44px;opacity:.85">Mau latihan SKD lengkap</div><div class=big style="font-size:62px;margin-top:10px">+ Tryout CAT?</div><div style="margin:50px auto 0;width:660px;background:#c8102e;border-radius:70px;padding:18px 0;font-weight:800;font-size:84px">almahya.id</div>');
 const a=mk(s,'left:0;top:620px;width:452px;height:130px;border-radius:65px;border:4px solid #14234b;text-align:center;font-weight:800;font-size:50px;padding-top:30px','SIMPAN');
 const b=mk(s,'left:500px;top:620px;width:452px;height:130px;border-radius:65px;background:#ffd23f;text-align:center;font-weight:800;font-size:50px;padding-top:30px','BAGIKAN');
 S.push(u=>{show(c,u,0.1);show(a,u,4.8);show(b,u,5.6)})}
const sub=document.getElementById('sub');
window.setT=function(t){
 let i=D.times.findIndex(x=>t>=x[0]&&t<x[1]);if(i<0)i=D.times.length-1;
 const u=t-D.times[i][0],dur=D.times[i][1]-D.times[i][0]-0.35;
 document.querySelectorAll('.scene').forEach((e,k)=>e.style.display=k==i?'block':'none');
 S[i](u);
 const subs=D.subs[i],w=subs.map(x=>x.length),tot=w.reduce((a,b)=>a+b,0);let acc=0,cur=-1;
 for(let k=0;k<subs.length;k++){const a=acc/tot*dur;acc+=w[k];const b=acc/tot*dur;if(u>=a-0.05&&u<b){cur=k}}
 if(cur<0&&u<dur+0.1)cur=subs.length-1;
 if(cur<0){sub.style.display='none'}else{sub.style.display='block';sub.textContent=subs[cur]}
 document.getElementById('prog').style.width=(t/D.times[D.times.length-1][1]*1080)+'px';
};
setT(0);
</script>'''
open("reel.html","w").write(html.replace("__DATA__",json.dumps(data)))
