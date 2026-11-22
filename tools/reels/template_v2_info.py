import json,re
src=open("build_html.py").read()
head=src.split("html=r'''")[1].split("const S=[];")[0].replace("TIPS SKD","INFO CPNS").replace("font-size:56px;line-height:1.25;color:#fff","font-size:50px;line-height:1.25;color:#fff").replace("const D=__DATA__;","const D=__DATA__;")
times=[(0,10.71),(10.71,28.58),(28.58,37.30),(37.30,51.79),(51.79,58.3),(58.3,64.6)]
subs=[
 [(0,4.47,"CPNS 2026 dan CPNS 2027."),(4.47,5.62,"Bedanya apa?"),(5.62,8.35,"Per 22 November 2026."),(8.35,10.71,"Ini yang sudah jelas dan yang belum.")],
 [(10.71,13.17,"CPNS 2026"),(13.17,16.49,"Pemerintah memutuskan rekrutmen dibuka tahun ini."),(16.49,19.54,"Kuotanya sekitar 150 ribu formasi."),(19.54,21.83,"Tapi angkanya masih dihitung ulang."),(21.83,25.1,"Prioritas: Polisi Hutan, Manggala Agni,"),(25.1,28.58,"guru sekolah terintegrasi & Sekolah Unggul Garuda.")],
 [(28.58,32.82,"Akun SSCASN sudah bisa dibuat sejak 14 November."),(32.82,35.0,"Tapi rincian formasi dan pendaftarannya"),(35.0,37.3,"masih menunggu pengumuman resmi.")],
 [(37.3,39.68,"CPNS 2027"),(39.68,42.71,"Jadwal dan jumlah formasinya belum diumumkan."),(42.71,44.51,"Yang sudah disampaikan pemerintah,"),(44.51,47.8,"PPPK penuh waktu, termasuk guru,"),(47.8,51.79,"diberi kesempatan ikut seleksi CPNS secara terbuka dan kompetitif.")],
 [(51.79,53.43,"Jadi jangan menunggu."),(53.43,55.6,"Siapkan akun dan dokumenmu sekarang."),(55.7,58.3,"Lalu mulai latihan SKD dan SKB.")],
 [(58.3,60.5,"Belajar di almahya.id"),(60.6,64.6,"Pantau info resmi hanya lewat SSCASN BKN.")],
]
body=r'''const S=[];
function scene(){const s=document.createElement('div');s.className='scene';stage.appendChild(s);return s}
function ttl(s,h){const t=mk(s,'');t.className='title';t.innerHTML=h;return t}
function card(s,css,html){const c=mk(s,css,html);c.className='card';c.style.position='absolute';return c}
// 1
{const s=scene();
 const a=card(s,'left:0;top:60px;width:410px;height:430px;background:#14234b;border-color:#14234b;color:#fff','<div style="text-align:center;margin-top:90px;font-weight:600;font-size:44px;opacity:.85">CPNS</div><div class=big style="text-align:center;font-size:118px">2026</div>');
 const b=card(s,'left:542px;top:60px;width:410px;height:430px;background:#c8102e;border-color:#c8102e;color:#fff','<div style="text-align:center;margin-top:90px;font-weight:600;font-size:44px;opacity:.9">CPNS</div><div class=big style="text-align:center;font-size:118px">2027</div>');
 const v=mk(s,'left:396px;top:215px;width:160px;height:120px;border-radius:60px;background:#ffd23f;color:#14234b;text-align:center;font-weight:800;font-size:64px;padding-top:26px;box-shadow:0 10px 30px rgba(0,0,0,.25)','VS');
 const q=mk(s,'left:0;top:560px;width:952px;text-align:center;font-weight:800;font-size:60px;line-height:1.2','Apa <span style="color:#c8102e">bedanya</span>?');
 const p=mk(s,'left:126px;top:700px;width:700px;height:110px;border-radius:55px;background:#eef1f8;text-align:center;font-weight:700;font-size:40px;padding-top:28px;color:#14234b','Posisi per 22 November 2026');
 S.push(u=>{show(a,u,0.1);show(b,u,0.4);const k=bk((u-0.8)/0.6);v.style.opacity=clamp((u-0.8)/0.2);v.style.transform=`scale(${k})`;show(q,u,4.6);show(p,u,5.8)})}
// 2
{const s=scene();
 const t=ttl(s,'<span>CPNS 2026</span> · Dibuka tahun ini');
 const bd=mk(s,'left:0;top:100px;width:952px;height:90px;border-radius:45px;background:#e6f6ec;border:3px solid #1a9a52;color:#1a9a52;font-weight:800;font-size:40px;text-align:center;padding-top:18px','✓ Rekrutmen diputuskan dibuka tahun ini');
 const c=card(s,'left:0;top:225px;width:952px;height:290px','<div style="text-align:center;font-weight:600;font-size:38px;margin-top:26px;color:#5b6786">kuota sekitar</div><div class=big id=n150 style="text-align:center;font-size:130px;color:#14234b;margin-top:6px">0 ribu</div><div style="text-align:center;font-weight:700;font-size:40px;color:#c8102e;margin-top:6px">formasi</div>');
 const nt=mk(s,'left:150px;top:535px;width:652px;height:76px;border-radius:38px;background:#fff6dd;border:3px solid #f0b400;text-align:center;font-weight:700;font-size:34px;padding-top:15px;color:#7a5800','⚠ angka masih dihitung ulang');
 const ch=['Polisi Hutan','Manggala Agni','Guru Sekolah Terintegrasi','Guru Sekolah Unggul Garuda'].map((x,i)=>mk(s,`left:${(i%2)*486}px;top:${645+Math.floor(i/2)*100}px;width:466px;height:88px;border-radius:24px;background:#14234b;color:#fff;font-weight:700;font-size:${i>1?27:34}px;text-align:center;padding-top:${i>1?27:22}px`,x));
 const lb=mk(s,'left:0;top:610px;width:952px;font-weight:700;font-size:30px;color:#c8102e;text-align:center;display:none','');
 const d=[11.6,13.0,14.5,16.2].map(x=>x-10.71+0.0);
 S.push(u=>{show(t,u,0.1);show(bd,u,2.5);show(c,u,5.6);
  const p=ez((u-5.8)/1.2);document.getElementById('n150').textContent=Math.round(150*p)+' ribu';
  show(nt,u,8.8,20);ch.forEach((e,i)=>show(e,u,[11.3,12.6,14.1,15.6][i],20))})}
// 3
{const s=scene();
 const t=ttl(s,'<span>SSCASN</span> · Status saat ini');
 const a=card(s,'left:0;top:130px;width:952px;height:210px;border-color:#1a9a52','<div style="position:absolute;left:36px;top:40px;width:110px;height:110px;border-radius:55px;background:#1a9a52;color:#fff;font-size:70px;text-align:center;line-height:108px;font-weight:800">✓</div><div style="position:absolute;left:180px;top:30px;font-weight:800;font-size:50px">Akun SSCASN</div><div style="position:absolute;left:180px;top:105px;font-weight:600;font-size:36px;color:#1a9a52">sudah bisa dibuat sejak 14 November</div>');
 const b=card(s,'left:0;top:380px;width:952px;height:210px;border-color:#f0b400','<div style="position:absolute;left:36px;top:40px;width:110px;height:110px;border-radius:55px;background:#f0b400;color:#fff;font-size:60px;text-align:center;line-height:108px;font-weight:800">…</div><div style="position:absolute;left:180px;top:30px;font-weight:800;font-size:50px">Pendaftaran formasi</div><div style="position:absolute;left:180px;top:105px;font-weight:600;font-size:36px;color:#a57600">menunggu pengumuman resmi</div>');
 const n=mk(s,'left:0;top:650px;width:952px;height:130px;border-radius:30px;background:#14234b;color:#fff;text-align:center;font-weight:700;font-size:40px;padding-top:30px','Portal resmi: sscasn.bkn.go.id');
 S.push(u=>{show(t,u,0.1);show(a,u,0.4);show(b,u,4.3);show(n,u,6.6)})}
// 4
{const s=scene();
 const t=ttl(s,'<span>CPNS 2027</span> · Belum ada jadwal');
 const a=card(s,'left:0;top:130px;width:952px;height:250px;border-color:#c8102e;border-width:6px','<div class=big style="text-align:center;font-size:62px;margin-top:40px;color:#c8102e">BELUM DIUMUMKAN</div><div style="text-align:center;font-weight:700;font-size:44px;margin-top:16px">jadwal & jumlah formasi</div>');
 const b=card(s,'left:0;top:430px;width:952px;height:290px;background:#14234b;border-color:#14234b;color:#fff','<div style="text-align:center;font-weight:600;font-size:36px;margin-top:34px;opacity:.85">yang sudah disampaikan pemerintah</div><div class=big style="text-align:center;font-size:62px;margin-top:14px">PPPK penuh waktu</div><div style="text-align:center;font-weight:700;font-size:40px;margin-top:12px;color:#ffd23f">termasuk guru, boleh ikut seleksi CPNS</div>');
 const c1=mk(s,'left:0;top:750px;width:452px;height:90px;border-radius:45px;background:#fdeceb;border:3px solid #c8102e;color:#c8102e;font-weight:800;font-size:40px;text-align:center;padding-top:18px','Terbuka');
 const c2=mk(s,'left:500px;top:750px;width:452px;height:90px;border-radius:45px;background:#fdeceb;border:3px solid #c8102e;color:#c8102e;font-weight:800;font-size:40px;text-align:center;padding-top:18px','Kompetitif');
 S.push(u=>{show(t,u,0.1);show(a,u,2.4);show(b,u,7.2);show(c1,u,11.4,20);show(c2,u,12.4,20)})}
// 5
{const s=scene();
 const t=ttl(s,'<span>Persiapan</span> dari sekarang');
 const rows=['Siapkan akun SSCASN','Siapkan dokumen','Latihan SKD & SKB'].map((x,i)=>card(s,`left:0;top:${140+i*170}px;width:952px;height:140px`,`<div style="position:absolute;left:36px;top:30px;width:80px;height:80px;border-radius:20px;background:#14234b;color:#fff;font-size:56px;text-align:center;line-height:78px;font-weight:800">✓</div><div style="position:absolute;left:150px;top:36px;font-weight:800;font-size:48px">${x}</div>`));
 const w=mk(s,'left:0;top:670px;width:952px;text-align:center;font-weight:800;font-size:56px;color:#c8102e','Jangan menunggu!');
 S.push(u=>{show(t,u,0.1);show(w,u,0.2);show(rows[0],u,1.7);show(rows[1],u,2.1);show(rows[2],u,4.2)})}
// 6
{const s=scene();
 const c=mk(s,'left:0;top:40px;width:952px;height:520px;background:#14234b;border-radius:48px;color:#fff;text-align:center;padding-top:60px','<div style="font-weight:600;font-size:44px;opacity:.85">Latihan SKD + SKB</div><div class=big style="font-size:62px;margin-top:10px">Belajar di</div><div style="margin:40px auto 0;width:660px;background:#c8102e;border-radius:70px;padding:18px 0;font-weight:800;font-size:84px">almahya.id</div>');
 const r=mk(s,'left:0;top:610px;width:952px;height:140px;border-radius:70px;border:4px solid #14234b;text-align:center;font-weight:800;font-size:42px;padding-top:34px','Info resmi: SSCASN BKN');
 S.push(u=>{show(c,u,0.1);show(r,u,2.4)})}
const sub=document.getElementById('sub');
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
data=dict(times=times,subs=subs)
open("reel2.html","w").write((head+body).replace("__DATA__",json.dumps(data)))
json.dump(times,open("times2.json","w"))
