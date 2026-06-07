const fs = require('fs');
const path = require('path');

const PROJECT_ROOT = path.join(__dirname, '..');
const HTML_FILE = path.join(PROJECT_ROOT, 'projectpulse.html');
const STATUS_MD_FILE = path.join(PROJECT_ROOT, 'docs', 'user_manual', 'project_status.md');
const CONFIG_MD_FILE = path.join(PROJECT_ROOT, 'docs', 'user_manual', 'configuration_reference.md');
const STATE_JSON_FILE = path.join(PROJECT_ROOT, 'project_state.json');

console.log('--- ProjectPulse Manual Dynamic Compiler ---');

// 1. Read and parse configuration from projectpulse.html
if (!fs.existsSync(HTML_FILE)) {
  console.error(`Error: projectpulse.html not found at ${HTML_FILE}`);
  process.exit(1);
}

const htmlContent = fs.readFileSync(HTML_FILE, 'utf8');

// Simple regex extraction for dropdowns config
let dropdowns = {};
const dropdownsRegex = /dropdowns:\s*(\{\s*status:\s*\[[\s\S]*?\n\s*\})/i;
const match = htmlContent.match(dropdownsRegex);
if (match) {
  try {
    // Clean up key names and arrays to parse as JSON or evaluate safely
    let objStr = match[1]
      .replace(/(\w+):/g, '"$1":') // Wrap keys in double quotes
      .replace(/'/g, '"') // Replace single quotes with double quotes
      .replace(/,\s*\}/g, '}') // Remove trailing commas
      .replace(/,\s*\]/g, ']'); // Remove trailing commas in arrays
    dropdowns = JSON.parse(objStr);
    console.log('Successfully parsed system dropdown configurations.');
  } catch (e) {
    console.warn('Warning: Could not parse dropdowns object as JSON directly. Attempting fallback evaluation.');
    // Fallback using simple eval-like parsing since it is controlled node execution
    try {
      const evalStr = match[1].replace(/(\w+):/g, '"$1":').replace(/'/g, '"');
      dropdowns = Function(`return ${evalStr}`)();
    } catch (err) {
      console.error('Failed to parse dropdown options from HTML source code:', err);
    }
  }
}

// 2. Generate Configuration Reference Page
let configMd = `# Configuration Reference

This page is auto-generated daily to reflect the active configuration settings, role schemas, and taxonomy types configured in the ProjectPulse codebase.

---

## Active Dropdown Options

Here is the current taxonomical setup utilized in the Delivery Matrix, RAID Register, Defect Tracker, and Team Capacity Hub:

`;

for (const [key, values] of Object.entries(dropdowns)) {
  const title = key.charAt(0).toUpperCase() + key.slice(1).replace(/([A-Z])/g, ' $1');
  configMd += `### ${title}\n`;
  configMd += `*   **Key**: \`${key}\`\n`;
  configMd += `*   **Options**:\n`;
  if (Array.isArray(values)) {
    values.forEach(val => {
      configMd += `    - ${val}\n`;
    });
  } else {
    configMd += `    - *No options configured.*\n`;
  }
  configMd += `\n`;
}

configMd += `---

*Last compiled on: ${new Date().toUTCString()}*
`;

// Create docs/user_manual directory if not exists
const docsDir = path.join(PROJECT_ROOT, 'docs', 'user_manual');
if (!fs.existsSync(docsDir)) {
  fs.mkdirSync(docsDir, { recursive: true });
}

fs.writeFileSync(CONFIG_MD_FILE, configMd, 'utf8');
console.log(`Successfully compiled Configuration Reference to: ${CONFIG_MD_FILE}`);

// 3. Compile Project Status Page from project_state.json if available
let statusMd = `# Live Project Status Dashboard

This status dashboard is updated daily. It aggregates the live operational statistics of the project, including progress indices, risk logs, and team loads.

`;

if (fs.existsSync(STATE_JSON_FILE)) {
  console.log(`Found project state export at: ${STATE_JSON_FILE}. Injecting live project telemetry.`);
  try {
    const rawState = fs.readFileSync(STATE_JSON_FILE, 'utf8');
    const state = JSON.parse(rawState);
    const p = state.P || state;

    const taskCount = p.tasks ? p.tasks.length : 0;
    const completedTasks = p.tasks ? p.tasks.filter(t => t.status === 'Completed').length : 0;
    const progressAvg = p.tasks && taskCount > 0 ? (p.tasks.reduce((sum, t) => sum + (t.progress || 0), 0) / taskCount).toFixed(1) : 0;
    const defectCount = p.defects ? p.defects.length : 0;
    const activeDefects = p.defects ? p.defects.filter(d => d.status !== 'Closed' && d.status !== 'Rejected').length : 0;
    const activeRaids = p.raids ? p.raids.filter(r => r.status === 'Active' || r.status === 'Identified').length : 0;

    statusMd += `## Real-time Telemetry Dashboard

> [!TIP]
> The statistics below are hydrated directly from the latest workspace export (\`project_state.json\`).

### 1. High-level Summary
- **Project Name**: ${p.name || 'Unnamed Project'}
- **Description**: ${p.desc || 'No description provided.'}
- **Overall Completion**: **${progressAvg}%**
- **Active RAID Log Count**: **${activeRaids}** elements
- **Open Defects**: **${activeDefects}** (out of ${defectCount} logged)

### 2. Task Completion Progress
- **Total Registered Tasks**: ${taskCount}
- **Completed Tasks**: ${completedTasks}
- **Pending Tasks**: ${taskCount - completedTasks}

### 3. Core Task List Summary
| ID | Module | Task Name | Assignee | Status | Progress |
| :--- | :--- | :--- | :--- | :--- | :--- |
`;

    if (p.tasks && p.tasks.length > 0) {
      p.tasks.slice(0, 20).forEach(t => {
        statusMd += `| ${t.id || 'N/A'} | ${t.module || 'N/A'} | ${t.name || 'N/A'} | ${t.assignee || 'Unassigned'} | ${t.status || 'N/A'} | ${t.progress || 0}% |\n`;
      });
      if (p.tasks.length > 20) {
        statusMd += `| ... | ... | ... and ${p.tasks.length - 20} more tasks ... | ... | ... | ... |\n`;
      }
    } else {
      statusMd += `| *No tasks configured.* | | | | | |\n`;
    }

  } catch (err) {
    console.error('Error parsing project_state.json:', err);
    statusMd += `\n> [!WARNING]\n> Could not parse the project_state.json export file. Stale or invalid format.\n`;
  }
} else {
  console.log('No project_state.json file detected in workspace root. Compiling default seed templates.');
  
  // Extract default tasks from html seed templates
  let defaultTasksCount = 0;
  const defaultTasksMatch = htmlContent.match(/tasks:\s*\[([\s\S]*?)\]\s*,\s*defects:/i);
  if (defaultTasksMatch) {
    // Count objects
    defaultTasksCount = (defaultTasksMatch[1].match(/name:/g) || []).length;
  }

  statusMd += `## Default Workspace Template State

> [!NOTE]
> Currently reading defaults from the project template configuration as no live \`project_state.json\` has been exported to the project root.

- **System Status**: Ready / Development Mode
- **Initial Seed Deliverables Count**: **${defaultTasksCount}** default tasks
- **Default Database Schema**: Active / Pre-hydrated
- **Action Required**: Save project data as \`project_state.json\` in the workspace root, and the compiler will pull live figures on the next run.
`;
}

statusMd += `\n---\n*Last updated: ${new Date().toUTCString()}*\n`;
fs.writeFileSync(STATUS_MD_FILE, statusMd, 'utf8');
console.log(`Successfully compiled Project Status to: ${STATUS_MD_FILE}`);
console.log('--- Compiler Finished Successfully ---');
