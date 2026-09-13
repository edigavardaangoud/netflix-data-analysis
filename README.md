# Netflix: Content, Growth & Market Analysis

A data analysis portfolio project combining a self-built Python data pipeline with Excel-based business analysis, exploring Netflix's content catalog, subscriber growth, revenue, and viewership trends.

## What this project does

- **Collects** Netflix's content catalog (India region) live from The Movie Database (TMDB) API — 7,961 titles across movies and TV shows
- **Cleans** the dataset using pandas — deduplication, missing value handling — down to a final analysis-ready set of 7,859 titles
- **Analyzes** the data in Excel using pivot tables and charts: content mix, genre distribution, ratings, release trends
- **Contextualizes** the content data against Netflix's real business performance (2013–2025): subscriber growth, revenue, profitability, and viewership — sourced from Netflix's official SEC filings and engagement reports

## Tools used

- **Python** — `requests`, `pandas`, `python-dotenv`
- **TMDB API** — content catalog data source
- **Excel** — Power Query, pivot tables, PivotCharts, formulas, dashboard design

## Project structure

```
├── fetch_netflix_catalog.py      # Pulls movies & TV shows from TMDB API
├── clean_data.py                 # Cleans and combines the raw datasets
├── netflix_portfolio_report.xlsx # Full Excel analysis (8 sheets, 7 charts)
├── Netflix_Project_Summary.docx  # 2-page executive summary
└── README.md
```

## Key findings

- Netflix India's catalog skews toward movies (57%) over TV shows (43%)
- Drama, Comedy, and Documentary are the top three genres, together over 40% of the catalog
- 66% of titles rate "Good (6–8)," only 1.8% rate "Low" — indicating strong content curation
- Global subscribers grew 7x from 44M (2013) to 325M (2025)
- 2022 was a major inflection point: growth slowed to 4.0% YoY alongside Netflix's first-ever subscriber loss, followed by a strong recovery via the password-sharing crackdown and ad-tier launch
- Operating margin nearly doubled, from 17.8% (2022) to 29.5% (2025) — a clear pivot toward profitability
- Netflix discontinued quarterly subscriber disclosure starting Q1 2025, shifting focus to revenue and engagement

Full analysis and charts in `netflix_portfolio_report.xlsx`. Full written summary in `Netflix_Project_Summary.docx`.

## Data sources

- Content catalog: [TMDB API](https://www.themoviedb.org/documentation/api)
- Subscriber & revenue data: Netflix, Inc. Quarterly Shareholder Letters (SEC Form 8-K), [ir.netflix.net](https://ir.netflix.net)
- Viewership data: Netflix's official ["What We Watched"](https://about.netflix.com) Engagement Reports

## How to run this yourself

1. Get a free API key from [themoviedb.org](https://www.themoviedb.org)
2. Create a `.env` file with `TMDB_API_KEY=your_key_here`
3. `pip install requests pandas python-dotenv`
4. Run `python fetch_netflix_catalog.py`, then `python clean_data.py`

---
*Built as a portfolio project to demonstrate end-to-end data analysis skills: data collection via API, data cleaning, business analysis, and insight communication.*
