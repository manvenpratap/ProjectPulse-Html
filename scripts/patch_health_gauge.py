#!/usr/bin/env python3
"""
patch_health_gauge.py
Replaces the Project Health Gauge widget (lines 27096–27504) with a
premium redesigned version:
  - Unique SVG filter IDs per gauge instance
  - Score text repositioned below the arc (no needle overlap)
  - CSS-only hover states (no inline onmouseover/onmouseout)
  - Premium status strip with sparkline pill badges
  - Enhanced breakdown panel with stacked bar visualization
  - Entrance animation on the whole gauge block
"""

import sys, os, re

HTML_FILE = os.path.join(os.path.dirname(__file__), '..', 'projectpulse.html')

# ── Sentinel markers ───────────────────────────────────────────────────────────
START_MARKER = "// ── CARD 2: Project Health Gauge ──"
END_MARKER   = "// ── CARD 3: Schedule"

NEW_BLOCK = r"""// ── CARD 2: Project Health Gauge ──
          const gId = 'dash-health-gauge';
          const gSpan = (P.widgetSpans && P.widgetSpans[gId]) || 2;
          const gCard = mkCC('Project Health Gauge', 'Composite Rating & Performance Index', gId, '', 'standard', '<b>Project Health Gauge:</b> A premium multi-ring composite gauge displaying the weighted health index, schedule performance (SPI), completion rate, and live penalty breakdown.', 'View Explanation', 'gauge');
          gCard.style.gridColumn = `span ${gSpan}`;
          grid.appendChild(gCard);

          // ── Calculations for Health Gauge ──
          const healthScoreVal  = getHealthScore(tasks);
          const healthLabel     = healthScoreVal >= 80 ? 'Healthy' : healthScoreVal >= 60 ? 'At Risk' : 'Critical';
          const healthLabelColor = healthScoreVal >= 80 ? 'var(--green)' : healthScoreVal >= 60 ? 'var(--amber)' : 'var(--red)';
          const healthBg        = healthScoreVal >= 80 ? 'rgba(16,185,129,0.10)' : healthScoreVal >= 60 ? 'rgba(245,158,11,0.10)' : 'rgba(239,68,68,0.10)';

          const spiVal   = spi.toFixed(2);
          const spiColor = spi  >= 0.95 ? 'var(--green)' : spi  >= 0.80 ? 'var(--amber)' : 'var(--red)';
          const cpiVal   = cpi.toFixed(2);
          const cpiColor = cpi  >= 1.00 ? 'var(--green)' : cpi  >= 0.85 ? 'var(--amber)' : 'var(--red)';

          const overdueTasksCount   = tasks.filter(t => { const d = daysDiff(t.dueDate); return d !== null && d < 0 && t.status !== 'Completed' && t.status !== 'Cancelled'; }).length;
          const blockedTasksCount   = tasks.filter(t => t.status === 'On Hold').length;
          const remainingTasksCount = tasks.filter(t => t.status !== 'Completed' && t.status !== 'Cancelled').length;

          const gActiveTasks = tasks.filter(t => t.status !== 'Completed' && t.status !== 'Cancelled');
          const gTotalActive = gActiveTasks.length || 1;
          let overduePenaltyWt = 0, blockedPenaltyWt = 0, onHoldPenaltyWt = 0;
          gActiveTasks.forEach(t => {
            const pw = 1 - (parseInt(t.progress, 10) || 0) / 100;
            if (t.dueDate) { const dd = daysDiff(t.dueDate); if (dd !== null && dd < 0) overduePenaltyWt += pw; }
            if (t.status === 'On Hold') onHoldPenaltyWt += pw;
          });
          blockedPenaltyWt = blockedTasksCount > 0
            ? gActiveTasks.filter(t => t.status === 'On Hold').reduce((s, t) => s + (1 - (parseInt(t.progress,10)||0)/100), 0)
            : 0;
          const accurateOverduePenalty = Math.round((overduePenaltyWt / gTotalActive) * 50 * 10) / 10;
          const accurateBlockedPenalty = Math.round((blockedPenaltyWt / gTotalActive) * 30 * 10) / 10;
          const accurateOnHoldPenalty  = Math.round((onHoldPenaltyWt  / gTotalActive) * 20 * 10) / 10;

          // ── Shared SVG helpers ──
          function describeArc(cx, cy, r, startDeg, endDeg) {
            const toR = d => d * Math.PI / 180;
            const sx = cx + r * Math.cos(toR(startDeg)); const sy = cy + r * Math.sin(toR(startDeg));
            const ex = cx + r * Math.cos(toR(endDeg));   const ey = cy + r * Math.sin(toR(endDeg));
            const large = endDeg - startDeg > 180 ? 1 : 0;
            return `M ${sx} ${sy} A ${r} ${r} 0 ${large} 1 ${ex} ${ey}`;
          }

          const cX = 110, cY = 110;   // pivot
          const rDial = 80, sWidth = 13;
          const dCircum = Math.PI * rDial;

          const dashHVal = (healthScoreVal / 100) * dCircum;
          const dashSVal = Math.min(1, Math.max(0, spi / 1.5)) * dCircum;
          const dashCVal = Math.min(1, Math.max(0, cpi / 1.5)) * dCircum;

          const phiAngle = (healthScoreVal / 100) * 180;
          const spiAngle = Math.min(1, Math.max(0, spi / 1.5)) * 180;
          const cpiAngle = Math.min(1, Math.max(0, cpi / 1.5)) * 180;

          const gaugeUid = 'ghg-' + gId.replace(/[^a-z0-9]/g,'');

          // Scale ticks
          let ticksHTML = '';
          for (let i = 0; i <= 10; i++) {
            const angle = 180 + i * 18;
            const rad = angle * Math.PI / 180;
            const isMajor = i % 5 === 0;
            const rS = isMajor ? 60 : 65, rE = 71;
            const x1 = cX + rS * Math.cos(rad), y1 = cY + rS * Math.sin(rad);
            const x2 = cX + rE * Math.cos(rad), y2 = cY + rE * Math.sin(rad);
            ticksHTML += `<line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" stroke="var(--color-border)" stroke-width="${isMajor?1.5:0.8}" opacity="${isMajor?0.6:0.3}"/>`;
          }

          // Helper: build one speedometer SVG
          function makeGaugeSVG(uid, gradId, dashVal, angle, needleId, scoreText, color, arcAnim) {
            return `
              <svg viewBox="0 0 220 135" width="100%" style="display:block;overflow:visible;" aria-label="Gauge: ${scoreText}">
                <defs>
                  <linearGradient id="${gradId}" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%"   stop-color="#ef4444"/>
                    <stop offset="45%"  stop-color="#f59e0b"/>
                    <stop offset="100%" stop-color="#10b981"/>
                  </linearGradient>
                  <!-- Unique filter IDs per gauge instance -->
                  <filter id="${uid}-glow" x="-20%" y="-20%" width="140%" height="140%">
                    <feGaussianBlur stdDeviation="3" result="blur"/>
                    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                  </filter>
                  <filter id="${uid}-nshadow">
                    <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.25"/>
                  </filter>
                </defs>

                <!-- Background arc track -->
                <path d="${describeArc(cX, cY, rDial, 180, 359.9)}"
                      fill="none" stroke="var(--color-surface-3)" stroke-width="${sWidth}"
                      stroke-linecap="round" opacity="0.5"/>

                <!-- Coloured fill arc -->
                <path d="${describeArc(cX, cY, rDial, 180, 359.9)}"
                      fill="none" stroke="url(#${gradId})" stroke-width="${sWidth}"
                      stroke-linecap="round"
                      stroke-dasharray="${dCircum.toFixed(1)}"
                      stroke-dashoffset="${(dCircum - dashVal).toFixed(1)}"
                      style="animation:${arcAnim} 1.6s cubic-bezier(0.34,1.2,0.64,1) forwards;"/>

                <!-- Scale ticks -->
                ${ticksHTML}

                <!-- Zone labels: Low / Mid / High -->
                <text x="${cX - 66}" y="${cY + 14}" font-size="7" fill="var(--color-text-faint)" font-family="var(--mono)" opacity="0.7">LOW</text>
                <text x="${cX - 4}"  y="${cY - 78}" font-size="7" fill="var(--color-text-faint)" font-family="var(--mono)" opacity="0.7" text-anchor="middle">MID</text>
                <text x="${cX + 54}" y="${cY + 14}" font-size="7" fill="var(--color-text-faint)" font-family="var(--mono)" opacity="0.7">HIGH</text>

                <!-- Tapered needle -->
                <g id="${needleId}"
                   style="transform:rotate(0deg);transform-origin:${cX}px ${cY}px;transform-box:view-box;transition:transform 1.8s cubic-bezier(0.25,1,0.5,1);">
                  <path d="M ${cX} ${cY-3} L ${cX-74} ${cY} L ${cX} ${cY+3} Z"
                        fill="var(--color-text)" filter="url(#${uid}-nshadow)"/>
                </g>

                <!-- Pivot cap -->
                <circle cx="${cX}" cy="${cY}" r="7" fill="${color}"
                        stroke="var(--color-surface)" stroke-width="2.5"
                        filter="url(#${uid}-nshadow)"/>
                <circle cx="${cX}" cy="${cY}" r="3" fill="var(--color-surface)"/>

                <!-- Score text BELOW the arc (y = cY + 20 so it sits in the open space) -->
                <text x="${cX}" y="${cY + 22}"
                      font-size="26" font-weight="900" fill="${color}"
                      text-anchor="middle" dominant-baseline="auto"
                      font-family="var(--mono)">${scoreText}</text>
              </svg>
            `;
          }

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
                from { opacity:0; transform:translateY(8px); }
                to   { opacity:1; transform:translateY(0); }
              }

              /* CSS hover on gauge cards — no inline JS */
              .ghg-dial-card {
                flex: 1; min-width: 190px; max-width: 240px;
                position: relative; display: flex; flex-direction: column; align-items: center;
                background: var(--color-surface-2);
                border: 1px solid var(--color-border-faint);
                border-radius: 16px; padding: 18px 14px 10px;
                transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1),
                            box-shadow 0.3s ease, border-color 0.2s ease;
                cursor: default;
              }
              .ghg-dial-card:hover {
                transform: translateY(-4px) scale(1.01);
                box-shadow: 0 12px 28px rgba(0,0,0,0.07);
                border-color: var(--color-border);
              }
              .ghg-dial-label {
                display: flex; align-items: center; justify-content: center;
                gap: 5px; font-size: 9px; font-weight: 800;
                color: var(--color-text-muted); text-transform: uppercase;
                letter-spacing: 1px; margin-bottom: 8px;
                font-family: var(--mono); text-align: center;
              }
              /* Metric mini-cards */
              .ghg-metric-card {
                background: var(--color-surface-2);
                border: 1px solid var(--color-border-faint);
                border-radius: 12px; padding: 12px 14px;
                display: flex; align-items: center; gap: 12px;
                transition: transform 0.25s cubic-bezier(0.34,1.56,0.64,1),
                            box-shadow 0.25s ease;
                cursor: default;
              }
              .ghg-metric-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 18px rgba(0,0,0,0.07);
              }
              /* Breakdown button */
              .ghg-breakdown-btn {
                font-size: 10px; padding: 6px 16px; border-radius: 20px;
                cursor: pointer; font-weight: 700;
                border: 1px solid var(--color-border);
                background: var(--color-surface); color: var(--color-text);
                display: inline-flex; align-items: center; gap: 6px;
                transition: background 0.2s ease, border-color 0.2s ease, color 0.2s ease;
              }
              .ghg-breakdown-btn:hover {
                background: var(--color-primary-highlight);
                border-color: var(--color-primary);
              }
              /* Breakdown bar segments */
              .ghg-bar-segment {
                height: 100%; border-radius: 3px;
                transition: width 0.8s cubic-bezier(0.16,1,0.3,1);
              }
            </style>

            <div style="display:flex;flex-direction:column;align-items:center;width:100%;gap:20px;padding:4px 0;animation:${gaugeUid}-fadeIn 0.45s ease both;">

              <!-- ── THREE SPEEDOMETERS ── -->
              <div style="display:flex;flex-direction:row;align-items:stretch;justify-content:center;width:100%;gap:16px;flex-wrap:wrap;">

                <!-- PHI gauge -->
                <div class="ghg-dial-card" style="border-top:3px solid ${healthLabelColor};">
                  <div class="ghg-dial-label">
                    <i data-lucide="${healthScoreVal >= 80 ? 'shield-check' : healthScoreVal >= 60 ? 'shield-alert' : 'shield-x'}" style="width:11px;height:11px;color:${healthLabelColor};flex-shrink:0;"></i>
                    Health Score (PHI)
                  </div>
                  ${makeGaugeSVG(
                    gaugeUid+'-phi',
                    gaugeUid+'-grad-phi',
                    dashHVal, phiAngle,
                    gaugeUid+'-needle-phi',
                    healthScoreVal,
                    healthLabelColor,
                    gaugeUid+'-phi-arc'
                  )}
                  <div style="font-size:9px;font-weight:700;color:${healthLabelColor};letter-spacing:0.5px;text-transform:uppercase;margin-top:2px;">${healthLabel}</div>
                </div>

                <!-- SPI gauge -->
                <div class="ghg-dial-card" style="border-top:3px solid ${spiColor};">
                  <div class="ghg-dial-label">
                    <i data-lucide="clock" style="width:11px;height:11px;color:${spiColor};flex-shrink:0;"></i>
                    Schedule Index (SPI)
                  </div>
                  ${makeGaugeSVG(
                    gaugeUid+'-spi',
                    gaugeUid+'-grad-spi',
                    dashSVal, spiAngle,
                    gaugeUid+'-needle-spi',
                    spiVal,
                    spiColor,
                    gaugeUid+'-spi-arc'
                  )}
                  <div style="font-size:9px;font-weight:700;color:${spiColor};letter-spacing:0.5px;text-transform:uppercase;margin-top:2px;">${spi >= 0.95 ? 'On Schedule' : spi >= 0.80 ? 'Behind' : 'Critical'}</div>
                </div>

                <!-- CPI gauge -->
                <div class="ghg-dial-card" style="border-top:3px solid ${cpiColor};">
                  <div class="ghg-dial-label">
                    <i data-lucide="coins" style="width:11px;height:11px;color:${cpiColor};flex-shrink:0;"></i>
                    Cost Index (CPI)
                  </div>
                  ${makeGaugeSVG(
                    gaugeUid+'-cpi',
                    gaugeUid+'-grad-cpi',
                    dashCVal, cpiAngle,
                    gaugeUid+'-needle-cpi',
                    cpiVal,
                    cpiColor,
                    gaugeUid+'-cpi-arc'
                  )}
                  <div style="font-size:9px;font-weight:700;color:${cpiColor};letter-spacing:0.5px;text-transform:uppercase;margin-top:2px;">${cpi >= 1.0 ? 'Under Budget' : cpi >= 0.85 ? 'Near Budget' : 'Over Budget'}</div>
                </div>

              </div>

              <!-- ── STATUS BADGE STRIP ── -->
              <div style="display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap;width:100%;animation:${gaugeUid}-fadeIn 0.5s 0.2s both;">
                <!-- Overall health -->
                <div style="display:flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;background:${healthBg};border:1px solid ${healthLabelColor};font-size:10px;font-weight:800;color:${healthLabelColor};">
                  <i data-lucide="${healthScoreVal >= 80 ? 'shield-check' : healthScoreVal >= 60 ? 'shield-alert' : 'shield-x'}" style="width:11px;height:11px;"></i>
                  ${healthLabel} · ${healthScoreVal}/100
                </div>
                <!-- Overdue -->
                ${overdueTasksCount > 0 ? `
                <div style="display:flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.3);font-size:10px;font-weight:800;color:var(--red);">
                  <i data-lucide="clock-alert" style="width:11px;height:11px;"></i>
                  ${overdueTasksCount} Overdue
                </div>` : `
                <div style="display:flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.2);font-size:10px;font-weight:700;color:var(--green);">
                  <i data-lucide="check-circle" style="width:11px;height:11px;"></i>
                  No Overdue
                </div>`}
                <!-- Blocked -->
                ${blockedTasksCount > 0 ? `
                <div style="display:flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;background:rgba(245,158,11,0.08);border:1px solid rgba(245,158,11,0.3);font-size:10px;font-weight:800;color:var(--amber);">
                  <i data-lucide="ban" style="width:11px;height:11px;"></i>
                  ${blockedTasksCount} Blocked
                </div>` : ''}
                <!-- SPI pill -->
                <div style="display:flex;align-items:center;gap:4px;padding:5px 12px;border-radius:20px;background:var(--color-surface-2);border:1px solid var(--color-border-faint);font-size:10px;font-weight:700;color:var(--color-text-muted);">
                  <i data-lucide="${spi >= 0.95 ? 'trending-up' : 'trending-down'}" style="width:11px;height:11px;color:${spiColor};"></i>
                  SPI ${spiVal} · CPI ${cpiVal}
                </div>
              </div>

              <!-- ── SCORE BREAKDOWN TOGGLE ── -->
              <button class="ghg-breakdown-btn" id="${gaugeUid}-breakdown-btn">
                <i data-lucide="bar-chart-2" style="width:12px;height:12px;"></i> Score Breakdown
              </button>

              <!-- ── BREAKDOWN PANEL ── -->
              <div id="${gaugeUid}-breakdown-panel" style="width:100%;display:none;animation:${gaugeUid}-fadeIn 0.25s ease;">
                <div style="background:var(--color-surface-2);padding:16px;border-radius:14px;border:1px solid var(--color-border-faint);display:flex;flex-direction:column;gap:12px;">

                  <!-- Stacked visual bar -->
                  <div style="display:flex;flex-direction:column;gap:4px;">
                    <div style="font-size:8px;font-weight:800;text-transform:uppercase;letter-spacing:1px;color:var(--color-text-faint);font-family:var(--mono);">Composite Score Breakdown</div>
                    <div style="height:10px;background:var(--color-surface-3);border-radius:5px;overflow:hidden;display:flex;gap:1px;">
                      <div class="ghg-bar-segment" style="width:${Math.max(0, 100 - accurateOverduePenalty - accurateBlockedPenalty - accurateOnHoldPenalty)}%;background:${healthLabelColor};"></div>
                      <div class="ghg-bar-segment" style="width:${accurateOverduePenalty}%;background:var(--red);opacity:0.7;"></div>
                      <div class="ghg-bar-segment" style="width:${accurateBlockedPenalty}%;background:var(--amber);opacity:0.7;"></div>
                      <div class="ghg-bar-segment" style="width:${accurateOnHoldPenalty}%;background:#a78bfa;opacity:0.7;"></div>
                    </div>
                    <div style="display:flex;gap:12px;font-size:8px;font-weight:700;color:var(--color-text-faint);">
                      <span style="display:flex;align-items:center;gap:3px;"><span style="width:8px;height:8px;border-radius:2px;background:${healthLabelColor};display:inline-block;"></span>Score</span>
                      <span style="display:flex;align-items:center;gap:3px;"><span style="width:8px;height:8px;border-radius:2px;background:var(--red);opacity:0.7;display:inline-block;"></span>Overdue</span>
                      <span style="display:flex;align-items:center;gap:3px;"><span style="width:8px;height:8px;border-radius:2px;background:var(--amber);opacity:0.7;display:inline-block;"></span>Blocked</span>
                      <span style="display:flex;align-items:center;gap:3px;"><span style="width:8px;height:8px;border-radius:2px;background:#a78bfa;opacity:0.7;display:inline-block;"></span>On Hold</span>
                    </div>
                  </div>

                  <!-- Component rows -->
                  <div style="display:flex;flex-direction:column;gap:0;border-top:1px solid var(--color-border-faint);padding-top:10px;">
                    <div style="display:flex;justify-content:space-between;align-items:center;font-size:9px;font-weight:800;text-transform:uppercase;letter-spacing:1px;color:var(--color-text-faint);font-family:var(--mono);padding-bottom:6px;margin-bottom:2px;border-bottom:1px solid var(--color-border-faint);">
                      <span>Component</span><span>Impact (Max)</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;align-items:center;padding:5px 0;font-size:11px;">
                      <span style="font-weight:700;color:var(--color-text);">Base Score</span>
                      <span style="font-family:var(--mono);color:var(--green);font-weight:700;">+100.0</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;align-items:center;padding:5px 0;border-top:1px dashed var(--color-border-faint);font-size:11px;">
                      <span style="color:var(--color-text-muted);">Overdue Penalty (Weighted)</span>
                      <span style="font-family:var(--mono);color:${accurateOverduePenalty > 0 ? 'var(--red)' : 'var(--color-text-faint)'};font-weight:700;">-${accurateOverduePenalty} (max 50)</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;align-items:center;padding:5px 0;border-top:1px dashed var(--color-border-faint);font-size:11px;">
                      <span style="color:var(--color-text-muted);">Blocked Penalty (Weighted)</span>
                      <span style="font-family:var(--mono);color:${accurateBlockedPenalty > 0 ? 'var(--red)' : 'var(--color-text-faint)'};font-weight:700;">-${accurateBlockedPenalty} (max 30)</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;align-items:center;padding:5px 0;border-top:1px dashed var(--color-border-faint);font-size:11px;">
                      <span style="color:var(--color-text-muted);">On Hold Penalty (Weighted)</span>
                      <span style="font-family:var(--mono);color:${accurateOnHoldPenalty > 0 ? 'var(--red)' : 'var(--color-text-faint)'};font-weight:700;">-${accurateOnHoldPenalty} (max 20)</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;align-items:center;padding-top:8px;border-top:2px solid var(--color-border-faint);margin-top:4px;font-size:12px;">
                      <span style="font-weight:800;color:var(--color-text);">Composite PHI Score</span>
                      <span style="font-family:var(--mono);color:${healthLabelColor};font-weight:900;">${healthScoreVal} / 100</span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- ── LOWER METRIC CARDS ── -->
              <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;width:100%;animation:${gaugeUid}-fadeIn 0.5s 0.35s both;">

                <!-- Schedule -->
                <div class="ghg-metric-card">
                  <svg width="38" height="38" viewBox="0 0 36 36" style="flex-shrink:0;" aria-hidden="true">
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--color-surface-3)" stroke-width="3.5"/>
                    <circle cx="18" cy="18" r="14" fill="none" stroke="${spiColor}" stroke-width="3.5"
                            stroke-dasharray="${(2*Math.PI*14).toFixed(1)}"
                            stroke-dashoffset="${((1-Math.min(1,spi))*2*Math.PI*14).toFixed(1)}"
                            stroke-linecap="round" transform="rotate(-90 18 18)"/>
                  </svg>
                  <div>
                    <div style="font-size:8px;font-weight:800;color:var(--color-text-muted);text-transform:uppercase;letter-spacing:0.5px;">Schedule (SPI)</div>
                    <div style="font-size:18px;font-weight:900;color:${spiColor};line-height:1.2;font-family:var(--mono);">${spiVal}</div>
                    <div style="font-size:9px;color:var(--color-text-faint);margin-top:1px;">${spi >= 1.0 ? 'On Schedule' : spi >= 0.85 ? 'Behind Schedule' : 'Critical Delay'}</div>
                  </div>
                </div>

                <!-- Cost -->
                <div class="ghg-metric-card">
                  <svg width="38" height="38" viewBox="0 0 36 36" style="flex-shrink:0;" aria-hidden="true">
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--color-surface-3)" stroke-width="3.5"/>
                    <circle cx="18" cy="18" r="14" fill="none" stroke="${cpiColor}" stroke-width="3.5"
                            stroke-dasharray="${(2*Math.PI*14).toFixed(1)}"
                            stroke-dashoffset="${((1-Math.min(1.3,cpi)/1.3)*2*Math.PI*14).toFixed(1)}"
                            stroke-linecap="round" transform="rotate(-90 18 18)"/>
                  </svg>
                  <div>
                    <div style="font-size:8px;font-weight:800;color:var(--color-text-muted);text-transform:uppercase;letter-spacing:0.5px;">Cost (CPI)</div>
                    <div style="font-size:18px;font-weight:900;color:${cpiColor};line-height:1.2;font-family:var(--mono);">${cpiVal}</div>
                    <div style="font-size:9px;color:var(--color-text-faint);margin-top:1px;">${cpi >= 1.0 ? 'Under Budget' : cpi >= 0.85 ? 'Near Budget' : 'Over Budget'}</div>
                  </div>
                </div>

                <!-- Avg Progress -->
                <div class="ghg-metric-card">
                  <svg width="38" height="38" viewBox="0 0 36 36" style="flex-shrink:0;" aria-hidden="true">
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--color-surface-3)" stroke-width="3.5"/>
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--green)" stroke-width="3.5"
                            stroke-dasharray="${(2*Math.PI*14).toFixed(1)}"
                            stroke-dashoffset="${((1-avgProgress/100)*2*Math.PI*14).toFixed(1)}"
                            stroke-linecap="round" transform="rotate(-90 18 18)"/>
                  </svg>
                  <div>
                    <div style="font-size:8px;font-weight:800;color:var(--color-text-muted);text-transform:uppercase;letter-spacing:0.5px;">Avg. Progress</div>
                    <div style="font-size:18px;font-weight:900;color:var(--green);line-height:1.2;font-family:var(--mono);">${avgProgress}%</div>
                    <div style="font-size:9px;color:var(--color-text-faint);margin-top:1px;">${tasks.filter(t=>t.status==='Completed').length} of ${tasks.length} done</div>
                  </div>
                </div>

                <!-- Remaining -->
                <div class="ghg-metric-card">
                  <svg width="38" height="38" viewBox="0 0 36 36" style="flex-shrink:0;" aria-hidden="true">
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--color-surface-3)" stroke-width="3.5"/>
                    <circle cx="18" cy="18" r="14" fill="none" stroke="var(--amber)" stroke-width="3.5"
                            stroke-dasharray="${(2*Math.PI*14).toFixed(1)}"
                            stroke-dashoffset="${((1-remainingTasksCount/(tasks.length||1))*2*Math.PI*14).toFixed(1)}"
                            stroke-linecap="round" transform="rotate(-90 18 18)"/>
                  </svg>
                  <div>
                    <div style="font-size:8px;font-weight:800;color:var(--color-text-muted);text-transform:uppercase;letter-spacing:0.5px;">Remaining</div>
                    <div style="font-size:18px;font-weight:900;color:var(--amber);line-height:1.2;font-family:var(--mono);">${remainingTasksCount}</div>
                    <div style="font-size:9px;color:var(--color-text-faint);margin-top:1px;">tasks to complete</div>
                  </div>
                </div>

              </div>
            </div>
          `;

          // Needle animations + breakdown toggle
          setTimeout(() => {
            // Animate needles to final angle
            const np = gCard.querySelector('#' + gaugeUid + '-phi-needle-phi') ||
                       gCard.querySelector('#' + gaugeUid + '-needle-phi');
            const ns = gCard.querySelector('#' + gaugeUid + '-needle-spi');
            const nc = gCard.querySelector('#' + gaugeUid + '-needle-cpi');
            if (np) np.style.transform = `rotate(${phiAngle}deg)`;
            if (ns) ns.style.transform = `rotate(${spiAngle}deg)`;
            if (nc) nc.style.transform = `rotate(${cpiAngle}deg)`;

            // Breakdown toggle
            const btn   = gCard.querySelector('#' + gaugeUid + '-breakdown-btn');
            const panel = gCard.querySelector('#' + gaugeUid + '-breakdown-panel');
            if (btn && panel) {
              btn.onclick = () => {
                const open = panel.style.display !== 'none';
                panel.style.display = open ? 'none' : 'block';
                btn.innerHTML = open
                  ? '<i data-lucide="bar-chart-2" style="width:12px;height:12px;"></i> Score Breakdown'
                  : '<i data-lucide="eye-off"    style="width:12px;height:12px;"></i> Hide Breakdown';
                btn.style.background   = open ? '' : 'var(--color-primary)';
                btn.style.color        = open ? '' : 'var(--color-surface)';
                btn.style.borderColor  = open ? '' : 'var(--color-primary)';
                if (window.lucide) lucide.createIcons(btn);
              };
            }
            if (window.lucide) lucide.createIcons(gCard);
          }, 150);
"""


def main():
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find start
    start_idx = content.find(START_MARKER)
    if start_idx == -1:
        print("ERROR: START_MARKER not found"); sys.exit(1)

    # Find end (next card marker after start)
    end_idx = content.find(END_MARKER, start_idx)
    if end_idx == -1:
        print("ERROR: END_MARKER not found"); sys.exit(1)

    # The replacement keeps END_MARKER at the start of the next card
    new_content = content[:start_idx] + NEW_BLOCK + '\n          ' + content[end_idx:]

    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)

    lines_before = content.count('\n')
    lines_after  = new_content.count('\n')
    print(f"Done. Lines: {lines_before} → {lines_after} (delta {lines_after-lines_before:+d})")


if __name__ == '__main__':
    main()
