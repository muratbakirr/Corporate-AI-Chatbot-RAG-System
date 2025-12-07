"""
Test Local LLM + Embeddings + Caching
Run with:  python test_llm.py
"""

import time
from llm import chat_model, base_embeddings  # import your objects

# ----------------------------
# Test 1 — LLM basic response
# ----------------------------
def test_llm():
    print("\n== Test 1: LLM Response ==")
    time_start = time.time()
    reply = chat_model.invoke("Explain what a alp disicpline ski style is in one short sentence.")
    time_finish = time.time()
    print(f"Latency: {time_finish - time_start:.4f} seconds")
    print("LLM Output:", reply)


# -----------------------------------
# Test 2 — Embedding + Cache Behavior
# -----------------------------------
def test_embeddings():
    print("\n== Test 2: Embedding & Cache Timing ==")

    text = "This is a test sentence for embedding performance."

    # First run → slow (model must compute)
    t1_start = time.time()
    vec1 = base_embeddings.embed_query(text)
    t1_end = time.time()
    print(f"First embedding time:  {t1_end - t1_start:.4f} seconds")

    # Second run → FAST (should use cache)
    t2_start = time.time()
    vec2 = base_embeddings.embed_query(text)
    t2_end = time.time()
    print(f"Second embedding time: {t2_end - t2_start:.4f} seconds")
    
        # Second run → FAST (should use cache)
    t3_start = time.time()
    vec2 = base_embeddings.embed_query(text)
    t3_end = time.time()
    print(f"Third embedding time: {t3_end - t3_start:.4f} seconds")

    # Check similarity (should be same vector)
    same = vec1 == vec2
    print("Embeddings identical (cache hit):", same)


if __name__ == "__main__":
    test_llm()
    test_embeddings()