import os

os.environ["OPENAI_API_KEY"] = "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"
from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# load from disk
index = GPTSimpleVectorIndex.load_from_disk(
    "/Users/alexisneuhaus/Documents/Coding/GPTIndexFeb12/gpt_index/examples/paul_graham_essay/data/index.json"
)

response = index.query(
    "Please describe trends between Master Kim individual sessions from 2022 to 2023?"
)
print(response)