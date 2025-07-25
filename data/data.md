# Custom Dataset
The data in the following JSON files was curated from the comment sections of TikTok posts I liked. The goal was to teach the model the style and structure of modern, short-form internet humor.

Each file contains **500 caption–joke pairs**.

## Caption
Captions describe a situation, usually the context of a TikTok post.

**Example:** `"A man smiling when asked about fighting"`

To give the model more variety, I often reused the same caption 2–5 times (or more) with different jokes. This helped the model learn multiple humorous responses to a single scenario.

## Jokes

Each joke is a funny comment I found under a TikTok post with the corresponding caption.

**Example:** `"A man smiling when asked about fighting" -> "Bro showed all 32"`

Many jokes shared common internet humor patterns, including repeated phrases like *“Bro,” “ahh dog,”* or *“POV.”* These linguistic trends were intentionally preserved to help the model learn the tone and style of Gen Z humor.

## Dataset Versions
`jokesV1.json`

This was the original dataset I created. Captions typically followed a subject–action format 

**Example:** `"A man smiling while looking at the camera"`

While training and testing the model, I noticed a few issues:

- **Overfitting:** The model often repeated irrelevant phrases like “while looking at the camera”, which didn’t add to the humor.

- **Gender mismatches:** Jokes frequently used “Bro” even when the caption referred to a woman. While this might occasionally be funny, I wanted the model to preserve basic contextual consistency.


###

`jokesV2.json`

This improved version of the dataset was designed to reduce noise and increase response quality.

Key changes:
- **Simplified captions**: I removed subjects like *“a man,” “a woman,” or “a bird”* unless they were essential to the joke. Captions now primarily describe actions.
- **Reduced overfitting**: By eliminating repetitive or non-humorous elements (e.g., *“while looking at the camera”*), I reduced the model's tendency to echo irrelevant phrases.