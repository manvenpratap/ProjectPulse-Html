const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const PROJECT_ROOT = path.join(__dirname, '..');
const UPDATE_SCRIPT = path.join(PROJECT_ROOT, 'scripts', 'update_manual.js');
const LOG_FILE = path.join(PROJECT_ROOT, 'scripts', 'update_manual.log');
const HOME = process.env.HOME || `/Users/${process.env.USER || 'manvenpratapsingh'}`;
const LAUNCH_AGENT_DIR = path.join(HOME, 'Library', 'LaunchAgents');
const PLIST_FILE = path.join(LAUNCH_AGENT_DIR, 'com.projectpulse.manualupdate.plist');

console.log('--- macOS LaunchAgent Scheduler Installer ---');

// Parse flags
const checkMode = process.argv.includes('--check');
const uninstallMode = process.argv.includes('--uninstall');

if (uninstallMode) {
  uninstall();
  process.exit(0);
}

if (checkMode) {
  checkStatus();
  process.exit(0);
}

install();

function install() {
  console.log('1. Verifying pre-requisites...');
  if (!fs.existsSync(UPDATE_SCRIPT)) {
    console.error(`Error: Compiler script does not exist at ${UPDATE_SCRIPT}`);
    process.exit(1);
  }

  // Ensure LaunchAgents folder exists
  if (!fs.existsSync(LAUNCH_AGENT_DIR)) {
    fs.mkdirSync(LAUNCH_AGENT_DIR, { recursive: true });
  }

  // Get path to node executable
  let nodePath = 'node';
  try {
    nodePath = execSync('which node').toString().trim();
    console.log(`Found node executable at: ${nodePath}`);
  } catch (err) {
    console.warn('Warning: "which node" failed. Using default "node" name. Ensure Node is on your system PATH.');
  }

  // Create plist contents
  const plistContent = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.projectpulse.manualupdate</string>
    <key>ProgramArguments</key>
    <array>
        <string>${nodePath}</string>
        <string>${UPDATE_SCRIPT}</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>0</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>${LOG_FILE}</string>
    <key>StandardErrorPath</key>
    <string>${LOG_FILE}</string>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
`;

  console.log(`2. Writing LaunchAgent Plist to: ${PLIST_FILE}`);
  fs.writeFileSync(PLIST_FILE, plistContent, 'utf8');

  console.log('3. Registering plist with macOS launchctl...');
  try {
    // Unload if already loaded to avoid "Service already loaded" error
    try {
      execSync(`launchctl unload "${PLIST_FILE}" 2>/dev/null`);
    } catch (_) {}

    execSync(`launchctl load "${PLIST_FILE}"`);
    console.log('Launchctl registration succeeded!');
    console.log('The update task has been scheduled to run daily at 00:00 AM (and upon system/user load).');
    
    // Run an initial compile to verify and populate logs
    console.log('4. Performing initial compilation test run...');
    const compileResult = execSync(`"${nodePath}" "${UPDATE_SCRIPT}"`).toString();
    console.log(compileResult);

  } catch (err) {
    console.error('Error loading plist or executing compiler:', err.message);
    process.exit(1);
  }
}

function checkStatus() {
  console.log('Checking status of ProjectPulse daily updater...');
  if (!fs.existsSync(PLIST_FILE)) {
    console.log('Status: NOT INSTALLED (plist file does not exist)');
    return;
  }
  
  console.log(`Plist file exists at: ${PLIST_FILE}`);

  try {
    const listResult = execSync('launchctl list | grep com.projectpulse.manualupdate || true').toString().trim();
    if (listResult) {
      const parts = listResult.split(/\s+/);
      const pid = parts[0];
      const status = parts[1];
      const name = parts[2];
      console.log(`Status: REGISTERED`);
      console.log(`- Last execution exit status: ${status === '0' ? '0 (Success)' : status}`);
      console.log(`- Active PID: ${pid === '-' ? 'None (Idle)' : pid}`);
    } else {
      console.log('Status: NOT REGISTERED (file exists but not loaded in launchctl)');
    }
  } catch (err) {
    console.error('Error querying launchctl:', err.message);
  }

  if (fs.existsSync(LOG_FILE)) {
    console.log(`Log file size: ${fs.statSync(LOG_FILE).size} bytes`);
    console.log('Last log entries:');
    const logs = fs.readFileSync(LOG_FILE, 'utf8').split('\n').slice(-10).join('\n');
    console.log(logs);
  } else {
    console.log('No log file found yet.');
  }
}

function uninstall() {
  console.log('Uninstalling ProjectPulse daily updater...');
  if (fs.existsSync(PLIST_FILE)) {
    try {
      execSync(`launchctl unload "${PLIST_FILE}" 2>/dev/null`);
      console.log('Unloaded launchd job.');
    } catch (err) {
      console.warn('Failed to unload job, it might already be unloaded.');
    }
    try {
      fs.unlinkSync(PLIST_FILE);
      console.log('Deleted plist file.');
    } catch (err) {
      console.error('Failed to delete plist file:', err.message);
    }
  } else {
    console.log('No plist file found. Nothing to uninstall.');
  }
}
