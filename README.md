# Druid Jev Enrichment

Experimental community alpha v0.1.0 · MIT.

## Français

Un outil enrichit des lignes JSON avec des dimensions Jev avant leur ingestion dans Apache Druid. Les lignes en échec sont conservées dans un fichier de revue séparé.

Installation :

```sh
python3 enrich.py examples/events.jsonl enriched.jsonl review.jsonl
# Ingest enriched.jsonl with your existing Druid ingestion pipeline.
```

Variables serveur : `TYPESAFE_API_KEY`. Garder les secrets hors du dépôt et de la configuration visible par les utilisateurs.

Interroger ensuite `jev_outcome`, `jev_choice` et `jev_probability` comme des dimensions ordinaires. L’évaluation a lieu avant l’ingestion, jamais à chaque ligne d’une requête SQL.

## English

A tool adds Jev dimensions to JSON rows before Apache Druid ingestion. Failed rows are preserved in a separate review file.

Setup:

```sh
python3 enrich.py examples/events.jsonl enriched.jsonl review.jsonl
# Ingest enriched.jsonl with your existing Druid ingestion pipeline.
```

Server variables: `TYPESAFE_API_KEY`. Keep secrets outside the repository and user-visible configuration.

Query `jev_outcome`, `jev_choice`, and `jev_probability` as ordinary dimensions. Evaluation happens before ingestion, never for each SQL query row.

## Español

Una herramienta añade dimensiones Jev a filas JSON antes de ingerirlas en Apache Druid. Las filas fallidas se conservan en un archivo de revisión separado.

Instalación:

```sh
python3 enrich.py examples/events.jsonl enriched.jsonl review.jsonl
# Ingest enriched.jsonl with your existing Druid ingestion pipeline.
```

Variables del servidor: `TYPESAFE_API_KEY`. Mantén los secretos fuera del repositorio y de la configuración visible para usuarios.

Consulta `jev_outcome`, `jev_choice` y `jev_probability` como dimensiones normales. La evaluación ocurre antes de la ingesta, nunca para cada fila de una consulta SQL.

## Verification / Vérification / Verificación

```sh
python3 -m unittest discover -s tests -v
```

Tests use synthetic Jev responses and host event fixtures. Threshold `0.9` in `policy.json` is an example and must be calibrated on labeled data before automatic actions. No live host or Jev service has been exercised. / Les tests utilisent des réponses synthétiques et le seuil doit être calibré ; aucun hôte ni service Jev réel n’a été testé. / Las pruebas usan respuestas sintéticas y el umbral debe calibrarse; no se ha probado un host ni un servicio Jev real.

Host reference / Référence de l’hôte / Referencia del host: https://druid.apache.org/docs/latest/development/modules/
