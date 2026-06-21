#!/usr/bin/env python3
"""
Patch script: Enhanced Project Health Gauge (Card 2 of steering_hero section)
Replaces the existing gauge block with a premium multi-ring concentric dial,
status strip, animated metric cards, and an accurate score breakdown drawer.
"""
import sys, re

HTML_PATH = 'projectpulse.html'

START_MARKER = "          // ── CARD 2: Project Health Gauge ──"
END_MARKER   = "          // ── CARD 3: Schedule & Status Overview ──"

NEW_BLOCK = r"""          // ── CARD 2: Project Health Gauge ──
          const gId = 'dash-health-gauge';
          const gSpan = (P.widgetSpans && P.widgetSpans[gId]) || 2;
          const gCard = mkCC('Project Health Gauge', 'Composite Rating & Performance Index', gId, '', 'standard', '<b>Project Health Gauge:</b> A premium multi-ring composite gauge displaying the weighted health index, schedule performance (SPI), completion rate, and live penalty breakdown.', 'View Explanation', 'gauge');
          gCard.style.gridColumn = `span ${gSpan}`;
          grid.appendChild(gCard);

          // ── Calculations for Health Gauge ──
          const healthScoreVal = getHealthScore(tasks);
          const healthLabel = healthScoreVal >= 80 ? 'Healthy' : healthScoreVal >= 60 ? 'At Risk' : 'Critical';
          const healthLabelColor = healthScoreVal >= 80 ? 'var(--green)' : healthScoreVal >= 60 ? 'var(--amber)' : 'var(--red)';
          const healthBg = healthScoreVal >= 80 ? 'rgba(16,185,129,0.08)' : healthScoreVal >= 60 ? 'rgba(245,158,11,0.08)' : 'rgba(239,68,68,0.08)';

          const spiVal = spi.toFixed(2);
          const spiColor = spi >= 0.95 ? 'var(--green)' : spi >= 0.80 ? 'var(--amber)' : 'var(--red)';
          const spiIcon = spi >= 0.95 ? 'trending-up' : 'trending-down';

          const cpiVal = cpi.toFixed(2);
          const cpiColor = cpi >= 1.0 ? 'var(--green)' : cpi >= 0.85 ? 'var(--amber)' : 'var(--red)';
          const cpiIcon = cpi >= 1.0 ? 'trending-up' : 'trending-down';

          const overdueTasksCount = tasks.filter(t => { const d = daysDiff(t.dueDate); return d !== null && d < 0 && t.status !== 'Completed' && t.status !== 'Cancelled'; }).length;
          const blockedTasksCount = tasks.filter(t => t.status === 'On Hold').length;
          const remainingTasksCount = tasks.filter(t => t.status !== 'Completed' && t.status !== 'Cancelled').length;

          // Accurate weighted penalty values matching getHealthScore() formula
          const activeTasks = tasks.filter(t => t.status !== 'Completed' && t.status !== 'Cancelled');
          const totalActive = activeTasks.length || 1;
          let overduePenaltyWt = 0, blockedPenaltyWt = 0, onHoldPenaltyWt = 0;
          activeTasks.forEach(t => {
            const pw = 1 - (parseInt(t.progress, 10) || 0) / 100;
            if (t.dueDate) { const dd = daysDiff(t.dueDate); if (dd !== null && dd < 0) overduePenaltyWt += pw; }
            if (t.status === 'On Hold') onHoldPenaltyWt += pw;
          });
          // blockedPenalty uses dependency check; approximate with On Hold for widget display
          blockedPenaltyWt = blockedTasksCount > 0 ? activeTasks.filter(t => t.status === 'On Hold').reduce((s, t) => s + (1 - (parseInt(t.progress,10)||0)/100), 0) : 0;
          const accurateOverduePenalty = Math.round((overduePenaltyWt / totalActive) * 50 * 10) / 10;
          const accurateBlockedPenalty = Math.round((blockedPenaltyWt / totalActive) * 30 * 10) / 10;
          const accurateOnHoldPenalty  = Math.round((onHoldPenaltyWt  / totalActive) * 20 * 10) / 10;

          // SVG arc helpers — semicircle (180°) ring-segment math
          // Centre: cx=200, cy=190. Rings: r=130 (outer), r=105 (middle), r=80 (inner)
          function describeArc(cx, cy, r, startDeg, endDeg) {
            const toR = d => d * Math.PI / 180;
            const sx = cx + r * Math.cos(toR(startDeg));
            const sy = cy + r * Math.sin(toR(startDeg));
            const ex = cx + r * Math.cos(toR(endDeg));
            const ey = cy + r * Math.sin(toR(endDeg));
            const large = endDeg - startDeg > 180 ? 1 : 0;
            return `M ${sx} ${sy} A ${r} ${r} 0 ${large} 1 ${ex} ${ey}`;
          }
          // Map a 0-100 score onto a 180° arc (180° = full left, 360°/0° = full right)
          function scoreArc(cx, cy, r, score100) {
            const deg = 180 + (score100 / 100) * 180;
            return describeArc(cx, cy, r, 180, Math.min(deg, 359.9));
          }
          // Map SPI (0.5–1.2) onto 180° arc
          function spiArc(cx, cy, r, spiNum) {
            const pct = Math.min(1, Math.max(0, (spiNum - 0.5) / 0.7));
            return scoreArc(cx, cy, r, pct * 100);
          }

          const cx = 200, cy = 185;
          const rOuter = 130, rMid = 102, rInner = 74;
          const strokeW = 14;

          // Background track arcs (full 180°)
          const trackPath = (r) => describeArc(cx, cy, r, 180, 359.9);

          // Colored fill arcs
          const healthArc   = healthScoreVal > 0 ? scoreArc(cx, cy, rOuter, healthScoreVal) : null;
          const spiArcPath  = spi > 0.5 ? spiArc(cx, cy, rMid, spi) : null;
          const progArcPath = avgProgress > 0 ? scoreArc(cx, cy, rInner, avgProgress) : null;

          // Circumference-based dashoffset for CSS-animated stroke
          const circumOuter = Math.PI * rOuter; // half-circle
          const circumMid   = Math.PI * rMid;
          const circumInner = Math.PI * rInner;
          const dashHealth  = (healthScoreVal / 100) * circumOuter;
          const dashSpi     = (Math.min(1, Math.max(0, (spi - 0.5) / 0.7))) * circumMid;
          const dashProg    = (avgProgress / 100) * circumInner;

          // Needle tip coords for health score
          const needleAngleDeg = 180 + (healthScoreVal / 100) * 180;
          const needleRad = needleAngleDeg * Math.PI / 180;
          const needleTipX = cx + (rOuter - strokeW) * Math.cos(needleRad);
          const needleTipY = cy + (rOuter - strokeW) * Math.sin(needleRad);

          // Unique animation ID to avoid collision with other gauges
          const gaugeUid = 'ghg-' + gId.replace(/[^a-z0-9]/g,'');

          gCard.querySelector('.cb').innerHTML = `
            <style>
              @keyframes ${gaugeUid}-outer {
                from { stroke-dashoffset: ${circumOuter.toFixed(1)}; }
                to   { stroke-dashoffset: ${(circumOuter - dashHealth).toFixed(1)}; }
              }
              @keyframes ${gaugeUid}-mid {
                from { stroke-dashoffset: ${circumMid.toFixed(1)}; }
                to   { stroke-dashoffset: ${(circumMid - dashSpi).toFixed(1)}; }
              }
              @keyframes ${gaugeUid}-inner {
                from { stroke-dashoffset: ${circumInner.toFixed(1)}; }
                to   { stroke-dashoffset: ${(circumInner - dashProg).toFixed(1)}; }
              }
              @keyframes ${gaugeUid}-pulse {
                0%, 100% { opacity: 1; } 50% { opacity: 0.3; }
              }
              @keyframes ${gaugeUid}-fadeIn {
                from { opacity: 0; transform: translateY(6px); }
                to   { opacity: 1; transform: translateY(0); }
              }
            </style>

            <div style="display:flex; flex-direction:column; align-items:center; width:100%; gap:16px;">

              <!-- ── MULTI-RING GAUGE SVG ── -->
              <div style="position:relative; width:100%; max-width:340px;">
                <svg viewBox="0 0 400 200" width="100%" style="overflow:visible; display:block;" aria-label="Health score gauge: ${healthScoreVal}%">
                  <defs>
                    <!-- Outer ring gradient: health score -->
                    <linearGradient id="${gaugeUid}-grad-outer" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%"   stop-color="#ef4444"/>
                      <stop offset="45%"  stop-color="#f59e0b"/>
                      <stop offset="100%" stop-color="#10b981"/>
                    </linearGradient>
                    <!-- Middle ring gradient: SPI -->
                    <linearGradient id="${gaugeUid}-grad-mid" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%"   stop-color="#ef4444"/>
                      <stop offset="100%" stop-color="${spiColor === 'var(--green)' ? '#10b981' : spiColor === 'var(--amber)' ? '#f59e0b' : '#ef4444'}"/>
                    </linearGradient>
                    <!-- Inner ring: completion -->
                    <linearGradient id="${gaugeUid}-grad-inner" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%"   stop-color="#3b82f6"/>
                      <stop offset="100%" stop-color="#10b981"/>
                    </linearGradient>
                    <!-- Glow filter for healthy state -->
                    <filter id="${gaugeUid}-glow" x="-20%" y="-20%" width="140%" height="140%">
                      <feGaussianBlur stdDeviation="4" result="blur"/>
                      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                    </filter>
                    <filter id="${gaugeUid}-needle-shadow">
                      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.25"/>
                    </filter>
                  </defs>

                  <!-- ── Background tracks ── -->
                  <path d="${trackPath(rOuter)}" fill="none" stroke="var(--color-surface-3)" stroke-width="${strokeW}" stroke-linecap="round" opacity="0.5"/>
                  <path d="${trackPath(rMid)}"   fill="none" stroke="var(--color-surface-3)" stroke-width="${strokeW}" stroke-linecap="round" opacity="0.5"/>
                  <path d="${trackPath(rInner)}" fill="none" stroke="var(--color-surface-3)" stroke-width="${strokeW}" stroke-linecap="round" opacity="0.5"/>

                  <!-- ── Animated fill arcs ── -->
                  <!-- Outer: Health Score -->
                  <path d="${trackPath(rOuter)}" fill="none"
                        stroke="url(#${gaugeUid}-grad-outer)" stroke-width="${strokeW}" stroke-linecap="round"
                        stroke-dasharray="${circumOuter.toFixed(1)}"
                        stroke-dashoffset="${(circumOuter - dashHealth).toFixed(1)}"
                        style="animation: ${gaugeUid}-outer 1.6s cubic-bezier(0.34,1.2,0.64,1) forwards; transform-origin: ${cx}px ${cy}px;"
                        ${healthScoreVal >= 80 ? `filter="url(#${gaugeUid}-glow)"` : ''}/>

                  <!-- Middle: SPI -->
                  <path d="${trackPath(rMid)}" fill="none"
                        stroke="url(#${gaugeUid}-grad-mid)" stroke-width="${strokeW}" stroke-linecap="round"
                        stroke-dasharray="${circumMid.toFixed(1)}"
                        stroke-dashoffset="${(circumMid - dashSpi).toFixed(1)}"
                        style="animation: ${gaugeUid}-mid 1.8s cubic-bezier(0.34,1.2,0.64,1) 0.1s both;"/>

                  <!-- Inner: Completion % -->
                  <path d="${trackPath(rInner)}" fill="none"
                        stroke="url(#${gaugeUid}-grad-inner)" stroke-width="${strokeW}" stroke-linecap="round"
                        stroke-dasharray="${circumInner.toFixed(1)}"
                        stroke-dashoffset="${(circumInner - dashProg).toFixed(1)}"
                        style="animation: ${gaugeUid}-inner 2s cubic-bezier(0.34,1.2,0.64,1) 0.2s both;"/>

                  <!-- ── Ring labels (outer right edge) ── -->
                  <text x="${cx + rOuter + 10}" y="${cy + 5}" font-size="8" font-weight="800" fill="var(--color-text-faint)" font-family="var(--mono)" text-anchor="start">PHI</text>
                  <text x="${cx + rMid + 10}" y="${cy + 5}" font-size="8" font-weight="800" fill="var(--color-text-faint)" font-family="var(--mono)" text-anchor="start">SPI</text>
                  <text x="${cx + rInner + 10}" y="${cy + 5}" font-size="8" font-weight="800" fill="var(--color-text-faint)" font-family="var(--mono)" text-anchor="start">CPL</text>

                  <!-- ── Tick marks at 0, 25, 50, 75, 100 ── -->
                  <g stroke="var(--color-border)" stroke-width="1.5" opacity="0.7">
                    <!-- 0° = left = 180deg -->
                    <line x1="${(cx - rOuter - strokeW/2 - 4).toFixed(1)}" y1="${cy}" x2="${(cx - rOuter - strokeW/2 - 10).toFixed(1)}" y2="${cy}"/>
                    <!-- 45° = 225deg -->
                    <line x1="${(cx + (rOuter+strokeW/2+4)*Math.cos(225*Math.PI/180)).toFixed(1)}" y1="${(cy + (rOuter+strokeW/2+4)*Math.sin(225*Math.PI/180)).toFixed(1)}"
                          x2="${(cx + (rOuter+strokeW/2+10)*Math.cos(225*Math.PI/180)).toFixed(1)}" y2="${(cy + (rOuter+strokeW/2+10)*Math.sin(225*Math.PI/180)).toFixed(1)}"/>
                    <!-- 90° = top = 270deg -->
                    <line x1="${cx}" y1="${(cy - rOuter - strokeW/2 - 4).toFixed(1)}" x2="${cx}" y2="${(cy - rOuter - strokeW/2 - 10).toFixed(1)}"/>
                    <!-- 135° = 315deg -->
                    <line x1="${(cx + (rOuter+strokeW/2+4)*Math.cos(315*Math.PI/180)).toFixed(1)}" y1="${(cy + (rOuter+strokeW/2+4)*Math.sin(315*Math.PI/180)).toFixed(1)}"
                          x2="${(cx + (rOuter+strokeW/2+10)*Math.cos(315*Math.PI/180)).toFixed(1)}" y2="${(cy + (rOuter+strokeW/2+10)*Math.sin(315*Math.PI/180)).toFixed(1)}"/>
                    <!-- 180° = right = 360deg -->
                    <line x1="${(cx + rOuter + strokeW/2 + 4).toFixed(1)}" y1="${cy}" x2="${(cx + rOuter + strokeW/2 + 10).toFixed(1)}" y2="${cy}"/>
                  </g>

                  <!-- ── Tick labels ── -->
                  <text x="${(cx - rOuter - strokeW/2 - 14).toFixed(1)}" y="${cy + 4}" font-size="8" font-weight="700" fill="var(--color-text-faint)" text-anchor="middle" font-family="var(--mono)">0</text>
                  <text x="${cx}" y="${(cy - rOuter - strokeW/2 - 13).toFixed(1)}" font-size="8" font-weight="700" fill="var(--color-text-faint)" text-anchor="middle" font-family="var(--mono)">50</text>
                  <text x="${(cx + rOuter + strokeW/2 + 14).toFixed(1)}" y="${cy + 4}" font-size="8" font-weight="700" fill="var(--color-text-faint)" text-anchor="middle" font-family="var(--mono)">100</text>

                  <!-- ── Centre readout ── -->
                  <text x="${cx}" y="${cy - 20}" font-size="8" font-weight="800" fill="var(--color-text-faint)" text-anchor="middle" letter-spacing="1.8" font-family="var(--mono)">HEALTH INDEX</text>
                  <text x="${cx}" y="${cy + 14}" font-size="38" font-weight="900" fill="${healthLabelColor}" text-anchor="middle" font-family="var(--mono)">${healthScoreVal}</text>
                  <text x="${cx}" y="${cy + 30}" font-size="9" font-weight="700" fill="var(--color-text-faint)" text-anchor="middle" font-family="var(--mono)">/100</text>

                  <!-- Status badge -->
                  <rect x="${cx - 28}" y="${cy + 36}" width="56" height="16" rx="8" fill="${healthBg}" stroke="${healthLabelColor}" stroke-width="1" opacity="0.9"/>
                  <text x="${cx}" y="${cy + 47}" font-size="8" font-weight="800" fill="${healthLabelColor}" text-anchor="middle" font-family="var(--mono)">${healthLabel.toUpperCase()}</text>
                  ${healthScoreVal < 60 ? `<circle cx="${cx + 32}" cy="${cy + 44}" r="3" fill="var(--red)" style="animation: ${gaugeUid}-pulse 1.2s ease-in-out infinite;"/>` : ''}

                  <!-- ── Needle ── -->
                  <line x1="${cx}" y1="${cy}"
                        x2="${needleTipX.toFixed(2)}" y2="${needleTipY.toFixed(2)}"
                        stroke="var(--color-text)" stroke-width="2" stroke-linecap="round"
                        filter="url(#${gaugeUid}-needle-shadow)"
                        style="transform-origin:${cx}px ${cy}px; transform:rotate(0deg);
                               animation:${gaugeUid}-outer 1.6s cubic-bezier(0.34,1.2,0.64,1) forwards;"/>
                  <circle cx="${cx}" cy="${cy}" r="7" fill="var(--color-primary)" stroke="var(--color-surface)" stroke-width="2" filter="url(#${gaugeUid}-needle-shadow)"/>
                  <circle cx="${cx}" cy="${cy}" r="3" fill="var(--color-surface)"/>
                </svg>
              </div>

              <!-- ── STATUS STRIP ── -->
              <div style="display:flex; align-items:center; justify-content:center; gap:8px; flex-wrap:wrap; animation: ${gaugeUid}-fadeIn 0.5s 0.3s both;">
                <div style="display:flex; align-items:center; gap:5px; padding:5px 10px; border-radius:20px; background:${healthBg}; border:1px solid ${healthLabelColor}; font-size:10px; font-weight:800; color:${healthLabelColor};">
                  <i data-lucide="${healthScoreVal >= 80 ? 'shield-check' : healthScoreVal >= 60 ? 'shield-alert' : 'shield-x'}" style="width:11px; height:11px;"></i>
                  ${healthLabel}
                </div>
                ${overdueTasksCount > 0 ? `
                <div style="display:flex; align-items:center; gap:5px; padding:5px 10px; border-radius:20px; background:rgba(239,68,68,0.08); border:1px solid rgba(239,68,68,0.3); font-size:10px; font-weight:800; color:var(--red);">
                  <i data-lucide="clock-alert" style="width:11px; height:11px;"></i>
                  ${overdueTasksCount} Overdue
                </div>` : `
                <div style="display:flex; align-items:center; gap:5px; padding:5px 10px; border-radius:20px; background:rgba(16,185,129,0.06); border:1px solid rgba(16,185,129,0.2); font-size:10px; font-weight:700; color:var(--green);">
                  <i data-lucide="check-circle" style="width:11px; height:11px;"></i>
                  No Overdue
                </div>`}
                ${blockedTasksCount > 0 ? `
                <div style="display:flex; align-items:center; gap:5px; padding:5px 10px; border-radius:20px; background:rgba(245,158,11,0.08); border:1px solid rgba(245,158,11,0.3); font-size:10px; font-weight:800; color:var(--amber);">
                  <i data-lucide="ban" style="width:11px; height:11px;"></i>
                  ${blockedTasksCount} Blocked
                </div>` : ''}
                <div style="display:flex; align-items:center; gap:4px; padding:5px 10px; border-radius:20px; background:var(--color-surface-2); border:1px solid var(--color-border-faint); font-size:10px; font-weight:700; color:var(--color-text-muted);">
                  <i data-lucide="${spi >= 0.95 ? 'trending-up' : 'trending-down'}" style="width:11px; height:11px; color:${spiColor};"></i>
                  SPI ${spiVal}
                </div>
              </div>

              <!-- ── BREAKDOWN TRIGGER ── -->
              <button id="health-breakdown-btn" style="font-size:10px; padding:6px 16px; border-radius:20px; cursor:pointer; font-weight:700; border:1px solid var(--color-border); background:var(--color-surface); color:var(--color-text); display:flex; align-items:center; gap:6px; transition:all 0.2s ease;"
                onmouseover="this.style.background='var(--color-primary-highlight)'; this.style.borderColor='var(--color-primary)';"
                onmouseout="this.style.background='var(--color-surface)'; this.style.borderColor='var(--color-border)';">
                <i data-lucide="bar-chart-2" style="width:12px; height:12px;"></i> Score Breakdown
              </button>

              <!-- ── ACCURATE SCORE BREAKDOWN PANEL ── -->
              <div id="health-breakdown-panel" style="width:100%; display:none; animation:${gaugeUid}-fadeIn 0.25s ease;">
                <div style="background:var(--color-surface-2); padding:14px 16px; border-radius:12px; border:1px solid var(--color-border-faint); font-size:11px; display:flex; flex-direction:column; gap:0;">
                  <!-- Header row -->
                  <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:8px; border-bottom:1px solid var(--color-border-faint); margin-bottom:6px;">
                    <span style="font-size:9px; font-weight:800; text-transform:uppercase; letter-spacing:1px; color:var(--color-text-faint); font-family:var(--mono);">Score Component</span>
                    <span style="font-size:9px; font-weight:800; text-transform:uppercase; letter-spacing:1px; color:var(--color-text-faint); font-family:var(--mono);">Impact</span>
                  </div>
                  <!-- Active task base -->
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:6px 0; border-bottom:1px solid var(--color-border-faint);">
                    <div style="display:flex; align-items:center; gap:7px;">
                      <div style="width:8px; height:8px; border-radius:50%; background:var(--color-primary); flex-shrink:0;"></div>
                      <span style="color:var(--color-text-muted);">Base Score</span>
                    </div>
                    <span style="color:var(--color-primary); font-weight:800; font-family:var(--mono);">+100</span>
                  </div>
                  <!-- Overdue penalty -->
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:6px 0; border-bottom:1px solid var(--color-border-faint);">
                    <div style="display:flex; align-items:center; gap:7px;">
                      <div style="width:8px; height:8px; border-radius:50%; background:var(--red); flex-shrink:0;"></div>
                      <span style="color:var(--color-text-muted);">Overdue Penalty <span style="color:var(--color-text-faint); font-size:9px;">(${overdueTasksCount} tasks · ×50 weight)</span></span>
                    </div>
                    <span style="color:${accurateOverduePenalty > 0 ? 'var(--red)' : 'var(--green)'}; font-weight:800; font-family:var(--mono);">${accurateOverduePenalty > 0 ? '-' + accurateOverduePenalty.toFixed(1) : '0'}</span>
                  </div>
                  <!-- Blocked/On Hold penalty -->
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:6px 0; border-bottom:1px solid var(--color-border-faint);">
                    <div style="display:flex; align-items:center; gap:7px;">
                      <div style="width:8px; height:8px; border-radius:50%; background:var(--amber); flex-shrink:0;"></div>
                      <span style="color:var(--color-text-muted);">On Hold Penalty <span style="color:var(--color-text-faint); font-size:9px;">(${blockedTasksCount} tasks · ×30 weight)</span></span>
                    </div>
                    <span style="color:${accurateBlockedPenalty > 0 ? 'var(--amber)' : 'var(--green)'}; font-weight:800; font-family:var(--mono);">${accurateBlockedPenalty > 0 ? '-' + accurateBlockedPenalty.toFixed(1) : '0'}</span>
                  </div>
                  <!-- On Hold penalty -->
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:6px 0; border-bottom:1px solid var(--color-border-faint);">
                    <div style="display:flex; align-items:center; gap:7px;">
                      <div style="width:8px; height:8px; border-radius:50%; background:var(--color-text-muted); flex-shrink:0;"></div>
                      <span style="color:var(--color-text-muted);">Stalled Penalty <span style="color:var(--color-text-faint); font-size:9px;">(on-hold tasks · ×20 weight)</span></span>
                    </div>
                    <span style="color:${accurateOnHoldPenalty > 0 ? 'var(--color-text-muted)' : 'var(--green)'}; font-weight:800; font-family:var(--mono);">${accurateOnHoldPenalty > 0 ? '-' + accurateOnHoldPenalty.toFixed(1) : '0'}</span>
                  </div>
                  <!-- Final score -->
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:8px 0 2px 0;">
                    <span style="font-weight:800; color:var(--color-text);">Project Health Index</span>
                    <span style="font-size:16px; font-weight:900; color:${healthLabelColor}; font-family:var(--mono);">${healthScoreVal}<span style="font-size:10px; font-weight:600; color:var(--color-text-muted);">/100</span></span>
                  </div>
                </div>
              </div>

              <!-- ── METRIC CARDS 2×2 ── -->
              <div style="display:grid; grid-template-columns:repeat(2,1fr); gap:10px; width:100%; animation:${gaugeUid}-fadeIn 0.5s 0.25s both;">

                <!-- SPI -->
                <div style="background:var(--color-surface-2); border:1px solid var(--color-border-faint); border-radius:12px; padding:12px 14px; display:flex; align-items:center; gap:12px; transition:all 0.2s; cursor:default;"
                  onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.08)';"
                  onmouseout="this.style.transform='none'; this.style.boxShadow='none';">
                  <!-- Mini arc ring -->
                  <svg width="36" height="36" viewBox="0 0 36 36" style="flex-shrink:0;" aria-hidden="true">
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--color-surface-3)" stroke-width="3.5"/>
                    <circle cx="18" cy="18" r="14" fill="none" stroke="${spiColor}" stroke-width="3.5"
                            stroke-dasharray="${(2 * Math.PI * 14).toFixed(1)}"
                            stroke-dashoffset="${((1 - Math.min(1, Math.max(0, (spi - 0.5)/0.7))) * 2 * Math.PI * 14).toFixed(1)}"
                            stroke-linecap="round" transform="rotate(-90 18 18)"/>
                    <i data-lucide="${spiIcon}" style="display:none;"></i>
                  </svg>
                  <div>
                    <div style="font-size:9px; font-weight:800; color:var(--color-text-muted); text-transform:uppercase; letter-spacing:0.5px;">Schedule (SPI)</div>
                    <div style="font-size:18px; font-weight:900; color:${spiColor}; line-height:1.2; font-family:var(--mono);">${spiVal}</div>
                    <div style="font-size:9px; color:var(--color-text-faint); margin-top:1px;">${spi >= 0.95 ? 'On Schedule' : spi >= 0.80 ? 'Slight Delay' : 'Behind Schedule'}</div>
                  </div>
                </div>

                <!-- CPI -->
                <div style="background:var(--color-surface-2); border:1px solid var(--color-border-faint); border-radius:12px; padding:12px 14px; display:flex; align-items:center; gap:12px; transition:all 0.2s; cursor:default;"
                  onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.08)';"
                  onmouseout="this.style.transform='none'; this.style.boxShadow='none';">
                  <svg width="36" height="36" viewBox="0 0 36 36" style="flex-shrink:0;" aria-hidden="true">
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--color-surface-3)" stroke-width="3.5"/>
                    <circle cx="18" cy="18" r="14" fill="none" stroke="${cpiColor}" stroke-width="3.5"
                            stroke-dasharray="${(2 * Math.PI * 14).toFixed(1)}"
                            stroke-dashoffset="${((1 - Math.min(1.3, cpi) / 1.3) * 2 * Math.PI * 14).toFixed(1)}"
                            stroke-linecap="round" transform="rotate(-90 18 18)"/>
                  </svg>
                  <div>
                    <div style="font-size:9px; font-weight:800; color:var(--color-text-muted); text-transform:uppercase; letter-spacing:0.5px;">Cost (CPI)</div>
                    <div style="font-size:18px; font-weight:900; color:${cpiColor}; line-height:1.2; font-family:var(--mono);">${cpiVal}</div>
                    <div style="font-size:9px; color:var(--color-text-faint); margin-top:1px;">${cpi >= 1.0 ? 'Under Budget' : cpi >= 0.85 ? 'Near Budget' : 'Over Budget'}</div>
                  </div>
                </div>

                <!-- % Complete -->
                <div style="background:var(--color-surface-2); border:1px solid var(--color-border-faint); border-radius:12px; padding:12px 14px; display:flex; align-items:center; gap:12px; transition:all 0.2s; cursor:default;"
                  onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.08)';"
                  onmouseout="this.style.transform='none'; this.style.boxShadow='none';">
                  <svg width="36" height="36" viewBox="0 0 36 36" style="flex-shrink:0;" aria-hidden="true">
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--color-surface-3)" stroke-width="3.5"/>
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--green)" stroke-width="3.5"
                            stroke-dasharray="${(2 * Math.PI * 14).toFixed(1)}"
                            stroke-dashoffset="${((1 - avgProgress / 100) * 2 * Math.PI * 14).toFixed(1)}"
                            stroke-linecap="round" transform="rotate(-90 18 18)"/>
                  </svg>
                  <div>
                    <div style="font-size:9px; font-weight:800; color:var(--color-text-muted); text-transform:uppercase; letter-spacing:0.5px;">Avg. Progress</div>
                    <div style="font-size:18px; font-weight:900; color:var(--green); line-height:1.2; font-family:var(--mono);">${avgProgress}%</div>
                    <div style="font-size:9px; color:var(--color-text-faint); margin-top:1px;">${tasks.filter(t => t.status === 'Completed').length} of ${tasks.length} done</div>
                  </div>
                </div>

                <!-- Remaining Tasks -->
                <div style="background:var(--color-surface-2); border:1px solid var(--color-border-faint); border-radius:12px; padding:12px 14px; display:flex; align-items:center; gap:12px; transition:all 0.2s; cursor:default;"
                  onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.08)';"
                  onmouseout="this.style.transform='none'; this.style.boxShadow='none';">
                  <svg width="36" height="36" viewBox="0 0 36 36" style="flex-shrink:0;" aria-hidden="true">
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--color-surface-3)" stroke-width="3.5"/>
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--amber)" stroke-width="3.5"
                            stroke-dasharray="${(2 * Math.PI * 14).toFixed(1)}"
                            stroke-dashoffset="${(remainingTasksCount / (tasks.length || 1) * 2 * Math.PI * 14).toFixed(1)}"
                            stroke-linecap="round" transform="rotate(-90 18 18)"/>
                  </svg>
                  <div>
                    <div style="font-size:9px; font-weight:800; color:var(--color-text-muted); text-transform:uppercase; letter-spacing:0.5px;">Remaining</div>
                    <div style="font-size:18px; font-weight:900; color:var(--amber); line-height:1.2; font-family:var(--mono);">${remainingTasksCount}</div>
                    <div style="font-size:9px; color:var(--color-text-faint); margin-top:1px;">tasks to complete</div>
                  </div>
                </div>

              </div>
            </div>
          `;

          // Setup Score Breakdown toggle listener
          setTimeout(() => {
            const btn = gCard.querySelector('#health-breakdown-btn');
            const panel = gCard.querySelector('#health-breakdown-panel');
            if (btn && panel) {
              btn.onclick = () => {
                const open = panel.style.display !== 'none';
                panel.style.display = open ? 'none' : 'block';
                const icon = open ? 'bar-chart-2' : 'eye-off';
                const label = open ? 'Score Breakdown' : 'Hide Breakdown';
                btn.innerHTML = `<i data-lucide="${icon}" style="width:12px;height:12px;"></i> ${label}`;
                btn.style.background = open ? 'var(--color-surface)' : 'var(--color-primary)';
                btn.style.color = open ? 'var(--color-text)' : 'var(--color-surface)';
                btn.style.borderColor = open ? 'var(--color-border)' : 'var(--color-primary)';
                if (window.lucide) lucide.createIcons(btn);
              };
            }
            if (window.lucide) lucide.createIcons(gCard);
          }, 150);

"""

def main():
    try:
        with open(HTML_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f'Error reading file: {e}')
        sys.exit(1)

    if START_MARKER not in content:
        print(f'ERROR: Start marker not found:\n  {START_MARKER!r}')
        sys.exit(1)
    if END_MARKER not in content:
        print(f'ERROR: End marker not found:\n  {END_MARKER!r}')
        sys.exit(1)
    if content.count(START_MARKER) != 1:
        print(f'ERROR: Start marker found {content.count(START_MARKER)} times (expected 1)')
        sys.exit(1)

    s = content.index(START_MARKER)
    e = content.index(END_MARKER, s)
    new_content = content[:s] + NEW_BLOCK + content[e:]

    try:
        with open(HTML_PATH, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('SUCCESS: Health Gauge widget enhanced.')
    except Exception as ex:
        print(f'Error writing file: {ex}')
        sys.exit(1)

if __name__ == '__main__':
    main()
