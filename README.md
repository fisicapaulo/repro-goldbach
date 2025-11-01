# repro-goldbach

Repositório para experimentos e pipeline relacionados a verificações e estimativas no contexto da conjectura de Goldbach, incluindo componentes de “minor arcs”, ajustes de janelas (phi), pesos e utilitários de auditoria.

## Visão geral

Este projeto organiza scripts e módulos para:
- Configuração de parâmetros (janelas `phi`, pesos padrão, amostras).
- Estimativas em arcos menores (minor arcs gap).
- Componentes auxiliares (arquimedeano, constantes de tipo, etc.).
- Auditoria e validação dos resultados.

Estrutura típica:
```
repro-goldbach/
├─ data/
│  ├─ samples/            # Configurações e amostras (ex.: config_N1e8.json)
│  ├─ weights/            # Pesos padrão (ex.: w_default.json)
│  └─ windows/            # Janelas phi padrão (ex.: phi_default.json)
├─ scripts/
│  └─ estimate_Cdd.py     # Script principal de estimativa (exemplo)
├─ src/
│  ├─ archimedean.py
│  ├─ arcs.py
│  ├─ audit.py
│  ├─ hl_singular.py
│  ├─ minors_gap.py
│  └─ type_constants.py
└─ requirements.txt
```

## Requisitos

- Python 3.10+ recomendado
- Pacotes listados em `requirements.txt`

Instalação (Windows PowerShell):
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Uso rápido

Exemplo de execução do script de estimativa:
```bash
# Ative o ambiente virtual antes (se usar venv)
python scripts/estimate_Cdd.py --config data/samples/config_N1e8.json
```

Parâmetros comuns:
- `--config`: caminho para o arquivo de configuração de amostra.
- Outros parâmetros podem existir conforme o script (consulte a ajuda interna).

## Desenvolvimento

- Organização modular em `src/`.
- Padronização de finais de linha: `.gitattributes` com `* text=auto` (opcional).
- Commits com mensagens curtas e descritivas.

## Contribuição

Contribuições são bem-vindas:
1. Faça um fork deste repositório.
2. Crie uma branch: `git checkout -b feature/nome-da-feature`.
3. Commit: `git commit -m "Add: descrição da feature"`.
4. Push: `git push origin feature/nome-da-feature`.
5. Abra um Pull Request com detalhes.

## Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais informações.

## Autor e contato

- Autor: Paulo Vieira
- Email: paulo.henrique@educacao.mg.gov.br
- Contato: (adicione seu e-mail ou site)
- Repositório: https://github.com/fisicapaulo/repro-goldbach
