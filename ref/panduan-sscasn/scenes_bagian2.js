// ===== BAGIAN 2 (71.81 s) =====
s=scene(0,3.45);
el(s,'● PANDUAN DAFTAR CPNS · 2/2','left:70px;top:290px;background:#c8102e;color:#fff;font-weight:800;font-size:42px;padding:12px 40px;border-radius:50px',0.1,'pop');
el(s,'<div style="font-weight:800;font-size:100px;line-height:1.03;color:#ffd23f">SUDAH PILIH<br>FORMASI?</div><div style="font-weight:600;font-size:44px;margin-top:14px">Jangan salah langkah di tahap berikutnya</div>','left:70px;top:400px;width:940px;height:420px;background:#14234b;border-radius:56px;color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 56px',0.4);
pres(s,'warning',1.3,3.45,'right:10px;top:850px',470);
[['1','Unggah dokumen',1.6],['2','Resume & finalisasi',2.1],['3','Hasil & kartu ujian',2.6]].forEach((r,i)=>card(s,`<div style="width:78px;height:78px;border-radius:50%;background:#c8102e;color:#fff;font-size:44px;display:flex;align-items:center;justify-content:center;flex:none">${r[0]}</div><div style="padding-left:22px;font-size:36px">${r[1]}</div>`,`left:70px;top:${860+i*150}px;width:600px;height:122px;padding:0 26px`,r[2],'#14234b'));
// B unggah dokumen 3.45-23.85
s=scene(3.45,23.85);
hd(s,'1 · Unggah <span class=r>dokumen</span>',3.59);
shot(s,'4-9_dokumen',917/1107,4.2,11.2,[[4.2,.5,.33,1.0],[6.5,.5,.42,1.25],[7.07,.5,.62,1.45],[10.9,.5,.62,1.45]]);
shot(s,'4-9_meterai',978/547,11.2,16.85,[[11.2,.6,.35,1.0],[11.9,.6,.42,1.5],[14.53,.55,.58,1.6]]);
chip(s,'Sesuai persyaratan instansi',4.41,7.0);
chip(s,'Format PDF / JPEG',7.07,8.9);
chip(s,'Ukuran minimal 80 KB',8.95,11.2);
chip(s,'Surat lamaran & pernyataan: bermeterai',11.26,14.5,'#14234b','#ffd23f',36);
chip(s,'e-Meterai atau Meterai tempel',14.53,16.85);
card(s,`<div style="width:110px;height:110px;flex:none">${IC.warn}</div><div style="padding-left:24px;font-size:40px">Persyaratan di SSCASN beda dengan pengumuman instansi?</div>`,'left:70px;top:480px;width:940px;height:210px;padding:0 28px',16.92,'#c8102e');
card(s,`<div style="width:110px;height:110px;flex:none">${IC.help}</div><div style="padding-left:24px;font-size:42px">Lapor ke <span class=r>instansi</span> atau <span class=r>helpdesk BKN</span></div>`,'left:70px;top:760px;width:940px;height:210px;padding:0 28px',20.96,'#14234b');
el(s,'SEBELUM melanjutkan pendaftaran','left:70px;top:1030px;width:940px;text-align:center;background:#ffd23f;font-weight:800;font-size:42px;padding:16px 0;border-radius:60px',22.4-s.a,'pop');
// C resume + finalisasi 23.85-37.95
s=scene(23.85,37.95);
hd(s,'2 · Resume & <span class=r>finalisasi</span>',23.9,58);
shot(s,'4-10_resume',614/1503,24.5,29.0,[[24.5,.5,.08,1.0],[26.04,.5,.3,1.0],[28.6,.5,.55,1.0]]);
shot(s,'4-12_finalisasi',1635/514,29.0,34.0,[[29.0,.2,.65,1.7],[31.78,.5,.7,1.4],[32.4,.9,.85,1.9]],520,520);
shot(s,'4-12_peringatan',759/396,34.0,37.95,[[34.0,.5,.5,1.0],[35.5,.5,.35,1.2],[36.7,.8,.8,1.5]],470,640);
chip(s,'Tab Resume',24.61,26.0);
chip(s,'Periksa & centang setiap data',26.04,29.0);
chip(s,'Centang pernyataan kebenaran data',29.1,31.7,'#14234b','#ffd23f',36);
chip(s,'Klik “Akhiri Proses Pendaftaran”',31.78,34.4,'#14234b','#ffd23f',36);
chip(s,'Setelah diakhiri: tidak bisa diubah!',34.46,37.95,'#c8102e','#fff',38);
// D kartu pendaftaran 37.95-40.3
s=scene(37.95,40.3);
hd(s,'<span class=r>Kartu Pendaftaran</span> SSCASN',38.04,56);
shot(s,'4-12_cetak_kartu',748/130,38.2,40.3,[[38.2,.5,.5,1.1],[39.6,.6,.5,1.15]],520,240);
el(s,'Bukti resmi pendaftaran selesai','left:70px;top:820px;width:940px;text-align:center;background:#1a8f4c;color:#fff;font-weight:800;font-size:42px;padding:16px 0;border-radius:60px',39.0-s.a,'pop');
// E hasil administrasi 40.3-50.05
s=scene(40.3,50.05);
hd(s,'3 · Hasil seleksi <span class=r>administrasi</span>',40.4,54);
shot(s,'5-3_lulus_administrasi',1232/306,41.0,44.2,[[41.0,.5,.4,1.5],[42.0,.9,.35,2.6]],560,420);
shot(s,'5-4_tms',1283/665,44.2,47.7,[[44.2,.5,.5,1.0],[44.4,.85,.15,2.0],[45.81,.12,.92,2.2]]);
shot(s,'5-5_form_sanggah',856/1033,47.7,50.05,[[47.7,.5,.2,1.1],[48.02,.5,.6,1.4]]);
chip(s,'Pantau di halaman Resume',41.16,44.2);
chip(s,'Status: TMS',44.28,45.75,'#c8102e','#fff');
chip(s,'Ajukan sanggah sebelum batas waktu',45.81,47.9,'#14234b','#ffd23f',36);
chip(s,'Alasan sesuai dokumen',48.02,50.05);
// F sanggah bukan perbaikan 50.05-52.95
s=scene(50.05,52.95);
card(s,`<div style="width:130px;height:130px;flex:none">${IC.warn}</div><div style="padding-left:26px;font-size:50px">Sanggah <span class=r>bukan</span> untuk memperbaiki salah unggah</div>`,'left:70px;top:420px;width:940px;height:330px;padding:0 30px',50.11,'#c8102e');
pres(s,'warning',50.4,52.9,'right:10px;top:820px',480);
// G lulus 52.95-61.4
s=scene(52.95,61.4);
hd(s,'<span class=r>Lulus?</span> Tunggu jadwal ujian',53.1,56);
shot(s,'5-3_lulus_administrasi',1232/306,53.0,55.3,[[53.0,.85,.4,1.8],[53.8,.3,.8,2.4]],560,420);
shot(s,'5-6_cetak_kartu_ujian',1100/291,55.37,59.3,[[55.37,.35,.7,1.9],[57.5,.35,.7,2.2]],560,420);
chip(s,'Tunggu jadwal ujian',53.1,55.3);
chip(s,'Cetak setelah jadwal ditetapkan',55.37,59.3);
const KTP=SV(600,380,`<rect x="10" y="10" width="580" height="360" rx="30" fill="#2f5fd0"/><rect x="26" y="26" width="548" height="328" rx="22" fill="#eaf1ff"/><text x="300" y="80" text-anchor="middle" font-size="34" font-weight="800" fill="#14234b" font-family="Poppins">KARTU TANDA PENDUDUK</text><circle cx="470" cy="210" r="60" fill="#f2c9a0"/><path d="M410 190 Q470 120 530 190 Q500 160 410 190Z" fill="#2b2b2b"/><rect x="60" y="130" width="260" height="22" rx="10" fill="#c3cde6"/><rect x="60" y="175" width="300" height="22" rx="10" fill="#c3cde6"/><rect x="60" y="220" width="240" height="22" rx="10" fill="#c3cde6"/><rect x="60" y="265" width="280" height="22" rx="10" fill="#c3cde6"/>`);
el(s,KTP,'left:240px;top:520px;width:600px;height:380px',59.4-s.a,'pop');
el(s,'Bawa bersama KTP asli','left:70px;top:960px;width:940px;text-align:center;background:#14234b;color:#ffd23f;font-weight:800;font-size:46px;padding:16px 0;border-radius:60px',59.9-s.a,'pop');
// H CTA 61.4-71.81
s=scene(61.4,71.81);
hd(s,'Lanjut belajar <span class=r>SKD</span>',61.55);
el(s,'almahya.id','left:70px;top:430px;background:#ffd23f;font-weight:800;font-size:84px;padding:18px 60px;border-radius:70px',62.9-s.a,'pop');
[['Tryout lengkap + pembahasan',64.52],['Soal sesuai kisi-kisi',66.54],['Paket bundling SKD + SKB + bimbingan online',68.07]].forEach((r,i)=>card(s,`<div style="font-size:32px">${r[0]}</div>`,`left:70px;top:${620+i*190}px;width:500px;height:165px;padding:0 24px`,r[1],['#14234b','#1a8f4c','#c8102e'][i]));
pres(s,'point-up',64.6,71.7,'right:-30px;top:760px',520);
const SUB=[[0,1.04,'Sudah pilih formasi?'],[1.40,3.26,'Jangan salah langkah di tahap berikutnya.'],[3.59,6.73,'Pertama, unggah dokumen sesuai persyaratan instansi.'],[7.07,8.63,'Format PDF atau JPEG,'],[8.95,10.96,'ukuran minimal 80 KB.'],[11.26,14.23,'Surat lamaran dan surat pernyataan wajib bermeterai:'],[14.53,16.68,'pilih e-meterai atau meterai tempel.'],[16.92,20.76,'Kalau persyaratan di SSCASN berbeda dengan pengumuman instansi,'],[20.96,23.56,'lapor dulu ke instansi atau helpdesk BKN.'],[23.88,25.70,'Kedua, buka tab Resume.'],[26.04,28.75,'Periksa semua data dan centang setiap butirnya.'],[29.10,31.68,'Lalu centang pernyataan kebenaran data'],[31.78,33.52,'dan klik Akhiri Proses Pendaftaran.'],[33.85,37.69,'Ingat, setelah diakhiri, data dan berkas tidak bisa diubah.'],[38.04,40.01,'Cetak Kartu Pendaftaran sebagai bukti.'],[40.35,44.04,'Ketiga, pantau hasil seleksi administrasi di halaman Resume.'],[44.28,45.58,'Kalau Tidak Memenuhi Syarat,'],[45.81,47.77,'ajukan sanggah sebelum batas waktu,'],[48.02,49.80,'dengan alasan yang sesuai dokumen.'],[50.11,52.80,'Sanggah bukan untuk memperbaiki salah unggah.'],[53.10,55.12,'Kalau lulus, tunggu jadwal ujian.'],[55.37,59.10,'Kartu Peserta Ujian baru bisa dicetak setelah jadwal ditetapkan.'],[59.40,61.26,'Bawa bersama KTP asli.'],[61.53,64.23,'Lanjut belajar SKD di almahya.id:'],[64.52,66.39,'tryout lengkap dengan pembahasan,'],[66.54,67.95,'soal sesuai kisi-kisi,'],[68.07,69.55,'dan paket bundling'],[69.69,71.61,'SKD + SKB + bimbingan online.']];
