# druid-jev-enrichment — contrôle d’adoption · adoption check · comprobación de adopción

## Français

Point de départ local, après la préparation indiquée dans le README :

```sh
python3 -m unittest discover -s tests -v
```

Une ligne qui contient déjà une dimension `jev_` doit aller en revue plutôt qu’être écrasée avant ingestion. Vérifiez aussi les permissions et la rétention du fichier de revue.

## English

Local starting point, after the setup described in the README:

```sh
python3 -m unittest discover -s tests -v
```

A row that already has a `jev_` dimension should go to review instead of being overwritten before ingestion. Also check permissions and retention for the review file.

## Español

Punto de partida local, después de la preparación descrita en el README:

```sh
python3 -m unittest discover -s tests -v
```

Una fila que ya contiene una dimensión `jev_` debe ir a revisión en lugar de sobrescribirse antes de la ingesta. Compruebe además los permisos y la retención del archivo de revisión.
## Variante synthétique · Synthetic variation · Variante sintética

```text
{"event_id":"synthetic-1","jev_choice":"preexisting"}
```

FR : adaptez une copie de la fixture locale à cette situation, puis vérifiez le comportement décrit ci-dessus. Les valeurs sont illustratives, pas des résultats Jev mesurés.

EN: adapt a copy of the local fixture to this situation, then check the behavior described above. Values are illustrative, not measured Jev output.

ES: adapte una copia de la fixture local a esta situación y compruebe el comportamiento descrito arriba. Los valores son ilustrativos, no resultados Jev medidos.

## Second cas · Second case · Segundo caso

```text
line={"event_id":"synthetic-2","text":null}
```

**FR :** Une ligne inutilisable doit être conservée pour revue au lieu de recevoir des dimensions Jev inventées. Vérifiez le traitement des erreurs avant ingestion.

**EN:** An unusable row should be preserved for review instead of receiving invented Jev dimensions. Check error handling before ingestion.

**ES:** Una fila inutilizable debe conservarse para revisión en lugar de recibir dimensiones Jev inventadas. Compruebe el tratamiento de errores antes de la ingesta.

FR : `python3 -m examples.offline_invalid_row` exerce une ligne JSONL invalide, conserve la ligne brute en revue et échoue avant tout appel réseau.

EN: `python3 -m examples.offline_invalid_row` exercises an invalid JSONL row, preserves the raw row for review, and fails before any network call.

ES: `python3 -m examples.offline_invalid_row` prueba una fila JSONL no válida, conserva la fila original para revisión y falla antes de cualquier llamada de red.
