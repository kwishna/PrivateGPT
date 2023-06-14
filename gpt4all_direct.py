import gpt4all
gptj = gpt4all.GPT4All(
    model_name='ggml-gpt4all-j-v1.3-groovy',
    model_path="models") # Download The Model Place In The Given Folder.
messages = [{"role": "user", "content": "Name 3 colors"}]
gptj.chat_completion(messages)
