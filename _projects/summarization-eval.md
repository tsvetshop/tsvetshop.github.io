---
title: Evaluation of Summarization

description: |
  While there have been significant improvement in abstractive summarization, we show that recent developments have been overlooking the faithfulness of the information presented in the summaries. We first propose a linguistically grounded and operational definition of factuality which can be used in human evaluation of summarization. We demonstrate that current evaluation metrics for summarization, like ROUGE, are not correlated with human judgement of factuality. 

people:
  - artidoro

layout: project
last-updated: 2020-01-15
status: active
---
While there have been significant improvement in abstractive summarization, we show that recent developments have been overlooking the faithfulness of the information presented in the summaries. We first propose a linguistically grounded and operational definition of factuality which can be used in human evaluation of summarization. We demonstrate that current evaluation metrics for summarization, like ROUGE, are not correlated with human judgement of factuality. 

We develop a general metric for the evaluation of factuality in summarization that correlates with human judgement. Unlike prior work, our metric operates on an intermediate representation of the texts obtained by creating document level semantic graphs. The calculation of the distance between two graphs draws from the literature on embedded graphs. We evaluate our methodology with several state-of-the-art summarization models on common data sets.