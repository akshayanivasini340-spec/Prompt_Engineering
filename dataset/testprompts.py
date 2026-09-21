import pandas as pd
import os

# Create dataset folder if it does not exist
os.makedirs("dataset", exist_ok=True)

# --------------------------------------------------
# 1. PROMPTS
# --------------------------------------------------

prompts = [
    {
        "technique": "Zero-Shot",
        "prompt": "Explain artificial intelligence in simple words."
    },
    {
        "technique": "One-Shot",
        "prompt": "Example: Python is a programming language.\nNow explain Java in a similar way."
    },
    {
        "technique": "Few-Shot",
        "prompt": "Example 1: Cat -> Animal\nExample 2: Rose -> Plant\nExample 3: Eagle -> Bird\nNow classify: Dolphin"
    },
    {
        "technique": "Role Prompting",
        "prompt": "Act as a computer science teacher and explain machine learning to a beginner."
    },
    {
        "technique": "Chain-of-Thought",
        "prompt": "Solve this problem step by step: If a student studies 2 hours per day for 5 days, how many hours do they study?"
    }
]

# --------------------------------------------------
# 2. GENERATE SAMPLE RESPONSES
# --------------------------------------------------

responses = []

for item in prompts:

    technique = item["technique"]
    prompt = item["prompt"]

    if technique == "Zero-Shot":
        response = (
            "Artificial intelligence is technology that allows computers "
            "to perform tasks that normally require human intelligence."
        )

    elif technique == "One-Shot":
        response = (
            "Java is a programming language used to build applications, "
            "web systems, and other software."
        )

    elif technique == "Few-Shot":
        response = "Dolphin -> Animal"

    elif technique == "Role Prompting":
        response = (
            "Machine learning is a part of artificial intelligence where "
            "computers learn patterns from data and use those patterns "
            "to make predictions or decisions."
        )

    elif technique == "Chain-of-Thought":
        response = (
            "The student studies 2 hours each day. "
            "There are 5 days. Therefore, 2 × 5 = 10 hours."
        )

    responses.append({
        "technique": technique,
        "prompt": prompt,
        "generated_response": response
    })

# --------------------------------------------------
# 3. SAVE PROMPTS
# --------------------------------------------------

prompt_df = pd.DataFrame(prompts)

prompt_df.to_csv(
    "dataset/prompts.csv",
    index=False
)

prompt_df.to_csv(
    "dataset/prompt.csv",
    index=False
)

# --------------------------------------------------
# 4. SAVE GENERATED RESPONSES
# --------------------------------------------------

response_df = pd.DataFrame(responses)

response_df.to_csv(
    "dataset/generated_responses.csv",
    index=False
)

# --------------------------------------------------
# 5. PROMPT COMPARISON
# --------------------------------------------------

comparison = []

for item in responses:
    comparison.append({
        "technique": item["technique"],
        "prompt_length": len(item["prompt"]),
        "response_length": len(item["generated_response"])
    })

comparison_df = pd.DataFrame(comparison)

comparison_df.to_csv(
    "dataset/prompt_comparison.csv",
    index=False
)

# --------------------------------------------------
# 6. EVALUATION
# --------------------------------------------------

evaluation = []

for item in responses:
    evaluation.append({
        "technique": item["technique"],
        "clarity": 5,
        "relevance": 5,
        "specificity": 4,
        "remarks": "Clear and relevant response"
    })

evaluation_df = pd.DataFrame(evaluation)

evaluation_df.to_csv(
    "dataset/evaluation_results.csv",
    index=False
)

# --------------------------------------------------
# 7. PROMPT TEMPLATES
# --------------------------------------------------

templates = [
    {
        "technique": "Zero-Shot",
        "template": "Explain [TOPIC] in simple words."
    },
    {
        "technique": "One-Shot",
        "template": "Example: [EXAMPLE]. Now explain [TOPIC] in a similar way."
    },
    {
        "technique": "Few-Shot",
        "template": "Example 1: [A]. Example 2: [B]. Example 3: [C]. Now classify [INPUT]."
    },
    {
        "technique": "Role Prompting",
        "template": "Act as a [ROLE] and explain [TOPIC] to a beginner."
    },
    {
        "technique": "Chain-of-Thought",
        "template": "Solve the following problem step by step: [PROBLEM]."
    }
]

templates_df = pd.DataFrame(templates)

templates_df.to_csv(
    "dataset/prompt_templates.csv",
    index=False
)

# --------------------------------------------------
# 8. DISPLAY RESULTS
# --------------------------------------------------

print("\n========== GENERATED RESPONSES ==========\n")

for item in responses:
    print("Technique:", item["technique"])
    print("Prompt:", item["prompt"])
    print("Response:", item["generated_response"])
    print("-" * 60)

print("\nProject completed successfully!")