const fs = require('fs');
const vm = require('vm');

const filePath = '/Users/manvenpratapsingh/Downloads/ProjectPulse/projectpulse.html';
const content = fs.readFileSync(filePath, 'utf8');

const makeDummyElement = (tagName) => {
  const dummy = {
    tagName: (tagName || 'DIV').toUpperCase(),
    style: {},
    dataset: {},
    classList: {
      add: () => {},
      remove: () => {},
      toggle: () => {},
      contains: () => false
    },
    appendChild: (child) => child || dummy,
    insertBefore: (child) => child || dummy,
    removeChild: () => {},
    after: () => {},
    before: () => {},
    remove: () => {},
    replaceWith: () => {},
    setAttribute: () => {},
    getAttribute: () => '',
    removeAttribute: () => {},
    addEventListener: () => {},
    removeEventListener: () => {},
    querySelector: () => dummy,
    querySelectorAll: () => [],
    cloneNode: () => dummy,
    focus: () => {},
    click: () => {},
    getContext: () => ({
      fillRect: () => {},
      fillText: () => {},
      beginPath: () => {},
      moveTo: () => {},
      lineTo: () => {},
      stroke: () => {},
      fill: () => {},
      arc: () => {},
      closePath: () => {},
      measureText: () => ({ width: 10 }),
      clearRect: () => {},
      createLinearGradient: () => ({ addColorStop: () => {} }),
      setLineDash: () => {},
      roundRect: () => {},
      rect: () => {}
    })
  };
  return dummy;
};

// Mock a minimal browser environment
const domMock = {
  window: {},
  addEventListener: () => {},
  getComputedStyle: () => ({
    getPropertyValue: () => 'Inter, sans-serif'
  }),
  document: {
    head: { appendChild: () => {} },
    documentElement: {
      setAttribute: (k, v) => { domMock.documentElementAttributes[k] = v; },
      getAttribute: (k) => domMock.documentElementAttributes[k],
      style: {}
    },
    getElementById: (id) => {
      if (id === 'tf-body' || id === 'tf-details' || id === 'backup-list-container-inline') {
        return { appendChild: () => {}, innerHTML: '' };
      }
      return makeDummyElement();
    },
    querySelector: () => makeDummyElement(),
    querySelectorAll: () => [],
    addEventListener: () => {},
    createElement: (tag) => makeDummyElement(tag),
    createElementNS: (ns, tag) => makeDummyElement(tag),
    body: makeDummyElement('BODY')
  },
  console: {
    log: (...args) => console.log('[MOCK LOG]', ...args),
    warn: (...args) => console.warn('[MOCK WARN]', ...args),
    error: (...args) => console.error('[MOCK ERROR]', ...args)
  },
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  setInterval: setInterval,
  clearInterval: clearInterval,
  requestAnimationFrame: (cb) => setTimeout(cb, 16),
  cancelAnimationFrame: (id) => clearTimeout(id),
  localStorage: {
    getItem: (k) => null,
    setItem: (k, v) => {},
    removeItem: (k) => {}
  },
  navigator: {
    userAgent: 'node'
  },
  devicePixelRatio: 1,
  documentElementAttributes: {},
  location: { href: '' }
};

domMock.window = domMock;
domMock.document.body.style = {};

const context = vm.createContext(domMock);

// Find all script blocks
const scriptRegex = /<script[^>]*>([\s\S]*?)<\/script>/gi;
let match;
let blockNum = 0;

console.log('--- STARTING RUNTIME EXECUTION OF ALL SCRIPT BLOCKS ---');

try {
  while ((match = scriptRegex.exec(content)) !== null) {
    blockNum++;
    const scriptContent = match[1].trim();
    if (!scriptContent) continue;
    
    // Ignore external source scripts (which would fail to load in Node)
    if (match[0].includes('src=')) {
      console.log(`Skipping external script block #${blockNum}`);
      continue;
    }
    
    console.log(`Executing script block #${blockNum}...`);
    vm.runInContext(scriptContent, context, { filename: `block-${blockNum}` });
  }
  console.log('✅ All script blocks executed successfully!');
  
  // Now simulate toggleColorMode
  console.log('\n--- SIMULATING toggleColorMode() ---');
  const PBefore = context.P;
  console.log('P.colorMode before:', PBefore.colorMode);
  console.log('data-color-mode attribute before:', context.document.documentElement.getAttribute('data-color-mode'));
  
  // Call toggleColorMode
  try {
    context.toggleColorMode();
  } catch (err) {
    console.log('[MOCK ERROR IGNORED]', err.message);
  }
  
  console.log('P.colorMode after:', PBefore.colorMode);
  console.log('data-color-mode attribute after:', context.document.documentElement.getAttribute('data-color-mode'));
  console.log('--- toggleColorMode() SIMULATION COMPLETE ---');
} catch (e) {
  console.error(`❌ RUNTIME ERROR in script block #${blockNum}:`);
  console.error(e.stack || e.message);
}
console.log('------------------------------------------------------');
