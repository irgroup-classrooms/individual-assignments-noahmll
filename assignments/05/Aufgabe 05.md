1.  
Spalten  
1: Leer    - sollte aber ID (vom Datentyp int) sein  
2: char    - Charakter des Filmes der gerade spricht (vom Datentyp string), möglicherweise irreführend, wegen Datentyp char  
3: dialog  - Das was der Charakter sagt, in Anführungsstrichen (vom Datentyp string)  
4: movie   - Der Film, in dem der Charakter den Dialog spricht (vom Datentyp string)  
  
2.  
Transformationen in Open Refine:  
```json
[
  {
    "op": "core/text-transform",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "dialog",
    "expression": "value.replace(/[\\p{Zs}\\s]+/,' ')",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10,
    "description": "Text transform on cells in column dialog using expression value.replace(/[\\p{Zs}\\s]+/,' ')"
  },
  {
    "op": "core/text-transform",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "dialog",
    "expression": "value.trim()",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10,
    "description": "Text transform on cells in column dialog using expression value.trim()"
  },
  {
    "op": "core/text-transform",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "char",
    "expression": "value.trim()",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10,
    "description": "Text transform on cells in column char using expression value.trim()"
  },
  {
    "op": "core/text-transform",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "movie",
    "expression": "value.trim()",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10,
    "description": "Text transform on cells in column movie using expression value.trim()"
  },
  {
    "op": "core/text-transform",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "Column",
    "expression": "value.trim()",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10,
    "description": "Text transform on cells in column Column using expression value.trim()"
  },
  {
    "op": "core/text-transform",
    "engineConfig": {
      "facets": [],
      "mode": "row-based"
    },
    "columnName": "dialog",
    "expression": "grel:value.replace(\",\",\"\").replace(/\\s{2,}/,\" \").replace(/^ | $/,\"\")",
    "onError": "keep-original",
    "repeat": false,
    "repeatCount": 10,
    "description": "Text transform on cells in column dialog using expression grel:value.replace(\",\",\"\").replace(/\\s{2,}/,\" \").replace(/^ | $/,\"\")"
  },
  {
    "op": "core/column-rename",
    "oldColumnName": "Column",
    "newColumnName": "ID",
    "description": "Rename column Column to ID"
  },
  {
    "op": "core/column-rename",
    "oldColumnName": "char",
    "newColumnName": "character",
    "description": "Rename column char to character"
  }
]
```  
  
3.  
```sh
$ wc –l lotr-scripts_cleaned.csv
2391 lotr-scripts_cleaned.csv
$ wc -w lotr-scripts_cleaned.csv
32334 lotr-scripts_cleaned.csv
```
