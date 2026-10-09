# Druid Jev Enrichment

Experimental community alpha v0.1.2 · MIT.

## Français

Un outil enrichit des lignes JSON avec des dimensions Jev avant leur ingestion dans Apache Druid. Les lignes en échec sont conservées dans un fichier de revue séparé.

Installation :

```sh
mkdir -p .local
python3 enrich.py examples/events.jsonl .local/enriched.jsonl .local/review.jsonl
```

Ingérer ensuite `.local/enriched.jsonl` avec votre pipeline Druid. Les deux fichiers de sortie ont des permissions `600` et `.local/` est ignoré par Git. Le fichier de revue peut contenir les lignes d’origine : limiter son accès et sa durée de conservation.

Variables serveur : `TYPESAFE_API_KEY`. Garder les secrets hors du dépôt et de la configuration visible par les utilisateurs.

Interroger ensuite `jev_outcome`, `jev_choice` et `jev_probability` comme des dimensions ordinaires. L’évaluation a lieu avant l’ingestion, jamais à chaque ligne d’une requête SQL.

Une ligne qui possède déjà un champ `jev_` est envoyée au fichier de revue sans être modifiée.

## English

A tool adds Jev dimensions to JSON rows before Apache Druid ingestion. Failed rows are preserved in a separate review file.

Setup:

```sh
mkdir -p .local
python3 enrich.py examples/events.jsonl .local/enriched.jsonl .local/review.jsonl
```

Ingest `.local/enriched.jsonl` with your Druid pipeline. Both output files have `600` permissions and `.local/` is ignored by Git. The review file may contain original rows: restrict access and retention.

Server variables: `TYPESAFE_API_KEY`. Keep secrets outside the repository and user-visible configuration.

Query `jev_outcome`, `jev_choice`, and `jev_probability` as ordinary dimensions. Evaluation happens before ingestion, never for each SQL query row.

A row that already has a `jev_` field goes to the review file without modification.

## Español

Una herramienta añade dimensiones Jev a filas JSON antes de ingerirlas en Apache Druid. Las filas fallidas se conservan en un archivo de revisión separado.

Instalación:

```sh
mkdir -p .local
python3 enrich.py examples/events.jsonl .local/enriched.jsonl .local/review.jsonl
```

Ingiere `.local/enriched.jsonl` con tu pipeline de Druid. Ambos archivos de salida tienen permisos `600` y Git ignora `.local/`. El archivo de revisión puede contener filas originales: limita su acceso y conservación.

Variables del servidor: `TYPESAFE_API_KEY`. Mantén los secretos fuera del repositorio y de la configuración visible para usuarios.

Consulta `jev_outcome`, `jev_choice` y `jev_probability` como dimensiones normales. La evaluación ocurre antes de la ingesta, nunca para cada fila de una consulta SQL.

Una fila que ya tenga un campo `jev_` se envía al archivo de revisión sin modificaciones.

## Verification / Vérification / Verificación

```sh
python3 -m unittest discover -s tests -v
```

Tests use synthetic Jev responses and host event fixtures. Threshold `0.9` in `policy.json` is an example and must be calibrated on labeled data before automatic actions. No live host or Jev service has been exercised. / Les tests utilisent des réponses synthétiques et le seuil doit être calibré ; aucun hôte ni service Jev réel n’a été testé. / Las pruebas usan respuestas sintéticas y el umbral debe calibrarse; no se ha probado un host ni un servicio Jev real.

Host reference / Référence de l’hôte / Referencia del host: https://druid.apache.org/docs/latest/development/modules/

## Contrôle d’adoption · Adoption check · Comprobación de adopción

[Français : essayer un cas concret](examples/adoption-check.md) · [English: try a concrete case](examples/adoption-check.md) · [Español: pruebe un caso concreto](examples/adoption-check.md).
