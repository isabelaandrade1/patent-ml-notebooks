# Patent-ML Notebooks

Guia rapido e didatico para rodar a aplicacao Flask que expõe um modelo TensorFlow salvo em `modelo_ia.keras`.

## Requisitos
- Python 3.9+ (sugestao: usar ambiente virtual)
- Dependencias listadas em `requirements.txt` (Flask, TensorFlow). Em maquinas sem GPU, prefira usar apenas `tensorflow-cpu` para evitar downloads duplicados.

## Como configurar e executar
1) Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2) Instale as dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3) Garanta que o arquivo do modelo `modelo_ia.keras` esteja no diretorio raiz do projeto.
4) Suba o servidor Flask em modo de desenvolvimento:
   ```bash
   python app.py
   ```
   O servidor inicia em `http://127.0.0.1:5000/`.

Para execucao em producao (Linux), use `gunicorn app:app`. Em Windows, prefira servico como `waitress` ou execute via `flask run`/`python app.py`.

## Endpoints principais
- `/` — teste rapido para checar se o servidor esta respondendo.
- `/pagina` — renderiza `pagina.html` (pagina simples de boas-vindas).
- `/predict` — recebe JSON e retorna a previsao do modelo.

### Formato esperado em `/predict`
Envie um POST com `Content-Type: application/json`:
```json
{
  "input": [
    [1.0, 2.0, 3.0, 4.0]
  ]
}
```
- `input` deve ser um array 2D (lista de amostras). O codigo tenta remodelar entradas 3D com forma `(n, 2, features)` para `(n, features)` se necessario.
- A resposta retorna `previsao` como lista Python (convertida de NumPy), por exemplo:
```json
{
  "previsao": [[0.12, 0.88]]
}
```
Em caso de erro de formato, a API devolve JSON com campo `error` e status HTTP adequado.

## Estrutura do projeto
- `app.py` — servidor Flask, carrega o modelo e expõe rotas.
- `modelo_ia.keras` / `modelo_ia.h5` — pesos do modelo treinado (usar o `.keras` carregado em `app.py`).
- `pagina.html` — pagina simples acessada em `/pagina`.
- `TesteIA.ipynb` — notebook para exploracao/treino.
- `requirements.txt` — lista de dependencias.
- `agiliza-pi/`, `Test-PI/` — pastas vazias reservadas.

## Dicas
- Se o carregamento do modelo falhar, confirme o caminho do arquivo e a versao do TensorFlow. Modelos salvos com versoes diferentes podem exigir reexportacao.
- Antes de atender trafego, valide o shape das entradas que seu modelo espera e adapte o reshape em `app.py` se necessario.
