import os

os.environ["OPENAI_API_KEY"] = "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"
from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader(
    "/Users/alexisneuhaus/Documents/Coding/GPTIndexFeb12/gpt_index/examples/paul_graham_essay/data2/"
).load_data()
index = GPTSimpleVectorIndex(documents)

response = index.query(
    "What would recommendations be for an SX2 with a blindspot in SP and SO as the middle?"
)
print(response)

# save to disk
index.save_to_disk("index.json")
# load from disk
index = GPTSimpleVectorIndex.load_from_disk("index.json")
