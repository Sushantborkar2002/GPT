from tokenizers import ByteLevelBPETokenizer
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling
from datasets import load_dataset
from transformers import Trainer, TrainingArguments
from colorama import Fore

path = ["python_code_text_data.txt"]
test = True
if test:
    tokenizer = ByteLevelBPETokenizer()
    tokenizer.train(files=path, vocab_size=52_000, min_frequency=2, special_tokens=
    [
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>"
    ])
    tokenizer.save_model(r'C:\Users\sushant\PycharmProjects\GPT\tokenizers')
tokenizer = GPT2Tokenizer.from_pretrained(r'C:\Users\sushant\PycharmProjects\GPT\tokenizers')
tokenizer.add_special_tokens(
    {
        "bos_token": "<s>",
        "pad_token": "<pad>",
        "eos_token": "</s>",
        "unk_token": "<unk>",
        "mask_token": "<mask>"
    })

t = tokenizer.encode("print('Hello World!')")
print(t)
print(tokenizer.decode(t))

config = GPT2Config(
    vocab_size=tokenizer.vocab_size,
    bos_token=tokenizer.bos_token_id,
    eos_token=tokenizer.eos_token_id
)
model = GPT2LMHeadModel()

dataset = load_dataset("text", data_files=["python_code_text_data.txt"])


def encode(lines):
    return tokenizer(lines['text'], add_special_tokens=True, truncation=True, max_length=1024)


dataset.set_transform(encode)
dataset = dataset['train']
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.3)

training_args = TrainingArguments(
    output_dir="GpyT",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=3,
    save_steps=100,
    save_total_limit=1,
    prediction_loss_only=True,
    remove_unused_columns=True
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset
)

trainer.train()
trainer.save_model("GpyT")
