---
title: Conditional Language Generation with Continuous Outputs

description: |
  We develop a method of conditional language generation using seq2seq models which produce word embeddings instead of a softmax based distribution over the vocabulary at each step enabling much faster training while maintaining generation quality.

people:
  - sachin
  - chan
  - gayatri

layout: project
image: /img/project/conmt.png
code: 
  - https://github.com/Sachin19/seq2seq-con
  - https://github.com/chan0park/PCoNMT

paper:
  - title: "Von Mises-Fisher Loss for Training Sequence to Sequence Models with Continuous Outputs"
    url: https://arxiv.org/pdf/1812.04616
  - title: "Learning to Generate Word- and Phrase-Embeddings for Efficient Phrase-Based Neural Machine Translation"
    url: https://www.aclweb.org/anthology/D19-5626.pdf
  - title: "A Margin-based Loss with Synthetic Negative Samples for Continuous-output Machine Translation"
    url: https://www.aclweb.org/anthology/D19-5621.pdf

last-updated: 2019-11-01
---

The Softmax function is used in the final layer of nearly all existing sequence-to-sequence models for language generation. However, it is usually the slowest layer to compute which limits the vocabulary size to a subset of most frequent types; and it has a large memory footprint. We propose a general technique for replacing the softmax layer with a continuous embedding layer. Our primary innovations are a novel probabilistic loss and a training and inference procedure in which we generate a probability distribution over pre-trained word embeddings, instead of a multinomial distribution over the vocabulary obtained via softmax. We evaluate this new class of sequence-to-sequence models with continuous outputs on the task of neural machine translation. We show that our models obtain upto 2.5x speed-up in training time while performing on par with the state-of-the-art models in terms of translation quality. These models are capable of handling very large vocabularies without compromising on translation quality. They also produce more meaningful errors than in the softmax-based models, as these errors typically lie in a subspace of the vector space of the reference translations.

## Phrase-based NMT systems with continuous-output layer
Current neural machine translation (NMT) often fails in the one-to-many translation of multi-word phrases and collocations. To tackle this problem, phrase-based NMT systems have been proposed; these typically combine word-based NMT with phrase-based statistical MT systems or external phrase dictionaries. These solutions introduce a significant overhead of additional resources and computational costs. In this project, we are working on a phrase-based NMT model built upon continuous-output NMT, in which the decoder generates embeddings of words *or* phrases. 
