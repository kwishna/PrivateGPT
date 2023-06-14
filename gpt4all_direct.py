import gpt4all
from gpt4all import GPT4All

gptj = gpt4all.GPT4All(
    model_name='ggml-gpt4all-j-v1.3-groovy',
    model_path="models")

# Download The Model Place In The Given Folder.
# If the path not given, it will be downloaded to default directory ~/.cache/gpt4all/..
# It may consume a couple of GB of space.
# model list https://gpt4all.io/models/models.json
# GPT4All.download_model(model_filename=, model_path=)
# GPT4All.list_models();

messages = [{"role": "user", "content": "Name 3 colors"}]
gptj.chat_completion(messages)
