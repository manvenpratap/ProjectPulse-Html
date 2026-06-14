"""
build_all.py
============
Master build orchestrator for the ProjectPulse three-document documentation suite.
Runs all three document builders in sequence and reports results.

Usage:
  python scripts/build_all.py           -- Build all three documents
  python scripts/build_all.py --pcd     -- Build PCD only
  python scripts/build_all.py --fsd     -- Build FSD only
  python scripts/build_all.py --umi     -- Build UMI only
"""
import os, sys, time, datetime
sys.path.insert(0, os.path.dirname(__file__))

def main():
    args = set(sys.argv[1:])
    build_pcd_flag = "--pcd" in args or not args
    build_fsd_flag = "--fsd" in args or not args
    build_umi_flag = "--umi" in args or not args

    results = []
    start_total = time.time()

    print("\n" + "="*65)
    print("  ProjectPulse — Documentation Suite Build")
    print(f"  Started: {datetime.datetime.now().strftime('%d %B %Y, %H:%M:%S')}")
    print("="*65)

    if build_pcd_flag:
        try:
            t0 = time.time()
            from build_pcd import build_pcd
            path = build_pcd()
            elapsed = time.time() - t0
            size = os.path.getsize(path) / 1024
            results.append(("PCD", path, f"{size:.0f} KB", f"{elapsed:.1f}s", "OK"))
        except Exception as e:
            results.append(("PCD", "—", "—", "—", f"FAILED: {e}"))

    if build_fsd_flag:
        try:
            t0 = time.time()
            from build_fsd import build_fsd
            path = build_fsd()
            elapsed = time.time() - t0
            size = os.path.getsize(path) / 1024
            results.append(("FSD", path, f"{size:.0f} KB", f"{elapsed:.1f}s", "OK"))
        except Exception as e:
            results.append(("FSD", "—", "—", "—", f"FAILED: {e}"))

    if build_umi_flag:
        try:
            t0 = time.time()
            from build_umi import build_umi
            path = build_umi()
            elapsed = time.time() - t0
            size = os.path.getsize(path) / 1024
            results.append(("UMI", path, f"{size:.0f} KB", f"{elapsed:.1f}s", "OK"))
        except Exception as e:
            results.append(("UMI", "—", "—", "—", f"FAILED: {e}"))

    total_elapsed = time.time() - start_total

    print("\n" + "="*65)
    print("  BUILD RESULTS")
    print("="*65)
    for doc_type, path, size, elapsed, status in results:
        status_label = "  OK  " if status == "OK" else "FAILED"
        print(f"  [{status_label}] {doc_type}  |  {size}  |  {elapsed}  |  {os.path.basename(path) if path != '--' else '--'}")
        if status != "OK":
            print(f"          Error: {status}")
    print(f"\n  Total build time: {total_elapsed:.1f}s")
    print("="*65 + "\n")

    failed = [r for r in results if r[4] != "OK"]
    sys.exit(1 if failed else 0)

if __name__ == "__main__":
    main()
