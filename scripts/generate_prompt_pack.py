"""
Simple script to create a sample AI prompt pack.

This script generates a text file containing a list of curated ChatGPT prompts designed to boost productivity and creativity.  In a production pipeline, this would be replaced by a more sophisticated generation process that pulls topics from the optimisation loop and formats them for sale.
"""

import datetime
import os

PROMPTS = [
    "Brainstorm five unique article ideas about AI tools for productivity.",
    "Write a step‑by‑step guide on how to automate your morning routine using AI.",
    "List ten eco‑friendly habits that can be adopted in a home office.",
    "Create a social‑media script promoting an AI‑generated image pack.",
    "Generate an outline for a video on reducing plastic use with the help of smart apps.",
    "Draft a newsletter section comparing three productivity apps using AI summarisation."
]

def save_prompt_pack(output_dir: str = "../digital_products"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"prompt_pack_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("AI Prompt Pack\n")
        f.write("Generated: {}\n\n".format(datetime.datetime.now()))
        for idx, prompt in enumerate(PROMPTS, start=1):
            f.write(f"{idx}. {prompt}\n")
    return filepath

if __name__ == "__main__":
    path = save_prompt_pack()
    print(f"Prompt pack saved to {path}")
