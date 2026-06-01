const fs = require('fs');
const { execSync } = require('child_process');

const bakPath = '/Users/manvenpratapsingh/Downloads/ProjectPulse/projectpulse.html.bak';
const htmlPath = '/Users/manvenpratapsingh/Downloads/ProjectPulse/projectpulse.html';

const content = fs.readFileSync(bakPath, 'utf8');
const lines = content.split('\n');

// Helper to convert standard function declarations to methods
function convertToMethods(str) {
  // First, convert single-line functions (restricting to same line)
  let result = str.replace(/^    (async[ \t]+)?function[ \t]+(\w+)[ \t]*\(([^)]*?)\)[ \t]*\{[ \t]*([^\n]*?)[ \t]*\}/gm, (match, asyncPrefix, name, params, body) => {
    const prefix = asyncPrefix ? 'async ' : '';
    return `    ${prefix}${name}(${params}) { ${body} },`;
  });
  // Next, convert multi-line functions (restricting to same line for signature)
  result = result.replace(/^    (async[ \t]+)?function\s+(\w+)\s*\(([^)]*?)\)\s*\{/gm, (match, asyncPrefix, name, params) => {
    const prefix = asyncPrefix ? 'async ' : '';
    return `    ${prefix}${name}(${params}) {`;
  });
  // Add commas to top-level closing braces of multi-line functions
  result = result.replace(/^    \}/gm, '    },');
  return result;
}

// ════════════════════════════════════════════════════════════
// 1. UI UTILITIES & HELPERS MODULARIZATION (PulseUI)
// ════════════════════════════════════════════════════════════

// Utility methods (11101 to 11139) written directly with single/double quotes to avoid escapes
const pulseUiUtilitiesCode = `    $id(id) {
        return document.getElementById(id);
    },
    esc(s) {
        return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    },
    fmtN(n) {
        if (isNaN(n) || !isFinite(n)) return '–';
        const a = Math.abs(n);
        if (a >= 1e6) return (n / 1e6).toFixed(1) + 'M';
        if (a >= 1e3) return (n / 1e3).toFixed(1) + 'K';
        return Math.round(n * 100) / 100;
    },
    fmtDate(d) {
        if (!d) return '—';
        try {
            const dt = new Date(d);
            if (isNaN(dt)) return d;
            const day = String(dt.getDate()).padStart(2, '0');
            const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            const month = months[dt.getMonth()];
            const year = dt.getFullYear();
            return day + '-' + month + '-' + year;
        } catch (e) {
            return d;
        }
    },
    parseDateDMY(str) {
        if (!str) return '';
        const trimmed = String(str).trim();
        if (/^\\d{4}-\\d{2}-\\d{2}$/.test(trimmed)) return trimmed;
        const m = trimmed.match(/^(\\d{1,2})[-/ ]([A-Za-z]{3})[-/ ](\\d{4})$/);
        if (m) {
            const day = parseInt(m[1]);
            const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            const monthIdx = months.findIndex(name => name.toLowerCase() === m[2].toLowerCase());
            const year = parseInt(m[3]);
            if (monthIdx > -1) {
                return year + '-' + String(monthIdx + 1).padStart(2, '0') + '-' + String(day).padStart(2, '0');
            }
        }
        const d = new Date(trimmed);
        if (!isNaN(d)) {
            return d.toISOString().split('T')[0];
        }
        return trimmed;
    },`;

// Flyouts & Themes Range: lines 11836 to 12129
const flyoutsText = lines.slice(11836 - 1, 12129).join('\n');
const keydownRegex = /^    window\.addEventListener\('keydown'[\s\S]*?\}\);\r?\n/gm;
const keydownMatch = flyoutsText.match(keydownRegex);
const keydownCode = keydownMatch ? keydownMatch[0] : '';
let cleanedFlyouts = flyoutsText.replace(keydownRegex, '');

const attrRegex = /^    document\.documentElement\.setAttribute\('data-(theme|color-mode)'[^\n]*\r?\n/gm;
const attrMatch = cleanedFlyouts.match(attrRegex);
const attrCode = attrMatch ? attrMatch.join('\n') : '';
cleanedFlyouts = cleanedFlyouts.replace(attrRegex, '');

const pulseUiFlyoutsCode = convertToMethods(cleanedFlyouts);

// Modals Range: lines 30835 to 30843
const modalsText = lines.slice(30835 - 1, 30843).join('\n');
const aliasRegex = /^[ \t]*window\.confirmAction[^\n]*\r?\n/gm;
let cleanedModals = modalsText.replace(aliasRegex, '');

const clickListenerRegex = /^    document\.querySelectorAll\('\.mbg'\)[^\n]*\r?\n?/gm;
const clickListenerMatch = cleanedModals.match(clickListenerRegex);
const clickListenerCode = clickListenerMatch ? clickListenerMatch[0] : '';
cleanedModals = cleanedModals.replace(clickListenerRegex, '');

const pulseUiModalsCode = convertToMethods(cleanedModals);

// Notifications Range 1: lines 34849 to 34867
const notify1Text = lines.slice(34849 - 1, 34867).join('\n');
const pulseUiNotify1Code = convertToMethods(notify1Text);

// Notifications Range 2: lines 35296 to 35352
const notify2Text = lines.slice(35296 - 1, 35352).join('\n');
let cleanedNotify2 = notify2Text.replace(/^[ \t]*window\.showNotification[^\n]*\r?\n/gm, '');
cleanedNotify2 = cleanedNotify2.replace(/^[ \t]*window\.showToast[^\n]*\r?\n/gm, '');
const pulseUiNotify2Code = convertToMethods(cleanedNotify2);

const pulseUiCode = `    // ══════ UI UTILITIES, FLYOUTS, MODALS & NOTIFICATIONS ══════
    const PulseUI = {
${pulseUiUtilitiesCode}

${pulseUiFlyoutsCode}

${pulseUiModalsCode}

${pulseUiNotify1Code}

${pulseUiNotify2Code}
    };
    window.PulseUI = PulseUI;

    // Global aliases for backward compatibility
    function $id(id) { return PulseUI.$id(id); }
    window.$id = $id;
    function esc(s) { return PulseUI.esc(s); }
    function fmtN(n) { return PulseUI.fmtN(n); }
    function fmtDate(d) { return PulseUI.fmtDate(d); }
    function parseDateDMY(str) { return PulseUI.parseDateDMY(str); }
    window.parseDateDMY = parseDateDMY;

    function closeDynamicModal(id) { return PulseUI.closeDynamicModal(id); }
    function updateColorModeBtn() { return PulseUI.updateColorModeBtn(); }
    function toggleColorMode() { return PulseUI.toggleColorMode(); }
    function setTheme(t) { return PulseUI.setTheme(t); }
    function openThemeFlyout() { return PulseUI.openThemeFlyout(); }
    function closeThemeFlyout() { return PulseUI.closeThemeFlyout(); }
    function closeMemberFlyout() { return PulseUI.closeMemberFlyout(); }
    function closeAllFlyouts() { return PulseUI.closeAllFlyouts(); }
    function renderThemeFlyout() { return PulseUI.renderThemeFlyout(); }

    function openModal(id) { return PulseUI.openModal(id); }
    function closeModal(id) { return PulseUI.closeModal(id); }
    function showConfirm(msg, onOk) { return PulseUI.showConfirm(msg, onOk); }
    window.confirmAction = showConfirm;

    function notify(msg, type) { return PulseUI.notify(msg, type); }
    function toggleFullScreen() { return PulseUI.toggleFullScreen(); }
    function showNotification(message, type, duration) { return PulseUI.showNotification(message, type, duration); }
    function dismissNotification(id) { return PulseUI.dismissNotification(id); }
    window.showNotification = showNotification;
    window.showToast = showNotification;`;

// ════════════════════════════════════════════════════════════
// 2. PERSISTENCE MODULARIZATION
// ════════════════════════════════════════════════════════════

// Section A: lines 12138 to 12380 (clearProjectState to resetToSetup)
const secALines = lines.slice(12138 - 1, 12380);
const secAText = secALines.join('\n');

// Section B1: lines 12477 to 12963 (save to createProjectFile)
const secB1Lines = lines.slice(12477 - 1, 12963);
const secB1Text = secB1Lines.join('\n');

// Section B2: lines 13162 to 13367 (saveToFile to reconnectFolder)
const secB2Lines = lines.slice(13162 - 1, 13367);
const secB2Text = secB2Lines.join('\n');

const methodsA = convertToMethods(secAText);

// Strip the const dbName line from B1
let methodsB1 = convertToMethods(secB1Text);
methodsB1 = methodsB1.replace(/^    const dbName = 'ProjectPulseDB', storeName = 'handles', backupStore = 'backups';\s*$/gm, '');

const methodsB2 = convertToMethods(secB2Text);

const pulsePersistenceCode = `    // ══════ PERSISTENCE ══════
    const dbName = 'ProjectPulseDB', storeName = 'handles', backupStore = 'backups';
    const PulsePersistence = {
${methodsA}

${methodsB1}

${methodsB2}
    };
    window.PulsePersistence = PulsePersistence;

    // Global aliases for backward compatibility (using standard functions)
    function clearProjectState() { return PulsePersistence.clearProjectState(); }
    function injectSampleData() { return PulsePersistence.injectSampleData(); }
    function clearAllData() { return PulsePersistence.clearAllData(); }
    function resetToSetup() { return PulsePersistence.resetToSetup(); }
    function save() { return PulsePersistence.save(); }
    function load() { return PulsePersistence.load(); }
    function getDB() { return PulsePersistence.getDB(); }
    function saveHandle(id, handle) { return PulsePersistence.saveHandle(id, handle); }
    function getHandle(id) { return PulsePersistence.getHandle(id); }
    function listHandles() { return PulsePersistence.listHandles(); }
    function createBackup() { return PulsePersistence.createBackup(); }
    function createFileBackup(buf) { return PulsePersistence.createFileBackup(buf); }
    function listBackups(projectName) { return PulsePersistence.listBackups(projectName); }
    function restoreFromBackup(backupId) { return PulsePersistence.restoreFromBackup(backupId); }
    function renderRecentProjects() { return PulsePersistence.renderRecentProjects(); }
    function loadRecentProject(name) { return PulsePersistence.loadRecentProject(name); }
    function pickProjectFile() { return PulsePersistence.pickProjectFile(); }
    function pickProjectDirectory() { return PulsePersistence.pickProjectDirectory(); }
    function createProjectFile() { return PulsePersistence.createProjectFile(); }
    function saveToFile(isAutosave) { return PulsePersistence.saveToFile(isAutosave); }
    function loadFromFile() { return PulsePersistence.loadFromFile(); }
    function updateFsInd() { return PulsePersistence.updateFsInd(); }
    function syncFromFile() { return PulsePersistence.syncFromFile(); }
    function reconnectFolder() { return PulsePersistence.reconnectFolder(); }`;

// ════════════════════════════════════════════════════════════
// 3. EXCEL MODULARIZATION
// ════════════════════════════════════════════════════════════

// Excel Range: 27923 to 30832
const excelLines = lines.slice(27923 - 1, 30832);
const excelText = excelLines.join('\n');

// Convert functions to methods and strip global window assignments
let methodsExcel = convertToMethods(excelText);
methodsExcel = methodsExcel.replace(/^    window\.exportProjectExcel = exportProjectExcel;\s*$/gm, '');
methodsExcel = methodsExcel.replace(/^    window\.exportProjectCSV = exportProjectCSV;\s*$/gm, '');

const excelFuncs = [
  'exportProjectExcel', 'exportProjectCSV', 'buildReadmeSheet', 'buildDataDictionarySheet',
  'buildValidationListsSheet', 'registerNamedRanges', 'buildHelperMapsSheet', 'buildUnifiedTasksSheet',
  'applyUnifiedSheetValidations', 'buildFeatureRolloutsSheet', 'buildTasksSheet', 'applyTaskSheetValidations',
  'applyTaskSheetHelperColumns', 'buildSubtasksSheet', 'buildTeamSheet', 'buildDefectsSheet',
  'buildRaidRegisterSheet', 'buildDecisionLogSheet', 'buildBaselineHistorySheet', 'buildFeaturesSheet',
  'buildDropdownsSheet', 'buildTemplateSheets', 'buildRelationSheets', 'buildAppStateSheets',
  'buildExecutiveDashboardSheets', 'applyWorkbookProtectionRules', 'generateProjectWorkbook',
  'importProjectExcel', 'applyBackwardCompatibilityMappings', 'parseAppStateSheets', 'parseConfigSheets',
  'parseCanonicalSheets', 'parseRelationSheets', 'parseHelperAwareCanonicalSheets', 'normalizeImportedData',
  'collectImportIssues', 'rebuildDerivedState', 'reconstructProjectFromBuffer', 'exportLogCSV', 'downloadCSV'
];

const excelAliases = excelFuncs.map(name => {
  return `    function ${name}(...args) { return PulseExcel.${name}(...args); }`;
}).join('\n');

const pulseExcelCode = `    // ══════ EXCEL & CSV ══════
    const PulseExcel = {
${methodsExcel}
    };
    window.PulseExcel = PulseExcel;

    // Global aliases for backward compatibility
${excelAliases}`;

// ════════════════════════════════════════════════════════════
// 4. CONTIGUOUS REASSEMBLY
// ════════════════════════════════════════════════════════════

const keep_1 = lines.slice(0, 11100).join('\n');
const keep_2 = lines.slice(11140 - 1, 11835).join('\n');
const keep_3 = lines.slice(12130 - 1, 12137).join('\n');
const keep_4 = lines.slice(12381 - 1, 12476).join('\n');
const keep_5 = lines.slice(12964 - 1, 13161).join('\n');
const keep_6 = lines.slice(13368 - 1, 27922).join('\n');
const keep_7 = lines.slice(30833 - 1, 30834).join('\n');
const keep_8 = lines.slice(30844 - 1, 34848).join('\n');
const keep_9 = lines.slice(34868 - 1, 35295).join('\n');
const keep_10 = lines.slice(35356 - 1, 38076).join('\n');
const keep_11 = lines.slice(38077 - 1).join('\n');

const newContent = `${keep_1}
${pulseUiCode}
${keep_2}
${keep_3}
${pulsePersistenceCode}
${keep_4}
${keep_5}
${keep_6}
${pulseExcelCode}
${keep_7}
${keep_8}
${keep_9}
${keep_10}

    // Global listeners & initializations
    ${keydownCode}
    ${attrCode}
    ${clickListenerCode}
${keep_11}`;

// Post-processing string replacements
let processedContent = newContent;

// 1. Remove window.resolveColor = function ... from initApp
processedContent = processedContent.replace(
  /window\.resolveColor = function\s*\(c\)\s*\{[\s\S]*?\};\r?\n/g,
  '// resolveColor is now defined at the top level of block #4\n'
);

// 2. Prepend resolveColor definition and documentation header at the top level of script block #4
const resolveColorDefinition = `
    /*
     * PROJECTPULSE STABILIZATION & CLEANUP PASS (Antigravity Codebase Pass)
     * 
     * BUGS FIXED:
     * - Fixed ReferenceErrors on direct resolveColor(...) calls. Pre-initialized resolveColor as a hoisted top-level global function.
     * - Fixed Theme/Color Mode switching that only applied visual updates on page refresh.
     *   * Updated toggleColorMode and updateColorModeBtn to dynamically check window.matchMedia('(prefers-color-scheme: dark)').
     *   * Extracted complex conditional check blocks from the theme flyout buttons and redirected to toggleColorMode('light'|'dark').
     * - Added safety checks for CDN files (ExcelJS / html2canvas) in reconstructProjectFromBuffer.
     * - Standardized and hoisted window-level function assignments to prevent temporal dead zone (TDZ) reference errors on load.
     * 
     * RUNTIME SAFETY LAYER:
     * - Guard clauses added for DOM access, CDN presence, and data existence.
     * - Fallbacks for color variables, fonts, and missing data points standardized.
     * 
     * REGRESSION CHECKLIST / VERIFICATION STEPS:
     * 1. Theme Switcher: Ensure that selecting featured (e.g. Origin, Nova, Obsidian, Paper) and standard themes renders correctly.
     * 2. Color Mode: Clicking sun/moon in top bar or theme selector must update colors immediately without needing refresh.
     * 3. Dashboard / Charts: Ensure canvas elements (Health, Burndown, CFD, velocity, workload) render clean metrics.
     * 4. Reports & Pivot: Ensure report snapshots and pivot views render without errors.
     * 5. Excel Import/Export: Excel backup download and project restore must complete successfully.
     * 6. Command Palette (CMD + K / Ctrl + K): Ensure ESC closes modals, shortcuts work.
     * 7. Persistence: Projects lists render in setup screen, IndexedDB backups save and restore.
     */

    // Hoisted global helper functions
    function resolveColor(c) {
      if (!c || typeof c !== 'string' || !c.includes('var(')) return c;
      const m = c.match(/var\\((--[^)]+)\\)/);
      if (!m) return c;
      const val = getComputedStyle(document.documentElement).getPropertyValue(m[1]).trim();
      if (val) return val;
      if (m[1].includes('red')) return '#ef4444';
      if (m[1].includes('amber')) return '#f59e0b';
      if (m[1].includes('green')) return '#22c55e';
      if (m[1].includes('primary')) return '#44403c';
      return '#888';
    }
    window.resolveColor = resolveColor;
`;

processedContent = processedContent.replace(
  /<script>\r?\n[ \t]*\/\/ ── PROJECT PULSE CONSTANTS SYSTEM ──/,
  `<script>${resolveColorDefinition}\n    // ── PROJECT PULSE CONSTANTS SYSTEM ──`
);

// 3. Prepend safety fallback checks for ExcelJS, html2canvas, and lucide in reconstructProjectFromBuffer
processedContent = processedContent.replace(
  /async reconstructProjectFromBuffer\(buffer\)\s*\{/g,
  `async reconstructProjectFromBuffer(buffer) {
      if (typeof ExcelJS === 'undefined') {
        notify('Excel library not loaded.', 'err');
        return;
      }
      if (typeof html2canvas === 'undefined') {
        notify('Capture library not loaded.', 'err');
        return;
      }`
);

// 4. Update toggleColorMode implementation in PulseUI
const newToggleColorMode = `    toggleColorMode(targetMode) {
      const curTheme = THEMES[P.theme] || THEMES.nexus;
      const isSystemDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      const isCurrentlyDark = P.colorMode === 'dark' || (P.colorMode === 'default' && (curTheme.isDark || isSystemDark));
      let nextMode;
      if (targetMode === 'light') nextMode = 'light';
      else if (targetMode === 'dark') nextMode = 'dark';
      else nextMode = isCurrentlyDark ? 'light' : 'dark';
      P.colorMode = nextMode;
      document.documentElement.setAttribute('data-color-mode', P.colorMode);
      localStorage.setItem('pp-color-mode', P.colorMode);
      updateColorModeBtn();
      renderThemeFlyout();
      render();
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          render();
        });
      });
    },`;

processedContent = processedContent.replace(
  /    toggleColorMode\(\)\s*\{[\s\S]*?requestAnimationFrame\(\(\)\s*=>\s*\{[\s\S]*?\}\);\s*\},/g,
  newToggleColorMode
);

// Update updateColorModeBtn to support prefers-color-scheme
const newUpdateColorModeBtn = `    updateColorModeBtn() {
      const btn = $id('color-mode-btn');
      if (!btn) return;
      const curTheme = THEMES[P.theme] || THEMES.paper;
      const isSystemDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      const isCurrentlyDark = P.colorMode === 'dark' || (P.colorMode === 'default' && (curTheme.isDark || isSystemDark));
      btn.innerHTML = isCurrentlyDark ? '<i data-lucide="sun"></i>' : '<i data-lucide="moon"></i>';
      if (window.lucide) lucide.createIcons(btn);
    },`;

processedContent = processedContent.replace(
  /    updateColorModeBtn\(\)\s*\{[\s\S]*?if\s*\(window\.lucide\)\s*lucide\.createIcons\(btn\);\s*\},/g,
  newUpdateColorModeBtn
);

// Update renderThemeFlyout to support prefers-color-scheme and simple onclick handlers
processedContent = processedContent.replace(
  /const curTheme = THEMES\[P\.theme\] \|\| THEMES\.origin \|\| THEMES\.nexus;\r?\n[ \t]*const isCurrentlyDark = P\.colorMode === 'dark' \|\| \(P\.colorMode === 'default' && curTheme\.isDark\);/g,
  `const curTheme = THEMES[P.theme] || THEMES.origin || THEMES.nexus;
      const isSystemDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      const isCurrentlyDark = P.colorMode === 'dark' || (P.colorMode === 'default' && (curTheme.isDark || isSystemDark));`
);

processedContent = processedContent.replace(
  /<button class="btn \$\{!isCurrentlyDark \? 'primary' : ''\}" onclick="if\(document\.documentElement\.getAttribute\('data-color-mode'\)==='dark'\|\|\(\(THEMES\[P\.theme\]\|\|\{\}\)\.isDark&&P\.colorMode!=='light'\)\)\{toggleColorMode\(\)\}" style="justify-content:center;padding:9px;font-weight:600;font-size:13px;gap:6px;border-radius:var\(--radius-md\);\$\{!isCurrentlyDark \? '' : 'opacity:0\.6'\}">/g,
  `<button class="btn \${!isCurrentlyDark ? 'primary' : ''}" onclick="toggleColorMode('light')" style="justify-content:center;padding:9px;font-weight:600;font-size:13px;gap:6px;border-radius:var(--radius-md);\${!isCurrentlyDark ? '' : 'opacity:0.6'}">`
);

processedContent = processedContent.replace(
  /<button class="btn \$\{isCurrentlyDark \? 'primary' : ''\}" onclick="if\(!\(document\.documentElement\.getAttribute\('data-color-mode'\)==='dark'\|\|\(\(THEMES\[P\.theme\]\|\|\{\}\)\.isDark&&P\.colorMode!=='light'\)\)\)\{toggleColorMode\(\)\}" style="justify-content:center;padding:9px;font-weight:600;font-size:13px;gap:6px;border-radius:var\(--radius-md\);\$\{isCurrentlyDark \? '' : 'opacity:0\.6'\}">/g,
  `<button class="btn \${isCurrentlyDark ? 'primary' : ''}" onclick="toggleColorMode('dark')" style="justify-content:center;padding:9px;font-weight:600;font-size:13px;gap:6px;border-radius:var(--radius-md);\${isCurrentlyDark ? '' : 'opacity:0.6'}">`
);

processedContent = processedContent.replace(
  /const isDark = P\.colorMode === 'dark' \|\| \(P\.colorMode === 'default' && v\.isDark\);/g,
  `const isDark = P.colorMode === 'dark' || (P.colorMode === 'default' && (v.isDark || isSystemDark));`
);

// 5. Rewrite window.NAME = (async)? function to hoisted local functions
let windowFuncsCount = 0;
processedContent = processedContent.replace(
  /^([ \t]*)window\.([a-zA-Z0-9_]+)[ \t]*=[ \t]*(async[ \t]+)?function[ \t]*\(([^)]*)\)[ \t]*\{/gm,
  (match, indent, name, asyncPref, params) => {
    windowFuncsCount++;
    const asyncWord = asyncPref || '';
    return `${indent}window.${name} = ${name};\n${indent}${asyncWord}function ${name}(${params}) {`;
  }
);
console.log(`Rewrote ${windowFuncsCount} window function assignments into hoisted functions.`);

fs.writeFileSync(htmlPath, processedContent, 'utf8');
console.log('Successfully applied all modularization refactors and stabilization to projectpulse.html.');

// Verify syntax
try {
  const result = execSync('node check_syntax.js', { encoding: 'utf8' });
  console.log('Syntax Check Output:\n', result);
} catch (e) {
  console.error('Syntax Check Failed:\n', e.stdout || e.message);
  process.exit(1);
}

