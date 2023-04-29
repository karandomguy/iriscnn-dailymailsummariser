# IRIS - CNN/DailyMail Summariser
Extractive and abstractive summarisation of CNN/Daily Mail Dataset

## Description
This summarisation task is subdivided into two parts
- Exatractive Summarization
- Abstractive Summarization  

I have used https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail dataset instead of the mentioned https://github.com/abisee/cnn-dailymail dataset for this task and then tested out the results over the rogue metric  
- For the extractive summarisation I've used the *huggingface pipeline api* and iterated through the text in chunks.  
- For the abstractive summarisation part I used PyTorch and T5 transformer and Autotokenizer and LMHead model

