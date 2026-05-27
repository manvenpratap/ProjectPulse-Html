with open('/Users/manvenpratapsingh/Downloads/ProjectPulse/projectpulse.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_orphan = None
end_orphan = None

for i, line in enumerate(lines):
    if i > 17619 and start_orphan is None and "$id('view-actions').innerHTML" in line:
        start_orphan = i
    if start_orphan is not None and 'function animateCounter' in line:
        end_orphan = i
        break

print(f"Orphan block: lines {start_orphan+1} to {end_orphan} (1-indexed)")
print(f"  First: {lines[start_orphan][:80]!r}")
print(f"  Before end: {lines[end_orphan-1][:80]!r}")

new_lines = lines[:start_orphan] + lines[end_orphan:]

with open('/Users/manvenpratapsingh/Downloads/ProjectPulse/projectpulse.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Done. Removed {end_orphan - start_orphan} orphan lines.")
print(f"New total lines: {len(new_lines)}")
