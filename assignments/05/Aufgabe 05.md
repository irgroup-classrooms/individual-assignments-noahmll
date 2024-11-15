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
  
5.1  
```sh
$ wc –l lotr-scripts_cleaned.csv
2391 lotr-scripts_cleaned.csv
$ cut -d',' -f3 lotr-scripts_cleaned.csv | tr ' ' '\n' | tr "[!?.]" "\n" | sort | uniq | wc -l
4059
```
5.2  
```sh
$ cat lotr-scripts_cleaned.csv | awk -F',' '{print $4}' | sort | uniq -c
    507 The Fellowship of the Ring
    873 The Return of the King
   1010 The Two Towers
      1 movie
```
5.3  
```sh
$ cut -d',' -f2 lotr-scripts_cleaned.csv | sort | uniq -c | sort -nr | head -5
    226 FRODO
    217 SAM
    205 GANDALF
    187 ARAGORN
    163 PIPPIN
```
5.4  
```sh
$ cut -d',' -f3 lotr-scripts_cleaned.csv | tr ' ' '\n' | grep -oP '\b[A-Z][a-z]+\b' | sort | uniq -c | sort -nr | head -5
    225 The
    220 You
    180 It
    161 We
    148 Frodo
```
