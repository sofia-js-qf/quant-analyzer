
# Quant Analyzer — Retrieval‑Augmented PDF Question Answering

This project allows you to **ask natural language questions about your own research papers** and receive answers grounded in the actual text of those documents.  

It combines **semantic search** (FAISS) with a **text generation model** to create a Retrieval‑Augmented Generation (RAG) pipeline.

---

## Purpose

The goal is to make your research papers *interactive*. Instead of manually searching through PDFs, you can query them directly and get synthesized answers that cite the relevant sections.

This project was built using the following papers as the primary knowledge base:

- Leippold, Markus and Matthys, Felix, Economic Policy Uncertainty and the Yield Curve (April 25, 2022). Swiss Finance Institute Research Paper No. 22-36, Forthcoming, Review of Finance, Available at SSRN: https://ssrn.com/abstract=2669500 or http://dx.doi.org/10.2139/ssrn.2669500
- Ait-Sahalia, Yacine and Matthys, Felix and Osambela, Emilio and Sircar, Ronnie, When Uncertainty and Volatility are Disconnected: Implications for Asset Pricing and Portfolio Performance (September, 2021). FEDS Working Paper No. 2021-63, Available at SSRN: https://ssrn.com/abstract=3945259 or http://dx.doi.org/10.17016/FEDS.2021.063
- Ait-Sahalia, Yacine and Matthys, Felix, Robust Consumption and Portfolio Policies When Asset Prices Can Jump (September 24, 2018). Journal of Economic Theory, 2019, 179, 1-56., Available at SSRN: https://ssrn.com/abstract=2976562 or http://dx.doi.org/10.2139/ssrn.2976562
- Leippold, Markus, Value-at-Risk and Other Risk Measures (March 16, 2015). Available at SSRN: https://ssrn.com/abstract=2579256 or http://dx.doi.org/10.2139/ssrn.2579256
- Leippold, Markus, Don't Rely on VAR. Euromoney, November 2004, Available at SSRN: https://ssrn.com/abstract=981134
---

## Features

- **PDF ingestion** → splits your papers into semantic chunks and stores them in a FAISS index.
- **Semantic retrieval** → finds the most relevant chunks for your question.
- **Modek**:
  - GPT‑2 for quick tests (smaller context window, faster load).

- **Progress indicators** → see exactly when the system is loading, retrieving, and generating.
- **Token‑safe truncation** → avoids model errors from overly long prompts.

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/quant-analyzer.git
cd quant-analyzer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Usage

### 1. Ingest your PDFs
Place your PDFs in `data/papers/` and run:
```bash
python src/retrieval/ingest.py
```

### 2. Ask questions

python src/main.py 
```

When prompted, type your question, e.g.:
```
Summarize the methodology for calculating Expected Shortfall as described in my papers, and explain how it differs from Value at Risk.


## How it works

1. **Ingestion** — PDFs are split into overlapping text chunks, embedded with `sentence-transformers`, and stored in a FAISS index along with metadata.
2. **Retrieval** — For each question, the system encodes it into an embedding and searches FAISS for the most relevant chunks.
3. **Prompt construction** — The retrieved chunks are combined with your question into a single prompt.
4. **Generation** — The prompt is sent to the chosen model, which produces an answer grounded in your documents.

---

### Citations
- Leippold, Markus and Matthys, Felix, Economic Policy Uncertainty and the Yield Curve (April 25, 2022). Swiss Finance Institute Research Paper No. 22-36, Forthcoming, Review of Finance, Available at SSRN: https://ssrn.com/abstract=2669500 or http://dx.doi.org/10.2139/ssrn.2669500
- Ait-Sahalia, Yacine and Matthys, Felix and Osambela, Emilio and Sircar, Ronnie, When Uncertainty and Volatility are Disconnected: Implications for Asset Pricing and Portfolio Performance (September, 2021). FEDS Working Paper No. 2021-63, Available at SSRN: https://ssrn.com/abstract=3945259 or http://dx.doi.org/10.17016/FEDS.2021.063
- Ait-Sahalia, Yacine and Matthys, Felix, Robust Consumption and Portfolio Policies When Asset Prices Can Jump (September 24, 2018). Journal of Economic Theory, 2019, 179, 1-56., Available at SSRN: https://ssrn.com/abstract=2976562 or http://dx.doi.org/10.2139/ssrn.2976562
- Leippold, Markus, Value-at-Risk and Other Risk Measures (March 16, 2015). Available at SSRN: https://ssrn.com/abstract=2579256 or http://dx.doi.org/10.2139/ssrn.2579256
- Leippold, Markus, Don't Rely on VAR. Euromoney, November 2004, Available at SSRN: https://ssrn.com/abstract=981134

---

## 📌 Notes

- First run of `--full` mode will download the GPT‑Neo 1.3B weights (~5 GB).
- Retrieval quality depends on the clarity of your question and the quality of your PDF text extraction.
- For deployment, you can run locally, in Docker, or adapt to a web UI (e.g., Streamlit).


