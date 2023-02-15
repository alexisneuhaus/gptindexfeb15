import os

os.environ["OPENAI_API_KEY"] = "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"
from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# load from disk
index = GPTSimpleVectorIndex.load_from_disk(
    "/Users/alexisneuhaus/Documents/Coding/GPTIndexFeb12/gpt_index/examples/paul_graham_essay/data2/index.json"
)

# response = index.query(
#    "What would recommendations be for an Enneagram 2 who took an instinctual subtypes test and got the following scores out of 60: Self-Preservation: 35, Sexual: 53, Social: 47"
#)
#print(response)
