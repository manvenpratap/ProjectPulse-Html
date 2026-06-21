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
          const cpiVal = cpi.toFixed(2);
          const cpiColor = cpi >= 1.0 ? 'var(--green)' : cpi >= 0.85 ? 'var(--amber)' : 'var(--red)';

          const overdueTasksCount = tasks.filter(t => { const d = daysDiff(t.dueDate); return d !== null && d < 0 && t.status !== 'Completed' && t.status !== 'Cancelled'; }).length;
          const blockedTasksCount = tasks.filter(t => t.status === 'On Hold').length;
          const remainingTasksCount = tasks.filter(t => t.status !== 'Completed' && t.status !== 'Cancelled').length;

          const gActiveTasks = tasks.filter(t => t.status !== 'Completed' && t.status !== 'Cancelled');
          const gTotalActive = gActiveTasks.length || 1;
          let overduePenaltyWt = 0, blockedPenaltyWt = 0, onHoldPenaltyWt = 0;
          gActiveTasks.forEach(t => {
            const pw = 1 - (parseInt(t.progress, 10) || 0) / 100;
            if (t.dueDate) { const dd = daysDiff(t.dueDate); if (dd !== null && dd < 0) overduePenaltyWt += pw; }
            if (t.status === 'On Hold') onHoldPenaltyWt += pw;
          });
          blockedPenaltyWt = blockedTasksCount > 0 ? gActiveTasks.filter(t => t.status === 'On Hold').reduce((s, t) => s + (1 - (parseInt(t.progress,10)||0)/100), 0) : 0;
          const accurateOverduePenalty = Math.round((overduePenaltyWt / gTotalActive) * 50 * 10) / 10;
          const accurateBlockedPenalty = Math.round((blockedPenaltyWt / gTotalActive) * 30 * 10) / 10;
          const accurateOnHoldPenalty  = Math.round((onHoldPenaltyWt  / gTotalActive) * 20 * 10) / 10;

          function describeArc(cx, cy, r, startDeg, endDeg) {
            const toR = d => d * Math.PI / 180;
            const sx = cx + r * Math.cos(toR(startDeg));
            const sy = cy + r * Math.sin(toR(startDeg));
            const ex = cx + r * Math.cos(toR(endDeg));
            const ey = cy + r * Math.sin(toR(endDeg));
            const large = endDeg - startDeg > 180 ? 1 : 0;
            return `M ${sx} ${sy} A ${r} ${r} 0 ${large} 1 ${ex} ${ey}`;
          }

          const cX = 110, cY = 115;
          const rDial = 80;
          const sWidth = 12;
          const dCircum = Math.PI * rDial;

          const dashHVal = (healthScoreVal / 100) * dCircum;
          const dashSVal = Math.min(1, Math.max(0, spi / 1.5)) * dCircum;
          const dashCVal = Math.min(1, Math.max(0, cpi / 1.5)) * dCircum;

          const phiAngle = (healthScoreVal / 100) * 180;
          const spiAngle = Math.min(1, Math.max(0, spi / 1.5)) * 180;
          const cpiAngle = Math.min(1, Math.max(0, cpi / 1.5)) * 180;

          // Generate speedometer inner scale tick marks dynamically
          let ticksHTML = '';
          for (let i = 0; i <= 10; i++) {
            const angle = 180 + i * 18;
            const rad = angle * Math.PI / 180;
            const isMajor = i % 5 === 0;
            const rStart = isMajor ? 62 : 66;
            const rEnd = 70;
            const x1 = cX + rStart * Math.cos(rad);
            const y1 = cY + rStart * Math.sin(rad);
            const x2 = cX + rEnd * Math.cos(rad);
            const y2 = cY + rEnd * Math.sin(rad);
            ticksHTML += `<line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" stroke="var(--color-border)" stroke-width="${isMajor ? 1.5 : 0.8}" opacity="${isMajor ? 0.7 : 0.4}" />`;
          }

          const gaugeUid = 'ghg-' + gId.replace(/[^a-z0-9]/g,'');

          gCard.querySelector('.cb').innerHTML = `
            <style>
              @keyframes ${gaugeUid}-phi-arc {
                from { stroke-dashoffset: ${dCircum.toFixed(1)}; }
                to   { stroke-dashoffset: ${(dCircum - dashHVal).toFixed(1)}; }
              }
              @keyframes ${gaugeUid}-spi-arc {
                from { stroke-dashoffset: ${dCircum.toFixed(1)}; }
                to   { stroke-dashoffset: ${(dCircum - dashSVal).toFixed(1)}; }
              }
              @keyframes ${gaugeUid}-cpi-arc {
                from { stroke-dashoffset: ${dCircum.toFixed(1)}; }
                to   { stroke-dashoffset: ${(dCircum - dashCVal).toFixed(1)}; }
              }
              @keyframes ${gaugeUid}-fadeIn {
                from { opacity: 0; transform: translateY(6px); }
                to   { opacity: 1; transform: translateY(0); }
              }
              #${gaugeUid}-needle-phi,
              #${gaugeUid}-needle-spi,
              #${gaugeUid}-needle-cpi {
                transition: transform 1.8s cubic-bezier(0.25, 1, 0.5, 1);
                transform-origin: ${cX}px ${cY}px;
                transform-box: view-box;
              }
            </style>

            <div style="display:flex; flex-direction:column; align-items:center; width:100%; gap:24px; padding:8px 0;">

              <!-- ── THREE SIDE-BY-SIDE SPEEDOMETERS ── -->
              <div style="display:flex; flex-direction:row; align-items:center; justify-content:center; width:100%; gap:20px; flex-wrap:wrap;">
                
                <!-- Left Speedometer: PHI -->
                <div style="flex:1; min-width:200px; max-width:240px; position:relative; display:flex; flex-direction:column; align-items:center; background:var(--color-surface-2); border:1px solid var(--color-border-faint); border-radius:16px; padding:20px 16px; box-shadow:0 4px 12px rgba(0,0,0,0.01); transition:all 0.3s ease; cursor:default;"
                     onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 8px 24px rgba(0,0,0,0.04)'; this.style.borderColor='var(--color-border)';"
                     onmouseout="this.style.transform='none'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.01)'; this.style.borderColor='var(--color-border-faint)';">
                  <div style="display:flex; align-items:center; justify-content:center; gap:6px; font-size:10px; font-weight:800; color:var(--color-text-muted); text-transform:uppercase; letter-spacing:1px; margin-bottom:12px; font-family:var(--mono); text-align:center;">
                    <i data-lucide="${healthScoreVal >= 80 ? 'shield-check' : healthScoreVal >= 60 ? 'shield-alert' : 'shield-x'}" style="width:12px; height:12px; color:${healthLabelColor}; flex-shrink:0;"></i>
                    Health Score (PHI)
                  </div>
                  <svg viewBox="0 0 220 140" width="100%" style="display:block; overflow:visible;" aria-label="Health score gauge: ${healthScoreVal}%">
                    <defs>
                      <linearGradient id="${gaugeUid}-grad-phi" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%"   stop-color="#ef4444"/>
                        <stop offset="45%"  stop-color="#f59e0b"/>
                        <stop offset="100%" stop-color="#10b981"/>
                      </linearGradient>
                      <filter id="${gaugeUid}-glow" x="-20%" y="-20%" width="140%" height="140%">
                        <feGaussianBlur stdDeviation="3" result="blur"/>
                        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                      </filter>
                      <filter id="${gaugeUid}-nshadow">
                        <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.2"/>
                      </filter>
                    </defs>

                    <!-- Background track -->
                    <path d="${describeArc(cX, cY, rDial, 180, 359.9)}" fill="none" stroke="var(--color-surface-3)" stroke-width="${sWidth}" stroke-linecap="round" opacity="0.45"/>

                    <!-- Colored fill arc -->
                    <path d="${describeArc(cX, cY, rDial, 180, 359.9)}" fill="none"
                          stroke="url(#${gaugeUid}-grad-phi)" stroke-width="${sWidth}" stroke-linecap="round"
                          stroke-dasharray="${dCircum.toFixed(1)}"
                          stroke-dashoffset="${(dCircum - dashHVal).toFixed(1)}"
                          style="animation:${gaugeUid}-phi-arc 1.6s cubic-bezier(0.34,1.2,0.64,1) forwards;"
                          ${healthScoreVal >= 80 ? `filter="url(#${gaugeUid}-glow)"` : ''}/>

                    <!-- Scale Ticks -->
                    ${ticksHTML}

                    <!-- Sweeping needle (tapered) -->
                    <g id="${gaugeUid}-needle-phi" style="transform: rotate(0deg); transform-origin: ${cX}px ${cY}px; transition: transform 1.6s cubic-bezier(0.25, 1, 0.5, 1);">
                      <path d="M ${cX} ${cY - 3} L ${cX - 72} ${cY} L ${cX} ${cY + 3} Z" fill="var(--color-text)" filter="url(#${gaugeUid}-nshadow)"/>
                    </g>
                    <circle cx="${cX}" cy="${cY}" r="6" fill="${healthLabelColor}" stroke="var(--color-surface)" stroke-width="2" filter="url(#${gaugeUid}-nshadow)"/>
                    <circle cx="${cX}" cy="${cY}" r="2.5" fill="var(--color-surface)"/>

                    <text x="${cX}" y="${cY - 25}" font-size="28" font-weight="900" fill="${healthLabelColor}" text-anchor="middle" font-family="var(--mono)">${healthScoreVal}</text>
                  </svg>
                </div>

                <!-- Middle Speedometer: SPI -->
                <div style="flex:1; min-width:200px; max-width:240px; position:relative; display:flex; flex-direction:column; align-items:center; background:var(--color-surface-2); border:1px solid var(--color-border-faint); border-radius:16px; padding:20px 16px; box-shadow:0 4px 12px rgba(0,0,0,0.01); transition:all 0.3s ease; cursor:default;"
                     onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 8px 24px rgba(0,0,0,0.04)'; this.style.borderColor='var(--color-border)';"
                     onmouseout="this.style.transform='none'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.01)'; this.style.borderColor='var(--color-border-faint)';">
                  <div style="display:flex; align-items:center; justify-content:center; gap:6px; font-size:10px; font-weight:800; color:var(--color-text-muted); text-transform:uppercase; letter-spacing:1px; margin-bottom:12px; font-family:var(--mono); text-align:center;">
                    <i data-lucide="clock" style="width:12px; height:12px; color:${spiColor}; flex-shrink:0;"></i>
                    Schedule Index (SPI)
                  </div>
                  <svg viewBox="0 0 220 140" width="100%" style="display:block; overflow:visible;" aria-label="Schedule Performance Index">
                    <defs>
                      <linearGradient id="${gaugeUid}-grad-spi" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%"   stop-color="#ef4444"/>
                        <stop offset="50%"  stop-color="#f59e0b"/>
                        <stop offset="100%" stop-color="#10b981"/>
                      </linearGradient>
                      <filter id="${gaugeUid}-nshadow">
                        <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.2"/>
                      </filter>
                    </defs>
                    <path d="${describeArc(cX, cY, rDial, 180, 359.9)}" fill="none" stroke="var(--color-surface-3)" stroke-width="${sWidth}" stroke-linecap="round" opacity="0.45"/>
                    <path d="${describeArc(cX, cY, rDial, 180, 359.9)}" fill="none"
                          stroke="url(#${gaugeUid}-grad-spi)" stroke-width="${sWidth}" stroke-linecap="round"
                          stroke-dasharray="${dCircum.toFixed(1)}"
                          stroke-dashoffset="${(dCircum - dashSVal).toFixed(1)}"
                          style="animation:${gaugeUid}-spi-arc 1.6s cubic-bezier(0.34,1.2,0.64,1) forwards;"/>
                    
                    <!-- Scale Ticks -->
                    ${ticksHTML}

                    <!-- Sweeping needle (tapered) -->
                    <g id="${gaugeUid}-needle-spi" style="transform: rotate(0deg); transform-origin: ${cX}px ${cY}px; transition: transform 1.6s cubic-bezier(0.25, 1, 0.5, 1);">
                      <path d="M ${cX} ${cY - 3} L ${cX - 72} ${cY} L ${cX} ${cY + 3} Z" fill="var(--color-text)" filter="url(#${gaugeUid}-nshadow)"/>
                    </g>
                    <circle cx="${cX}" cy="${cY}" r="6" fill="${spiColor}" stroke="var(--color-surface)" stroke-width="2" filter="url(#${gaugeUid}-nshadow)"/>
                    <circle cx="${cX}" cy="${cY}" r="2.5" fill="var(--color-surface)"/>

                    <text x="${cX}" y="${cY - 25}" font-size="28" font-weight="900" fill="${spiColor}" text-anchor="middle" font-family="var(--mono)">${spiVal}</text>
                  </svg>
                </div>

                <!-- Right Speedometer: CPI -->
                <div style="flex:1; min-width:200px; max-width:240px; position:relative; display:flex; flex-direction:column; align-items:center; background:var(--color-surface-2); border:1px solid var(--color-border-faint); border-radius:16px; padding:20px 16px; box-shadow:0 4px 12px rgba(0,0,0,0.01); transition:all 0.3s ease; cursor:default;"
                     onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 8px 24px rgba(0,0,0,0.04)'; this.style.borderColor='var(--color-border)';"
                     onmouseout="this.style.transform='none'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.01)'; this.style.borderColor='var(--color-border-faint)';">
                  <div style="display:flex; align-items:center; justify-content:center; gap:6px; font-size:10px; font-weight:800; color:var(--color-text-muted); text-transform:uppercase; letter-spacing:1px; margin-bottom:12px; font-family:var(--mono); text-align:center;">
                    <i data-lucide="dollar-sign" style="width:12px; height:12px; color:${cpiColor}; flex-shrink:0;"></i>
                    Cost Index (CPI)
                  </div>
                  <svg viewBox="0 0 220 140" width="100%" style="display:block; overflow:visible;" aria-label="Cost Performance Index">
                    <defs>
                      <linearGradient id="${gaugeUid}-grad-cpi" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%"   stop-color="#ef4444"/>
                        <stop offset="50%"  stop-color="#f59e0b"/>
                        <stop offset="100%" stop-color="#10b981"/>
                      </linearGradient>
                      <filter id="${gaugeUid}-nshadow">
                        <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.2"/>
                      </filter>
                    </defs>
                    <path d="${describeArc(cX, cY, rDial, 180, 359.9)}" fill="none" stroke="var(--color-surface-3)" stroke-width="${sWidth}" stroke-linecap="round" opacity="0.45"/>
                    <path d="${describeArc(cX, cY, rDial, 180, 359.9)}" fill="none"
                          stroke="url(#${gaugeUid}-grad-cpi)" stroke-width="${sWidth}" stroke-linecap="round"
                          stroke-dasharray="${dCircum.toFixed(1)}"
                          stroke-dashoffset="${(dCircum - dashCVal).toFixed(1)}"
                          style="animation:${gaugeUid}-cpi-arc 1.6s cubic-bezier(0.34,1.2,0.64,1) forwards;"/>
                    
                    <!-- Scale Ticks -->
                    ${ticksHTML}

                    <!-- Sweeping needle (tapered) -->
                    <g id="${gaugeUid}-needle-cpi" style="transform: rotate(0deg); transform-origin: ${cX}px ${cY}px; transition: transform 1.6s cubic-bezier(0.25, 1, 0.5, 1);">
                      <path d="M ${cX} ${cY - 3} L ${cX - 72} ${cY} L ${cX} ${cY + 3} Z" fill="var(--color-text)" filter="url(#${gaugeUid}-nshadow)"/>
                    </g>
                    <circle cx="${cX}" cy="${cY}" r="6" fill="${cpiColor}" stroke="var(--color-surface)" stroke-width="2" filter="url(#${gaugeUid}-nshadow)"/>
                    <circle cx="${cX}" cy="${cY}" r="2.5" fill="var(--color-surface)"/>

                    <text x="${cX}" y="${cY - 25}" font-size="28" font-weight="900" fill="${cpiColor}" text-anchor="middle" font-family="var(--mono)">${cpiVal}</text>
                  </svg>
                </div>

              </div>

              <!-- ── STATUS STRIP ── -->
              <div style="display:flex; align-items:center; justify-content:center; gap:8px; flex-wrap:wrap; width:100%; animation: ${gaugeUid}-fadeIn 0.5s 0.3s both;">
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
                    <span style="font-size:9px; font-weight:800; text-transform:uppercase; letter-spacing:1px; color:var(--color-text-faint); font-family:var(--mono);">Impact (Max)</span>
                  </div>
                  <!-- Rows -->
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:5px 0;">
                    <span style="color:var(--color-text); font-weight:700;">Base Score</span>
                    <span style="font-family:var(--mono); color:var(--green); font-weight:700;">+100.0</span>
                  </div>
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:5px 0; border-top:1px dashed var(--color-border-faint);">
                    <span style="color:var(--color-text-muted);">Overdue Penalty (Weighted)</span>
                    <span style="font-family:var(--mono); color:${accurateOverduePenalty > 0 ? 'var(--red)' : 'var(--color-text-faint)'}; font-weight:700;">-${accurateOverduePenalty} (max 50)</span>
                  </div>
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:5px 0; border-top:1px dashed var(--color-border-faint);">
                    <span style="color:var(--color-text-muted);">Blocked Penalty (Weighted)</span>
                    <span style="font-family:var(--mono); color:${accurateBlockedPenalty > 0 ? 'var(--red)' : 'var(--color-text-faint)'}; font-weight:700;">-${accurateBlockedPenalty} (max 30)</span>
                  </div>
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:5px 0; border-top:1px dashed var(--color-border-faint);">
                    <span style="color:var(--color-text-muted);">On Hold Penalty (Weighted)</span>
                    <span style="font-family:var(--mono); color:${accurateOnHoldPenalty > 0 ? 'var(--red)' : 'var(--color-text-faint)'}; font-weight:700;">-${accurateOnHoldPenalty} (max 20)</span>
                  </div>
                  <!-- Total row -->
                  <div style="display:flex; justify-content:space-between; align-items:center; padding-top:8px; border-top:1px solid var(--color-border-faint); margin-top:6px;">
                    <span style="font-weight:800; color:var(--color-text);">Composite PHI Score</span>
                    <span style="font-family:var(--mono); color:${healthLabelColor}; font-weight:900; font-size:12px;">${healthScoreVal} / 100</span>
                  </div>
                </div>
              </div>

              <!-- ── LOWER METRIC CARDS ── -->
              <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; width:100%; animation: ${gaugeUid}-fadeIn 0.5s 0.4s both;">
                
                <!-- Schedule card -->
                <div style="background:var(--color-surface-2); border:1px solid var(--color-border-faint); border-radius:12px; padding:12px 14px; display:flex; align-items:center; gap:12px; transition:all 0.2s; cursor:default;"
                  onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.08)';"
                  onmouseout="this.style.transform='none'; this.style.boxShadow='none';">
                  <svg width="36" height="36" viewBox="0 0 36 36" style="flex-shrink:0;" aria-hidden="true">
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--color-surface-3)" stroke-width="3.5"/>
                    <circle cx="18" cy="18" r="14" fill="none" stroke="${spiColor}" stroke-width="3.5"
                            stroke-dasharray="${(2 * Math.PI * 14).toFixed(1)}"
                            stroke-dashoffset="${((1 - Math.min(1, spi)) * 2 * Math.PI * 14).toFixed(1)}"
                            stroke-linecap="round" transform="rotate(-90 18 18)"/>
                  </svg>
                  <div>
                    <div style="font-size:9px; font-weight:800; color:var(--color-text-muted); text-transform:uppercase; letter-spacing:0.5px;">Schedule (SPI)</div>
                    <div style="font-size:18px; font-weight:900; color:${spiColor}; line-height:1.2; font-family:var(--mono);">${spiVal}</div>
                    <div style="font-size:9px; color:var(--color-text-faint); margin-top:1px;">${spi >= 1.0 ? 'On Schedule' : spi >= 0.85 ? 'Behind Schedule' : 'Critical Delay'}</div>
                  </div>
                </div>

                <!-- Cost card -->
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
                            stroke-dashoffset="${((1 - remainingTasksCount / (tasks.length || 1)) * 2 * Math.PI * 14).toFixed(1)}"
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

          // Setup Score Breakdown toggle listener and needle animations
          setTimeout(() => {
            const needlePhi = gCard.querySelector('#' + gaugeUid + '-needle-phi');
            const needleSpi = gCard.querySelector('#' + gaugeUid + '-needle-spi');
            const needleCpi = gCard.querySelector('#' + gaugeUid + '-needle-cpi');
            if (needlePhi) needlePhi.style.transform = `rotate(${phiAngle}deg)`;
            if (needleSpi) needleSpi.style.transform = `rotate(${spiAngle}deg)`;
            if (needleCpi) needleCpi.style.transform = `rotate(${cpiAngle}deg)`;

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
