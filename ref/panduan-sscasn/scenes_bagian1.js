// ===== BAGIAN 1 (71.47 s) =====
// A hook 0-6.8
s=scene(0,6.8);
el(s,'● PANDUAN DAFTAR CPNS · 1/2','left:70px;top:290px;background:#c8102e;color:#fff;font-weight:800;font-size:42px;padding:12px 40px;border-radius:50px',0.1,'pop');
el(s,'<div style="font-weight:800;font-size:100px;line-height:1.03;color:#ffd23f">DAFTAR CPNS<br>DI SSCASN</div><div style="font-weight:600;font-size:42px;margin-top:14px">Setelah punya akun, ini urutannya</div>','left:70px;top:400px;width:940px;height:400px;background:#14234b;border-radius:56px;color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 56px',0.4);
pres(s,'thinking',0.9,4.4,'right:10px;top:850px',470);
pres(s,'explain',4.48,6.8,'right:10px;top:850px',470);
[['1','Login + MFA',4.8],['2','Lengkapi profil',5.54],['3','Pilih formasi',6.07]].forEach((r,i)=>card(s,`<div style="width:78px;height:78px;border-radius:50%;background:#c8102e;color:#fff;font-size:44px;display:flex;align-items:center;justify-content:center;flex:none">${r[0]}</div><div style="padding-left:18px;font-size:34px">${r[1]}</div>`,`left:70px;top:${860+i*150}px;width:470px;height:122px;padding:0 20px`,r[2],'#14234b'));
// B1 login + MFA 6.8-25.6
s=scene(6.8,25.6);
hd(s,'1 · <span class=r>Login + MFA</span>',6.93);
shot(s,'2-2_login',781/646,7.1,10.8,[[7.1,.5,.5,1.25],[10.8,.5,.58,1.9]]);
shot(s,'2-3_mfa_aktivasi',1008/894,10.8,18.95,[[10.8,.5,.25,1.2],[12.85,.5,.24,1.5],[15.28,.5,.47,1.7],[16.55,.5,.78,1.7],[18.9,.5,.78,1.7]]);
shot(s,'2-4_mfa_verifikasi',733/830,18.95,25.6,[[18.95,.5,.3,1.0],[21.0,.5,.5,1.1],[23.64,.5,.72,1.15]]);
chip(s,'NIK + Password + Captcha',7.69,10.8);
chip(s,'Aktifkan MFA',10.84,12.8);
chip(s,'Google Authenticator / Authy',12.85,15.2);
chip(s,'Scan kode QR',15.28,16.5);
chip(s,'Masukkan kode 6 digit',16.55,18.1);
chip(s,'Cukup sekali!',18.2,19.0,'#1a8f4c','#fff');
chip(s,'Login berikutnya: cukup kode OTP',19.06,21.8);
chip(s,'Ganti HP / lupa password?',21.85,23.55,'#c8102e','#fff');
chip(s,'Reset lewat tautan di halaman login',23.64,25.6);
// B2 profil 25.6-37.65
s=scene(25.6,37.65);
hd(s,'2 · Lengkapi <span class=r>profil</span>',25.71);
shot(s,'3-2_biodata',963/823,26.2,31.6,[[26.2,.5,.15,1.0],[27.46,.45,.45,1.35],[28.45,.15,.55,1.9],[29.65,.35,.9,1.5],[31.5,.35,.9,1.5]]);
shot(s,'3-3_pendidikan',1009/523,31.6,37.65,[[31.6,.5,.5,1.0],[32.84,.5,.45,1.5],[35.48,.5,.8,1.5]]);
chip(s,'Biodata diri',27.46,28.4);
chip(s,'Pasfoto terbaru',28.45,29.6);
chip(s,'Alamat KTP',29.65,30.65);
chip(s,'Alamat domisili',30.7,31.6);
chip(s,'Riwayat pendidikan',31.68,32.8);
chip(s,'Kampus & prodi dari daftar BKN',32.84,35.4);
chip(s,'Unggah ijazah + transkrip',35.48,37.65);
// B3 daftar formasi 37.65-52.3
s=scene(37.65,52.3);
hd(s,'3 · Daftar <span class=r>formasi</span>',37.8);
el(s,'Klik “Mulai Pendaftaran”','left:70px;top:390px;background:#ffd23f;color:#14234b;font-weight:800;font-size:40px;padding:10px 36px;border-radius:50px',38.46-s.a,'pop');setEnd(s,44.4);
shot(s,'3-1_beranda',919/573,38.3,39.9,[[38.3,.5,.5,1.0],[38.8,.5,.83,2.3]],470,500);
shot(s,'4-2_event',1283/495,39.9,42.0,[[39.9,.5,.5,1.0],[40.5,.62,.6,1.8]],470,500);
shot(s,'4-3_instansi',1283/337,42.0,44.6,[[42.0,.5,.5,1.0],[42.6,.5,.5,1.8]],470,500);
chip(s,'Pilih event: Seleksi CASN',39.92,42.0);
chip(s,'Pilih instansi',42.06,43.0);
chip(s,'Jenis pengadaan: CPNS',43.01,44.6,'#c8102e','#fff');
// stepper 44.6-52.3
const rows=[['Event','Seleksi CASN',44.6,598-128,118],['Instansi','Pilih instansi pembuka',44.75,598,118],['Jenis pengadaan','CPNS',44.9,726,118],['Formasi','',45.05,854,200],['Lokasi ujian','+ data ijazah',45.2,1064,118]];
const rowEls=rows.map((r,i)=>{const done=i<3;const e=el(s,`<div style="width:78px;height:78px;border-radius:50%;background:${done?'#1a8f4c':'#14234b'};color:#fff;font-size:${done?46:44}px;display:flex;align-items:center;justify-content:center;flex:none">${done?'✓':i+1}</div><div style="padding-left:24px;font-size:40px;flex:1"><div>${r[0]}</div><div style="font-size:30px;font-weight:600;color:#5b6585">${r[1]}</div>${i==3?'<div class=mc style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px"></div>':''}</div>`,`left:70px;top:${r[3]}px;width:940px;height:${r[4]}px;padding:0 28px;border-left:14px solid #14234b;font-weight:800;display:flex;align-items:center;background:#fff;border-radius:26px;box-shadow:0 4px 14px #14234b1a`,r[2]-s.a);return e});
const sS=s;
ticks.push(t=>{const act=[null,null,null,[44.69,49.3],[49.41,52.3]];rowEls.forEach((e,i)=>{const a=act[i];e.style.borderLeftColor=a&&t>=a[0]&&t<a[1]?'#c8102e':(i<3?'#1a8f4c':'#14234b')});const mc=rowEls[3].querySelector('.mc');if(mc){const L=[['Jenis formasi',45.88],['Pendidikan',46.97],['Jabatan',47.82],['Lokasi',48.7]];mc.innerHTML=L.filter(x=>t>=x[1]).map(x=>`<span style="background:#ffd23f;border-radius:30px;padding:4px 18px;font-size:28px">${x[0]}</span>`).join('')}});
// C ingat 52.3-57.35
s=scene(52.3,57.35);
hd(s,'Ingat <span class=r>2 hal ini</span>',52.42);
card(s,`<div style="width:96px;height:96px;flex:none">${IC.warn}</div><div style="padding-left:24px;font-size:42px">Hanya 1 jenis seleksi</div>`,'left:70px;top:480px;width:940px;height:150px;padding:0 28px',52.92,'#c8102e');
card(s,`<div style="width:96px;height:96px;flex:none">${IC.clock}</div><div style="padding-left:24px;font-size:40px">Usia dihitung saat memilih formasi</div>`,'left:70px;top:660px;width:940px;height:150px;padding:0 28px',54.53,'#14234b');
pres(s,'warning',52.9,57.2,'right:20px;top:850px',470);
ticks.push(t=>{const q=x=>Q(sS,x);});
// D simpan 57.35-61.65
s=scene(57.35,61.65);
hd(s,'Simpan <span class=r>video ini</span>',57.4);
el(s,BOOK,'left:70px;top:420px;width:150px;height:150px',57.5-s.a,'pop');
card(s,'Bagian 2: unggah dokumen sampai kartu ujian','left:70px;top:620px;width:940px;height:190px;padding:20px 34px;font-size:44px',58.52,'#c8102e');
pres(s,'point-right',58.6,61.5,'right:10px;top:850px',470);
// E CTA 61.65-71.47
s=scene(61.65,71.47);
hd(s,'Siapkan <span class=r>SKD-nya</span>',61.81);
el(s,'almahya.id','left:70px;top:430px;background:#ffd23f;font-weight:800;font-size:84px;padding:18px 60px;border-radius:70px',63.0-s.a,'pop');
[['Tryout lengkap + pembahasan',64.36],['Soal sesuai kisi-kisi',66.3],['Paket bundling SKD + SKB + bimbingan online',67.9]].forEach((r,i)=>card(s,`<div style="font-size:32px">${r[0]}</div>`,`left:70px;top:${620+i*190}px;width:500px;height:165px;padding:0 24px`,r[1],['#14234b','#1a8f4c','#c8102e'][i]));
pres(s,'point-up',64.4,71.4,'right:-30px;top:760px',520);
const SUB=[[0,4.16,'Sudah punya akun SSCASN, tapi bingung langkah daftar CPNS-nya?'],[4.48,6.57,'Ini urutannya, singkat dan lengkap.'],[6.93,10.51,'Pertama, login dengan NIK, password, dan captcha.'],[10.84,15.03,'Lalu aktifkan MFA: pasang Google Authenticator atau Authy,'],[15.28,17.94,'scan kode QR, masukkan kode enam digit.'],[18.20,18.82,'Cukup sekali.'],[19.06,21.55,'Login berikutnya, tinggal masukkan kode OTP.'],[21.85,23.35,'Ganti HP atau lupa password?'],[23.64,25.41,'Ada tautan reset di halaman login.'],[25.71,27.20,'Kedua, lengkapi profil.'],[27.46,28.22,'Biodata diri:'],[28.45,31.37,'pasfoto terbaru, alamat KTP, dan domisili.'],[31.68,32.64,'Riwayat pendidikan:'],[32.84,37.45,'pilih kampus dan prodi dari daftar BKN, lalu unggah ijazah dan transkrip.'],[37.77,39.69,'Ketiga, klik Mulai Pendaftaran.'],[39.92,41.83,'Pilih event Seleksi CASN,'],[42.06,42.81,'instansi,'],[43.01,44.50,'jenis pengadaan CPNS,'],[44.69,49.13,'lalu formasi: jenis formasi, pendidikan, jabatan, dan lokasi.'],[49.41,52.14,'Terakhir, isi lokasi ujian dan data ijazah.'],[52.42,54.31,'Ingat, hanya satu jenis seleksi,'],[54.53,57.10,'dan usia dihitung saat kamu memilih formasi.'],[57.40,58.31,'Simpan video ini,'],[58.52,61.52,'bagian dua membahas unggah dokumen sampai kartu ujian.'],[61.81,64.12,'Siapkan SKD-nya di almahya.id:'],[64.36,66.15,'tryout lengkap dengan pembahasan,'],[66.30,69.24,'soal sesuai kisi-kisi, dan paket bundling'],[69.36,71.21,'SKD + SKB + bimbingan online.']];
