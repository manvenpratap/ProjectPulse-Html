#!/usr/bin/env python3
"""
patch_steering_hero.py
Replaces the old Project Steering Hero widget JS/HTML block (lines 26782–27122)
with the redesigned premium version.
"""

import sys, os

HTML_FILE = os.path.join(os.path.dirname(__file__), '..', 'projectpulse.html')

# Replacement block – everything between (and replacing) the old lines 26782-27122.
# Uses raw Python string to avoid escape issues.
NEW_BLOCK = r"""          // Calculations for Steering Hero
          const heroActiveRel = (P.releases || []).find(r => r.status === 'Active') || { name: 'v1.0.0', date: '2026-06-30' };
          const heroRelDate = new Date(heroActiveRel.date);
          const heroRelDueDateFormatted = heroRelDate.toLocaleDateString([], { month: 'short', day: 'numeric', year: 'numeric' });
          const msDiff = heroRelDate - now;
          const daysRemaining = Math.max(0, Math.ceil(msDiff / (1000 * 60 * 60 * 24)));

          const p1_start = new Date(heroRelDate); p1_start.setDate(heroRelDate.getDate() - 30);
          const p1_end   = new Date(heroRelDate); p1_end.setDate(heroRelDate.getDate()   - 20);
          const p2_start = new Date(heroRelDate); p2_start.setDate(heroRelDate.getDate() - 20);
          const p2_end   = new Date(heroRelDate); p2_end.setDate(heroRelDate.getDate()   - 10);
          const p3_start = new Date(heroRelDate); p3_start.setDate(heroRelDate.getDate() - 10);
          const p3_end   = new Date(heroRelDate); p3_end.setDate(heroRelDate.getDate()   -  2);
          const p4_start = new Date(heroRelDate); p4_start.setDate(heroRelDate.getDate() -  2);
          const p4_end   = heroRelDate;

          const heroPhases = [
            { name: 'Planning',  start: p1_start, end: p1_end, color: 'var(--color-primary)', icon: 'compass'     },
            { name: 'Execution', start: p2_start, end: p2_end, color: 'var(--amber)',          icon: 'play'        },
            { name: 'Testing',   start: p3_start, end: p3_end, color: 'var(--green)',          icon: 'test-tube-2' },
            { name: 'Release',   start: p4_start, end: p4_end, color: '#a78bfa',               icon: 'rocket'      }
          ];

          const currentDate = new Date();
          heroPhases.forEach(p => {
            if      (currentDate > p.end)                              p.status = 'completed';
            else if (currentDate >= p.start && currentDate <= p.end)  p.status = 'active';
            else                                                       p.status = 'upcoming';
          });
          if (!heroPhases.some(p => p.status === 'active'))
            heroPhases[currentDate < heroPhases[0].start ? 0 : 2].status = 'active';

          const activeIdx = heroPhases.findIndex(p => p.status === 'active');
          heroPhases.forEach((p, idx) => {
            if (idx < activeIdx) p.status = 'completed';
            if (idx > activeIdx) p.status = 'upcoming';
          });

          function fmtHeroPhaseDateRange(start, end) {
            const sm = start.toLocaleDateString([], { month: 'short' });
            const sd = start.getDate();
            const em = end.toLocaleDateString([], { month: 'short' });
            const ed = end.getDate();
            return sm === em ? `${sm} ${sd}\u2013${ed}` : `${sm} ${sd} \u2013 ${em} ${ed}`;
          }

          // SPI & CPI
          let ev = 0, pv = 0, ac = 0;
          tasks.forEach(t => {
            const effort = t.baselineEffort || t.estEffort || 5;
            ev += ((t.progress || 0) / 100) * effort;
            const baseDue = t.baselineDueDate ? new Date(t.baselineDueDate)
                          : (t.dueDate ? new Date(t.dueDate) : null);
            if (baseDue && baseDue <= now) pv += effort;
            else if (!baseDue)            pv += effort * 0.7;
            const act = t.actEffort || (t.progress > 0 ? (t.progress / 100) * (t.estEffort || 5) * 1.1 : 0);
            ac += act;
          });
          const spi = pv > 0 ? Math.min(1.2, Math.max(0.5, ev / pv)) : 0.95;
          const spiStatus = spi >= 0.95 ? 'On Track' : 'Off Track';
          const cpi = ac > 0 ? Math.min(1.3, Math.max(0.5, ev / ac)) : 1.12;
          const avgProgress = Math.round(tasks.reduce((s, t) => s + (t.progress || 0), 0) / (tasks.length || 1));

          // Team
          const totalMembers  = P.members.filter(m => m.status !== 'Departed').length || 15;
          const activeMembers = P.members.filter(m => m.status === 'Active').length    ||  4;
          const remoteMembers = totalMembers - activeMembers                            || 11;

          // Budget
          let estEffortTotal = 0, actEffortTotal = 0;
          tasks.forEach(t => {
            const effort = t.baselineEffort || t.estEffort || 5;
            estEffortTotal  += effort;
            actEffortTotal  += t.actEffort || (t.progress > 0 ? (t.progress / 100) * effort * 1.1 : 0);
          });
          const budgetUsedPct    = Math.min(100, Math.round((actEffortTotal / (estEffortTotal || 1)) * 100)) || 85;
          const budgetStatusText = cpi >= 1.0 ? `Under Budget (${budgetUsedPct}% Used)` : `Over Budget (${budgetUsedPct}% Used)`;
          const budgetBarColor   = cpi >= 1.0 ? 'var(--green)' : 'var(--red)';

          // Risk
          const activeRaids       = (P.raids || []).filter(r => r.status !== 'Closed' && r.status !== 'Mitigated');
          const highPriorityRisks = activeRaids.filter(r =>
            r.severity.startsWith('S1') || r.severity.startsWith('S2') || r.impact === 'High'
          ).length;
          let riskLevel = 'Low', riskColor = 'var(--green)';
          if      (highPriorityRisks >= 4) { riskLevel = 'High';   riskColor = 'var(--red)';   }
          else if (highPriorityRisks >= 1) { riskLevel = 'Medium'; riskColor = 'var(--amber)'; }

          // Timeline fill: proportion of track completed
          const trackFillPct = activeIdx <= 0 ? 0 : Math.round((activeIdx / (heroPhases.length - 1)) * 76);

          // Build phase nodes
          const phaseHtml = heroPhases.map((phase, i) => {
            const isActive    = phase.status === 'active';
            const isCompleted = phase.status === 'completed';
            let nodeStyle, arrowHtml = '', ringHtml = '';

            if (isCompleted) {
              nodeStyle = `background:var(--green);border:3px solid var(--color-surface);color:#fff;box-shadow:0 2px 8px rgba(0,0,0,0.15);`;
            } else if (isActive) {
              nodeStyle = `background:var(--color-surface);border:3px solid ${phase.color};color:${phase.color};box-shadow:0 0 14px ${phase.color};`;
              arrowHtml = `<div class="sh-active-arrow" style="filter:drop-shadow(0 0 6px ${phase.color});">
                <svg width="18" height="22" viewBox="0 0 24 28" fill="none">
                  <path d="M12 25V3M12 25L4 17M12 25L20 17" stroke="${phase.color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>`;
              ringHtml = `<div class="sh-node-ring" style="color:${phase.color};"></div>`;
            } else {
              nodeStyle = `background:var(--color-surface-3);border:3px solid var(--color-border);color:var(--color-text-faint);`;
            }

            return `
              <div class="sh-phase" data-phase-index="${i}">
                ${arrowHtml}
                ${ringHtml}
                <div class="sh-node" style="${nodeStyle}">
                  ${isCompleted
                    ? `<i data-lucide="check" style="width:12px;height:12px;stroke-width:4px;"></i>`
                    : `<i data-lucide="${phase.icon}" style="width:12px;height:12px;stroke-width:${isActive?'2.5':'2'}px;"></i>`
                  }
                </div>
                <div class="sh-phase-label">
                  <div class="sh-phase-name" style="color:${isActive ? phase.color : 'var(--color-text)'};">${phase.name}</div>
                  <div class="sh-phase-dates">${fmtHeroPhaseDateRange(phase.start, phase.end)}</div>
                </div>
              </div>
            `;
          }).join('');

          // ── RISK GAUGE maths ──
          // Needle angle: Low~166deg, Med~90deg, High~14deg (from left)
          const _rAngle  = riskLevel==='High' ? 0.05 : riskLevel==='Medium' ? 0.5 : 0.92;
          const _rNeedleX = (24 + 16 * Math.cos(Math.PI * _rAngle)).toFixed(2);
          const _rNeedleY = (26 - 16 * Math.sin(Math.PI * _rAngle)).toFixed(2);
          const _rArcEnd  = riskLevel==='High' ? '44 26' : riskLevel==='Medium' ? '24 6' : '13.2 9.4';

          sCard.querySelector('.cb').innerHTML = `
            <div class="steering-hero-body">

              <!-- Header -->
              <div class="sh-header">
                <div>
                  <div class="sh-eyebrow">${esc(P.name || 'ProjectPulse')}</div>
                  <div class="sh-title">${esc(heroActiveRel.name)} Release Cycle</div>
                </div>
                <div class="sh-status-badge"
                     style="background:${spi>=0.95?'rgba(16,185,129,0.12)':'rgba(239,68,68,0.12)'};
                            color:${spi>=0.95?'var(--green)':'var(--red)'};">
                  <i data-lucide="${spi>=0.95?'trending-up':'trending-down'}" style="width:10px;height:10px;"></i>
                  ${spiStatus}
                </div>
              </div>

              <!-- KPI bento strip -->
              <div class="sh-kpi-grid">

                <div class="sh-kpi-card" onclick="filterDashboardMetric('status','')">
                  <div class="sh-kpi-row">
                    <span class="sh-kpi-label">Total Scope</span>
                    <div class="sh-kpi-icon" style="background:rgba(59,130,246,0.1);color:var(--color-primary);">
                      <i data-lucide="layers" style="width:13px;height:13px;"></i>
                    </div>
                  </div>
                  <div class="sh-kpi-value">${tasks.length}</div>
                  <div class="sh-kpi-sub">
                    <i data-lucide="play" style="width:10px;height:10px;color:var(--color-primary);"></i>
                    ${tasks.filter(t=>t.status==='In Progress').length} in progress
                  </div>
                </div>

                <div class="sh-kpi-card" onclick="filterDashboardMetric('status','Completed')">
                  <div class="sh-kpi-row">
                    <span class="sh-kpi-label">Pacing Rate</span>
                    <div class="sh-kpi-icon" style="background:rgba(16,185,129,0.1);color:var(--green);">
                      <i data-lucide="check-circle" style="width:13px;height:13px;"></i>
                    </div>
                  </div>
                  <div style="display:flex;align-items:center;gap:12px;margin:6px 0 4px;">
                    <div class="sh-kpi-value" style="margin:0;">${avgProgress}%</div>
                    <svg width="28" height="28" viewBox="0 0 36 36" style="flex-shrink:0;">
                      <circle cx="18" cy="18" r="15" fill="none" stroke="var(--color-surface-3)" stroke-width="3.5"/>
                      <circle cx="18" cy="18" r="15" fill="none" stroke="var(--green)" stroke-width="3.5"
                              stroke-dasharray="94.2" stroke-dashoffset="${94.2-(94.2*avgProgress)/100}"
                              stroke-linecap="round" transform="rotate(-90 18 18)"/>
                    </svg>
                  </div>
                  <div class="sh-kpi-sub" style="color:${spi>=0.95?'var(--green)':'var(--red)'};">
                    <i data-lucide="${spi>=0.95?'trending-up':'trending-down'}" style="width:10px;height:10px;"></i>
                    SPI ${spi.toFixed(2)} \u00b7 ${spiStatus}
                  </div>
                </div>

                <div class="sh-kpi-card">
                  <div class="sh-kpi-row">
                    <span class="sh-kpi-label">Remaining</span>
                    <div class="sh-kpi-icon" style="background:rgba(245,158,11,0.1);color:var(--amber);">
                      <i data-lucide="calendar-clock" style="width:13px;height:13px;"></i>
                    </div>
                  </div>
                  <div class="sh-kpi-value">${daysRemaining}<span style="font-size:14px;font-weight:600;color:var(--color-text-muted);margin-left:4px;">days</span></div>
                  <div class="sh-kpi-sub">
                    <i data-lucide="clock" style="width:10px;height:10px;"></i>
                    Target: ${heroRelDueDateFormatted}
                  </div>
                </div>

              </div>

              <!-- Phase Timeline -->
              <div class="sh-timeline-wrap">
                <div class="sh-track-bg"></div>
                <div class="sh-track-fill" style="width:${trackFillPct}%;"></div>
                ${phaseHtml}
              </div>

              <!-- Selected Phase Focus Info -->
              <div id="hero-phase-desc" style="min-height:56px;"></div>

              <!-- Bottom Meta Bar -->
              <div class="sh-meta-bar">

                <div class="sh-meta-cell">
                  <div class="sh-meta-icon" style="background:var(--color-primary-highlight);color:var(--color-primary);">
                    <i data-lucide="users" style="width:18px;height:18px;"></i>
                  </div>
                  <div>
                    <div class="sh-meta-label">Team Capacity</div>
                    <div class="sh-meta-value">${totalMembers} Resources</div>
                    <div class="sh-meta-sub">${activeMembers} Active \u00b7 ${remoteMembers} Remote</div>
                  </div>
                </div>

                <div class="sh-meta-cell">
                  <div class="sh-meta-icon" style="background:rgba(16,185,129,0.1);color:${budgetBarColor};">
                    <i data-lucide="coins" style="width:18px;height:18px;"></i>
                  </div>
                  <div style="flex:1;min-width:0;">
                    <div class="sh-meta-label">Budget Status</div>
                    <div style="display:flex;align-items:center;gap:8px;">
                      <div class="sh-budget-bar-track" style="flex:1;">
                        <div class="sh-budget-bar-fill" style="width:${budgetUsedPct}%;background:${budgetBarColor};"></div>
                      </div>
                      <span style="font-size:11px;font-weight:800;color:var(--color-text);font-family:var(--mono);">${budgetUsedPct}%</span>
                    </div>
                    <div class="sh-meta-sub">${budgetStatusText}</div>
                  </div>
                </div>

                <div class="sh-meta-cell">
                  <div style="position:relative;width:48px;height:26px;flex-shrink:0;">
                    <svg width="48" height="26" viewBox="0 0 48 26">
                      <path d="M4 26 A20 20 0 0 1 44 26" stroke="var(--color-surface-3)" stroke-width="5" fill="none" stroke-linecap="round"/>
                      <path d="M4 26 A20 20 0 0 1 ${_rArcEnd}" stroke="${riskColor}" stroke-width="5" fill="none" stroke-linecap="round"/>
                      <line x1="24" y1="26" x2="${_rNeedleX}" y2="${_rNeedleY}"
                            stroke="var(--color-text)" stroke-width="2" stroke-linecap="round"/>
                      <circle cx="24" cy="26" r="2.5" fill="var(--color-text)"/>
                    </svg>
                  </div>
                  <div>
                    <div class="sh-meta-label">RAID Risk Profile</div>
                    <div style="display:flex;align-items:center;gap:5px;margin-top:2px;">
                      <span style="font-size:13px;font-weight:800;color:${riskColor};">${riskLevel}</span>
                      <i data-lucide="shield-alert" style="width:11px;height:11px;color:${riskColor};"></i>
                    </div>
                    <div class="sh-meta-sub">${highPriorityRisks} high severity items</div>
                  </div>
                </div>

              </div>
            </div>
          `;

          // Interactive phase details
          setTimeout(() => {
            const phaseBtns = sCard.querySelectorAll('.sh-phase');
            const phaseDesc = sCard.querySelector('#hero-phase-desc');

            const totalFeatureTasks    = tasks.filter(t => t.category === 'Feature').length || 10;
            const completedFeatures    = tasks.filter(t => t.category === 'Feature' && t.status === 'Completed').length || 6;
            const featurePct           = Math.round((completedFeatures / totalFeatureTasks) * 100);
            const activeExecutionTasks = tasks.filter(t => t.status === 'In Progress' || t.status === 'Under Review').length;
            const activeEffortSum      = tasks.filter(t => t.status === 'In Progress').reduce((s,t) => s+(t.estEffort||5), 0);
            const qaTasks              = tasks.filter(t => t.category==='Bug'||t.category==='QA'||t.name.toLowerCase().includes('test')).length;
            const completedQa          = tasks.filter(t => (t.category==='Bug'||t.category==='QA'||t.name.toLowerCase().includes('test'))&&t.status==='Completed').length;
            const defectsActive        = P.defects ? P.defects.filter(d => d.status!=='Resolved'&&d.status!=='Closed').length : 0;
            const remainingWorkload    = tasks.filter(t => t.status!=='Completed'&&t.status!=='Cancelled').length;

            const phaseDetails = [
              { desc: 'Requirements alignment, architectural scoping, and technical sprint backlog planning.',               target: `${featurePct}% Features Ready`,       stat: `${completedFeatures}/${totalFeatureTasks} Features Scoped` },
              { desc: 'Active engineering iteration sprints, cross-functional review processes, and integration testing.',  target: `${activeExecutionTasks} Sprints Active`, stat: `${activeEffortSum}d Active Effort` },
              { desc: 'Vulnerability assessments, QA test case coverage, end-to-end execution, and regression monitoring.',target: `${defectsActive} Open Defects`,          stat: `${completedQa}/${qaTasks} Test Cases Run` },
              { desc: 'Release manifest validation, target deployment check, final stakeholder sign-off, and launch.',     target: `Due in ${daysRemaining} Days`,           stat: `${remainingWorkload} Tasks Left` }
            ];

            function showPhaseDesc(idx) {
              phaseBtns.forEach((b, k) => { b.style.opacity = k === idx ? '1' : '0.5'; });
              phaseDesc.innerHTML = `
                <div class="sh-phase-desc-box">
                  <div style="flex:1;">
                    <div class="sh-desc-eyebrow">${heroPhases[idx].name} Phase \u00b7 Details</div>
                    <div class="sh-desc-body">${phaseDetails[idx].desc}</div>
                  </div>
                  <div class="sh-desc-stat">
                    <span class="sh-desc-stat-label">${phaseDetails[idx].stat}</span>
                    <span class="sh-desc-stat-value">${phaseDetails[idx].target}</span>
                  </div>
                </div>
              `;
            }

            phaseBtns.forEach((btn, idx) => { btn.onclick = () => showPhaseDesc(idx); });
            if (activeIdx !== -1 && phaseBtns[activeIdx]) showPhaseDesc(activeIdx);
          }, 150);"""

def main():
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total = len(lines)
    print(f"Total lines: {total}")

    # Line numbers are 1-indexed; Python list is 0-indexed
    START = 26782 - 1   # inclusive
    END   = 27122 - 1   # inclusive

    # Verify sentinel lines
    first_line = lines[START].rstrip()
    last_line  = lines[END].rstrip()
    print(f"First line ({START+1}): {first_line!r}")
    print(f"Last  line ({END+1}):   {last_line!r}")

    if '// Calculations for Steering Hero' not in first_line:
        print("ERROR: start sentinel not found – aborting")
        sys.exit(1)
    if '}, 150);' not in last_line:
        print("ERROR: end sentinel not found – aborting")
        sys.exit(1)

    new_lines = lines[:START] + [NEW_BLOCK + '\n'] + lines[END+1:]

    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"Done. File now has {len(new_lines)} lines.")

if __name__ == '__main__':
    main()
