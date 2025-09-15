from transformers import pipeline

def load_model(model_id=None):
    """
    Loads a text generation model.
    If model_id is None, defaults to gpt2 (fast mode).
    """
    if model_id is None:
        model_id = "gpt2"  # Default fast mode

    print(f"Loading model: {model_id}...")
    pipe = pipeline(
        "text-generation",
        model=model_id,
        device_map="auto",   # Uses GPU if available
        torch_dtype="auto"   # Auto-detects best precision
    )
    return pipe

def generate_response(pipe, prompt, max_new_tokens=256):
    """
    Generates a response from the given pipeline and prompt.
    max_new_tokens can be adjusted for speed/length trade-offs.
    """
    output = pipe(prompt, max_new_tokens=max_new_tokens)
    return output[0]["generated_text"]
