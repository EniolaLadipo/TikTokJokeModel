## `funny.py`

This script is used to generate joke responses from the fine-tuned GPT-2 model based on a given caption (prompt). It allows you to control generation parameters such as:

- `temperature`
- `top-k`
- `top-p`
- `max_length` (token limit)

The script runs an interactive loop where each generated joke can be:
- Rated manually (0–4)
- Optionally saved to `results.txt` using the `record_joke()` function

---

### Token Length Considerations

The `max_length` parameter controls how many tokens the model can generate. Keep in mind:

- If too **short**, jokes may get cut off or be incomplete.
- If too **long**, the model may continue beyond the punchline or start a second joke, reducing clarity or coherence.

A reasonable range (e.g., 15-25 tokens) works well for short jokes.

---

### Output

When recording is enabled, each joke is saved in `results.txt` with:
- The prompt (`caption`)
- The joke
- The generation parameters
- The manual rating (0–4)
- A line separator
