<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Kavindu Oshadha Perera — Elite Profile</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@400;600;700&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --green: #00ff9d;
      --blue: #00b8ff;
      --red: #ff4c6e;
      --amber: #ffcc44;
      --purple: #b088ff;
      --bg: #050a0e;
      --bg2: #060d0a;
      --text: #c8d6df;
      --muted: #7a9aaa;
      --dim: #3a6b57;
    }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Share Tech Mono', monospace;
      min-height: 100vh;
      position: relative;
      overflow-x: hidden;
    }

    /* ── BACKGROUND LAYERS ── */
    .scanline {
      position: fixed;
      inset: 0;
      background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0,255,180,0.012) 2px,
        rgba(0,255,180,0.012) 4px
      );
      pointer-events: none;
      z-index: 999;
    }

    .grid-bg {
      position: fixed;
      inset: 0;
      background-image:
        linear-gradient(rgba(0,255,157,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,255,157,0.03) 1px, transparent 1px);
      background-size: 40px 40px;
      pointer-events: none;
      z-index: 0;
    }

    /* ── LAYOUT ── */
    .content {
      position: relative;
      z-index: 1;
      max-width: 900px;
      margin: 0 auto;
      padding: 32px 24px 48px;
      animation: fadeUp 0.6s ease-out both;
    }

    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(16px); }
      to   { opacity: 1; transform: none; }
    }

    /* ── BOOT BLOCK ── */
    .boot-block {
      border: 1px solid rgba(0,255,157,0.2);
      background: var(--bg2);
      border-radius: 4px;
      padding: 22px 28px;
      margin-bottom: 32px;
      position: relative;
    }

    .boot-block::before {
      content: 'BOOT_SEQUENCE.SH';
      position: absolute;
      top: -10px; left: 16px;
      background: var(--bg);
      color: var(--green);
      font-size: 11px;
      padding: 0 8px;
      letter-spacing: 2px;
    }

    .boot-line {
      font-size: 13px;
      line-height: 1.9;
    }

    .boot-line .ok     { color: #0aff7a; }
    .boot-line .dim    { color: var(--dim); }
    .boot-line .prompt { color: var(--blue); }
    .boot-line .danger { color: var(--red); }

    .cursor {
      display: inline-block;
      width: 8px; height: 14px;
      background: var(--green);
      vertical-align: middle;
      animation: blink 1s step-end infinite;
    }

    @keyframes blink { 50% { opacity: 0; } }

    /* ── HERO ── */
    .hero {
      display: flex;
      align-items: flex-start;
      gap: 32px;
      margin-bottom: 32px;
      flex-wrap: wrap;
    }

    .avatar-wrap { flex-shrink: 0; }

    .avatar {
      width: 116px; height: 116px;
      border-radius: 50%;
      background: rgba(0,255,157,0.04);
      border: 2px solid var(--green);
      display: flex; align-items: center; justify-content: center;
      font-family: 'Orbitron', monospace;
      font-size: 30px;
      font-weight: 900;
      color: var(--green);
      position: relative;
      animation: pulse-avatar 3s ease-in-out infinite;
    }

    @keyframes pulse-avatar {
      0%, 100% { box-shadow: 0 0 0 4px rgba(0,255,157,0.08), 0 0 0 10px rgba(0,255,157,0.04); }
      50%       { box-shadow: 0 0 0 8px rgba(0,255,157,0.14), 0 0 0 18px rgba(0,255,157,0.06); }
    }

    .avatar-dot {
      position: absolute;
      bottom: 8px; right: 8px;
      width: 13px; height: 13px;
      background: #0aff7a;
      border-radius: 50%;
      border: 2px solid var(--bg);
      animation: pulse-dot 2s ease-in-out infinite;
    }

    @keyframes pulse-dot { 0%,100%{opacity:1} 50%{opacity:0.35} }

    .hero-info { flex: 1; min-width: 220px; }

    .name {
      font-family: 'Orbitron', monospace;
      font-size: 22px;
      font-weight: 900;
      color: #fff;
      letter-spacing: 1px;
      margin-bottom: 4px;
      text-shadow: 0 0 40px rgba(0,255,157,0.25);
    }

    .handle {
      color: var(--green);
      font-size: 12px;
      letter-spacing: 3px;
      margin-bottom: 14px;
    }

    .tag-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 16px;
    }

    .tag {
      font-size: 10px;
      padding: 3px 11px;
      border-radius: 2px;
      letter-spacing: 1.5px;
    }

    .tag-green  { background: rgba(0,255,157,0.07); color: var(--green);  border: 1px solid rgba(0,255,157,0.25); }
    .tag-blue   { background: rgba(0,184,255,0.07); color: var(--blue);   border: 1px solid rgba(0,184,255,0.25); }
    .tag-amber  { background: rgba(255,204,68,0.07); color: var(--amber); border: 1px solid rgba(255,204,68,0.25); }
    .tag-red    { background: rgba(255,76,110,0.07); color: var(--red);   border: 1px solid rgba(255,76,110,0.25); }

    .bio {
      font-size: 13px;
      color: var(--muted);
      line-height: 1.75;
      border-left: 2px solid rgba(0,255,157,0.2);
      padding-left: 14px;
    }

    .bio .hl { color: var(--green); }

    /* ── DIVIDER ── */
    .divider {
      border: none;
      border-top: 1px solid rgba(0,255,157,0.1);
      margin: 28px 0;
      position: relative;
    }

    .divider::after {
      content: '//';
      position: absolute;
      top: -10px; left: 50%; transform: translateX(-50%);
      background: var(--bg);
      color: rgba(0,255,157,0.2);
      padding: 0 14px;
      font-size: 12px;
      letter-spacing: 4px;
    }

    /* ── SECTION LABEL ── */
    .section-label {
      font-family: 'Orbitron', monospace;
      font-size: 10px;
      color: var(--blue);
      letter-spacing: 4px;
      text-transform: uppercase;
      margin-bottom: 18px;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .section-label::after {
      content: '';
      flex: 1;
      height: 1px;
      background: linear-gradient(to right, rgba(0,184,255,0.2), transparent);
    }

    /* ── STATS GRID ── */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin-bottom: 32px;
    }

    @media (max-width: 560px) {
      .stats-grid { grid-template-columns: repeat(2, 1fr); }
    }

    .stat-card {
      background: var(--bg2);
      border: 1px solid rgba(0,255,157,0.1);
      border-radius: 4px;
      padding: 18px 14px;
      text-align: center;
      position: relative;
      overflow: hidden;
      transition: border-color 0.2s;
    }

    .stat-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 1px;
      background: linear-gradient(to right, transparent, rgba(0,255,157,0.35), transparent);
    }

    .stat-card:hover { border-color: rgba(0,255,157,0.3); }

    .stat-val {
      font-family: 'Orbitron', monospace;
      font-size: 22px;
      font-weight: 700;
      color: var(--green);
      display: block;
    }

    .stat-val.red  { color: var(--red); }
    .stat-val.blue { color: var(--blue); }

    .stat-lbl {
      font-size: 10px;
      color: var(--dim);
      letter-spacing: 1.5px;
      margin-top: 6px;
      display: block;
    }

    /* ── ARSENAL ── */
    .arsenal-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
      margin-bottom: 32px;
    }

    @media (max-width: 640px) {
      .arsenal-grid { grid-template-columns: 1fr; }
    }

    .arsenal-card {
      background: var(--bg2);
      border: 1px solid rgba(0,184,255,0.1);
      border-radius: 4px;
      padding: 18px 16px;
      position: relative;
    }

    .arsenal-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 1px;
      background: linear-gradient(to right, transparent, rgba(0,184,255,0.25), transparent);
    }

    .arsenal-title {
      font-family: 'Orbitron', monospace;
      font-size: 9px;
      color: var(--blue);
      letter-spacing: 2px;
      margin-bottom: 16px;
    }

    .skill-item {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
    }

    .skill-dot {
      width: 5px; height: 5px;
      border-radius: 50%;
      background: var(--green);
      flex-shrink: 0;
    }

    .skill-dot.blue  { background: var(--blue); }
    .skill-dot.red   { background: var(--red); }
    .skill-dot.amber { background: var(--amber); }

    .skill-name { font-size: 12px; color: var(--muted); flex: 1; }

    .bar-track {
      width: 72px; height: 3px;
      background: #0d1f18;
      border-radius: 2px;
      overflow: hidden;
      flex-shrink: 0;
    }

    .bar-fill {
      height: 100%;
      border-radius: 2px;
      background: linear-gradient(to right, var(--green), var(--blue));
      width: 0;
      transition: width 1.4s cubic-bezier(0.4,0,0.2,1);
    }

    .bar-fill.red { background: linear-gradient(to right, var(--red), #ff9944); }

    /* ── OPERATIONS ── */
    .ops-list { margin-bottom: 32px; }

    .op-item {
      display: flex;
      align-items: center;
      gap: 16px;
      background: var(--bg2);
      border: 1px solid rgba(255,76,110,0.1);
      border-left: 3px solid var(--red);
      border-radius: 0 4px 4px 0;
      padding: 16px 18px;
      margin-bottom: 12px;
      transition: border-color 0.2s;
    }

    .op-item:hover { border-color: rgba(255,76,110,0.25); }

    .op-item.blue  { border-left-color: var(--blue);  border-color: rgba(0,184,255,0.1); }
    .op-item.blue:hover  { border-color: rgba(0,184,255,0.25); }
    .op-item.green { border-left-color: var(--green); border-color: rgba(0,255,157,0.1); }
    .op-item.green:hover { border-color: rgba(0,255,157,0.25); }

    .op-badge {
      font-size: 10px;
      padding: 3px 10px;
      border-radius: 2px;
      letter-spacing: 1px;
      flex-shrink: 0;
      white-space: nowrap;
    }

    .op-badge.active   { background: rgba(255,76,110,0.1);  color: var(--red);   border: 1px solid rgba(255,76,110,0.3); }
    .op-badge.ongoing  { background: rgba(0,184,255,0.1);   color: var(--blue);  border: 1px solid rgba(0,184,255,0.3); }
    .op-badge.research { background: rgba(0,255,157,0.1);   color: var(--green); border: 1px solid rgba(0,255,157,0.3); }

    .op-text { flex: 1; }

    .op-name {
      font-family: 'Rajdhani', sans-serif;
      font-size: 14px;
      font-weight: 700;
      color: var(--text);
      letter-spacing: 0.5px;
    }

    .op-desc {
      font-size: 11px;
      color: var(--dim);
      margin-top: 3px;
      line-height: 1.6;
    }

    /* ── GITHUB STATS ── */
    .gh-stats {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 32px;
    }

    @media (max-width: 560px) { .gh-stats { grid-template-columns: 1fr; } }

    .gh-card {
      background: var(--bg2);
      border: 1px solid rgba(0,184,255,0.1);
      border-radius: 4px;
      overflow: hidden;
    }

    .gh-card img { width: 100%; display: block; }

    .gh-streak {
      grid-column: 1 / -1;
      background: var(--bg2);
      border: 1px solid rgba(0,255,157,0.1);
      border-radius: 4px;
      overflow: hidden;
      text-align: center;
    }

    .gh-streak img { width: 90%; max-width: 600px; }

    /* ── CONNECT ── */
    .connect-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 32px;
    }

    .connect-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 9px 18px;
      border-radius: 3px;
      font-family: 'Share Tech Mono', monospace;
      font-size: 11px;
      letter-spacing: 1.5px;
      text-decoration: none;
      border: 1px solid;
      cursor: pointer;
      transition: background 0.15s, border-color 0.15s;
    }

    .cb-green  { color: var(--green);  border-color: rgba(0,255,157,0.25);  background: rgba(0,255,157,0.04); }
    .cb-green:hover  { background: rgba(0,255,157,0.12); border-color: rgba(0,255,157,0.5); }
    .cb-blue   { color: var(--blue);   border-color: rgba(0,184,255,0.25);  background: rgba(0,184,255,0.04); }
    .cb-blue:hover   { background: rgba(0,184,255,0.12); }
    .cb-red    { color: var(--red);    border-color: rgba(255,76,110,0.25); background: rgba(255,76,110,0.04); }
    .cb-red:hover    { background: rgba(255,76,110,0.12); }
    .cb-amber  { color: var(--amber);  border-color: rgba(255,204,68,0.25); background: rgba(255,204,68,0.04); }
    .cb-amber:hover  { background: rgba(255,204,68,0.12); }
    .cb-purple { color: var(--purple); border-color: rgba(176,136,255,0.25); background: rgba(176,136,255,0.04); }
    .cb-purple:hover { background: rgba(176,136,255,0.12); }

    /* ── QUOTE ── */
    .quote-block {
      background: var(--bg2);
      border: 1px solid rgba(0,255,157,0.12);
      border-radius: 4px;
      padding: 22px 24px 20px;
      margin-bottom: 32px;
      position: relative;
    }

    .quote-mark {
      position: absolute;
      top: -16px; left: 18px;
      background: var(--bg);
      color: rgba(0,255,157,0.3);
      font-size: 44px;
      line-height: 1;
      font-family: Georgia, serif;
      padding: 0 8px;
    }

    .quote-text {
      font-size: 14px;
      color: #5a8a7a;
      line-height: 1.75;
      font-style: italic;
    }

    .quote-attr {
      font-size: 10px;
      color: rgba(0,255,157,0.3);
      margin-top: 12px;
      letter-spacing: 2px;
    }

    /* ── FOOTER ── */
    .footer {
      text-align: center;
    }

    .ping-badge {
      display: inline-block;
      background: rgba(0,255,157,0.07);
      color: var(--green);
      border: 1px solid rgba(0,255,157,0.18);
      border-radius: 3px;
      padding: 5px 16px;
      font-size: 11px;
      letter-spacing: 2px;
      margin-bottom: 18px;
    }

    .footer-text {
      font-size: 11px;
      color: rgba(0,255,157,0.15);
      letter-spacing: 3px;
    }

    /* ── ACTIVITY GRAPH ── */
    .activity-wrap {
      margin-bottom: 32px;
      border: 1px solid rgba(0,184,255,0.12);
      border-radius: 4px;
      overflow: hidden;
    }

    .activity-wrap img { width: 100%; display: block; }

    /* ── TROPHY ROW ── */
    .trophy-wrap {
      margin-bottom: 32px;
      text-align: center;
      border: 1px solid rgba(0,255,157,0.08);
      border-radius: 4px;
      overflow: hidden;
      background: var(--bg2);
      padding: 12px;
    }

    .trophy-wrap img { max-width: 100%; }
  </style>
</head>
<body>

  <div class="scanline"></div>
  <div class="grid-bg"></div>

  <div class="content">

    <!-- ── BOOT SEQUENCE ── -->
    <div class="boot-block">
      <div class="boot-line"><span class="ok">[  OK  ]</span> <span class="dim">Mounting virtual drives...</span></div>
      <div class="boot-line"><span class="ok">[  OK  ]</span> <span class="dim">Establishing secure tunnel → Cloudflare Edge...</span></div>
      <div class="boot-line"><span class="ok">[  OK  ]</span> <span class="dim">Loading DevOps arsenal [Docker · Kubernetes · AWS]...</span></div>
      <div class="boot-line"><span class="ok">[  OK  ]</span> <span class="dim">Bypassing firewall restrictions... </span><span class="danger">ACCESS GRANTED.</span></div>
      <div class="boot-line" style="margin-top:10px;">
        <span class="prompt">root@kavindu-oshadha:~# </span>./load_profile.sh<span class="cursor"></span>
      </div>
    </div>

    <!-- ── HERO ── -->
    <div class="hero">
      <div class="avatar-wrap">
        <div class="avatar">
          KO
          <div class="avatar-dot"></div>
        </div>
      </div>
      <div class="hero-info">
        <div class="name">KAVINDU OSHADHA PERERA</div>
        <div class="handle">// cit-24-01-0476-maker &nbsp;·&nbsp; Watareka, Sri Lanka</div>
        <div class="tag-row">
          <span class="tag tag-green">CYBER SECURITY</span>
          <span class="tag tag-blue">CLOUD ARCHITECT</span>
          <span class="tag tag-amber">FULL STACK DEV</span>
          <span class="tag tag-red">DEVOPS ENGINEER</span>
        </div>
        <div class="bio">
          3rd-year <span class="hl">BSc (Hons) Cyber Security Undergraduate</span> at SLTC Research University.
          Zero-trust advocate · High-availability cloud deployments · Secure full-stack apps with Next.js &amp; Firebase.
          Bridging the gap between hardcore backend security and immaculate frontend design.
          <br><br>
          <span class="hl">"I don't just write code — I engineer secure digital ecosystems."</span>
        </div>
      </div>
    </div>

    <hr class="divider">

    <!-- ── STATS ── -->
    <div class="section-label">SYSTEM TELEMETRY</div>
    <div class="stats-grid">
      <div class="stat-card">
        <span class="stat-val" id="c-commits">0</span>
        <span class="stat-lbl">COMMITS</span>
      </div>
      <div class="stat-card">
        <span class="stat-val blue" id="c-repos">0</span>
        <span class="stat-lbl">REPOSITORIES</span>
      </div>
      <div class="stat-card">
        <span class="stat-val" id="c-stars">0</span>
        <span class="stat-lbl">STARS EARNED</span>
      </div>
      <div class="stat-card">
        <span class="stat-val red">ROOT</span>
        <span class="stat-lbl">CLEARANCE LEVEL</span>
      </div>
    </div>

    <!-- ── GITHUB LIVE STATS ── -->
    <div class="section-label">GITHUB TELEMETRY &amp; LIVE GRAPHS</div>

    <div class="activity-wrap">
      <img
        src="https://github-readme-activity-graph.vercel.app/graph?username=cit-24-01-0476-maker&theme=radical&bg_color=060d0a&color=00FF9D&line=00b8ff&point=FFFFFF&hide_border=true&custom_title=System_Activity_Log"
        alt="GitHub Activity Graph"
      />
    </div>

    <div class="gh-stats">
      <div class="gh-card">
        <img
          src="https://github-readme-stats.vercel.app/api?username=cit-24-01-0476-maker&show_icons=true&theme=radical&hide_border=true&bg_color=060d0a&title_color=00FF9D&icon_color=00b8ff&text_color=c9d1d9"
          alt="GitHub Stats"
        />
      </div>
      <div class="gh-card">
        <img
          src="https://github-readme-stats.vercel.app/api/top-langs/?username=cit-24-01-0476-maker&layout=compact&theme=radical&hide_border=true&bg_color=060d0a&title_color=00FF9D&text_color=c9d1d9"
          alt="Top Languages"
        />
      </div>
      <div class="gh-streak">
        <img
          src="https://github-readme-streak-stats.herokuapp.com/?user=cit-24-01-0476-maker&theme=radical&hide_border=true&background=060d0a&ring=00FF9D&fire=00b8ff&currStreakNum=FFFFFF&sideNums=c9d1d9&sideLabels=00b8ff"
          alt="GitHub Streak"
        />
      </div>
    </div>

    <div class="trophy-wrap">
      <img
        src="https://github-profile-trophy.vercel.app/?username=cit-24-01-0476-maker&theme=radical&no-frame=true&no-bg=true&margin-w=15"
        alt="GitHub Trophies"
      />
    </div>

    <!-- ── TECH ARSENAL ── -->
    <div class="section-label">TECH ARSENAL &amp; INFRASTRUCTURE</div>

    <!-- Skill Icons -->
    <div style="text-align:center; margin-bottom:22px;">
      <img
        src="https://skillicons.dev/icons?i=aws,cloudflare,linux,kali,ubuntu,windows,apple,docker,kubernetes,bash,nextjs,react,nodejs,firebase,ts,js,html,css,python,figma,github,vscode&perline=11&theme=dark"
        alt="Tech Stack Icons"
        style="max-width:100%;"
      />
    </div>

    <div class="arsenal-grid">
      <!-- Cloud & Infra -->
      <div class="arsenal-card">
        <div class="arsenal-title">// CLOUD &amp; INFRASTRUCTURE</div>
        <div class="skill-item">
          <div class="skill-dot blue"></div>
          <span class="skill-name">Amazon AWS</span>
          <div class="bar-track"><div class="bar-fill" data-w="85"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot blue"></div>
          <span class="skill-name">Docker / Kubernetes</span>
          <div class="bar-track"><div class="bar-fill" data-w="78"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot blue"></div>
          <span class="skill-name">Cloudflare</span>
          <div class="bar-track"><div class="bar-fill" data-w="92"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot blue"></div>
          <span class="skill-name">Linux / Ubuntu</span>
          <div class="bar-track"><div class="bar-fill" data-w="94"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot blue"></div>
          <span class="skill-name">DigitalOcean VPS</span>
          <div class="bar-track"><div class="bar-fill" data-w="88"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot blue"></div>
          <span class="skill-name">Fastly CDN</span>
          <div class="bar-track"><div class="bar-fill" data-w="80"></div></div>
        </div>
      </div>

      <!-- Development -->
      <div class="arsenal-card">
        <div class="arsenal-title">// DEVELOPMENT STACK</div>
        <div class="skill-item">
          <div class="skill-dot"></div>
          <span class="skill-name">Next.js</span>
          <div class="bar-track"><div class="bar-fill" data-w="90"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot"></div>
          <span class="skill-name">TypeScript</span>
          <div class="bar-track"><div class="bar-fill" data-w="84"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot"></div>
          <span class="skill-name">Firebase</span>
          <div class="bar-track"><div class="bar-fill" data-w="87"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot"></div>
          <span class="skill-name">Node.js</span>
          <div class="bar-track"><div class="bar-fill" data-w="82"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot"></div>
          <span class="skill-name">React</span>
          <div class="bar-track"><div class="bar-fill" data-w="86"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot"></div>
          <span class="skill-name">Figma / UI Design</span>
          <div class="bar-track"><div class="bar-fill" data-w="75"></div></div>
        </div>
      </div>

      <!-- Security -->
      <div class="arsenal-card">
        <div class="arsenal-title">// SECURITY OPERATIONS</div>
        <div class="skill-item">
          <div class="skill-dot red"></div>
          <span class="skill-name">Kali Linux</span>
          <div class="bar-track"><div class="bar-fill red" data-w="89"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot red"></div>
          <span class="skill-name">V2Ray / VLESS / Trojan</span>
          <div class="bar-track"><div class="bar-fill red" data-w="86"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot red"></div>
          <span class="skill-name">Penetration Testing</span>
          <div class="bar-track"><div class="bar-fill red" data-w="80"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot red"></div>
          <span class="skill-name">Nmap / Recon</span>
          <div class="bar-track"><div class="bar-fill red" data-w="83"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot red"></div>
          <span class="skill-name">Zero-Trust Networks</span>
          <div class="bar-track"><div class="bar-fill red" data-w="85"></div></div>
        </div>
        <div class="skill-item">
          <div class="skill-dot red"></div>
          <span class="skill-name">DDoS Hardening</span>
          <div class="bar-track"><div class="bar-fill red" data-w="82"></div></div>
        </div>
      </div>
    </div>

    <!-- ── ACTIVE OPERATIONS ── -->
    <div class="section-label">CURRENT DIRECTIVES &amp; OPERATIONS</div>
    <div class="ops-list">
      <div class="op-item">
        <div class="op-badge active">ACTIVE</div>
        <div class="op-text">
          <div class="op-name">OSKA VPN PORTAL INFRASTRUCTURE</div>
          <div class="op-desc">
            Stack: Next.js · Firebase · DigitalOcean VPS — Architecting a zero-log VPN management dashboard.
            Custom proxy configs including V2Ray, VLESS, and Trojan over XTLS to bypass strict firewall restrictions.
          </div>
        </div>
      </div>
      <div class="op-item blue">
        <div class="op-badge ongoing">ONGOING</div>
        <div class="op-text">
          <div class="op-name">ENTERPRISE CLOUD DEPLOYMENTS</div>
          <div class="op-desc">
            Stack: AWS · Linux · Fastly CDN — Continuous configuration of robust cloud environments.
            SSH management via Termius · Aggressive DDoS protection · Cloudflare &amp; Fastly CDN optimization.
          </div>
        </div>
      </div>
      <div class="op-item green">
        <div class="op-badge research">RESEARCH</div>
        <div class="op-text">
          <div class="op-name">CYBER SECURITY ACADEMIC RESEARCH</div>
          <div class="op-desc">
            Org: SLTC Research University · Senior Year — Deep-dive studies in network penetration testing using Kali Linux.
            TryHackMe rooms · Nmap scanning · Security vulnerability analysis · Expanding into Figma UI/UX design.
          </div>
        </div>
      </div>
    </div>

    <!-- ── CONNECT ── -->
    <div class="section-label">SECURE COMMUNICATION LINES</div>
    <div class="connect-row">
      <a class="connect-btn cb-green" href="https://oshadha.live" target="_blank">&#9632; PORTFOLIO</a>
      <a class="connect-btn cb-blue"  href="https://www.linkedin.com/in/kavindu-oshadha-perera" target="_blank">&#9670; LINKEDIN</a>
      <a class="connect-btn cb-red"   href="mailto:oshadhaperera500@gmail.com">&#9711; SECURE MAIL</a>
      <a class="connect-btn cb-amber" href="https://t.me/oska_lex_vp" target="_blank">&#9672; TELEGRAM</a>
      <a class="connect-btn cb-purple" href="https://wa.me/94754565755" target="_blank">&#9670; WHATSAPP</a>
    </div>

    <hr class="divider">

    <!-- ── QUOTE ── -->
    <div class="quote-block">
      <div class="quote-mark">"</div>
      <div class="quote-text">
        Security is not a product, but a process. The enemy knows the system — you must know it better, faster, and deeper than they ever will.
      </div>
      <div class="quote-attr">// BRUCE SCHNEIER &nbsp;·&nbsp; ADAPTED</div>
    </div>

    <!-- ── FOOTER ── -->
    <div class="footer">
      <div class="ping-badge">SYSTEM_PINGS: ONLINE &nbsp;·&nbsp; ENCRYPTED &nbsp;·&nbsp; SECURE</div>
      <div class="footer-text">END OF FILE // THANK YOU FOR VISITING THE MAINFRAME</div>
    </div>

  </div><!-- /content -->

  <script>
    // Animate stat counters
    const counters = [
      { id: 'c-commits', target: 247 },
      { id: 'c-repos',   target: 34  },
      { id: 'c-stars',   target: 89  },
    ];

    counters.forEach(({ id, target }) => {
      const el = document.getElementById(id);
      if (!el) return;
      let count = 0;
      const step = Math.max(1, Math.ceil(target / 50));
      const iv = setInterval(() => {
        count = Math.min(count + step, target);
        el.textContent = count;
        if (count >= target) clearInterval(iv);
      }, 35);
    });

    // Animate skill bars on intersection
    const fills = document.querySelectorAll('.bar-fill');

    const obs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const w = el.getAttribute('data-w');
          el.style.width = w + '%';
          obs.unobserve(el);
        }
      });
    }, { threshold: 0.1 });

    fills.forEach(f => obs.observe(f));
  </script>
</body>
</html>
