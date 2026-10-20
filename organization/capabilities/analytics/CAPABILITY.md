# Capability: Analytics

**Lead role:** engineer (data) · strategist (interpretation) · **Status:** defined, manual entry

## Contract
A single set of metric definitions every channel reports against, so channels are
comparable.

## Standard metrics
| Metric | Definition |
|--------|------------|
| followers | Total followers at period end, per platform |
| follower_growth | Net change in followers over the period |
| posts_published | Count of pieces published in the period |
| reach | Unique accounts reached (platform-reported) |
| impressions | Total views/impressions (platform-reported) |
| engagement_rate | (likes + comments + shares + saves) ÷ reach |
| avg_watch_time | Video only, seconds |
| link_clicks | Clicks to tracked links |

## Cadence
- **Weekly snapshot** — `projects/<channel>/reports/analytics/YYYY-Www.yaml`
- **Monthly review** — strategist writes `YYYY-MM-review.md` with insights and
  recommended changes (recommendations become features/issues, not direct edits).

## Data entry
Manual (copied from platform dashboards) until an integration ADR is accepted.
Snapshot files follow [`snapshot.template.yaml`](snapshot.template.yaml).
