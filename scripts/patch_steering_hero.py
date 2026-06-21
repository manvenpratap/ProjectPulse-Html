#!/usr/bin/env python3
import sys

def main():
    html_path = 'projectpulse.html'
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {html_path}: {e}")
        sys.exit(1)

    start_marker = "        } else if (sec.id === 'steering_hero') {"
    end_marker = "          setTimeout(() => { if (window.lucide) lucide.createIcons(grid); }, 100);        } else if (sec.id === 'summary') {"

    if start_marker not in content:
        print("Error: start marker not found in file.")
        sys.exit(1)
    if end_marker not in content:
        print("Error: end marker not found in file.")
        sys.exit(1)

    # Let's verify that there is exactly one occurrence of each to avoid ambiguity
    if content.count(start_marker) != 1:
        print(f"Error: start marker occurs {content.count(start_marker)} times.")
        sys.exit(1)
    if content.count(end_marker) != 1:
        print(f"Error: end marker occurs {content.count(end_marker)} times.")
        sys.exit(1)

    # The block we are replacing
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx > end_idx:
        print("Error: start marker is after end marker.")
        sys.exit(1)

    # Let's define the new block code
    new_code = """        } else if (sec.id === 'steering_hero') {
          addST(inner, 'Project Steering & Health');
          const grid = addGrid(inner);

          // ── CARD 1: Project Steering Hero ──
          const sId = 'dash-steering-hero';
          const sSpan = (P.widgetSpans && P.widgetSpans[sId]) || 1;
          const sCard = mkCC('Project Steering Hero', 'Release Pacing & RAID Status', sId, '', 'standard', '<b>Project Steering Hero:</b> Active release timeline phase tracking, total tasks completion pacing, budget CPI bar, and RAID index needle meter.', 'View Explanation', 'navigation');
          sCard.style.gridColumn = `span ${sSpan}`;
          grid.appendChild(sCard);

          // Calculations for Steering Hero
          const heroActiveRel = (P.releases || []).find(r => r.status === 'Active') || { name: 'v1.0.0', date: '2026-06-30' };
          const heroRelDate = new Date(heroActiveRel.date);
          const heroRelDueDateFormatted = heroRelDate.toLocaleDateString([], { month: 'short', day: 'numeric', year: 'numeric' });
          const msDiff = heroRelDate - now;
          const daysRemaining = Math.max(0, Math.ceil(msDiff / (1000 * 60 * 60 * 24)));

          const p1_start = new Date(heroRelDate); p1_start.setDate(heroRelDate.getDate() - 30);
          const p1_end = new Date(heroRelDate); p1_end.setDate(heroRelDate.getDate() - 20);
          const p2_start = new Date(heroRelDate); p2_start.setDate(heroRelDate.getDate() - 20);
          const p2_end = new Date(heroRelDate); p2_end.setDate(heroRelDate.getDate() - 10);
          const p3_start = new Date(heroRelDate); p3_start.setDate(heroRelDate.getDate() - 10);
          const p3_end = new Date(heroRelDate); p3_end.setDate(heroRelDate.getDate() - 2);
          const p4_start = new Date(heroRelDate); p4_start.setDate(heroRelDate.getDate() - 2);
          const p4_end = heroRelDate;

          const heroPhases = [
            { name: 'Planning', start: p1_start, end: p1_end, color: 'var(--color-primary)' },
            { name: 'Execution', start: p2_start, end: p2_end, color: 'var(--amber)' },
            { name: 'Testing', start: p3_start, end: p3_end, color: 'var(--green)' },
            { name: 'Release', start: p4_start, end: p4_end, color: 'var(--color-text-muted)' }
          ];

          const currentDate = new Date();
          heroPhases.forEach((p, idx) => {
            if (currentDate > p.end) {
              p.status = 'completed';
            } else if (currentDate >= p.start && currentDate <= p.end) {
              p.status = 'active';
            } else {
              p.status = 'upcoming';
            }
          });

          if (!heroPhases.some(p => p.status === 'active')) {
            if (currentDate < heroPhases[0].start) {
              heroPhases[0].status = 'active';
            } else {
              heroPhases[2].status = 'active';
            }
          }

          const activeIdx = heroPhases.findIndex(p => p.status === 'active');
          heroPhases.forEach((p, idx) => {
            if (idx < activeIdx) p.status = 'completed';
            if (idx > activeIdx) p.status = 'upcoming';
          });

          function fmtHeroPhaseDateRange(start, end) {
            const startM = start.toLocaleDateString([], { month: 'short' });
            const startD = start.getDate();
            const endM = end.toLocaleDateString([], { month: 'short' });
            const endD = end.getDate();
            return startM === endM ? `${startM} ${startD}-${endD}` : `${startM} ${startD} - ${endM} ${endD}`;
          }

          const phaseHtml = heroPhases.map((phase, i) => {
            const isActive = phase.status === 'active';
            const isCompleted = phase.status === 'completed';
            
            let topIconHtml = '';
            let nodeIcon = 'circle';
            if (i === 0) nodeIcon = 'compass';
            else if (i === 1) nodeIcon = 'play';
            else if (i === 2) nodeIcon = 'test-tube-2';
            else if (i === 3) nodeIcon = 'rocket';

            if (isCompleted) {
              topIconHtml = `
                <div class="hero-timeline-node completed" style="position: absolute; top: 28px; left: 50%; transform: translateX(-50%); width: 28px; height: 28px; border-radius: 50%; background: var(--green); border: 3px solid var(--color-surface); display: flex; align-items: center; justify-content: center; color: #ffffff; z-index: 10; box-shadow: 0 2px 6px rgba(0,0,0,0.1); transition: all 0.2s ease;">
                  <i data-lucide="check" style="width: 12px; height: 12px; stroke-width: 4px;"></i>
                </div>
              `;
            } else if (isActive) {
              topIconHtml = `
                <div style="position: absolute; top: 0px; left: 50%; transform: translateX(-50%); z-index: 12; animation: arrow-bounce 1.5s infinite ease-in-out; filter: drop-shadow(0 0 6px ${phase.color});">
                  <svg width="20" height="24" viewBox="0 0 24 28" fill="none">
                    <path d="M12 25V3M12 25L4 17M12 25L20 17" stroke="${phase.color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <div class="hero-timeline-node active" style="position: absolute; top: 28px; left: 50%; transform: translateX(-50%); width: 28px; height: 28px; border-radius: 50%; background: var(--color-surface); border: 3px solid ${phase.color}; display: flex; align-items: center; justify-content: center; color: ${phase.color}; z-index: 10; box-shadow: 0 0 12px ${phase.color}; transition: all 0.2s ease;">
                  <i data-lucide="${nodeIcon}" style="width: 12px; height: 12px; stroke-width: 2.5px;"></i>
                </div>
              `;
            } else {
              topIconHtml = `
                <div class="hero-timeline-node upcoming" style="position: absolute; top: 28px; left: 50%; transform: translateX(-50%); width: 28px; height: 28px; border-radius: 50%; background: var(--color-surface-3); border: 3px solid var(--color-border); display: flex; align-items: center; justify-content: center; color: var(--color-text-faint); z-index: 10; transition: all 0.2s ease;">
                  <i data-lucide="${nodeIcon}" style="width: 12px; height: 12px; stroke-width: 2px;"></i>
                </div>
              `;
            }

            return `
              <div class="hero-phase-btn" data-phase-index="${i}" style="position: relative; flex: 1; display: flex; flex-direction: column; align-items: center; min-width: 0; cursor: pointer; transition: all 0.2s ease;">
                ${topIconHtml}
                <div style="text-align: center; margin-top: 64px;">
                  <div style="font-size: 13px; font-weight: 700; color: ${isActive ? phase.color : 'var(--color-text)'};">${phase.name}</div>
                  <div style="font-size: 11px; color: var(--color-text-faint); margin-top: 2px;">${fmtHeroPhaseDateRange(phase.start, phase.end)}</div>
                </div>
              </div>
            `;
          }).join('');

          // SPI & CPI
          let ev = 0, pv = 0, ac = 0;
          tasks.forEach(t => {
            const effort = t.baselineEffort || t.estEffort || 5;
            ev += ((t.progress || 0) / 100) * effort;
            
            const baseDue = t.baselineDueDate ? new Date(t.baselineDueDate) : (t.dueDate ? new Date(t.dueDate) : null);
            if (baseDue && baseDue <= now) {
              pv += effort;
            } else if (!baseDue) {
              pv += effort * 0.7;
            }

            const act = t.actEffort || (t.progress > 0 ? (t.progress / 100) * (t.estEffort || 5) * 1.1 : 0);
            ac += act;
          });
          const spi = pv > 0 ? Math.min(1.2, Math.max(0.5, ev / pv)) : 0.95;
          const spiStatus = spi >= 0.95 ? 'On Track' : 'Off Track';
          const cpi = ac > 0 ? Math.min(1.3, Math.max(0.5, ev / ac)) : 1.12;

          const avgProgress = Math.round(tasks.reduce((sum, t) => sum + (t.progress || 0), 0) / (tasks.length || 1));

          // Team Metadata
          const totalMembers = P.members.filter(m => m.status !== 'Departed').length || 15;
          const activeMembers = P.members.filter(m => m.status === 'Active').length || 4;
          const remoteMembers = totalMembers - activeMembers || 11;

          // Budget/CPI Status calculations
          let estEffortTotal = 0, actEffortTotal = 0;
          tasks.forEach(t => {
            const effort = t.baselineEffort || t.estEffort || 5;
            estEffortTotal += effort;
            actEffortTotal += t.actEffort || (t.progress > 0 ? (t.progress / 100) * effort * 1.1 : 0);
          });
          const budgetUsedPct = Math.min(100, Math.round((actEffortTotal / (estEffortTotal || 1)) * 100)) || 85;
          const budgetStatusText = cpi >= 1.0 ? `Under Budget (${budgetUsedPct}% Used)` : `Over Budget (${budgetUsedPct}% Used)`;
          const budgetBarColor = cpi >= 1.0 ? 'var(--green)' : 'var(--red)';

          // Risk Level from RAID
          const activeRaids = (P.raids || []).filter(r => r.status !== 'Closed' && r.status !== 'Mitigated');
          const highPriorityRisks = activeRaids.filter(r => r.severity.startsWith('S1') || r.severity.startsWith('S2') || r.impact === 'High').length;
          let riskLevel = 'Low';
          let riskColor = 'var(--green)';
          if (highPriorityRisks >= 4) {
            riskLevel = 'High';
            riskColor = 'var(--red)';
          } else if (highPriorityRisks >= 1) {
            riskLevel = 'Medium';
            riskColor = 'var(--amber)';
          }

          sCard.querySelector('.cb').innerHTML = `
            <div style="display: flex; flex-direction: column; gap: 20px; width: 100%;">
              <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                  <div style="font-size: 11px; font-weight: 800; color: var(--color-text-faint); text-transform: uppercase; letter-spacing: 1px; font-family: var(--mono);">${esc(P.name || 'ProjectPulse')}</div>
                  <div style="font-size: 20px; font-weight: 900; color: var(--color-text); margin-top: 4px; font-family: var(--font-headings);">${esc(heroActiveRel.name)} Release Cycle</div>
                </div>
              </div>

              <!-- Executive Bento KPI Stats -->
              <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
                <!-- Total Tasks Bento Card -->
                <div class="enhanced-scard" onclick="filterDashboardMetric('status','')" style="background: var(--color-surface-2); border: 1px solid var(--color-border-faint); border-radius: 12px; padding: 16px; cursor: pointer; transition: all 0.2s ease; position: relative; overflow: hidden;" onmouseover="this.style.transform='translateY(-2px)';" onmouseout="this.style.transform='none';">
                  <div style="display: flex; justify-content: space-between; align-items: flex-start; width: 100%;">
                    <div style="font-size: 10px; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; letter-spacing: 0.5px;">Total Scope</div>
                    <div style="width: 24px; height: 24px; border-radius: 6px; background: rgba(59, 130, 246, 0.1); color: var(--color-primary); display: flex; align-items: center; justify-content: center;"><i data-lucide="layers" style="width: 14px; height: 14px;"></i></div>
                  </div>
                  <div style="font-size: 32px; font-weight: 900; color: var(--color-text); margin: 8px 0; font-family: var(--mono);">${tasks.length}</div>
                  <div style="font-size: 11px; font-weight: 600; color: var(--color-text-muted); display: flex; align-items: center; gap: 4px;"><i data-lucide="play" style="width: 10px; height: 10px; color: var(--color-primary);"></i> ${tasks.filter(t => t.status === 'In Progress').length} in progress</div>
                </div>

                <!-- % Done Bento Card -->
                <div class="enhanced-scard" onclick="filterDashboardMetric('status','Completed')" style="background: var(--color-surface-2); border: 1px solid var(--color-border-faint); border-radius: 12px; padding: 16px; cursor: pointer; transition: all 0.2s ease; position: relative; overflow: hidden;" onmouseover="this.style.transform='translateY(-2px)';" onmouseout="this.style.transform='none';">
                  <div style="display: flex; justify-content: space-between; align-items: flex-start; width: 100%;">
                    <div style="font-size: 10px; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; letter-spacing: 0.5px;">Pacing Rate</div>
                    <div style="width: 24px; height: 24px; border-radius: 6px; background: rgba(16, 185, 129, 0.1); color: var(--green); display: flex; align-items: center; justify-content: center;"><i data-lucide="check-circle" style="width: 14px; height: 14px;"></i></div>
                  </div>
                  <div style="display: flex; align-items: center; gap: 14px; margin: 8px 0;">
                    <div style="font-size: 32px; font-weight: 900; color: var(--color-text); font-family: var(--mono);">${avgProgress}%</div>
                    <svg width="28" height="28" viewBox="0 0 36 36" style="flex-shrink:0;">
                      <circle cx="18" cy="18" r="15" fill="none" stroke="var(--color-surface-3)" stroke-width="3.5" />
                      <circle cx="18" cy="18" r="15" fill="none" stroke="var(--green)" stroke-width="3.5"
                              stroke-dasharray="94.2" stroke-dashoffset="${94.2 - (94.2 * avgProgress) / 100}"
                              stroke-linecap="round" transform="rotate(-90 18 18)" />
                    </svg>
                  </div>
                  <div style="display: inline-flex; align-items: center; gap: 4px; font-size: 9px; padding: 2px 8px; background: rgba(16, 185, 129, 0.1); border-radius: 12px; color: var(--green); font-weight: 800; text-transform: uppercase;"><i data-lucide="trending-up" style="width: 8px; height: 8px;"></i> ${spiStatus}</div>
                </div>

                <!-- Days Remaining Bento Card -->
                <div class="enhanced-scard" style="background: var(--color-surface-2); border: 1px solid var(--color-border-faint); border-radius: 12px; padding: 16px; transition: all 0.2s ease; position: relative; overflow: hidden;" onmouseover="this.style.transform='translateY(-2px)';" onmouseout="this.style.transform='none';">
                  <div style="display: flex; justify-content: space-between; align-items: flex-start; width: 100%;">
                    <div style="font-size: 10px; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; letter-spacing: 0.5px;">Remaining</div>
                    <div style="width: 24px; height: 24px; border-radius: 6px; background: rgba(245, 158, 11, 0.1); color: var(--amber); display: flex; align-items: center; justify-content: center;"><i data-lucide="calendar" style="width: 14px; height: 14px;"></i></div>
                  </div>
                  <div style="font-size: 32px; font-weight: 900; color: var(--color-text); margin: 8px 0; font-family: var(--mono);">${daysRemaining} <span style="font-size: 14px; font-weight: 600; color: var(--color-text-muted);">Days</span></div>
                  <div style="font-size: 11px; font-weight: 600; color: var(--color-text-muted); display: flex; align-items: center; gap: 4px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="Release deadline: ${heroRelDueDateFormatted}"><i data-lucide="clock" style="width: 10px; height: 10px;"></i> Target: ${heroRelDueDateFormatted}</div>
                </div>
              </div>

              <!-- Interactive Horizontal Timeline -->
              <div style="position: relative; width: 100%; display: flex; justify-content: space-between; align-items: center; padding: 24px 0 12px 0; border-bottom: 1px solid var(--color-border-faint); margin-top: -8px;">
                <!-- Background connecting track -->
                <div style="position: absolute; top: 40px; left: 12%; right: 12%; height: 4px; background: var(--color-surface-3); border-radius: 2px; z-index: 1;"></div>
                <!-- Active completed track highlight -->
                <div style="position: absolute; top: 40px; left: 12%; width: ${activeIdx === -1 ? 0 : (activeIdx / 3) * 76}%; height: 4px; background: var(--color-primary); border-radius: 2px; z-index: 2; transition: width 0.4s ease-in-out;"></div>
                ${phaseHtml}
              </div>
              
              <!-- Selected Phase Focus Info (Interactive) -->
              <div id="hero-phase-desc" style="min-height: 52px; transition: all 0.3s ease;"></div>

              <!-- Bottom Meta Cards -->
              <div style="display: flex; justify-content: space-between; align-items: center; gap: 16px; padding-top: 4px;">
                <!-- Team Size Card -->
                <div style="display: flex; align-items: center; gap: 10px; flex: 1; border-right: 1px solid var(--color-border-faint); padding-right: 8px;">
                  <div style="width: 36px; height: 36px; border-radius: 8px; background: var(--color-primary-highlight); color: var(--color-primary); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <i data-lucide="users" style="width: 18px; height: 18px;"></i>
                  </div>
                  <div>
                    <div style="font-size: 9px; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; letter-spacing: 0.5px;">Team Capacity</div>
                    <div style="font-size: 14px; font-weight: 800; color: var(--color-text); margin-top: 1px;">${totalMembers} Resources</div>
                    <div style="font-size: 10px; color: var(--color-text-faint); margin-top: 1px;">${activeMembers} Active · ${remoteMembers} Remote</div>
                  </div>
                </div>

                <!-- Budget Status Card -->
                <div style="display: flex; align-items: center; gap: 10px; flex: 1; border-right: 1px solid var(--color-border-faint); padding: 0 8px;">
                  <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(16, 185, 129, 0.08); color: var(--green); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <i data-lucide="coins" style="width: 18px; height: 18px;"></i>
                  </div>
                  <div style="flex: 1; min-width: 0;">
                    <div style="font-size: 9px; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; letter-spacing: 0.5px;">Budget Status</div>
                    <div style="display: flex; align-items: center; gap: 6px; margin-top: 1px;">
                      <div style="flex: 1; height: 5px; background: var(--color-surface-3); border-radius: 2.5px; overflow: hidden;">
                        <div style="height: 100%; width: ${budgetUsedPct}%; background: ${budgetBarColor}; border-radius: 2.5px;"></div>
                      </div>
                      <span style="font-size: 10px; font-weight: 700; color: var(--color-text); font-family: var(--mono);">${budgetUsedPct}%</span>
                    </div>
                    <div style="font-size: 9px; color: var(--color-text-faint); margin-top: 2px;">${budgetStatusText}</div>
                  </div>
                </div>

                <!-- Risk Level Speedometer -->
                <div style="display: flex; align-items: center; gap: 12px; flex: 1; padding-left: 8px;">
                  <div style="position: relative; width: 44px; height: 22px; overflow: hidden; flex-shrink: 0; display: flex; align-items: flex-end; justify-content: center;">
                    <svg width="44" height="22" viewBox="0 0 44 22" style="position: absolute; top: 0; left: 0;">
                      <path d="M 4 22 A 18 18 0 0 1 40 22" stroke="var(--color-surface-3)" stroke-width="4" fill="none" />
                      <path d="M 4 22 A 18 18 0 0 1 ${riskLevel === 'High' ? '40' : (riskLevel === 'Medium' ? '22' : '13')} 22" stroke="${riskColor}" stroke-width="4" fill="none" />
                    </svg>
                    <!-- Speedometer needle -->
                    <div style="position: absolute; bottom: 0; left: calc(50% - 1px); width: 2px; height: 16px; background: var(--color-text); border-radius: 1px; transform-origin: bottom center; transform: rotate(${riskLevel === 'High' ? '60deg' : (riskLevel === 'Medium' ? '0deg' : '-60deg')}); transition: transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);"></div>
                  </div>
                  <div>
                    <div style="font-size: 9px; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; letter-spacing: 0.5px;">RAID Risk profile</div>
                    <div style="display: flex; align-items: center; gap: 4px; margin-top: 1px;">
                      <span style="font-size: 12px; font-weight: 800; color: ${riskColor};">${riskLevel}</span>
                      <i data-lucide="shield-alert" style="width: 10px; height: 10px; color: ${riskColor};"></i>
                    </div>
                    <div style="font-size: 9px; color: var(--color-text-faint); margin-top: 1px;">${highPriorityRisks} high severity items</div>
                  </div>
                </div>
              </div>
            </div>
          `;

          // Setup dynamic phase details interactive listeners
          setTimeout(() => {
            const phaseBtns = sCard.querySelectorAll('.hero-phase-btn');
            const phaseDesc = sCard.querySelector('#hero-phase-desc');

            const totalFeatureTasks = tasks.filter(t => t.category === 'Feature').length || 10;
            const completedFeatures = tasks.filter(t => t.category === 'Feature' && t.status === 'Completed').length || 6;
            const featurePct = Math.round((completedFeatures / totalFeatureTasks) * 100);

            const activeExecutionTasks = tasks.filter(t => t.status === 'In Progress' || t.status === 'Under Review').length;
            const activeEffortSum = tasks.filter(t => t.status === 'In Progress').reduce((sum, t) => sum + (t.estEffort || 5), 0);

            const qaTasks = tasks.filter(t => t.category === 'Bug' || t.category === 'QA' || t.name.toLowerCase().includes('test')).length;
            const completedQa = tasks.filter(t => (t.category === 'Bug' || t.category === 'QA' || t.name.toLowerCase().includes('test')) && t.status === 'Completed').length;
            const defectsActive = P.defects ? P.defects.filter(d => d.status !== 'Resolved' && d.status !== 'Closed').length : 0;

            const remainingWorkload = tasks.filter(t => t.status !== 'Completed' && t.status !== 'Cancelled').length;

            const phaseDetails = [
              { desc: 'Requirements alignment, architectural scoping, and technical sprint backlog planning.', target: `${featurePct}% Features Ready`, stat: `${completedFeatures}/${totalFeatureTasks} Features Scoped` },
              { desc: 'Active engineering iteration sprints, cross-functional review processes, and integration testing.', target: `${activeExecutionTasks} Sprints Active`, stat: `${activeEffortSum}d Active Effort` },
              { desc: 'Vulnerability assessments, QA test case coverage, end-to-end execution, and regression monitoring.', target: `${defectsActive} Open Defects`, stat: `${completedQa}/${qaTasks} Test Cases Run` },
              { desc: 'Release manifest validation, target deployment check, final stakeholder sign-off, and launch.', target: `Due in ${daysRemaining} Days`, stat: `${remainingWorkload} Tasks Left` }
            ];
            
            phaseBtns.forEach((btn, idx) => {
              btn.onclick = () => {
                phaseBtns.forEach((b, k) => {
                  const node = b.querySelector('.hero-timeline-node');
                  if (node) {
                    if (node.classList.contains('completed')) {
                      node.style.background = 'var(--green)';
                      node.style.color = '#ffffff';
                      node.style.boxShadow = '0 2px 6px rgba(0,0,0,0.1)';
                    } else if (node.classList.contains('active')) {
                      node.style.background = 'var(--color-surface)';
                      node.style.color = heroPhases[k].color;
                      node.style.boxShadow = `0 0 12px ${heroPhases[k].color}`;
                    } else {
                      node.style.background = 'var(--color-surface-3)';
                      node.style.color = 'var(--color-text-faint)';
                      node.style.boxShadow = 'none';
                    }
                  }
                  b.style.opacity = '0.6';
                });
                
                btn.style.opacity = '1';
                const activeNode = btn.querySelector('.hero-timeline-node');
                if (activeNode) {
                  activeNode.style.boxShadow = `0 0 16px ${heroPhases[idx].color}`;
                }
                
                phaseDesc.innerHTML = `
                  <div style="background: var(--color-surface-2); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--color-border-faint); margin-top: 8px; display: flex; justify-content: space-between; align-items: center; transition: all 0.2s ease; gap: 12px;">
                    <div style="flex: 1;">
                      <span style="font-size: 8px; font-weight: 700; color: var(--color-primary); text-transform: uppercase; letter-spacing: 0.5px; font-family: var(--mono);">Selected Phase Details</span>
                      <div style="font-size: 11px; font-weight: 700; color: var(--color-text); margin-top: 2px; line-height: 1.3;">${phaseDetails[idx].desc}</div>
                    </div>
                    <div style="text-align: right; flex-shrink: 0;">
                      <span style="font-size: 8px; font-weight: 700; color: var(--color-text-faint); text-transform: uppercase; font-family: var(--mono);">${phaseDetails[idx].stat}</span>
                      <div style="font-size: 10px; font-weight: 800; color: var(--color-primary); margin-top: 2px;">${phaseDetails[idx].target}</div>
                    </div>
                  </div>
                `;
              };
            });
            if (activeIdx !== -1 && phaseBtns[activeIdx]) {
              phaseBtns[activeIdx].click();
            }
          }, 150);

          // ── CARD 2: Project Health Gauge ──
          const gId = 'dash-health-gauge';
          const gSpan = (P.widgetSpans && P.widgetSpans[gId]) || 1;
          const gCard = mkCC('Project Health Gauge', 'Composite Rating & Performance Index', gId, '', 'standard', '<b>Project Health Gauge:</b> A color-coded composite gauge dial displaying the calculated health index alongside dynamic SPI/CPI, completion rate, and remaining tasks.', 'View Explanation', 'gauge');
          gCard.style.gridColumn = `span ${gSpan}`;
          grid.appendChild(gCard);

          // Calculations for Health Gauge
          const healthScoreVal = getHealthScore(tasks);
          const angle = 180 + (healthScoreVal / 100) * 180;
          const rad = angle * Math.PI / 180;
          const nx = 250 + 105 * Math.cos(rad);
          const ny = 170 + 105 * Math.sin(rad);

          const spiVal = spi.toFixed(2);
          const spiColor = spi >= 0.95 ? 'var(--green)' : 'var(--red)';
          const spiIcon = spi >= 0.95 ? 'trending-up' : 'trending-down';

          const cpiVal = cpi.toFixed(2);
          const cpiColor = cpi >= 1.0 ? 'var(--green)' : 'var(--red)';
          const cpiIcon = cpi >= 1.0 ? 'trending-up' : 'trending-down';

          const overdueTasksCount = tasks.filter(t => { const d = daysDiff(t.dueDate); return d !== null && d < 0 && t.status !== 'Completed' && t.status !== 'Cancelled'; }).length;
          const blockedTasksCount = tasks.filter(t => t.status === 'On Hold').length;

          gCard.querySelector('.cb').innerHTML = `
            <div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
              <style>
                @keyframes gauge-sweep-dash-health-gauge {
                  from { transform: rotate(0deg); }
                  to { transform: rotate(${(healthScoreVal / 100) * 180}deg); }
                }
              </style>
              <!-- Gauge Visualization -->
              <svg width="100%" height="150" viewBox="0 0 500 210" style="max-width: 240px; overflow:visible;">
                <defs>
                  <linearGradient id="gauge-red-dash" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#ef4444" />
                    <stop offset="100%" stop-color="#f87171" />
                  </linearGradient>
                  <linearGradient id="gauge-orange-dash" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#f59e0b" />
                    <stop offset="100%" stop-color="#fbbf24" />
                  </linearGradient>
                  <linearGradient id="gauge-green-dash" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#10b981" />
                    <stop offset="100%" stop-color="#34d399" />
                  </linearGradient>
                  <filter id="needle-shadow-dash" x="-20%" y="-20%" width="140%" height="140%">
                    <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.2" />
                  </filter>
                </defs>
                <!-- Gauge Background Track -->
                <path d="M 130 170 A 120 120 0 0 1 370 170" stroke="var(--color-surface-3)" stroke-width="8" stroke-linecap="round" fill="none" opacity="0.6" />
                
                <!-- Gauge Colored Arcs -->
                <path d="M 130 170 A 120 120 0 0 1 204.1 59.1" stroke="url(#gauge-red-dash)" stroke-width="8" stroke-linecap="round" fill="none" />
                <path d="M 204.1 59.1 A 120 120 0 0 1 334.8 85.1" stroke="url(#gauge-orange-dash)" stroke-width="8" fill="none" />
                <path d="M 334.8 85.1 A 120 120 0 0 1 370 170" stroke="url(#gauge-green-dash)" stroke-width="8" stroke-linecap="round" fill="none" />

                <!-- Ticks Labels positioned cleanly outside -->
                <text x="105" y="180" font-size="10px" font-weight="800" fill="var(--color-text-muted)" text-anchor="middle" font-family="var(--mono)">0</text>
                <text x="148" y="72" font-size="10px" font-weight="800" fill="var(--color-text-muted)" text-anchor="middle" font-family="var(--mono)">25</text>
                <text x="250" y="32" font-size="10px" font-weight="800" fill="var(--color-text-muted)" text-anchor="middle" font-family="var(--mono)">50</text>
                <text x="352" y="72" font-size="10px" font-weight="800" fill="var(--color-text-muted)" text-anchor="middle" font-family="var(--mono)">75</text>
                <text x="395" y="180" font-size="10px" font-weight="800" fill="var(--color-text-muted)" text-anchor="middle" font-family="var(--mono)">100</text>

                <!-- Tick marks -->
                <g stroke="var(--color-border)" stroke-width="1.5" opacity="0.6">
                  <line x1="130" y1="170" x2="124" y2="170" />
                  <line x1="250" y1="50" x2="250" y2="44" />
                  <line x1="370" y1="170" x2="376" y2="170" />
                  <line x1="165.2" y1="85.2" x2="161.0" y2="81.0" />
                  <line x1="334.8" y1="85.2" x2="339.0" y2="81.0" />
                </g>

                <!-- Center Text Readout positioned to avoid overlapping needle center -->
                <text x="250" y="105" font-size="9px" font-weight="800" fill="var(--color-text-faint)" text-anchor="middle" letter-spacing="1.5px" font-family="var(--mono)">HEALTH SCORE</text>
                <text x="250" y="145" font-size="44px" font-weight="900" fill="var(--color-text)" text-anchor="middle" font-family="var(--mono)">${healthScoreVal}%</text>

                <!-- Tapered Needle Pointer with sweep animation -->
                <polygon points="250,172 145,170 250,168" fill="var(--color-primary)" filter="url(#needle-shadow-dash)"
                         style="transform-origin: 250px 170px; transform: rotate(${(healthScoreVal / 100) * 180}deg); animation: gauge-sweep-dash-health-gauge 1.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; transition: all 0.2s;" />
                <circle cx="250" cy="170" r="10" fill="var(--color-primary)" stroke="var(--color-surface)" stroke-width="2" filter="url(#needle-shadow-dash)" />
                <circle cx="250" cy="170" r="4" fill="var(--color-surface)" />
              </svg>

              <!-- Interactive calculation breakdown trigger -->
              <button id="health-breakdown-btn" class="btn outline" style="font-size: 10px; padding: 6px 14px; border-radius: 20px; cursor: pointer; font-weight: 700; margin-bottom: 12px; transition: all 0.2s ease; outline: none; border-color: var(--color-border); display: flex; align-items: center; gap: 6px; height: auto; background: var(--color-surface);" onmouseover="this.style.background='var(--color-primary-highlight)'; this.style.borderColor='var(--color-primary)';" onmouseout="this.style.background='var(--color-surface)'; this.style.borderColor='var(--color-border)';"><i data-lucide="calculator" style="width: 12px; height: 12px;"></i> Show Score Breakdown</button>
              
              <div id="health-breakdown-panel" style="width:100%; display:none; overflow:hidden; margin-bottom:12px; transition: all 0.3s ease;">
                <div style="background:var(--color-surface-2); padding:12px; border-radius:10px; border:1px solid var(--color-border-faint); font-size:11px; display: flex; flex-direction: column; gap: 8px;">
                  <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="color: var(--color-text-muted)">Task Completion Base</span>
                    <span style="color:var(--green); font-weight:bold; font-family: var(--mono);">+${avgProgress}</span>
                  </div>
                  <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="color: var(--color-text-muted)">Overdue Penalty (${overdueTasksCount} tasks)</span>
                    <span style="color:var(--red); font-weight:bold; font-family: var(--mono);">${overdueTasksCount > 0 ? '-' + (overdueTasksCount * 3) : '0'}</span>
                  </div>
                  <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="color: var(--color-text-muted)">Blocked Penalty (${blockedTasksCount} tasks)</span>
                    <span style="color:var(--red); font-weight:bold; font-family: var(--mono);">${blockedTasksCount > 0 ? '-' + (blockedTasksCount * 5) : '0'}</span>
                  </div>
                  <div style="display:flex; justify-content:space-between; align-items:center; border-top: 1px solid var(--color-border-faint); padding-top: 6px;">
                    <span style="color: var(--color-text-muted)">CPI Performance Modifier</span>
                    <span style="${cpi >= 1.0 ? 'color:var(--green)' : 'color:var(--red)'}; font-weight:bold; font-family: var(--mono);">${cpi >= 1.0 ? '+5' : '-10'}</span>
                  </div>
                </div>
              </div>

              <!-- Metrics Cards 2x2 Grid with dynamic hover effect -->
              <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:10px; width:100%; margin-top:4px;">
                <!-- SPI -->
                <div style="background:var(--color-surface-2); border:1px solid var(--color-border-faint); border-left:4px solid ${spiColor}; border-radius:10px; padding:10px 12px; display:flex; align-items:center; gap:10px; transition:all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
                  <div style="width:28px; height:28px; border-radius:50%; background:${spiColor}15; color:${spiColor}; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    <i data-lucide="${spiIcon}" style="width:14px; height:14px;"></i>
                  </div>
                  <div>
                    <div style="font-size:9px; font-weight:800; color:var(--color-text-muted); text-transform:uppercase; letter-spacing:0.5px;">SPI</div>
                    <div style="font-size:14px; font-weight:850; color:${spiColor}; line-height:1.2; font-family: var(--mono);">${spiVal}</div>
                  </div>
                </div>

                <!-- CPI -->
                <div style="background:var(--color-surface-2); border:1px solid var(--color-border-faint); border-left:4px solid ${cpiColor}; border-radius:10px; padding:10px 12px; display:flex; align-items:center; gap:10px; transition:all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
                  <div style="width:28px; height:28px; border-radius:50%; background:${cpiColor}15; color:${cpiColor}; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    <i data-lucide="${cpiIcon}" style="width:14px; height:14px;"></i>
                  </div>
                  <div>
                    <div style="font-size:9px; font-weight:800; color:var(--color-text-muted); text-transform:uppercase; letter-spacing:0.5px;">CPI</div>
                    <div style="font-size:14px; font-weight:850; color:${cpiColor}; line-height:1.2; font-family: var(--mono);">${cpiVal}</div>
                  </div>
                </div>

                <!-- % Complete -->
                <div style="background:var(--color-surface-2); border:1px solid var(--color-border-faint); border-left:4px solid var(--green); border-radius:10px; padding:10px 12px; display:flex; align-items:center; gap:10px; transition:all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
                  <div style="width:28px; height:28px; border-radius:50%; background:rgba(16,185,129,0.08); color:var(--green); display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    <i data-lucide="check-circle" style="width:14px; height:14px;"></i>
                  </div>
                  <div>
                    <div style="font-size:9px; font-weight:800; color:var(--color-text-muted); text-transform:uppercase; letter-spacing:0.5px;">% Done</div>
                    <div style="font-size:14px; font-weight:850; color:var(--green); line-height:1.2; font-family: var(--mono);">${avgProgress}%</div>
                  </div>
                </div>

                <!-- Tasks Remaining -->
                <div style="background:var(--color-surface-2); border:1px solid var(--color-border-faint); border-left:4px solid var(--amber); border-radius:10px; padding:10px 12px; display:flex; align-items:center; gap:10px; transition:all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
                  <div style="width:28px; height:28px; border-radius:50%; background:rgba(245,158,11,0.08); color:var(--amber); display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    <i data-lucide="clipboard" style="width:14px; height:14px;"></i>
                  </div>
                  <div>
                    <div style="font-size:9px; font-weight:800; color:var(--color-text-muted); text-transform:uppercase; letter-spacing:0.5px;">Rem. Tasks</div>
                    <div style="font-size:14px; font-weight:850; color:var(--amber); line-height:1.2; font-family: var(--mono);">${tasks.filter(t => t.status !== 'Completed' && t.status !== 'Cancelled').length}</div>
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
                if (panel.style.display === 'none') {
                  panel.style.display = 'block';
                  btn.innerHTML = '<i data-lucide="eye-off" style="width:12px; height:12px;"></i> Hide Score Breakdown';
                  btn.style.background = 'var(--color-primary)';
                  btn.style.color = 'var(--color-surface)';
                  btn.style.borderColor = 'var(--color-primary)';
                  btn.onmouseover = () => {
                    btn.style.background = 'var(--color-primary-hover)';
                  };
                  btn.onmouseout = () => {
                    btn.style.background = 'var(--color-primary)';
                  };
                } else {
                  panel.style.display = 'none';
                  btn.innerHTML = '<i data-lucide="calculator" style="width:12px; height:12px;"></i> Show Score Breakdown';
                  btn.style.background = 'var(--color-surface)';
                  btn.style.color = 'var(--color-text)';
                  btn.style.borderColor = 'var(--color-border)';
                  btn.onmouseover = () => {
                    btn.style.background = 'var(--color-primary-highlight)';
                    btn.style.borderColor = 'var(--color-primary)';
                  };
                  btn.onmouseout = () => {
                    btn.style.background = 'var(--color-surface)';
                    btn.style.borderColor = 'var(--color-border)';
                  };
                }
                if (window.lucide) lucide.createIcons(btn);
              };
            }
          }, 150);

          // ── CARD 3: Schedule & Status Overview ──
          const oId = 'dash-status-overview';
          const oSpan = (P.widgetSpans && P.widgetSpans[oId]) || 2;
          const oCard = mkCC('Schedule & Status Overview', 'Overall progress, overdue and blocked registers', oId, '', 'standard', '<b>Schedule & Status Overview:</b> High-level dashboard widget detailing active completed/remaining tasks progress bar, overdue task counts, and blocked item tables.', 'View Explanation', 'activity');
          oCard.style.gridColumn = `span ${oSpan}`;
          grid.appendChild(oCard);

          // Calculations for Status Overview
          const activeRel = (P.releases || []).find(r => r.status === 'Active');
          const phaseName = activeRel ? activeRel.name : 'Phase 2 — Execution';

          const overallStatus = spi >= 0.95 ? 'On Track' : (spi >= 0.85 ? 'At Risk' : 'Off Track');
          const overallStatusBg = overallStatus === 'On Track' ? 'var(--green)' : (overallStatus === 'At Risk' ? 'var(--amber)' : 'var(--red)');
          
          const lastSavedDate = P.lastSavedTime || new Date();
          const timeStr = lastSavedDate.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
          const lastSavedFormatted = `Today, ${timeStr}`;
          
          const activeTasks = tasks.filter(t => t.status !== 'Cancelled');
          const totalTasksCount = activeTasks.length;
          const completedTasks = activeTasks.filter(t => t.status === 'Completed').length;
          const remainingTasks = totalTasksCount - completedTasks;
          const tasksCompletionPct = totalTasksCount > 0 ? Math.round((completedTasks / totalTasksCount) * 100) : 0;
          
          const overdueTasksList = tasks.filter(t => { const d = daysDiff(t.dueDate); return d !== null && d < 0 && t.status !== 'Completed' && t.status !== 'Cancelled'; });
          const overdueCount = overdueTasksList.length;
          const formattedOverdueCount = overdueCount < 10 ? '0' + overdueCount : overdueCount;
          
          const blockedTasksList = tasks.filter(t => t.status === 'On Hold');
          const blockedCount = blockedTasksList.length;
          const formattedBlockedCount = blockedCount < 10 ? '0' + blockedCount : blockedCount;

          const overdueListHtml = overdueTasksList.slice(0, 3).map(t => {
            const days = Math.abs(daysDiff(t.dueDate));
            const label = days === 1 ? 'yesterday' : `${days}d ago`;
            return `
              <div style="font-size: 11px; color: var(--color-text-muted); padding: 4px 6px; border-bottom: 1px solid var(--color-divider-faint); display: flex; align-items: center; justify-content: space-between; gap: 8px;" title="${esc(t.name)} (Due ${label})">
                <span style="font-weight: 700; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">• ${esc(t.name)}</span>
                <span style="font-size: 9px; font-weight: 800; font-family: var(--mono); color: var(--red); background: rgba(239,68,68,0.1); padding: 1px 4px; border-radius: 4px; flex-shrink: 0;">${label}</span>
              </div>
            `;
          }).join('') || `<div style="font-size: 11px; color: var(--color-text-faint); padding: 6px 0;">All deadlines met</div>`;

          const blockedListHtml = blockedTasksList.slice(0, 3).map(t => `
            <div style="font-size: 11px; color: var(--color-text-muted); padding: 4px 6px; border-bottom: 1px solid var(--color-divider-faint); display: flex; flex-direction: column; gap: 2px;" title="${esc(t.name)}">
              <div style="font-weight: 700; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: var(--color-text);">• ${esc(t.name)}</div>
              <div style="font-size: 10px; color: var(--color-text-faint); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; padding-left: 8px;">${esc(t.slippageReason || t.notes || 'Awaiting unblocking')}</div>
            </div>
          `).join('') || `<div style="font-size: 11px; color: var(--color-text-faint); padding: 6px 0;">No active blockers</div>`;

          // Setup unified Segment Control headers
          const oTabsHeader = document.createElement('div');
          oTabsHeader.style = "display: inline-flex; background: var(--color-surface-3); padding: 4px; border-radius: 20px; border: 1px solid var(--color-border); margin-bottom: 16px; width: fit-content; gap: 4px;";

          const oBtnAll = document.createElement('button');
          oBtnAll.innerText = 'All Registers';
          oBtnAll.style = "background: var(--color-surface); color: var(--color-primary); border: 1px solid var(--color-border-faint); padding: 6px 16px; border-radius: 16px; font-size: 11px; font-weight: 700; cursor: pointer; transition: all 0.2s ease; outline: none; box-shadow: 0 2px 6px rgba(0,0,0,0.05);";

          const oBtnOverdue = document.createElement('button');
          oBtnOverdue.innerText = `Overdue (${overdueCount})`;
          oBtnOverdue.style = "background: transparent; color: var(--color-text-muted); border: 1px solid transparent; padding: 6px 16px; border-radius: 16px; font-size: 11px; font-weight: 700; cursor: pointer; transition: all 0.2s ease; outline: none;";

          const oBtnBlocked = document.createElement('button');
          oBtnBlocked.innerText = `Blocked (${blockedCount})`;
          oBtnBlocked.style = "background: transparent; color: var(--color-text-muted); border: 1px solid transparent; padding: 6px 16px; border-radius: 16px; font-size: 11px; font-weight: 700; cursor: pointer; transition: all 0.2s ease; outline: none;";

          oTabsHeader.appendChild(oBtnAll);
          oTabsHeader.appendChild(oBtnOverdue);
          oTabsHeader.appendChild(oBtnBlocked);

          const oTabContent = document.createElement('div');
          oTabContent.style = "flex: 1; display: flex; flex-direction: column;";

          const oTabAll = document.createElement('div');
          oTabAll.style.display = 'block';

          const oTabOverdue = document.createElement('div');
          oTabOverdue.style.display = 'none';

          const oTabBlocked = document.createElement('div');
          oTabBlocked.style.display = 'none';

          oTabContent.appendChild(oTabAll);
          oTabContent.appendChild(oTabOverdue);
          oTabContent.appendChild(oTabBlocked);

          oCard.querySelector('.cb').appendChild(oTabsHeader);
          oCard.querySelector('.cb').appendChild(oTabContent);

          const setOTabActive = (activeBtn, showTab) => {
            [oBtnAll, oBtnOverdue, oBtnBlocked].forEach(b => {
              b.style.background = 'transparent';
              b.style.color = 'var(--color-text-muted)';
              b.style.borderColor = 'transparent';
              b.style.boxShadow = 'none';
            });
            [oTabAll, oTabOverdue, oTabBlocked].forEach(t => t.style.display = 'none');
            activeBtn.style.background = 'var(--color-surface)';
            activeBtn.style.color = 'var(--color-primary)';
            activeBtn.style.borderColor = 'var(--color-border-faint)';
            activeBtn.style.boxShadow = '0 2px 6px rgba(0,0,0,0.05)';
            showTab.style.display = 'block';
            if (window.lucide) lucide.createIcons(showTab);
          };
          oBtnAll.onclick = () => setOTabActive(oBtnAll, oTabAll);
          oBtnOverdue.onclick = () => setOTabActive(oBtnOverdue, oTabOverdue);
          oBtnBlocked.onclick = () => setOTabActive(oBtnBlocked, oTabBlocked);

          oTabAll.innerHTML = `
            <div style="display: flex; flex-direction: column; gap: 16px; width: 100%;">
              <!-- Top Row -->
              <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
                <!-- Project and Progress -->
                <div style="display: flex; align-items: center; gap: 20px; flex: 1; min-width: 250px;">
                  <span style="font-size: 20px; font-weight: 900; color: var(--color-text); font-family: var(--font-headings);">${esc(P.name || 'ProjectPulse')}</span>
                  <div style="flex: 1; max-width: 300px; padding-top: 4px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; font-size: 10px; font-weight: 700; color: var(--color-text-muted); margin-bottom: 4px;">
                      <span style="background: var(--color-primary-highlight); color: var(--color-primary); padding: 2px 8px; border-radius: 12px; font-weight: 800; font-family: var(--mono);">${esc(phaseName)}</span>
                      <span>Overall Progress</span>
                    </div>
                    <div style="position: relative; height: 6px; background: var(--color-surface-3); border-radius: 3px; margin-top: 14px;">
                      <div style="height: 100%; width: ${avgProgress}%; background: var(--color-primary); border-radius: 3px;"></div>
                      <div style="position: absolute; top: -20px; left: calc(${avgProgress}% - 30px); background: var(--color-surface); border: 1px solid var(--color-border); padding: 2px 6px; border-radius: 6px; font-size: 9px; font-weight: 800; color: var(--color-text); white-space: nowrap; font-family: var(--mono); box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
                        ${avgProgress}% Done
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Status and Last Saved -->
                <div style="display: flex; align-items: center; gap: 16px;">
                  <div style="text-align: center;">
                    <div style="font-size: 9px; color: var(--color-text-faint); font-weight: 700; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.5px;">Steering Status</div>
                    <span style="background: ${overallStatusBg}; color: #ffffff; padding: 4px 10px; border-radius: 20px; font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; font-family: var(--mono);">${overallStatus}</span>
                  </div>
                  <div style="display: flex; align-items: center; gap: 8px; font-size: 10px; color: var(--color-text-muted); font-weight: 600; background: var(--color-surface-2); padding: 6px 12px; border-radius: 10px; border: 1px solid var(--color-border-faint);">
                    <i data-lucide="clock" style="width: 14px; height: 14px; color: var(--color-text-muted);"></i>
                    <span>Last Refreshed:<br><b style="color: var(--color-text)">${lastSavedFormatted}</b></span>
                  </div>
                </div>
              </div>
              
              <!-- Divider -->
              <div style="height: 1px; background: var(--color-border-faint); margin: 2px 0;"></div>
              
              <!-- Three Columns -->
              <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; min-width: 0;">
                <!-- Tasks Column -->
                <div style="border-right: 1px solid var(--color-border-faint); padding-right: 20px; display: flex; flex-direction: column; gap: 8px;">
                  <div style="display: flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 800; color: var(--color-text); text-transform: uppercase; letter-spacing: 0.5px;">
                    <i data-lucide="clipboard" style="width: 14px; height: 14px; color: var(--color-text-muted);"></i>
                    <span>Tasks</span>
                  </div>
                  
                  <div style="display: flex; align-items: baseline; justify-content: space-between;">
                    <span style="font-size: 32px; font-weight: 900; color: var(--color-text); line-height: 1; font-family: var(--mono);">${totalTasksCount}</span>
                    <span style="font-size: 11px; font-weight: 800; color: var(--color-text-muted); font-family: var(--mono);">${tasksCompletionPct}%</span>
                  </div>
                  <div style="font-size: 9px; font-weight: 700; color: var(--color-text-faint); text-transform: uppercase; margin-bottom: -4px;">Backlog Completion</div>
                  
                  <div style="height: 4px; background: var(--color-surface-3); border-radius: 2px; overflow: hidden;">
                    <div style="height: 100%; width: ${tasksCompletionPct}%; background: var(--green); border-radius: 2px;"></div>
                  </div>
                  
                  <div style="display: flex; flex-direction: column; gap: 4px; margin-top: 2px;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: var(--color-text-muted); font-weight: 600;">
                      <i data-lucide="check-circle-2" style="width: 12px; height: 12px; color: var(--green);"></i>
                      <span>${completedTasks} Completed</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: var(--color-text-muted); font-weight: 600;">
                      <i data-lucide="circle" style="width: 12px; height: 12px; color: var(--color-text-faint);"></i>
                      <span>${remainingTasks} Remaining</span>
                    </div>
                  </div>
                </div>
                
                <!-- Overdue Column -->
                <div style="border-right: 1px solid var(--color-border-faint); padding-right: 20px; display: flex; flex-direction: column; gap: 8px;">
                  <div style="display: flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 800; color: var(--red); text-transform: uppercase; letter-spacing: 0.5px;">
                    <i data-lucide="alert-triangle" style="width: 14px; height: 14px; color: var(--red);"></i>
                    <span>Overdue</span>
                  </div>
                  
                  <div style="display: flex; align-items: baseline; justify-content: space-between;">
                    <span style="font-size: 32px; font-weight: 900; color: var(--red); line-height: 1; font-family: var(--mono);">${formattedOverdueCount}</span>
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; margin-bottom: -4px;">Tasks Overdue</div>
                  
                  <div style="height: 5px; background: var(--color-surface-3); border-radius: 2.5px; overflow: hidden;">
                    <div style="height: 100%; width: ${Math.min(100, (overdueCount / (totalTasksCount || 1)) * 100)}%; background: var(--red); border-radius: 2.5px;"></div>
                  </div>
                  
                  <div style="display: flex; flex-direction: column; gap: 6px; margin-top: 2px; max-width: 100%;">
                    <div style="display: flex; align-items: center; gap: 4px; font-size: 11px; color: var(--red); font-weight: 800;">
                      <i data-lucide="clock" style="width: 12px; height: 12px; color: var(--red);"></i>
                      <span>Deadline missed</span>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 3px; max-width: 100%;">
                      ${overdueListHtml}
                    </div>
                  </div>
                </div>
                
                <!-- Blocked Column -->
                <div style="display: flex; flex-direction: column; gap: 8px; min-width: 0;">
                  <div style="display: flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 800; color: var(--amber); text-transform: uppercase; letter-spacing: 0.5px;">
                    <i data-lucide="shield-alert" style="width: 14px; height: 14px; color: var(--amber);"></i>
                    <span>Blocked</span>
                  </div>
                  
                  <div style="display: flex; align-items: baseline; justify-content: space-between;">
                    <span style="font-size: 32px; font-weight: 900; color: var(--amber); line-height: 1; font-family: var(--mono);">${formattedBlockedCount}</span>
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; margin-bottom: -4px;">Task Blocked</div>
                  
                  <div style="height: 5px; background: var(--color-surface-3); border-radius: 2.5px; overflow: hidden;">
                    <div style="height: 100%; width: ${Math.min(100, (blockedCount / (totalTasksCount || 1)) * 100)}%; background: var(--amber); border-radius: 2.5px;"></div>
                  </div>
                  
                  <div style="display: flex; flex-direction: column; gap: 6px; margin-top: 2px; max-width: 100%;">
                    <div style="display: flex; align-items: center; gap: 4px; font-size: 11px; color: var(--amber); font-weight: 800;">
                      <i data-lucide="clock" style="width: 12px; height: 12px; color: var(--amber);"></i>
                      <span>Blocked paths</span>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 4px; max-width: 100%;">
                      ${blockedListHtml}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          `;

          // Generate tables for Overdue / Blocked registers
          let overdueTableHtml = '';
          if (overdueCount > 0) {
            overdueTableHtml = `
              <div style="max-height: 220px; overflow-y: auto; border: 1px solid var(--color-border); border-radius: 8px;">
                <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 11px;">
                  <thead>
                    <tr style="background: var(--color-surface-3); border-bottom: 1px solid var(--color-border); position: sticky; top: 0; z-index: 2;">
                      <th style="padding: 8px 10px; font-weight: 800; color: var(--color-text-muted); font-family: var(--mono); text-transform: uppercase; width: 60px;">ID</th>
                      <th style="padding: 8px 10px; font-weight: 800; color: var(--color-text-muted);">Task Name</th>
                      <th style="padding: 8px 10px; font-weight: 800; color: var(--color-text-muted);">Assignee</th>
                      <th style="padding: 8px 10px; font-weight: 800; color: var(--color-text-muted); text-align: right; width: 90px;">Overdue By</th>
                      <th style="padding: 8px 10px; font-weight: 800; color: var(--color-text-muted); text-align: center; width: 80px;">Priority</th>
                    </tr>
                  </thead>
                  <tbody>
                    ${overdueTasksList.map(t => {
                      const days = Math.abs(daysDiff(t.dueDate));
                      const label = days === 1 ? '1 day' : `${days} days`;
                      const p = t.priority || 'Medium';
                      const pBg = p === 'High' || p === 'Critical' ? 'rgba(239, 68, 68, 0.1)' : p === 'Medium' ? 'var(--amber-t)' : 'rgba(100, 116, 139, 0.08)';
                      const pCol = p === 'High' || p === 'Critical' ? 'var(--red)' : p === 'Medium' ? 'var(--amber)' : 'var(--color-text-muted)';
                      return `
                        <tr style="border-bottom: 1px solid var(--color-divider-faint); background: var(--color-surface);" class="hover:bg-surface-hover transition-colors duration-150">
                          <td style="padding: 8px 10px; font-family: var(--mono); color: var(--color-text-faint); font-weight: 700;">${esc(t.id)}</td>
                          <td style="padding: 8px 10px; font-weight: 700; color: var(--color-text); max-width: 180px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="${esc(t.name)}">${esc(t.name)}</td>
                          <td style="padding: 8px 10px; color: var(--color-text-muted); font-weight: 600;">${esc(t.assignee || 'Unassigned')}</td>
                          <td style="padding: 8px 10px; text-align: right; font-weight: 800; color: var(--red); font-family: var(--mono);">${label}</td>
                          <td style="padding: 8px 10px; text-align: center;">
                            <span style="background: ${pBg}; color: ${pCol}; padding: 2px 6px; border-radius: 4px; font-size: 9px; font-weight: 800; text-transform: uppercase;">${p}</span>
                          </td>
                        </tr>
                      `;
                    }).join('')}
                  </tbody>
                </table>
              </div>
            `;
          } else {
            overdueTableHtml = `
              <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 32px; background: var(--color-surface-2); border-radius: 8px; border: 1px dashed var(--color-border-faint);">
                <div style="width: 36px; height: 36px; border-radius: 50%; background: rgba(34, 197, 94, 0.1); color: var(--green); display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
                  <i data-lucide="check-circle" style="width: 18px; height: 18px;"></i>
                </div>
                <div style="font-size: 12px; font-weight: 800; color: var(--color-text);">All Deadlines Met</div>
                <div style="font-size: 10px; color: var(--color-text-faint); margin-top: 2px;">No overdue tasks found in active sprint.</div>
              </div>
            `;
          }

          let blockedTableHtml = '';
          if (blockedCount > 0) {
            blockedTableHtml = `
              <div style="max-height: 220px; overflow-y: auto; border: 1px solid var(--color-border); border-radius: 8px;">
                <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 11px;">
                  <thead>
                    <tr style="background: var(--color-surface-3); border-bottom: 1px solid var(--color-border); position: sticky; top: 0; z-index: 2;">
                      <th style="padding: 8px 10px; font-weight: 800; color: var(--color-text-muted); font-family: var(--mono); text-transform: uppercase; width: 60px;">ID</th>
                      <th style="padding: 8px 10px; font-weight: 800; color: var(--color-text-muted);">Blocked Task</th>
                      <th style="padding: 8px 10px; font-weight: 800; color: var(--color-text-muted);">Assignee</th>
                      <th style="padding: 8px 10px; font-weight: 800; color: var(--color-text-muted);">Blocker Reason</th>
                      <th style="padding: 8px 10px; font-weight: 800; color: var(--color-text-muted); text-align: center; width: 80px;">Priority</th>
                    </tr>
                  </thead>
                  <tbody>
                    ${blockedTasksList.map(t => {
                      const reason = t.slippageReason || t.notes || 'Awaiting unblocking';
                      const p = t.priority || 'Medium';
                      const pBg = p === 'High' || p === 'Critical' ? 'rgba(239, 68, 68, 0.1)' : p === 'Medium' ? 'var(--amber-t)' : 'rgba(100, 116, 139, 0.08)';
                      const pCol = p === 'High' || p === 'Critical' ? 'var(--red)' : p === 'Medium' ? 'var(--amber)' : 'var(--color-text-muted)';
                      return `
                        <tr style="border-bottom: 1px solid var(--color-divider-faint); background: var(--color-surface);" class="hover:bg-surface-hover transition-colors duration-150">
                          <td style="padding: 8px 10px; font-family: var(--mono); color: var(--color-text-faint); font-weight: 700;">${esc(t.id)}</td>
                          <td style="padding: 8px 10px; font-weight: 700; color: var(--color-text); max-width: 150px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="${esc(t.name)}">${esc(t.name)}</td>
                          <td style="padding: 8px 10px; color: var(--color-text-muted); font-weight: 600;">${esc(t.assignee || 'Unassigned')}</td>
                          <td style="padding: 8px 10px; color: var(--red); font-weight: 500; max-width: 180px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="${esc(reason)}">${esc(reason)}</td>
                          <td style="padding: 8px 10px; text-align: center;">
                            <span style="background: ${pBg}; color: ${pCol}; padding: 2px 6px; border-radius: 4px; font-size: 9px; font-weight: 800; text-transform: uppercase;">${p}</span>
                          </td>
                        </tr>
                      `;
                    }).join('')}
                  </tbody>
                </table>
              </div>
            `;
          } else {
            blockedTableHtml = `
              <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 32px; background: var(--color-surface-2); border-radius: 8px; border: 1px dashed var(--color-border-faint);">
                <div style="width: 36px; height: 36px; border-radius: 50%; background: rgba(34, 197, 94, 0.1); color: var(--green); display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
                  <i data-lucide="shield-check" style="width: 18px; height: 18px;"></i>
                </div>
                <div style="font-size: 12px; font-weight: 800; color: var(--color-text);">No Blocked Tasks</div>
                <div style="font-size: 10px; color: var(--color-text-faint); margin-top: 2px;">All active paths are clear.</div>
              </div>
            `;
          }

          oTabOverdue.innerHTML = overdueTableHtml;
          oTabBlocked.innerHTML = blockedTableHtml;

          setTimeout(() => { if (window.lucide) lucide.createIcons(grid); }, 100);
        } else if (sec.id === 'summary') {"""

    # We replace the text in between start and end index
    new_content = content[:start_idx] + new_code + content[end_idx + len(end_marker):]

    try:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated projectpulse.html!")
    except Exception as e:
        print(f"Error writing to {html_path}: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
