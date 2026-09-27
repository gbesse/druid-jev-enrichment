-- After ingesting enriched.jsonl into a Druid datasource named events:
SELECT jev_outcome, COUNT(*) AS n
FROM events
WHERE __time >= TIMESTAMP '2026-01-01 00:00:00'
GROUP BY jev_outcome;
