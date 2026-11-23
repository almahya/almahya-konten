import json
src=open("build_html.py").read()
head=src.split("html=r'''")[1].split("const S=[];")[0].replace("TIPS SKD","INFO CPNS").replace("font-size:56px;line-height:1.25;color:#fff","font-size:50px;line-height:1.25;color:#fff")
times=[(0, 5.82), (5.82, 13.36), (13.36, 21.94), (21.94, 31.36), (31.36, 41.73), (41.73, 45.16), (45.16, 49.44), (49.44, 54.36)]
subs=[[(0, 1.97, 'Lolos SKD itu belum selesai!'), (2.28, 5.66, 'Karena bagian yang bobotnya paling besar justru SKB.')], [(5.97, 8.22, 'Pada seleksi CPNS 2024,'), (8.5, 11.37, 'nilai akhir dihitung dari SKD 40 persen'), (11.51, 13.2, 'dan SKB 60 persen.')], [(13.52, 14.22, 'Artinya,'), (14.39, 18.7, 'SKB bisa menentukan peringkatmu di antara peserta lain di formasi yang sama.'), (18.96, 21.72, 'Dan materi SKB berbeda untuk setiap formasi.')], [(22.16, 22.58, 'Lalu,'), (22.76, 25.74, 'kenapa memilih belajar di tempat yang hanya menyiapkan SKD?'), (26.08, 27.49, 'Saat kamu lolos SKD,'), (27.7, 31.25, 'kamu harus mulai dari nol mencari materi dan soal SKB.')], [(31.48, 32.8, 'Di almahya.id,'), (32.95, 34.38, 'SKD-nya super lengkap:'), (34.67, 36.41, 'materi, latihan soal,'), (36.53, 37.02, 'tryout,'), (37.15, 37.99, 'dan pembahasan.'), (38.19, 41.6, 'Dan SKB-nya sudah disiapkan sesuai formasi yang kamu daftar.')], [(41.87, 42.48, 'Satu tempat,'), (42.72, 43.26, 'dua tahap,'), (43.49, 45.06, 'tanpa bingung di tengah jalan.')], [(45.26, 47.14, 'Itu aturan seleksi 2024.'), (47.39, 49.34, 'Selalu cek pengumuman resmi terbaru ya.')], [(49.55, 52.15, 'Mulai siapkan sekarang di almahya.id.'), (52.4, 54.2, 'Simpan dan bagikan ke temanmu!')]]
body=r'''const S=[];
function scene(){const s=document.createElement('div');s.className='scene';stage.appendChild(s);return s}
function ttl(s,h){const t=mk(s,'');t.className='title';t.innerHTML=h;return t}
function card(s,css,html){const c=mk(s,css,html);c.className='card';c.style.position='absolute';return c}
const CHK='<div style="position:absolute;left:26px;top:14px;width:76px;height:76px;border-radius:20px;background:#1c9a4f;color:#fff;font-size:52px;text-align:center;line-height:74px;font-weight:800">✓</div>';
// 1: track SKD -> SKB
{const s=scene();
 const b=mk(s,'left:0;top:10px;width:560px;height:90px;border-radius:45px;background:#c8102e;color:#fff;font-weight:800;font-size:42px;text-align:center;padding-top:17px','● LOLOS SKD ≠ SELESAI');
 const a=card(s,'left:0;top:150px;width:452px;height:330px;border-color:#1c9a4f','<div class=big style="text-align:center;font-size:120px;margin-top:30px;color:#1c9a4f;line-height:1">✓</div><div class=big style="text-align:center;font-size:84px;margin-top:6px">SKD</div><div style="text-align:center;font-weight:600;font-size:34px;color:#5b6786">lolos</div>');
 const c=card(s,'left:500px;top:150px;width:452px;height:330px;background:#14234b;border-color:#c8102e;color:#fff','<div class=big style="text-align:center;font-size:120px;margin-top:30px;color:#ffd23f;line-height:1">?</div><div class=big style="text-align:center;font-size:84px;margin-top:6px">SKB</div><div style="text-align:center;font-weight:600;font-size:34px;opacity:.85">bobot terbesar</div>');
 const tr=mk(s,'left:60px;top:560px;width:832px;height:16px;border-radius:8px;background:#d7def0','');
 const mv=mk(s,'left:60px;top:530px;width:76px;height:76px;border-radius:38px;background:#c8102e;color:#fff;font-size:40px;text-align:center;line-height:74px;font-weight:800','▶');
 const fl=mk(s,'left:830px;top:480px;width:120px;text-align:center;font-weight:800;font-size:60px','🏁');
 S.push(u=>{show(b,u,0.1);show(a,u,0.3);show(c,u,2.4);show(tr,u,2.4);show(mv,u,2.4);show(fl,u,2.6);mv.style.left=(60+ez((u-3.0)/2.3)*700)+'px'})}
// 2: bars 40/60
{const s=scene();
 const t=ttl(s,'<span>Nilai akhir</span> CPNS 2024');
 const mk1=(x,hpx,col,lab,num,start)=>{const w=card(s,`left:${x}px;top:130px;width:452px;height:660px;padding:0`,`<div class=bar style="position:absolute;left:60px;bottom:90px;width:332px;height:${hpx}px;background:${col};border-radius:24px 24px 0 0;transform-origin:bottom"></div><div class=big style="position:absolute;left:0;width:452px;text-align:center;bottom:${hpx+100}px;font-size:84px;color:${col}">${num}</div><div class=big style="position:absolute;left:0;width:452px;text-align:center;bottom:20px;font-size:54px">${lab}</div>`);return {w,start,hpx}};
 const A=mk1(0,300,'#14234b','SKD','40%',2.7),B=mk1(500,450,'#c8102e','SKB','60%',5.7);
 S.push(u=>{show(t,u,0.1);[A,B].forEach(o=>{show(o.w,u,o.start-0.3,15);const p=ez((u-o.start)/0.9);o.w.querySelector('.bar').style.transform=`scaleY(${p})`;o.w.children[1].style.opacity=p})})}
// 3: leaderboard + formasi
{const s=scene();
 const t=ttl(s,'<span>SKB</span> menentukan peringkat');
 const rows=[['Peserta A',62],['Peserta B',58],['Kamu',55],['Peserta C',51]];
 const els=rows.map((r,i)=>card(s,`left:0;top:${130+i*118}px;width:952px;height:100px`,`<div style="position:absolute;left:24px;top:26px;font-weight:700;font-size:38px;${r[0]=='Kamu'?'color:#c8102e':''}">${r[0]}</div><div class=bk style="position:absolute;left:300px;top:32px;height:36px;width:${r[1]*5}px;background:${r[0]=='Kamu'?'#c8102e':'#14234b'};border-radius:18px"></div>`));
 const note=mk(s,'left:0;top:610px;width:952px;text-align:center;font-weight:600;font-size:30px;color:#5b6786','ilustrasi · peringkat per formasi');
 const f=['Formasi A','Formasi B','Formasi C'];
 const fe=f.map((x,i)=>card(s,`left:0;top:${130+i*215}px;width:952px;height:190px;border-left:20px solid #2f6fdc`,`<div class=big style="position:absolute;left:40px;top:28px;font-size:54px">${x}</div><div style="position:absolute;left:40px;top:104px;font-weight:700;font-size:38px;color:#2f6fdc">→ materi SKB berbeda</div>`));
 S.push(u=>{show(t,u,0.1);
  const tU=ez((u-3.2)/1.2);// SKB boost for Kamu: row index 2 moves up to 0
  els.forEach((e,i)=>{show(e,u,0.5+i*0.25,15);let pos=i;if(i==2)pos=2-2*tU;else if(i<2)pos=i+tU*(i<2?1:0);e.style.top=(130+pos*118)+'px';
   const bar=e.querySelector('div:nth-child(2)');if(i==2)bar.style.width=(55*5+tU*70)+'px'});
  show(note,u,0.8);fe.forEach((e,i)=>{show(e,u,5.6+i*0.8,20);if(u>=5.6){els.forEach(x=>x.style.opacity=Math.max(0,1-(u-5.4)*2));note.style.opacity=Math.max(0,1-(u-5.4)*2)}});})}
// 4: only SKD? -> from zero
{const s=scene();
 const q=card(s,'left:0;top:60px;width:952px;height:380px;border-color:#14234b','<div class=big style="text-align:center;font-size:62px;margin-top:40px;line-height:1.2">Belajar di tempat<br>yang hanya SKD?</div><div class=big style="text-align:center;font-size:120px;margin-top:6px;color:#c8102e;line-height:1">?</div>');
 const z=card(s,'left:0;top:480px;width:952px;height:360px;background:#14234b;border-color:#14234b;color:#fff','<div style="text-align:center;font-weight:600;font-size:38px;margin-top:26px;opacity:.85">Lolos SKD, lalu cari materi SKB dari</div><div class=big id=z0 style="text-align:center;font-size:170px;margin-top:0;color:#ffd23f;line-height:1.1">0</div><div style="margin:8px 60px 0;height:26px;border-radius:13px;background:rgba(255,255,255,.2)"><div style="width:0%;height:100%"></div></div>');
 const mg=mk(s,'left:60px;top:790px;width:90px;height:90px;font-size:70px;text-align:center','🔍');
 S.push(u=>{show(q,u,0.5);const on=u>=4.0;q.style.opacity=on?Math.max(0.0,1-(u-4.0)*3):1;if(u>=4.6&&u<5.0)q.style.display='none';show(z,u,4.1);z.style.display=u>=4.1?'block':'none';
  mg.style.display=u>=5.8?'block':'none';mg.style.left=(60+Math.abs(Math.sin((u-5.8)*2.2))*740)+'px';mg.style.transform=`rotate(${Math.sin((u-5.8)*6)*14}deg)`})}
// 5: almahya
{const s=scene();
 const p=mk(s,'left:0;top:0;width:952px;height:130px;background:#14234b;border-radius:48px;color:#fff;text-align:center;padding-top:14px','<div style="font-weight:600;font-size:28px;opacity:.85">Di</div><div style="font-weight:800;font-size:66px;line-height:1.05">almahya.id</div>');
 const hd=card(s,'left:0;top:160px;width:952px;height:100px;border-color:#14234b','<div class=big style="text-align:center;font-size:48px;margin-top:20px;color:#14234b">SKD super lengkap</div>');
 const it=[['Materi',3.3],['Latihan soal',3.9],['Tryout',5.2],['Pembahasan',5.9]];
 const ie=it.map((r,i)=>card(s,`left:${(i%2)*486}px;top:${290+Math.floor(i/2)*130}px;width:466px;height:110px`,`<div style="position:absolute;left:22px;top:18px;width:74px;height:74px;border-radius:20px;background:#1c9a4f;color:#fff;font-size:50px;text-align:center;line-height:72px;font-weight:800">✓</div><div style="position:absolute;left:114px;top:30px;font-weight:800;font-size:38px">${r[0]}</div>`));
 const sk=card(s,'left:0;top:580px;width:952px;height:260px;background:#c8102e;border-color:#c8102e;color:#fff','<div class=big style="text-align:center;font-size:64px;margin-top:30px">+ SKB</div><div style="text-align:center;font-weight:700;font-size:42px;margin-top:10px;line-height:1.25">sudah disiapkan sesuai<br>formasi yang kamu daftar</div>');
 S.push(u=>{show(p,u,0.1);show(hd,u,1.4);ie.forEach((e,i)=>show(e,u,it[i][1]-0.2,15));show(sk,u,6.8)})}
// 6: satu tempat dua tahap
{const s=scene();
 const w=card(s,'left:0;top:60px;width:952px;height:500px;background:#eef2fc;border-color:#14234b','<div class=big style="text-align:center;font-size:52px;margin-top:26px">almahya.id</div>');
 const a=mk(s,'left:80px;top:200px;width:340px;height:260px;border-radius:40px;background:#14234b;color:#fff;text-align:center','<div class=big style="font-size:110px;margin-top:40px;line-height:1">SKD</div><div style="font-weight:600;font-size:34px;opacity:.85;margin-top:10px">tahap 1</div>');
 const c=mk(s,'left:532px;top:200px;width:340px;height:260px;border-radius:40px;background:#c8102e;color:#fff;text-align:center','<div class=big style="font-size:110px;margin-top:40px;line-height:1">SKB</div><div style="font-weight:600;font-size:34px;opacity:.85;margin-top:10px">tahap 2</div>');
 const ar=mk(s,'left:430px;top:290px;width:96px;text-align:center;font-weight:800;font-size:80px;color:#14234b','→');
 const g=card(s,'left:0;top:610px;width:952px;height:150px;border-color:#1c9a4f;background:#e9f8ef','<div class=big style="text-align:center;font-size:56px;margin-top:36px;color:#1c9a4f">✓ Tanpa bingung</div>');
 S.push(u=>{show(w,u,0.1);show(a,u,1.0);show(c,u,1.2);show(ar,u,1.3);show(g,u,1.9)})}
// 7: aturan 2024
{const s=scene();
 const a=card(s,'left:0;top:80px;width:952px;height:360px;border-color:#f0b400;background:#fff6dd','<div style="text-align:center;font-weight:600;font-size:40px;margin-top:40px;color:#a57600">bobot ini aturan seleksi</div><div class=big style="text-align:center;font-size:190px;color:#a57600;line-height:1.1">2024</div>');
 const b=card(s,'left:0;top:490px;width:952px;height:210px;background:#14234b;border-color:#14234b;color:#fff','<div class=big style="text-align:center;font-size:52px;margin-top:36px;line-height:1.2">Cek pengumuman<br>resmi terbaru</div>');
 const c=mk(s,'left:0;top:740px;width:952px;height:100px;border-radius:50px;background:#c8102e;color:#fff;text-align:center;font-weight:800;font-size:42px;padding-top:24px','sscasn.bkn.go.id');
 S.push(u=>{show(a,u,0.1);show(b,u,1.8);show(c,u,3.0)})}
// 8: CTA
{const s=scene();
 const r1=card(s,'left:0;top:0;width:952px;height:120px',CHK.replace('top:14px','top:22px').replace('left:26px','left:30px')+'<div style="position:absolute;left:135px;top:30px;font-weight:800;font-size:42px">SKD lengkap + SKB sesuai formasi</div>');
 const c=mk(s,'left:0;top:170px;width:952px;height:400px;background:#14234b;border-radius:48px;color:#fff;text-align:center;padding-top:50px','<div style="font-weight:600;font-size:42px;opacity:.85">Mulai siapkan sekarang di</div><div style="margin:36px auto 0;width:660px;background:#c8102e;border-radius:70px;padding:18px 0;font-weight:800;font-size:84px">almahya.id</div><div style="font-weight:600;font-size:34px;margin-top:30px;opacity:.85">SKB: skb.almahya.id</div>');
 const a=mk(s,'left:0;top:640px;width:452px;height:100px;border-radius:50px;border:4px solid #14234b;text-align:center;font-weight:800;font-size:44px;padding-top:20px','SIMPAN');
 const b=mk(s,'left:500px;top:640px;width:452px;height:100px;border-radius:50px;background:#ffd23f;text-align:center;font-weight:800;font-size:44px;padding-top:20px','BAGIKAN');
 S.push(u=>{show(r1,u,0.3);show(c,u,0.9);show(a,u,3.0);show(b,u,3.5)})}
'''
tail=r'''const sub=document.getElementById('sub');
window.setT=function(t){
 let i=D.times.findIndex(x=>t>=x[0]&&t<x[1]);if(i<0)i=D.times.length-1;
 const u=t-D.times[i][0];
 document.querySelectorAll('.scene').forEach((e,k)=>e.style.display=k==i?'block':'none');
 S[i](u);
 let cur=null;for(const x of D.subs[i]){if(t>=x[0]-0.05&&t<x[1]+0.12)cur=x}
 if(!cur){sub.style.display='none'}else{sub.style.display='block';sub.textContent=cur[2]}
 document.getElementById('prog').style.width=(t/D.times[D.times.length-1][1]*1080)+'px';
};
setT(0);
</script>'''
inj=r'''
(function(){const SCH=[[0,'warning'],[5.82,'point-up'],[13.36,'explain'],[21.94,'thinking'],[27.6,'warning'],[31.36,'checklist'],[38.19,'laptop'],[41.73,'explain'],[45.16,'warning'],[49.44,'point-down'],[52.4,'closing']];
const img=document.createElement('img');img.style.cssText='position:absolute;right:40px;bottom:0;height:400px;z-index:50;transform-origin:50% 100%';document.body.appendChild(img);
let cur='',t0=0;const orig=window.setT;
window.setT=function(t){orig(t);let p=SCH[0];for(const x of SCH){if(t>=x[0])p=x}
 if(p[1]!=cur){cur=p[1];t0=p[0];img.src='file:///home/claude/presenter_png/'+cur+'.png'}
 const k=Math.min(1,(t-t0)/0.28),sc=0.82+0.18*(1-Math.pow(1-k,3))+0.012*Math.sin(t*2.2);
 img.style.transform=`translateY(${(1-k)*40+2*Math.sin(t*2.2)}px) scale(${sc})`;img.style.opacity=Math.min(1,k*2)}})();
</script>'''
body+=tail.rsplit("</script>",1)[0]+inj
json.dump(times,open("times7.json","w"))
open("reel7.html","w").write((head+body).replace("INFO CPNS","SKD + SKB").replace("__DATA__",json.dumps(dict(times=times,subs=subs))))
