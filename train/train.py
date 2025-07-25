# training script to load and train gpt-2 on jokes dataset through google colab


# code block 1 (start)

# importing dependencies
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import Dataset
import torch
import json

# code block 1 (end)


# code block 2 (start)

# uploading dataset (jokes.json)
from google.colab import files
uploaded = files.upload()

# code block 2 (end)


# code black 3 (start)

# loading dataset
with open("jokes.json") as f: # change depending on version
    data = json.load(f)

# combine caption and joke into a single string which helps GPT learn context and punchline
for item in data:
    item["text"] = f"{item['caption']}\n{item['joke']}"

# wrapping data into HuggingFaces dataset
dataset = Dataset.from_list(data).train_test_split(test_size=0.1)

# code block 3 (end)


#code block 4 (start)

# loading gpt2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token  # gpt2 doesn't have a pad token by default

def tokenize_function(example):
    encodings = tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=128 # 128 tokens is large enough for short jokes and reduces memory usage in training
    )
    encodings["labels"] = encodings["input_ids"].copy()
    return encodings

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# code block 4 (end)


# code block 5 (start)

model = GPT2LMHeadModel.from_pretrained("gpt2")
model.resize_token_embeddings(len(tokenizer))  # in case padding token was added

training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=5e-5,
    weight_decay=0.01, # a regulation technique that prevents overfitting by penalizing large weights in the model (0.01 is a common default for most NLP tasks)
    per_device_train_batch_size=4, # 4 items processed at a time with Colab's limited GPU memory usage
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    save_strategy="epoch",
    logging_steps=10,
    push_to_hub=False,
)

# code block 5 (end)


# code block 6 (start)

# data collator for language modeling
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False  # causal language modeling, we set this to False (predicts next token rather than fill in missing words)
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    data_collator=data_collator,
    tokenizer=tokenizer
)

# code block 6 (end)


# code block 7 (start)

trainer.train()

# code block 7 (end)


# code block 8 (start)

model.save_pretrained("joke_model")
tokenizer.save_pretrained("joke_model")

# code block 8 (end)