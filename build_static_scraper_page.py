from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd


ROOT = Path(r"C:\Users\uno\Documents\project\rhddb\3Scrapper_in_home")
OUTPUT = Path(r"C:\Users\uno\Documents\project\naroyounho.github.io\scraper_snapshot.html")


def _read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, encoding="utf-8-sig")


def _table_html(df: pd.DataFrame) -> str:
    if df.empty:
        return "<p>No results.</p>"
    return df.to_html(index=False, escape=True)


def main() -> None:
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    berlin = _read_csv(ROOT / "python.csv")
    web3 = _read_csv(ROOT / "web3_python.csv")
    wework = _read_csv(ROOT / "wework_python.csv")

    html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Scraper Snapshot</title>
    <style>
      body {{ font-family: Arial, sans-serif; margin: 32px; }}
      h1 {{ margin-bottom: 4px; }}
      .meta {{ color: #555; margin-bottom: 24px; }}
      table {{ border-collapse: collapse; width: 100%; margin-bottom: 28px; }}
      th, td {{ border: 1px solid #ddd; padding: 8px; font-size: 14px; }}
      th {{ background: #f5f5f5; text-align: left; }}
      .section {{ margin-bottom: 32px; }}
    </style>
  </head>
  <body>
    <h1>Scraper Snapshot</h1>
    <div class="meta">Generated at: {stamp} / keyword: python</div>

    <div class="section">
      <h2>BerlinStartupJobs</h2>
      {_table_html(berlin)}
    </div>

    <div class="section">
      <h2>Web3Career</h2>
      {_table_html(web3)}
    </div>

    <div class="section">
      <h2>WeWorkRemotely</h2>
      {_table_html(wework)}
    </div>
  </body>
</html>
"""
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
