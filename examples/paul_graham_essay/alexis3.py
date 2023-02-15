import os

os.environ["OPENAI_API_KEY"] = "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"
from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader(
    "/Users/alexisneuhaus/Documents/Coding/GPTIndexFeb12/gpt_index/examples/paul_graham_essay/data3/"
).load_data()
index = GPTSimpleVectorIndex(documents)

response = index.query(
    "Please describe net profit for January and February 2023 (extrapolating February numbers to what they would be for the full month) in comparison with November and December 2022?"
)
print(response)

# save to disk
index.save_to_disk("index.json")
# load from disk
# index = GPTSimpleVectorIndex.load_from_disk("index.json")
