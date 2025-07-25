from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import time

# fine-tuned gpt2 model
model_path = "joke_modelV2"

tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

model.eval()

def generate_joke(caption, temperature, top_k, top_p, max_length):
    prompt = caption + "\n"
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    joke = generated_text[len(prompt):].strip()  # remove prompt from output
    return joke

def record_joke(caption, joke, temperature, top_k, top_p, rating):
    with open("results.txt", "a") as log_file:
        log_file.write("\n")
        log_file.write(f"Caption: {caption}\n")
        log_file.write(f"Joke: {joke}\n")
        log_file.write(f"Temp: {temperature}, Top-k: {top_k}, Top-p: {top_p}\n")
        log_file.write(f"Rating: {rating}\n")
        log_file.write("-" * 40 + "\n")


caption = "A student crying"

# generation parameters - (adjust as needed)
temperature = 0.9
top_k = 50
top_p = 0.95

# total number of tokens used in response, 1 token = 1.3 words
max_length = 24

def main():
    loop = True
    while loop:

        joke = generate_joke(caption, temperature, top_k, top_p, max_length)

        print("\n" + joke + "\n")

        rating = input("Rate the joke: 0 [Not coherent] | 1 [Not funny] | 2 [Okay] | 3 [Interesting] | 4 [Funny] : ")

        record = input("Record result? [Y/N]: ")

        if record == "y":
            record_joke(caption, joke, temperature, top_k, top_p, rating)
            time.sleep(1)
            print("Joke was saved!")

        else:
            if record != "n":
                print("Input Invalid: Failed to save result...")
                time.sleep(1)

        proceed = input("Proceed? [Y/N]: ")
        if proceed == "y":
            print("Loading next joke...")
            continue
        else:
            print("Ending session...")
            loop = False

if __name__ == "__main__":
    main()