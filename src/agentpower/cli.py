"""Command line: `agentpower simulate` and `agentpower estimate`."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from . import __version__, estimators


def _simulate(args) -> int:
    from .experiments import run_all
    from .report import write_report

    results = run_all(seed=args.seed, quick=args.quick)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(json.dumps(results, indent=2, default=float), encoding="utf-8")
    if args.report:
        write_report(results, Path(args.report), figures=Path(args.figures) if args.figures else None)
    print(f"wrote {out / 'results.json'}" + (f" and {args.report}" if args.report else ""))
    return 0


def _estimate(args) -> int:
    """Capacity AP from a CSV with columns task, time_share, baseline_hours, ai_hours."""
    with open(args.tasks, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    shares = [float(r["time_share"]) for r in rows]
    speedups = [float(r["baseline_hours"]) / float(r["ai_hours"]) for r in rows]
    cap = estimators.capacity_ap(shares, speedups)
    print(f"AP-C (capacity): {cap:.2f}  [{estimators.band(cap)}]")
    if args.realised is not None:
        print(f"AP-Q (realised): {args.realised:.2f}  [{estimators.band(args.realised)}]")
        print(f"Absorption:      {estimators.absorption(args.realised, cap):.0%}")
    if args.cost is not None:
        ap = args.realised if args.realised is not None else cap
        print(f"Cost per extra AP: EUR {estimators.cost_per_ap(args.cost, ap):,.0f}/year")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="agentpower", description=__doc__)
    p.add_argument("--version", action="version", version=f"agentpower {__version__}")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("simulate", help="run the Monte Carlo experiments")
    s.add_argument("--seed", type=int, default=20261019)
    s.add_argument("--quick", action="store_true", help="small run for testing")
    s.add_argument("--out", default="results")
    s.add_argument("--report", help="write the markdown report to this path")
    s.add_argument("--figures", help="write SVG figures to this directory (needs matplotlib)")
    s.set_defaults(fn=_simulate)

    e = sub.add_parser("estimate", help="capacity AP from a task timing CSV")
    e.add_argument("tasks", help="CSV: task,time_share,baseline_hours,ai_hours")
    e.add_argument("--realised", type=float, help="measured AP-Q, to report absorption")
    e.add_argument("--cost", type=float, help="added AI cost per FTE and year in EUR")
    e.set_defaults(fn=_estimate)

    args = p.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
