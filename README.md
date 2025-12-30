# Patent-ML Notebooks

## 📋 Sobre o Projeto

Este projeto implementa uma **aplicação de Machine Learning para análise de patentes** utilizando TensorFlow. O sistema consiste em:

- **Modelo de IA treinado** (`modelo_ia.keras`) para classificação/previsão relacionada a dados de patentes
- **API REST em Flask** que expõe o modelo para inferências via requisições HTTP
- **Notebooks Jupyter** para exploração, treinamento e experimentação do modelo

O objetivo é disponibilizar um serviço web que recebe dados de entrada e retorna previsões do modelo de forma acessível e escalável.

## 🎯 Objetivo

Criar uma pipeline completa de Machine Learning que:
1. Processa e analisa dados relacionados a patentes
2. Treina modelos de classificação/regressão usando TensorFlow/Keras
3. Disponibiliza o modelo treinado através de uma API REST
4. Permite integração fácil com outras aplicações e sistemas

## 🧠 Sobre o Modelo

O modelo `modelo_ia.keras` é uma rede neural treinada para realizar previsões a partir de vetores de características extraídos de dados de patentes. 

- **Entrada**: Vetores numéricos representando características das patentes
- **Saída**: Probabilidades ou classificações (depende da tarefa específica)
- **Framework**: TensorFlow/Keras

## 🚀 Guia Rápido

### Requisitos
- Python 3.9+ (sugestão: usar ambiente virtual)
- Dependências listadas em `requirements.txt` (Flask, TensorFlow)
- Em máquinas sem GPU, prefira `tensorflow-cpu` para evitar downloads desnecessários

### Como Configurar e Executar

1) **Crie e ative um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # ou
   source .venv/bin/activate  # Linux/Mac
   ```

2) **Instale as dependências**: 
   ```bash
   pip install -r requirements.txt
   ```

3) **Garanta que o modelo esteja presente**:  o arquivo `modelo_ia.keras` deve estar no diretório raiz

4) **Inicie o servidor Flask**:
   ```bash
   python app.py
   ```
   O servidor iniciará em `http://127.0.0.1:5000/`

### Execução em Produção
- **Linux**:  use `gunicorn app:app`
- **Windows**: use `waitress-serve` ou `python app.py`

## 🔌 Endpoints da API

### `GET /`
Teste rápido para verificar se o servidor está respondendo.

**Resposta**:  Mensagem de status simples

---

### `GET /pagina`
Renderiza uma página HTML de boas-vindas (`pagina.html`).

---

### `POST /predict`
Endpoint principal para realizar previsões com o modelo. 

**Formato da requisição**:
```json
{
  "input": [
    [1.0, 2.0, 3.0, 4.0]
  ]
}
```

**Parâmetros**:
- `input`: Array 2D contendo as amostras (lista de vetores de características)
- O código automaticamente redimensiona entradas 3D `(n, 2, features)` para `(n, features)` se necessário

**Resposta de sucesso**:
```json
{
  "previsao":  [[0.12, 0.88]]
}
```

**Resposta de erro**: 
```json
{
  "error": "Mensagem de erro descritiva"
}
```

### Exemplo com cURL
```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"input": [[1.0, 2.0, 3.0, 4.0]]}'
```

## 📁 Estrutura do Projeto

```
patent-ml-notebooks/
├── app.py                 # Servidor Flask e rotas da API
├── modelo_ia. keras        # Modelo treinado (formato Keras)
├── modelo_ia.h5           # Backup do modelo (formato H5)
├── pagina.html            # Página web simples
├── TesteIA.ipynb          # Notebook para experimentação e treino
├── requirements.txt       # Dependências do projeto
├── agiliza-pi/            # Pasta auxiliar
└── Test-PI/               # Pasta auxiliar
```

## 💡 Dicas e Troubleshooting

### Problemas ao carregar o modelo
- Confirme que o arquivo `modelo_ia.keras` existe no diretório correto
- Verifique se a versão do TensorFlow é compatível com o modelo
- Modelos salvos em versões diferentes podem precisar ser reexportados

### Validação de entrada
- Antes de usar em produção, valide o shape esperado pelo modelo
- Adapte o código de reshape em `app.py` se necessário
- Teste com dados reais para garantir compatibilidade

### Performance
- Para inferências mais rápidas, considere usar TensorFlow Lite ou ONNX
- Em produção, configure workers do Gunicorn adequadamente
- Monitore uso de memória e CPU

## 📝 Desenvolvimento

Para explorar e treinar novos modelos, utilize o notebook `TesteIA.ipynb`:

```bash
jupyter notebook TesteIA.ipynb
```

## 🤝 Contribuindo

Contribuições são bem-vindas!  Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests
