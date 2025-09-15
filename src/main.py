import argparse
from transformers import AutoTokenizer
from retrieval.query import search_index
from model_integration import load_model, generate_response

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast", action="store_true", help="(Kept for compatibility) Fast mode with GPT-2")
    args = parser.parse_args()

    # Solo GPT-2
    model_id = "gpt2"
    top_k = 2
    max_context_chars = 1800   # más corto para evitar acercarnos al límite
    max_new_tokens = 80        # respuesta breve para no pasarnos del 1024 total

    print(f"[1/3] Loading model: {model_id} ...")
    pipe = load_model(model_id)
    print("[1/3] Model loaded successfully ✅")

    question = input("\nEnter your question: ")

    print("[2/3] Retrieving relevant chunks from your papers...")
    hits = search_index(question, top_k=top_k)
    if not hits:
        print("No relevant chunks found. Did you run ingest.py?")
        return
    print(f"[2/3] Retrieved {len(hits)} chunks ✅")

    # Combinar y recortar contexto por caracteres (primer filtro rápido)
    context = "\n\n".join([h["text"] for h in hits])
    if len(context) > max_context_chars:
        context = context[:max_context_chars] + "\n\n[Context truncated due to model token limit]"

    # Prompt claro y corto
    prompt = (
        "You are a financial research assistant. Answer concisely using only the provided context. "
        "If the answer is not in the context, say: Not found in the provided papers.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\nAnswer:"
    )

    # Truncado por tokens para evitar overflow en GPT-2 (1024 tokens total)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model_max_len = tokenizer.model_max_length  # 1024 en GPT-2
    reserved = max_new_tokens

    prompt_ids = tokenizer.encode(prompt, add_special_tokens=False)
    if len(prompt_ids) + reserved > model_max_len:
        allowed = max(model_max_len - reserved, 0)
        prompt_ids = prompt_ids[:allowed]
        prompt = tokenizer.decode(prompt_ids, skip_special_tokens=True)
        print(f"[!] Prompt truncated to fit model's max length ({model_max_len} tokens)")

    print("[3/3] Generating answer...")
    answer = generate_response(
        pipe,
        prompt,
        max_new_tokens=max_new_tokens
    )
    print("[3/3] Answer generated ✅\n")

    print("Model output:\n", answer)

if __name__ == "__main__":
    main()
