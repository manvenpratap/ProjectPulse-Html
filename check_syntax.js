const fs = require('fs');
const vm = require('vm');

const filePath = '/Users/manvenpratapsingh/Downloads/ProjectPulse/projectpulse.html';
const content = fs.readFileSync(filePath, 'utf8');

// Regex to find all script blocks
const scriptRegex = /<script[^>]*>([\s\S]*?)<\/script>/gi;
let match;
let blockNum = 0;
let errors = 0;

while ((match = scriptRegex.exec(content)) !== null) {
  blockNum++;
  const scriptContent = match[1].trim();
  if (!scriptContent) continue;
  
  try {
    new vm.Script(scriptContent, { filename: `block-${blockNum}` });
  } catch (e) {
    errors++;
    const lineInFile = content.substring(0, match.index).split('\n').length;
    console.error(`\n❌ SYNTAX ERROR in script block #${blockNum} (starts at line ~${lineInFile}):`);
    console.error(e.stack || e.message);
  }
}

if (errors === 0) {
  console.log(`✅ All ${blockNum} script blocks passed syntax validation.`);
} else {
  console.log(`\n⚠️  ${errors} out of ${blockNum} blocks have syntax errors.`);
}
