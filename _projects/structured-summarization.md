---
title: Structured Summarization

description: |
  Incorporate document structure into neural document representation models. Develop models to learn document structures that help in better document understanding. Analyze if the learned latent structures generalizable and useful as general document structures?

people:
  - vidhisha
  - artidoro
  - sachin
  - rishabh

paper:
  - balachandran2020structsum
  - dou2020deep
layout: project
image: /img/project/summarization.png
last-updated: 2020-01-06
status: active
---
**High-Level Approach**: We propose a structure-aware end-to-end model for summarization. Our proposed model augments the existing [pointer-generator network](https://www.aclweb.org/anthology/P17-1099/) with two novel components: (1) a latent-structure (LS) attention module that adapts [structured representations](https://www.aclweb.org/anthology/Q18-1005/) for the summarization task, and (2) an explicit-structure (ES) attention module, that incorporates a coreference graph. The explicit attention module is linguistically-motivated, which aims to incorporate sentence-level structures from any externally annotated document structure. We incorporate a coreference based sentence dependency graph, which is then combined with the output of the latent structure attention module to produce a hybrid structure-aware sentence representation.

**Hierarchical Model**: We propose a hierarchical encoder-decoder model using [Latent Structured-Attention](https://www.aclweb.org/anthology/Q18-1005/) (LS) to induce latent structure and Explicit Structured (ES) Attention to incorporate explicit linguistic structure, between sentences of a document,  The encoder uses a BiLSTM to encode the words and produce contextual word representations. The word representations of all words in a sentence are pooled to produce sentence representations. The latent structured-attention mechanism is used to produce attention scores between all pairs of sentences. An attention score aij in-turn predicts the probability of a dependency edge i->j. These attention values are used to produce latent structure-aware sentence representation, where every sentence is a latent structure-attention weighted representation of its parent nodes and its child nodes.  The explicit structure module uses a fixed coreference graph where sentences are linked if they have common co-referring mentions in them. The number of unique co-referring mentions is used as the attention score between two sentences and an explicit structure-aware sentence representation is produces as the explicit attention weighted sum. The new structure-aware sentence representations are concatenated with the word representation and provided to a standard [pointer-generator decoder](https://www.aclweb.org/anthology/P17-1099/). 

**Final Model**: We finally use the structure-aware encoder and augment it with the pointer generator decoder for summarization. To analyze the latent structures learned by the model, we additionally extract the best tree representing the document using the Chu-Liu-Edmonds algorithm.

## Summarization Evaluation
While there have been significant improvement in abstractive summarization, we show that recent developments have been overlooking the faithfulness of the information presented in the summaries. We first propose a linguistically grounded and operational definition of factuality which can be used in human evaluation of summarization. We demonstrate that current evaluation metrics for summarization, like ROUGE, are not correlated with human judgement of factuality. 

We develop a general metric for the evaluation of factuality in summarization that correlates with human judgement. Unlike prior work, our metric operates on an intermediate representation of the texts obtained by creating document level semantic graphs. The calculation of the distance between two graphs draws from the literature on embedded graphs. We evaluate our methodology with several state-of-the-art summarization models on common data sets.

## Cross-lingual Summarization