import json
import re
from pathlib import Path
from collections import Counter

def clean_label(label):
    # Remove parentheses, leading dots, etc.
    label = re.sub(r'[\(\)\.\{\}\:\[\]\-\_\>\!\$\@]', ' ', label)
    # Split by camelCase or snake_case
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\b)|\d+', label)
    return [w.lower() for w in words if len(w) > 1]

def generate_community_names():
    graph_path = Path("graphify-out/graph.json")
    if not graph_path.exists():
        print("graph.json not found!")
        return

    with open(graph_path, "r", encoding="utf-8") as f:
        graph_data = json.load(f)

    # Group nodes by community
    communities = {}
    for node in graph_data.get("nodes", []):
        cid = node.get("community")
        if cid is not None:
            communities.setdefault(cid, []).append(node)

    labels = {}
    stop_words = {
        "js", "fs", "content", "lines", "index", "match", "code", "file", "target", "path",
        "result", "data", "value", "list", "array", "object", "function", "var", "let", "const",
        "for", "each", "get", "set", "add", "remove", "update", "delete", "run", "test", "mock",
        "test_excel_export_mock", "scratch", "main", "config", "util", "helpers", "lib", "html", "css"
    }

    for cid, nodes in communities.items():
        # Heuristics for naming
        # 1. Collect all terms from node labels and filenames
        words_counter = Counter()
        files = set()
        file_types = Counter()
        
        for n in nodes:
            lbl = n.get("label", "")
            src_file = n.get("source_file", "")
            ftype = n.get("file_type", "")
            if src_file:
                files.add(Path(src_file).name)
            if ftype:
                file_types[ftype] += 1

            for w in clean_label(lbl):
                if w not in stop_words:
                    words_counter[w] += 1
            if src_file:
                # also count terms in filename
                for w in clean_label(Path(src_file).stem):
                    if w not in stop_words:
                        words_counter[w] += 2  # weight filename terms higher

        # 2. Get top terms
        top_terms = [item[0] for item in words_counter.most_common(5)]
        
        # 3. Formulate name
        if not top_terms:
            if files:
                # Name after the most common file
                name = f"Module {list(files)[0]}"
            else:
                name = f"Community {cid}"
        else:
            # Title case top terms
            name = " & ".join(w.capitalize() for w in top_terms[:3])
            
        # Clean up name length
        if len(name) > 60:
            name = name[:57] + "..."
            
        labels[cid] = name

    # Write labels to labels file
    labels_path = Path("graphify-out/.graphify_labels.json")
    with open(labels_path, "w", encoding="utf-8") as f:
        json.dump({str(k): v for k, v in labels.items()}, f, indent=2, ensure_ascii=False)

    print(f"Generated names for {len(labels)} communities.")

    # Now let's try to update GRAPH_REPORT.md and graph.html using graphify cluster-only
    # Wait, cluster-only command re-runs clustering but since we already have the labels, let's see if we can regenerate report.
    # We can load the labels and replace "Community X" with the actual name in GRAPH_REPORT.md.
    report_path = Path("graphify-out/GRAPH_REPORT.md")
    if report_path.exists():
        report_content = report_path.read_text(encoding="utf-8")
        for cid, name in labels.items():
            # Replace Community X - "Community X"
            report_content = report_content.replace(f'Community {cid} - "Community {cid}"', f'Community {cid} - "{name}"')
            report_content = report_content.replace(f'[[_COMMUNITY_Community {cid}|Community {cid}]]', f'[[_COMMUNITY_Community {cid}|{name}]]')
        report_path.write_text(report_content, encoding="utf-8")
        print("Updated GRAPH_REPORT.md with community names.")

if __name__ == "__main__":
    generate_community_names()
