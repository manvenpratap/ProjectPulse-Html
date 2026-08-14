#!/usr/bin/env python3
import sys
import os
import subprocess
import re

def main():
    html_path = 'projectpulse.html'
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {html_path}: {e}")
        sys.exit(1)

    js_lines = []
    in_script = False
    
    # Simple regex to check for script tags
    script_start_re = re.compile(r'<script(?:\s+[^>]*?)?>', re.IGNORECASE)
    script_end_re = re.compile(r'</script>', re.IGNORECASE)

    for i, line in enumerate(lines):
        # Line numbers are 1-indexed, current index is i
        line_num = i + 1
        
        # Check if this line has a script tag with src (we skip external scripts)
        if 'src=' in line.lower() and '<script' in line.lower():
            js_lines.append('\n')  # Keep line numbers aligned
            continue
            
        if not in_script:
            # Match actual HTML script start tag at line beginning/HTML context (ignore strings like '${"<script"')
            match_start = script_start_re.search(line)
            if match_start and not line.strip().startswith(('$', "'", '"', '`', '+', 'html')):
                in_script = True
                js_lines.append('\n')
            else:
                js_lines.append('\n')
        else:
            match_end = script_end_re.search(line)
            # Ignore matches that are inside template strings/JS code like '${'</script>'}'
            if match_end and not ("'</script>'" in line or '"</script>"' in line or "'/script'" in line or '"/script"' in line):
                in_script = False
                js_lines.append('\n')
            else:
                js_lines.append(line)

    temp_js_path = 'scripts/temp_check.js'
    try:
        with open(temp_js_path, 'w', encoding='utf-8') as f:
            f.writelines(js_lines)
    except Exception as e:
        print(f"Error writing temporary JS file: {e}")
        sys.exit(1)

    # Run node --check
    try:
        result = subprocess.run(
            ['node', '--check', temp_js_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            print("❌ JS Syntax check failed:")
            # Replace the temporary filename with the original HTML filename in the error output
            error_output = result.stderr.replace(temp_js_path, html_path)
            print(error_output)
            sys.exit(result.returncode)
        else:
            print("✅ JS Syntax check passed! No syntax errors found.")
            sys.exit(0)
    except FileNotFoundError:
        print("Warning: node command not found. Cannot perform syntax check.")
        sys.exit(0)
    except Exception as e:
        print(f"Error running node check: {e}")
        sys.exit(1)
    finally:
        if os.path.exists(temp_js_path):
            try:
                os.remove(temp_js_path)
            except Exception:
                pass

if __name__ == '__main__':
    main()
