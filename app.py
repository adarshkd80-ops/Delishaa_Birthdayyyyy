from flask import Flask, render_template_string
import json

app = Flask(__name__)

# Load base64 images
with open('images_base64.json', 'r') as f:
    BASE64_IMAGES = json.load(f)

print("Images loaded:")
for key, data in BASE64_IMAGES.items():
    print(f"  ✓ {key}: {len(data)} chars")

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Happy Birthday Delishaaa 💜</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Cinzel+Decorative:wght@400&family=Playfair+Display:ital,wght@0,400;1,400&display=swap" rel="stylesheet">
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  :root{--purple:#9b59b6;--brown:#8b4513;--rose:#e8a0b0;--blush:#f7dce4;--deep:#1a0a12;--gold:#c9a96e}
  body{background:var(--deep);color:var(--blush);font-family:'Cormorant Garamond',serif;min-height:100vh;overflow-x:hidden;cursor:none}
  .cursor{width:10px;height:10px;background:var(--purple);border-radius:50%;position:fixed;pointer-events:none;z-index:9999;transform:translate(-50%,-50%);mix-blend-mode:screen}
  .cursor-trail{width:28px;height:28px;border:2px solid var(--purple);border-radius:50%;position:fixed;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);opacity:0.6}
  canvas#stars{position:fixed;inset:0;z-index:0;pointer-events:none}
  .petal{position:fixed;top:-40px;font-size:1.2rem;opacity:0;animation:fall linear infinite;pointer-events:none;z-index:1}
  @keyframes fall{0%{transform:translateY(0) rotate(0deg);opacity:0.7}100%{transform:translateY(110vh) rotate(360deg);opacity:0}}
  .page-container{position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;width:100%;padding:2rem}
  .page{display:none;opacity:0;transform:translateY(30px);transition:all 0.8s ease;width:100%;max-width:1100px;text-align:center}
  .page.active{display:flex;opacity:1;transform:translateY(0);animation:pageIn 0.8s ease;flex-direction:column;align-items:center;justify-content:center}
  @keyframes pageIn{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
  .progress{position:fixed;top:2rem;right:2rem;font-size:0.9rem;letter-spacing:0.2em;color:var(--gold);z-index:100}
  .step-counter{position:fixed;bottom:2rem;left:2rem;font-size:0.85rem;letter-spacing:0.15em;color:rgba(155,89,182,0.6);z-index:100}
  .nav-buttons{display:flex;gap:1.5rem;justify-content:center;margin-top:2.5rem;flex-wrap:wrap}
  .content-box{background:linear-gradient(135deg,rgba(155,89,182,0.1),rgba(26,10,18,0.4));border:2px solid var(--purple);border-radius:8px;padding:2rem;margin:1.5rem auto;max-width:700px;backdrop-filter:blur(10px)}
  .content-box.alt{background:linear-gradient(135deg,rgba(139,69,19,0.1),rgba(26,10,18,0.4));border:2px solid var(--brown)}
  .content-box.gold{background:linear-gradient(135deg,rgba(201,169,110,0.1),rgba(26,10,18,0.4));border:2px solid var(--gold)}
  .orb{width:220px;height:220px;border-radius:50%;background:radial-gradient(circle at 38% 38%,#f7dce4 0%,var(--purple) 35%,var(--brown) 70%,#1a0a12 100%);box-shadow:0 0 60px 20px rgba(155,89,182,0.3),0 0 120px 40px rgba(139,69,19,0.2);margin-bottom:2rem;animation:pulse 4s ease-in-out infinite,float 6s ease-in-out infinite;cursor:pointer;position:relative}
  .orb::after{content:'💜';position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:4rem;animation:heartbeat 2.4s ease-in-out infinite}
  @keyframes pulse{0%,100%{box-shadow:0 0 60px 20px rgba(155,89,182,0.3),0 0 120px 40px rgba(139,69,19,0.2)}50%{box-shadow:0 0 80px 30px rgba(155,89,182,0.5),0 0 160px 60px rgba(139,69,19,0.3)}}
  @keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
  @keyframes heartbeat{0%,100%{transform:scale(1)}14%{transform:scale(1.18)}28%{transform:scale(1)}42%{transform:scale(1.10)}56%{transform:scale(1)}}
  .title{font-family:'Cinzel Decorative',cursive;font-size:clamp(1.4rem,5vw,2.6rem);letter-spacing:0.12em;color:var(--purple);text-shadow:0 0 30px rgba(155,89,182,0.6);margin-bottom:1rem}
  .subtitle{font-style:italic;font-weight:300;font-size:1.1rem;color:var(--gold);letter-spacing:0.2em;margin-bottom:2rem}
  .message{font-size:1.05rem;line-height:2;color:#f0d8e2;margin:1rem 0;font-style:italic}
  .metric-item{margin:1.5rem 0;text-align:center}
  .metric-label{font-size:0.9rem;letter-spacing:0.2em;color:var(--purple);margin-bottom:0.6rem;text-transform:uppercase;font-weight:600}
  .metric-bar{height:8px;background:rgba(155,89,182,0.2);border-radius:4px;overflow:hidden;margin:0.8rem auto;max-width:400px}
  .metric-fill{height:100%;background:linear-gradient(90deg,var(--purple),var(--brown));border-radius:4px;animation:fillBar 1.5s ease-out forwards}
  @keyframes fillBar{from{width:0%}to{width:100%}}
  .metric-text{font-size:1rem;color:#f0d8e2;font-style:italic}
  .photo-title{font-family:'Cinzel Decorative',cursive;font-size:2rem;color:var(--purple);margin-bottom:1.5rem;letter-spacing:0.1em}
  .photo-gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;max-width:900px;margin:2rem auto;width:100%;justify-items:center}
  .photo-item{width:200px;height:260px;border-radius:8px;overflow:hidden;border:4px solid var(--purple);box-shadow:0 12px 40px rgba(155,89,182,0.5);cursor:pointer;transition:all 0.4s;opacity:0;animation:fadeUp 0.8s ease forwards;transform-style:preserve-3d;perspective:1000px}
  .photo-item:nth-child(1){animation-delay:0.1s}.photo-item:nth-child(2){animation-delay:0.2s}.photo-item:nth-child(3){animation-delay:0.3s}.photo-item:nth-child(4){animation-delay:0.4s}.photo-item:nth-child(5){animation-delay:0.5s}.photo-item:nth-child(6){animation-delay:0.6s}
  .photo-item:hover{transform:scale(1.08) translateY(-10px);box-shadow:0 20px 60px rgba(155,89,182,0.7)}
  .photo-item img{width:100%;height:100%;object-fit:cover;display:block}
  .delishaaa-text{font-family:'Cinzel Decorative',cursive;font-size:clamp(2rem,8vw,4rem);color:var(--purple);text-shadow:0 0 40px rgba(155,89,182,0.8);margin:2rem 0;letter-spacing:0.2em;animation:glow 2s ease-in-out infinite}
  @keyframes glow{0%,100%{text-shadow:0 0 40px rgba(155,89,182,0.8)}50%{text-shadow:0 0 80px rgba(155,89,182,1)}}
  .cake-3d{width:420px;height:420px;margin:2rem auto;position:relative;perspective:1000px;filter:drop-shadow(0 30px 60px rgba(155,89,182,0.6))}
  .cake-image{width:100%;height:100%;border-radius:12px;overflow:hidden;border:5px solid var(--purple);position:relative;display:flex;align-items:center;justify-content:center;transform:rotateX(5deg) rotateY(-5deg) rotateZ(2deg);transition:all 0.4s;background:#000;box-shadow:inset 0 0 40px rgba(155,89,182,0.3),0 20px 60px rgba(155,89,182,0.4)}
  .cake-3d:hover .cake-image{transform:rotateX(8deg) rotateY(-8deg) rotateZ(3deg);box-shadow:inset 0 0 40px rgba(155,89,182,0.5),0 30px 80px rgba(155,89,182,0.6)}
  .cake-image img{width:100%;height:100%;object-fit:cover;position:absolute}
  .candle{position:absolute;top:30px;left:50%;transform:translateX(-50%);width:18px;height:160px;background:linear-gradient(90deg,#fffacd 0%,#fff 50%,#fffacd 100%);border-radius:12px;box-shadow:0 0 30px rgba(255,255,255,0.8),inset -2px 0 4px rgba(0,0,0,0.2);z-index:20}
  .candle::before{content:'';position:absolute;top:0;left:0;right:0;height:30px;background:rgba(255,255,255,0.3);border-radius:12px 12px 0 0}
  .flame{width:24px;height:70px;background:linear-gradient(to top,#ff6b00 0%,#ffd700 50%,#ffff00 100%);position:absolute;top:-70px;left:-3px;border-radius:50% 50% 40% 40%;animation:flicker 0.2s infinite;filter:drop-shadow(0 0 15px #ff6b00) drop-shadow(0 0 8px #ffd700);transform-origin:center bottom}
  .flame::before{content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);width:8px;height:20px;background:rgba(255,255,255,0.6);border-radius:50%;filter:blur(3px)}
  @keyframes flicker{0%{transform:scaleY(1) rotate(0deg)}12%{transform:scaleY(0.95) rotate(-1deg)}25%{transform:scaleY(1.05) rotate(1deg)}37%{transform:scaleY(0.98) rotate(-0.5deg)}50%{transform:scaleY(1.02) rotate(0.5deg)}62%{transform:scaleY(0.96) rotate(-1.5deg)}75%{transform:scaleY(1.03) rotate(1.5deg)}87%{transform:scaleY(0.99) rotate(-0.8deg)}100%{transform:scaleY(1) rotate(0deg)}}
  .blow-instruction{font-size:1.3rem;color:var(--gold);margin-bottom:2rem;letter-spacing:0.1em}
  .blow-btn{background:linear-gradient(135deg,var(--purple),var(--brown));border:none;color:#fff;font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:600;letter-spacing:0.2em;padding:1.1rem 3rem;cursor:pointer;border-radius:6px;transition:all 0.3s;text-transform:uppercase;margin:2rem 0;box-shadow:0 8px 25px rgba(155,89,182,0.4)}
  .blow-btn:hover{transform:scale(1.1);box-shadow:0 12px 40px rgba(155,89,182,0.6)}.blow-btn:active{transform:scale(0.95)}
  .timer{font-size:3.5rem;font-family:'Cinzel Decorative',cursive;color:var(--purple);font-weight:600;text-align:center;margin-bottom:1.5rem;animation:pulse-timer 1s infinite}
  @keyframes pulse-timer{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}
  .timer.blown{animation:none;font-size:2.5rem;color:var(--gold)}
  .wishes-card{max-width:700px;background:linear-gradient(135deg,rgba(155,89,182,0.15),rgba(26,10,18,0.6));border:3px solid var(--purple);border-radius:6px;padding:3rem 2.5rem;backdrop-filter:blur(12px);box-shadow:0 8px 60px rgba(0,0,0,0.6);margin:2rem auto;position:relative}
  .wishes-card::before,.wishes-card::after{content:'✦';position:absolute;color:var(--purple);font-size:1.2rem;opacity:0.8}
  .wishes-card::before{top:1.5rem;left:2rem}.wishes-card::after{bottom:1.5rem;right:2rem}
  .wishes-heading{font-family:'Cinzel Decorative',cursive;font-size:1.8rem;color:var(--purple);margin-bottom:2rem;text-align:center;letter-spacing:0.15em}
  .wishes-poem{font-family:'Playfair Display',serif;font-size:1.15rem;line-height:2.4;color:#f0d8e2;text-align:center;font-style:italic}
  .wishes-poem em{color:var(--gold);font-style:normal;font-weight:600}
  .wishes-divider{display:block;margin:1.5rem auto;width:80px;height:1px;background:linear-gradient(90deg,transparent,var(--purple),transparent);opacity:0.6}
  .forever-message{font-family:'Cinzel Decorative',cursive;font-size:clamp(1.8rem,6vw,3.5rem);color:var(--purple);text-shadow:0 0 50px rgba(155,89,182,0.7);text-align:center;line-height:1.8;max-width:700px;margin:2rem auto}
  .forever-hearts{font-size:3.5rem;margin:2rem 0;animation:bounce 1.5s infinite}
  @keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-20px)}}
  .btn{background:none;border:2px solid var(--purple);color:var(--purple);font-family:'Cormorant Garamond',serif;font-size:1.1rem;letter-spacing:0.25em;padding:0.9rem 2.5rem;cursor:pointer;text-transform:uppercase;transition:all 0.4s;position:relative;overflow:hidden}
  .btn::before{content:'';position:absolute;inset:0;background:var(--purple);transform:scaleX(0);transform-origin:left;transition:transform 0.4s;z-index:-1}
  .btn:hover{color:#fff;transform:scale(1.05)}.btn:hover::before{transform:scaleX(1)}
  .next-btn{display:none}
  .next-btn.show{display:inline-block;background:none;border:2px solid var(--purple);color:var(--purple);font-family:'Cormorant Garamond',serif;font-size:1.1rem;letter-spacing:0.25em;padding:0.9rem 2.5rem;cursor:pointer;text-transform:uppercase;transition:all 0.4s;position:relative;overflow:hidden;margin:0 0.8rem}
  .next-btn.show::before{content:'';position:absolute;inset:0;background:var(--purple);transform:scaleX(0);transform-origin:left;transition:transform 0.4s;z-index:-1}
  .next-btn.show:hover{color:#fff;transform:scale(1.05)}.next-btn.show:hover::before{transform:scaleX(1)}
  .prev-btn{display:inline-block;background:none;border:2px solid var(--brown);color:var(--brown);font-family:'Cormorant Garamond',serif;font-size:1.1rem;letter-spacing:0.25em;padding:0.9rem 2.5rem;cursor:pointer;text-transform:uppercase;transition:all 0.4s;position:relative;overflow:hidden;margin:0 0.8rem}
  .prev-btn::before{content:'';position:absolute;inset:0;background:var(--brown);transform:scaleX(0);transform-origin:right;transition:transform 0.4s;z-index:-1}
  .prev-btn:hover{color:#fff;transform:scale(1.05)}.prev-btn:hover::before{transform:scaleX(1)}
  .music-control{position:fixed;top:2rem;left:2rem;z-index:200;background:rgba(155,89,182,0.2);border:2px solid var(--purple);border-radius:50%;width:50px;height:50px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all 0.3s;font-size:1.5rem}
  .music-control:hover{background:rgba(155,89,182,0.4);transform:scale(1.1)}
  @keyframes fadeUp{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:translateY(0)}}
  @media(max-width:768px){.photo-gallery{grid-template-columns:repeat(2,1fr);gap:1rem}.photo-item{width:130px;height:170px}.cake-3d{width:300px;height:300px}.candle{height:120px;top:20px;width:14px}.blow-btn{font-size:1.1rem;padding:0.9rem 2.2rem}.content-box{padding:1.5rem}}
</style>
</head>
<body>
<div class="cursor" id="cursor"></div>
<div class="cursor-trail" id="trail"></div>
<canvas id="stars"></canvas>

<div class="music-control" id="musicControl" onclick="toggleMusic()" title="Toggle Birthday Music">
  🎵
</div>

<div class="progress" id="progress">STEP 1 / 7</div>
<div class="step-counter" id="stepCounter">━━━━━━━━</div>

<div class="page-container">

  <div class="page active" data-page="1">
    <div class="orb" id="orb"></div>
    <h1 class="title">For You, My Love</h1>
    <p class="subtitle">— written in starlight —</p>
    
    <div class="content-box">
      <div class="message">Every moment with you feels like a dream. Your smile brightens my darkest days, and your presence in my life is the greatest blessing I could ever ask for.</div>
    </div>

    <div class="content-box alt">
      <div class="message">You taught me what true love means. In your eyes, I found my home, my peace, and my forever.</div>
    </div>

    <div class="nav-buttons">
      <button class="btn" onclick="nextPage()">✦ Open My Heart ✦</button>
    </div>
  </div>

  <div class="page" data-page="2">
    <h2 class="title">How Much I Love You</h2>
    
    <div class="content-box">
      <div class="message">My heart belongs entirely to you. Every beat is a reminder of how deeply you mean to me, and how grateful I am to have you in my life.</div>
    </div>
    
    <div class="metric-item" style="margin-top:2rem">
      <div class="metric-label">Devotion Level</div>
      <div class="metric-bar"><div class="metric-fill" style="width:100%"></div></div>
      <div class="metric-text">Beyond infinity</div>
    </div>
    
    <div class="metric-item">
      <div class="metric-label">Heartbeats For You</div>
      <div class="metric-bar"><div class="metric-fill" style="width:100%"></div></div>
      <div class="metric-text">Every single one</div>
    </div>
    
    <div class="metric-item">
      <div class="metric-label">Admiration Quotient</div>
      <div class="metric-bar"><div class="metric-fill" style="width:100%"></div></div>
      <div class="metric-text">Immeasurable depths</div>
    </div>
    
    <div class="metric-item">
      <div class="metric-label">Forever Commitment</div>
      <div class="metric-bar"><div class="metric-fill" style="width:100%"></div></div>
      <div class="metric-text">Until eternity ends</div>
    </div>
    
    <div class="metric-item">
      <div class="metric-label">Soul Connection</div>
      <div class="metric-bar"><div class="metric-fill" style="width:100%"></div></div>
      <div class="metric-text">Eternally intertwined</div>
    </div>

    <div class="content-box gold">
      <div class="message">You are my greatest treasure, my reason to smile every day, and my forever home.</div>
    </div>
    
    <div class="nav-buttons">
      <button class="prev-btn" onclick="prevPage()">← Back</button>
      <button class="btn" onclick="nextPage()">✦ Continue ✦</button>
    </div>
  </div>

  <div class="page" data-page="3">
    <h2 class="photo-title">My Beautiful Moments With You</h2>
    
    <div class="content-box">
      <div class="message">These are my favorite memories with you — moments frozen in time that I'll cherish forever. Each photo captures a piece of my heart with you.</div>
    </div>

    <div class="photo-gallery" id="photoGallery"></div>

    <div class="content-box alt">
      <div class="message">Looking at your smile in these photos reminds me why I fall in love with you every single day. You are my greatest adventure.</div>
    </div>
    
    <div class="nav-buttons">
      <button class="prev-btn" onclick="prevPage()">← Back</button>
      <button class="btn" onclick="nextPage()">✦ Next ✦</button>
    </div>
  </div>

  <div class="page" data-page="4">
    <div class="delishaaa-text">For You<br>My Delishaaa 💜</div>
    
    <div class="content-box">
      <div class="message">You are my greatest blessing, my truest love, and the reason my heart feels so full. Today we celebrate you and the incredible joy you bring to my world.</div>
    </div>

    <div class="content-box gold">
      <div class="message">Happy Birthday to the most beautiful soul I know. May your day be filled with as much love as you give to everyone around you.</div>
    </div>

    <div class="content-box alt">
      <div class="message">You deserve every happiness, every dream come true, and endless moments of pure joy. Thank you for being you, for being mine.</div>
    </div>

    <div class="nav-buttons">
      <button class="prev-btn" onclick="prevPage()">← Back</button>
      <button class="btn" onclick="nextPage()">Let's Celebrate 🎉</button>
    </div>
  </div>

  <div class="page" data-page="5">
    <h2 class="title">Make A Wish</h2>
    
    <div class="content-box">
      <div class="message">Blow out this candle and make a wish, my love. I wish for countless tomorrows with you, endless moments of laughter, and a lifetime of love.</div>
    </div>

    <div class="timer" id="timer">Make a Wish!</div>
    <div class="blow-instruction">🎂 Blow out the candle & make your wish! 💜</div>
    <button class="blow-btn" onclick="blowCandle()">💨 Blow Candle! 🎉</button>
    
    <div class="cake-3d">
      <div class="cake-image" id="cakeImage">
        <div class="candle">
          <div class="flame" id="flame"></div>
        </div>
      </div>
    </div>

    <div class="content-box gold">
      <div class="message">Make a wish that brings you everything your heart desires. I wish for your dreams to come true and for our love to grow stronger every day.</div>
    </div>
    
    <div class="nav-buttons">
      <button class="prev-btn" onclick="prevPage()">← Back</button>
      <button class="next-btn" id="nextAfterCandle" onclick="nextPage()">✦ Continue ✦</button>
    </div>
  </div>

  <div class="page" data-page="6">
    <div class="wishes-card">
      <h2 class="wishes-heading">Birthday Wishes For My Love</h2>
      <p class="wishes-poem">
        On this most auspicious day,<br>
        When the heavens did ordain,<br>
        <em>Thy radiant presence graced our world</em>,<br>
        <span class="wishes-divider"></span>
        I wish for thee endless joy and boundless love,<br>
        For thy heart to be filled with dreams come true,<br>
        And for our souls to dance through eternity together.<br>
        <em>Thou art my greatest gift, my truest treasure</em>,<br>
        The reason my world is painted in colors of happiness.<br>
        <span class="wishes-divider"></span>
        May every moment of thy life be as beautiful as thy smile,<br>
        As precious as thy love, and as eternal as my devotion.<br>
        <em>Happy Birthday to the one who holds my heart.</em>
      </p>
    </div>

    <div class="content-box">
      <div class="message">You bring out the best in me. You make me braver, kinder, and more alive. With you, I've found my soulmate and my best friend.</div>
    </div>

    <div class="nav-buttons">
      <button class="prev-btn" onclick="prevPage()">← Back</button>
      <button class="btn" onclick="nextPage()">✦ Finally ✦</button>
    </div>
  </div>

  <div class="page" data-page="7">
    <h1 class="forever-message">
      I Love You<br>
      <em>Forever & Always</em>
    </h1>
    <div class="forever-hearts">💜 💜 💜</div>
    
    <div class="content-box">
      <div class="message">You are my greatest adventure, my favorite person, and my forever love. Thank you for being the most incredible part of my story. Happy Birthday, my Delishaaa!</div>
    </div>

    <div class="content-box gold">
      <div class="message">I love you with all of my heart, today and always. You make every day feel like a celebration just by being in it. Thank you for making life beautiful.</div>
    </div>

    <div class="content-box alt">
      <div class="message">Here's to you, to us, and to a lifetime of love, laughter, and endless adventures together. You are my everything. 💜</div>
    </div>

    <p style="font-size:1.2rem;margin-top:2rem;color:var(--gold);letter-spacing:0.15em">💜 Happy Birthday, My Love 💜</p>
    
    <div class="nav-buttons">
      <button class="prev-btn" onclick="prevPage()">← Back</button>
    </div>
  </div>

</div>

<audio id="bgMusic" loop style="display:none;">
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3" type="audio/mpeg">
</audio>

<script>
const IMAGES = """ + str(BASE64_IMAGES).replace("'", '"') + """;
let currentPage=1,totalPages=7,candleBlown=false,musicPlaying=false;

console.log('Images loaded:', Object.keys(IMAGES).length);

const cursor=document.getElementById('cursor'),trail=document.getElementById('trail');
document.addEventListener('mousemove',e=>{cursor.style.left=e.clientX+'px';cursor.style.top=e.clientY+'px';setTimeout(()=>{trail.style.left=e.clientX+'px';trail.style.top=e.clientY+'px'},80)});

const canvas=document.getElementById('stars'),ctx=canvas.getContext('2d');
let stars=[];
function resizeCanvas(){canvas.width=window.innerWidth;canvas.height=window.innerHeight}
function initStars(){stars=[];for(let i=0;i<160;i++)stars.push({x:Math.random()*canvas.width,y:Math.random()*canvas.height,r:Math.random()*1.4+0.2,a:Math.random(),speed:Math.random()*0.008+0.002,phase:Math.random()*Math.PI*2})}
function drawStars(t){ctx.clearRect(0,0,canvas.width,canvas.height);stars.forEach(s=>{const alpha=(Math.sin(t*s.speed+s.phase)+1)/2*0.8+0.1;ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,Math.PI*2);ctx.fillStyle=`rgba(247,220,228,${alpha})`;ctx.fill()});requestAnimationFrame(drawStars)}
resizeCanvas();initStars();requestAnimationFrame(drawStars);
window.addEventListener('resize',()=>{resizeCanvas();initStars()});

const petalSymbols=['🌸','✿','❀','🌺','✾'];
function spawnPetal(){const p=document.createElement('div');p.className='petal';p.textContent=petalSymbols[Math.floor(Math.random()*petalSymbols.length)];p.style.left=Math.random()*100+'vw';const dur=Math.random()*8+7;p.style.animationDuration=dur+'s';p.style.animationDelay=Math.random()*4+'s';p.style.fontSize=(Math.random()*1+0.8)+'rem';document.body.appendChild(p);setTimeout(()=>p.remove(),(dur+4)*1000)}
setInterval(spawnPetal,1200);
document.getElementById('orb').addEventListener('click',()=>{for(let i=0;i<8;i++)spawnPetal()});

function loadPhotos(){const gallery=document.getElementById('photoGallery');const photos=['photo1','photo2','photo3','photo4','photo5','photo6'];photos.forEach((photo,idx)=>{const item=document.createElement('div');item.className='photo-item';const img=document.createElement('img');img.src=`data:image/jpeg;base64,${IMAGES[photo]}`;img.alt=`Photo ${idx+1}`;item.appendChild(img);gallery.appendChild(item);console.log(`✓ Photo ${idx+1} created`)})}

function loadCake(){const cake=document.getElementById('cakeImage');const img=document.createElement('img');img.src=`data:image/jpeg;base64,${IMAGES.cake}`;cake.appendChild(img);console.log('✓ Cake image loaded')}

function nextPage(){if(currentPage===5&&!candleBlown){alert('Please blow out the candle first! 🎂');return}if(currentPage<totalPages){const current=document.querySelector(`.page[data-page="${currentPage}"]`);current.classList.remove('active');currentPage++;const next=document.querySelector(`.page[data-page="${currentPage}"]`);next.classList.add('active');updateProgress();window.scrollTo(0,0)}}

function prevPage(){if(currentPage>1){const current=document.querySelector(`.page[data-page="${currentPage}"]`);current.classList.remove('active');currentPage--;const next=document.querySelector(`.page[data-page="${currentPage}"]`);next.classList.add('active');updateProgress();window.scrollTo(0,0)}}

function updateProgress(){document.getElementById('progress').textContent=`STEP ${currentPage} / ${totalPages}`;const bars='━'.repeat(currentPage)+'━'.repeat(totalPages-currentPage);document.getElementById('stepCounter').textContent=bars}

function blowCandle(){if(candleBlown)return;candleBlown=true;const flame=document.getElementById('flame');flame.style.animation='none';flame.style.opacity='0';setTimeout(()=>{flame.style.opacity='0';flame.style.transition='opacity 0.5s ease-out';document.getElementById('timer').textContent='Your Wish is Made! ✨';document.getElementById('timer').classList.add('blown');document.getElementById('nextAfterCandle').classList.add('show');for(let i=0;i<25;i++)spawnPetal()},300)}

function toggleMusic(){const audio=document.getElementById('bgMusic');const control=document.getElementById('musicControl');if(musicPlaying){audio.pause();control.textContent='🔇';musicPlaying=false}else{audio.play().catch(e=>console.log('Music paused'));control.textContent='🔊';musicPlaying=true}}

loadPhotos();
loadCake();
updateProgress();
console.log('✓ Delishaaa Birthday Website Loaded!');
</script>
</body>
</html>"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🎂 Happy Birthday Delishaaa! 💜")
    print("="*60)
    print("📱 Open: http://localhost:5000")
    print("🎵 Slow Piano Music - Click to toggle!")
    print("="*60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
