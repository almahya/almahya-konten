// Presenter almahya (karakter orisinal). presenter(pose, t, talk) -> string SVG (viewBox 0 0 600 700)
function presenter(pose,t,talk){
 t=t||0;const NAVY='#14234b',RED='#c8102e',SKIN='#f0c39b',SKIN2='#d9a57c',HAIR='#1d1a2b';
 const L=[205,478],R=[395,478];
 const P={
  idle:{l:[[182,585],[188,672]],r:[[418,585],[412,672]]},
  wave:{l:[[182,585],[188,672]],r:[[478,470],[500+34*Math.sin(t*9),335]]},
  point:{l:[[182,585],[188,672]],r:[[470,505],[538,462]]},
  warning:{l:[[182,585],[188,672]],r:[[480,505],[478,360]]},
  thumbs:{l:[[182,585],[188,672]],r:[[455,545],[445,470]]},
  explain:{l:[[140,545],[108,478]],r:[[460,545],[492,478]]}
 }[pose]||{};
 const bob=3*Math.sin(2*Math.PI*t/3.2),mo=talk?(0.3+0.7*Math.abs(Math.sin(t*9))):0;
 const blink=(t%3.4)>3.28?0.1:1;
 let o='';
 const arm=(S,a,flip)=>{const E=a[0],H=a[1];let s=`<path d="M${S[0]} ${S[1]} L${E[0]} ${E[1]} L${H[0]} ${H[1]}" stroke="#22408f" stroke-width="58" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`;
  const big=(pose=='warning'&&!flip)?34:27;s+=`<circle cx="${H[0]}" cy="${H[1]}" r="${big}" fill="${SKIN}"/>`;
  if(pose=='thumbs'&&!flip)s+=`<circle cx="${H[0]}" cy="${H[1]}" r="33" fill="${SKIN}"/><ellipse cx="${H[0]-6}" cy="${H[1]-44}" rx="15" ry="30" fill="${SKIN}" transform="rotate(-12 ${H[0]} ${H[1]-44})"/><path d="M${H[0]-16} ${H[1]+6} H${H[0]+26} M${H[0]-16} ${H[1]+18} H${H[0]+24}" stroke="${SKIN2}" stroke-width="4" stroke-linecap="round"/>`;
  if(pose=='point'&&!flip)s+=`<rect x="${H[0]+8}" y="${H[1]-10}" width="46" height="19" rx="9" fill="${SKIN}" transform="rotate(-14 ${H[0]} ${H[1]})"/>`;
  return s};
 o+=`<g transform="translate(0,${bob})">`;
 // torso
 o+=`<path d="M135 700 Q140 520 200 450 Q300 420 400 450 Q460 520 465 700 Z" fill="${NAVY}"/>`;
 o+=`<rect x="272" y="372" width="56" height="80" rx="20" fill="${SKIN2}"/>`;
 o+=`<polygon points="262,440 300,500 338,440 320,432 300,452 280,432" fill="#fff"/>`;
 o+=`<polygon points="292,484 308,484 316,572 300,590 284,572" fill="${RED}"/><polygon points="288,470 312,470 308,486 292,486" fill="#a30d25"/>`;
 // arms
 o+=arm(L,P.l,true)+arm(R,P.r,false);
 // head
 o+=`<g transform="rotate(${talk?2*Math.sin(t*5):0} 300 400)">`;
 o+=`<circle cx="206" cy="300" r="20" fill="${SKIN}"/><circle cx="394" cy="300" r="20" fill="${SKIN}"/>`;
 o+=`<ellipse cx="300" cy="292" rx="96" ry="108" fill="${SKIN}"/>`;
 o+=`<path d="M203 290 Q196 170 300 168 Q404 170 397 290 Q388 226 300 222 Q212 226 203 290 Z" fill="${HAIR}"/>`;
 const brow=pose=='warning'?`<path d="M240 258 L282 270" stroke="${HAIR}" stroke-width="8" stroke-linecap="round"/><path d="M360 258 L318 270" stroke="${HAIR}" stroke-width="8" stroke-linecap="round"/>`:`<path d="M240 266 Q262 254 284 264" stroke="${HAIR}" stroke-width="8" stroke-linecap="round" fill="none"/><path d="M360 266 Q338 254 316 264" stroke="${HAIR}" stroke-width="8" stroke-linecap="round" fill="none"/>`;
 o+=brow;
 o+=`<ellipse cx="262" cy="296" rx="11" ry="${13*blink}" fill="${HAIR}"/><ellipse cx="338" cy="296" rx="11" ry="${13*blink}" fill="${HAIR}"/>`;
 o+=`<circle cx="266" cy="291" r="4" fill="#fff" opacity="${blink>0.5?1:0}"/><circle cx="342" cy="291" r="4" fill="#fff" opacity="${blink>0.5?1:0}"/>`;
 o+=`<ellipse cx="236" cy="334" rx="16" ry="9" fill="#f2a08f" opacity=".5"/><ellipse cx="364" cy="334" rx="16" ry="9" fill="#f2a08f" opacity=".5"/>`;
 if(pose=='warning'){o+=`<ellipse cx="300" cy="352" rx="16" ry="${10+8*mo}" fill="#7a2230"/>`}
 else if(talk){o+=`<path d="M268 340 Q300 ${344+34*mo} 332 340 Q300 ${338+4*mo} 268 340 Z" fill="#7a2230"/><path d="M276 342 Q300 ${346+10*mo} 324 342 Z" fill="#fff" opacity=".9"/>`}
 else{o+=`<path d="M270 340 Q300 366 330 340" stroke="#7a2230" stroke-width="7" stroke-linecap="round" fill="none"/>`}
 o+=`</g></g>`;
 return `<svg viewBox="0 0 600 700" xmlns="http://www.w3.org/2000/svg">${o}</svg>`}
if(typeof module!=='undefined')module.exports=presenter;
