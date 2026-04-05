import re

auth_file = 'auth.html'
sites_file = 'sites.html'

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update css root variables to immersive Nile Night
    root_old = r":root\{[^\}]+\}"
    root_new = """:root{
  --gold:#EAB308;
  --gold-b:#FBBF24;
  --gold-dim:rgba(234, 179, 8, .2);
  --teal:#0D9488;
  --dark:#090A0F;
  --dark2:#0F121C;
  --sand:#D4D4D8;
  --papyrus:#FEF3C7;
  --card-bg:rgba(15, 18, 28, .65);
  --fn-d:'Cinzel Decorative',cursive;
  --fn-h:'Cinzel',serif;
  --fn-b:'Crimson Text',serif;
}"""
    content = re.sub(root_old, root_new, content)

    # 2. Fix UI classes
    content = re.sub(r'background:rgba\(230,220,195,\.7\);', 'background:rgba(15, 18, 28, .5);', content)
    content = re.sub(r'color:rgba\(62,43,30,\.5\);', 'color:rgba(212, 212, 216, .5);', content)
    content = re.sub(r'border:1px solid rgba\(192,138,27,\.18\);', 'border:1px solid rgba(234, 179, 8, .15);', content)
    content = re.sub(r'border-color:rgba\(192,138,27,\.32\);', 'border-color:rgba(234, 179, 8, .3);', content)
    content = re.sub(r'color:rgba\(62,43,30,\.8\);', 'color:#D4D4D8;', content)
    
    # Cards
    content = re.sub(r'border:1px solid rgba\(192,138,27,\.25\);', 'border:1px solid rgba(234, 179, 8, .2); border-top:1px solid rgba(234, 179, 8, .4);', content)
    content = re.sub(r'box-shadow:0 28px 80px rgba\(62,43,30,\.1\),inset 0 0 60px rgba\(255,255,255,\.6\);', 'box-shadow:0 28px 80px rgba(0,0,0,.6),inset 0 1px 20px rgba(234, 179, 8, .1);', content)
    content = re.sub(r'color:rgba\(192,138,27,\.52\);', 'color:rgba(234, 179, 8, .5);', content)
    content = re.sub(r'color:rgba\(192,138,27,\.4\);', 'color:rgba(234, 179, 8, .3);', content)
    
    # Inputs
    content = re.sub(r'color:rgba\(62,43,30,\.7\);', 'color:rgba(212, 212, 216, .7);', content)
    content = re.sub(r'border-bottom:1px solid rgba\(192,138,27,\.25\);', 'border-bottom:1px solid rgba(234, 179, 8, .25);', content)
    content = re.sub(r'color:rgba\(62,43,30,\.3\);', 'color:rgba(212, 212, 216, .3);', content)
    
    # Button
    content = re.sub(r'background:linear-gradient\(135deg,#D3A766 0%,#FBE9B6 45%,#D3A766 100%\);', 'background:linear-gradient(135deg,#92400E 0%,#EAB308 50%,#B45309 100%);', content)
    content = re.sub(r'color:#2A1D13;', 'color:#000000;', content)
    content = re.sub(r'box-shadow:0 0 25px rgba\(192,138,27,\.2\),0 4px 15px rgba\(62,43,30,\.1\);', 'box-shadow:0 0 30px rgba(234, 179, 8, .3),0 4px 20px rgba(0,0,0,.5);', content)
    content = re.sub(r'background:linear-gradient\(to right,transparent,rgba\(255,255,255,\.5\),transparent\);', 'background:linear-gradient(to right,transparent,rgba(255,255,255,.2),transparent);', content)
    
    # Secondary btn
    content = re.sub(r'border:1px solid rgba\(192,138,27,\.3\);', 'border:1px solid rgba(234, 179, 8, .3);', content)
    content = re.sub(r'color:rgba\(62,43,30,\.6\);', 'color:rgba(234, 179, 8, .6);', content)

    # Scrolly
    content = re.sub(r'background:rgba\(192,138,27,\.3\)', 'background:rgba(234, 179, 8, .3)', content)

    # 3. Canvas JS replacement
    canvas_old = r"function drawBg\(\)\{.*?requestAnimationFrame\(drawBg\);\n\}"
    canvas_new = """function drawBg(){
  ctx.clearRect(0,0,W,H);
  // Deep immersive night sky
  const bg=ctx.createLinearGradient(0,0,0,H);
  bg.addColorStop(0,'#050814'); // ultra dark blue
  bg.addColorStop(.5,'#0B132B'); // deep blue
  bg.addColorStop(1,'#1C162A'); // warm deep violet horizon
  ctx.fillStyle=bg;ctx.fillRect(0,0,W,H);
  
  // Milky way glow
  const mw=ctx.createLinearGradient(0,0,W,H);
  mw.addColorStop(0,'rgba(234,179,8,0.01)');
  mw.addColorStop(0.5,'rgba(13,148,136,0.03)');
  mw.addColorStop(1,'rgba(234,179,8,0.01)');
  ctx.fillStyle=mw;ctx.fillRect(0,0,W,H);

  stars.forEach(s=>{
    s.tw+=s.ts;
    const a=s.a*(.4+.6*Math.sin(s.tw));
    ctx.beginPath();ctx.arc(s.x*W,s.y*H,s.r,0,Math.PI*2);
    // Silver/blue tint for stars
    ctx.fillStyle=`rgba(226,232,240,${a})`;ctx.fill();
  });
  
  // Magical fireflies/embers drifting up
  golds.forEach((p,i)=>{
    p.y+=p.vy;p.x+=p.vx;
    // adding a bit of wave motion
    p.x += Math.sin(p.life * 20) * 0.0003;
    p.life+=.0015;
    if(p.y<-.05||p.life>p.max){Object.assign(golds[i],mkP());return}
    const a=Math.sin(p.life/p.max*Math.PI)*.8;
    ctx.beginPath();ctx.arc(p.x*W,p.y*H,p.r,0,Math.PI*2);
    ctx.fillStyle=`rgba(234,179,8,${a})`;
    ctx.shadowBlur = 10;
    ctx.shadowColor = 'rgba(234,179,8,1)';
    ctx.fill();
    ctx.shadowBlur = 0;
  });
  
  // Whispering hieroglyphs
  fGlyphs.forEach(g=>{
    g.y+=g.vy;g.t+=.002;
    if(g.ph==='in'){g.op=Math.min(g.op+.001,g.top);if(g.t>.5)g.ph='out'}
    else{g.op=Math.max(0,g.op-.001);
      if(g.op<=0){g.x=Math.random();g.y=.1+Math.random()*.7;g.c=glyphs[Math.floor(Math.random()*glyphs.length)];g.t=0;g.ph='in';g.top=Math.random()*.08+.02}
    }
    if(g.op>0){
      ctx.save();ctx.globalAlpha=g.op;
      ctx.fillStyle='#EAB308';
      ctx.shadowBlur = 15; ctx.shadowColor = 'rgba(234,179,8,0.5)';
      ctx.font=`${g.sz}px serif`;ctx.fillText(g.c,g.x*W,g.y*H);
      ctx.restore();
    }
  });
  
  // Fog at the bottom
  const fog=ctx.createLinearGradient(0,H*.7,0,H);
  fog.addColorStop(0,'transparent');
  fog.addColorStop(1,'rgba(9,10,15,0.8)');
  ctx.fillStyle=fog;ctx.fillRect(0,H*.7,W,H*.3);

  requestAnimationFrame(drawBg);
}"""
    content = re.sub(canvas_old, canvas_new, content, flags=re.DOTALL)

    # 4. Auth-specific fixes: Moon & Pyramids
    if "auth.html" in filepath:
        # Revert Moon to magical glowing crescent or full moon
        moon_old = r"\.moon\{[^\}]+\}\n@keyframes moonPulse\{[^\}]+\}"
        moon_new = """.moon{
  position:fixed;top:10%;right:15%;
  width:90px;height:90px;border-radius:50%;
  background:radial-gradient(circle at 35% 35%, #FEF3C7, #FDE68A 30%, #D97706 80%, #78350F 100%);
  box-shadow:0 0 60px rgba(234,179,8,.2),0 0 120px rgba(217,119,6,.15);
  z-index:1;pointer-events:none;
  animation:moonPulse 6s ease-in-out infinite;
}
@keyframes moonPulse{
  0%,100%{box-shadow:0 0 60px rgba(234,179,8,.2),0 0 120px rgba(217,119,6,.15), inset 0 0 20px rgba(254,243,199,0.5)}
  50%{box-shadow:0 0 80px rgba(234,179,8,.35),0 0 160px rgba(217,119,6,.2), inset 0 0 30px rgba(254,243,199,0.8)}
}"""
        content = re.sub(moon_old, moon_new, content)

        # Pyramids to mystical deep blues
        svg_old = r"""<polygon points="340,4 55,248 625,248" fill="#D3A766"/>.+</svg>"""
        svg_new = """<polygon points="340,4 55,248 625,248" fill="#0A0D15"/>
  <polygon points="340,4 625,248 340,248" fill="#121626"/>
  <polygon points="900,52 695,248 1105,248" fill="#0D111A"/>
  <polygon points="900,52 1105,248 900,248" fill="#151A2D"/>
  <polygon points="1295,128 1208,248 1380,248" fill="#0F131E"/>
  <polygon points="1295,128 1380,248 1295,248" fill="#1A1E33"/>
  <path d="M 625 248 Q 640 230 665 238 Q 680 224 700 235 Q 718 220 736 233 Q 748 224 760 236 L 768 248 Z" fill="#07090F"/>
  <path d="M 0 248 Q 200 238 350 248 Q 500 255 700 248 Q 900 242 1100 248 Q 1300 254 1440 248 L 1440 280 L 0 280 Z" fill="#090A0F" opacity="0.9"/>
  <!-- Magical edge highlights -->
  <line x1="340" y1="6" x2="340" y2="246" stroke="rgba(234,179,8,0.15)" stroke-width="2" filter="url(#blur2)"/>
  <line x1="900" y1="54" x2="900" y2="246" stroke="rgba(234,179,8,0.1)" stroke-width="1.5" filter="url(#blur2)"/>
</svg>"""
        content = re.sub(svg_old, svg_new, content, flags=re.DOTALL)
        content = content.replace('fill="#DDBA84"', 'fill="#090A0F"') # ground replace
        
        # text shadows
        content = content.replace('text-shadow:0 8px 30px rgba(62,43,30,.15), 0 0 50px rgba(192,138,27,.25)', 'text-shadow:0 0 40px rgba(234,179,8,.4), 0 0 80px rgba(217,119,6,.2)')
        content = content.replace('text-shadow:0 12px 40px rgba(62,43,30,.2), 0 0 80px rgba(192,138,27,.35)', 'text-shadow:0 0 60px rgba(234,179,8,.6), 0 0 120px rgba(217,119,6,.3)')
        content = content.replace('color:rgba(192,138,27,.9)', 'color:rgba(234,179,8,.7)')
        content = content.replace('text-shadow:0 4px 15px rgba(62,43,30,.1)', 'text-shadow:0 0 20px rgba(254,243,199,.2)')
        content = content.replace('border:2px solid rgba(62,43,30,.2);border-top-color:var(--sand);', 'border:2px solid rgba(234,179,8,.2);border-top-color:var(--gold);')

    if "sites.html" in filepath:
        content = content.replace('background:rgba(253,251,247,.92)', 'background:rgba(9,10,15,.8)')
        content = content.replace('border-bottom:1px solid rgba(192,138,27,.18)', 'border-bottom:1px solid rgba(234,179,8,.15)')
        content = content.replace('color:rgba(62,43,30,.7)', 'color:rgba(212,212,216,.7)')
        content = content.replace('text-shadow:0 4px 10px rgba(192,138,27,.2)', 'text-shadow:0 0 20px rgba(234,179,8,.3)')
        content = content.replace('border:1px solid rgba(192,138,27,.26)', 'border:1px solid rgba(234,179,8,.25)')
        content = content.replace('text-shadow:0 8px 25px rgba(192,138,27,.25)', 'text-shadow:0 0 40px rgba(234,179,8,.3)')
        content = content.replace('background:linear-gradient(to right,transparent,rgba(192,138,27,.4))', 'background:linear-gradient(to right,transparent,rgba(234,179,8,.3))')
        content = content.replace('background:linear-gradient(to left,transparent,rgba(192,138,27,.4))', 'background:linear-gradient(to left,transparent,rgba(234,179,8,.3))')
        content = content.replace('color:rgba(192,138,27,.6)', 'color:rgba(234,179,8,.5)')
        content = content.replace('border:1px solid rgba(192,138,27,.2)', 'border:1px solid rgba(234,179,8,.15)')
        content = content.replace('border-color:rgba(192,138,27,.48)', 'border-color:rgba(234,179,8,.5)')
        content = content.replace('box-shadow:0 24px 50px rgba(62,43,30,.15),0 0 30px rgba(192,138,27,.15),inset 0 0 0 1px rgba(192,138,27,.2)', 'box-shadow:0 24px 70px rgba(0,0,0,.7),0 0 40px rgba(234,179,8,.15),inset 0 0 0 1px rgba(234,179,8,.1)')
        content = content.replace('filter:brightness(.95) saturate(1.1)', 'filter:brightness(.8) saturate(1.2)')
        content = content.replace('filter:brightness(1.05) saturate(1.25)', 'filter:brightness(1.1) saturate(1.3)')
        content = content.replace('background:linear-gradient(to top,\n    rgba(253,251,247,.95) 0%,\n    rgba(253,251,247,.75) 35%,\n    rgba(253,251,247,0) 65%,\n    transparent 100%)', 'background:linear-gradient(to top, rgba(9,10,15,1) 0%, rgba(9,10,15,.8) 40%, rgba(9,10,15,.2) 70%, transparent 100%)')
        content = content.replace('background:linear-gradient(to top,\n    rgba(253,251,247,.98) 0%,\n    rgba(253,251,247,.85) 40%,\n    rgba(253,251,247,0) 70%,\n    transparent 100%)', 'background:linear-gradient(to top, rgba(9,10,15,1) 0%, rgba(9,10,15,.9) 45%, rgba(9,10,15,.3) 75%, transparent 100%)')
        content = content.replace('background:rgba(253,251,247,.9)', 'background:rgba(15,18,28,.8)')
        content = content.replace('border:1px solid rgba(192,138,27,.32)', 'border:1px solid rgba(234,179,8,.3)')
        content = content.replace('border:1px solid rgba(192,138,27,.38)', 'border:1px solid rgba(234,179,8,.4)')
        content = content.replace('background:rgba(255,255,255,.6)', 'background:rgba(234,179,8,.2)')
        content = content.replace('border-top:1px solid rgba(192,138,27,.18)', 'border-top:1px solid rgba(234,179,8,.15)')
        content = content.replace('color:rgba(192,138,27,.4)', 'color:rgba(234,179,8,.3)')
        content = content.replace('color:rgba(62,43,30,.6)', 'color:rgba(212,212,216,.5)')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file(auth_file)
update_file(sites_file)

print("Updated perfectly to the immersive Nile night theme!")
