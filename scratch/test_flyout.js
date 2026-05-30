const fs = require('fs');

const htmlContent = fs.readFileSync('/Users/manvenpratapsingh/Downloads/ProjectPulse/projectpulse.html', 'utf8');

// Extract THEMES object
const themesMatch = htmlContent.match(/const THEMES = ({[\s\S]*?});/);
if (!themesMatch) {
  console.error("Could not find THEMES definition");
  process.exit(1);
}

// Evaluate THEMES object
const THEMES = eval(`(${themesMatch[1]})`);
console.log("Found themes keys:", Object.keys(THEMES));

// Let's check how many are legacy
const legacyEntries = Object.entries(THEMES).filter(([, v]) => v.legacy);
console.log("Legacy themes count:", legacyEntries.length);

// Let's extract the renderThemeFlyout function content
const startIdx = htmlContent.indexOf("function renderThemeFlyout()");
if (startIdx === -1) {
  console.error("Could not find renderThemeFlyout function definition");
  process.exit(1);
}

// Find matching curly brace for function
let openBraces = 0;
let endIdx = -1;
for (let i = startIdx; i < htmlContent.length; i++) {
  if (htmlContent[i] === '{') {
    openBraces++;
  } else if (htmlContent[i] === '}') {
    openBraces--;
    if (openBraces === 0) {
      endIdx = i;
      break;
    }
  }
}

if (endIdx === -1) {
  console.error("Could not find end of renderThemeFlyout function");
  process.exit(1);
}

const functionStr = htmlContent.substring(startIdx, endIdx + 1);
console.log("Extracted renderThemeFlyout of length:", functionStr.length);

// Mock browser objects
const document = {
  createElement(tag) {
    const el = {
      tag,
      style: {},
      appendChild(child) {
        if (!el.children) el.children = [];
        el.children.push(child);
      },
      addEventListener(event, fn) {
        if (!el.listeners) el.listeners = {};
        el.listeners[event] = fn;
      },
      querySelector(sel) {
        return null;
      }
    };
    return el;
  }
};

const cache = {};
const $id = (id) => {
  if (!cache[id]) {
    cache[id] = {
      id,
      appendChild(child) {
        if (!this.children) this.children = [];
        this.children.push(child);
      },
      innerHTML: ''
    };
  }
  return cache[id];
};


const esc = (s) => s;
const P = {
  theme: 'nova',
  colorMode: 'dark'
};
global.window = {
  _tfLegacyOpen: false,
  lucide: { createIcons: () => {} }
};
global.lucide = global.window.lucide;


// Create a executable block
const runCode = `
  ${functionStr}
  const body = $id('tf-body');
  renderThemeFlyout();
  body;
`;

try {
  const result = eval(runCode);
  console.log("Mock execution finished successfully.");
  console.log("Children in body:", result.children.map(c => c.tag));
  const legacyWrap = result.children.find(c => c.tag === 'div' && c.children && c.children.some(child => child.tag === 'button'));
  console.log("Found legacyWrapper div?", !!legacyWrap);
  if (legacyWrap) {
    const button = legacyWrap.children.find(c => c.tag === 'button');
    console.log("Button innerHTML:", button.innerHTML);
  }
} catch (err) {
  console.error("Error during run:", err.message);
  console.error(err.stack);
}
