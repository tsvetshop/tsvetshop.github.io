---
title: Contextualized Machine Translation

description: |
  We aim at improving the quality and coherence of conditional language generation by generating contextual word embeddings. Our current task is to contextualize neural machine translation. 

people:
  - chan

layout: project
image: /img/project/contextualized-mt.png
last-updated: 2019-01-11
---

We adapt [continuous-output neural machine translation](https://arxiv.org/pdf/1812.04616.pdf) models to multitask settings, and at each step we generate jointly type and token-level embeddings  (like ELMo and BERT). Through integrating contextualized token representations in continuous-output NMT, we improve the coherence of translations. 
