# Architecture — HELIOS-SBL

## Camadas

### 0. Thermodynamic Foundation
- Segunda Lei e irreversibilidade como restrições de projeto.
- Landauer como limite inferior de computação física.
- Métrica SPJ (Semantics per Joule).

### 1. Core SBL
- `Ideogram`: unidade de transferência semântica.
- `Bridge`: mecanismo de mapeamento entre agentes/modelos.
- `Metrics`: fidelidade semântica, perda, energia e entropia.

### 2. Validation Layer
- Checagem de tipos semânticos.
- Propriedades invariantes de transformação.
- Integração futura com provadores formais.

### 3. Ontology Layer
- Grafos semânticos e atualização incremental.
- Política explícita para incerteza e lacunas.

### 4. Visual Layer
- Renderização de grafos, diagnósticos e auditoria.

### 5. Affective Layer
- Coerência comunicacional para colaboração multiagente.

## Diretórios

- `docs/architecture`: especificações de alto nível por camada.
- `docs/theory`: fundamentos formais e filosóficos.
- `docs/specifications`: protocolos e formatos.
- `src/*`: implementação progressiva por módulo.
