---
title: Phrase-based Neural Machine Translation

description: |
  We aim at improving the one-to-many translation of multi-word phrases and collocations using phrase-based neural machine translation systems. 

people:
  - chan

layout: project
image: /img/project/pconmt.png
last-updated: 2019-06-21
status: active
---

Current neural machine translation (NMT) often fails in the one-to-many translation of multi-word phrases and collocations. To tackle this problem, phrase-based NMT systems have been proposed; these typically combine word-based NMT with phrase-based statistical MT systems or external phrase dictionaries. These solutions introduce a significant overhead of additional resources and computational costs. In this project, we are working on a phrase-based NMT model built upon [continuous-output NMT](https://arxiv.org/pdf/1812.04616.pdf), in which the decoder generates embeddings of words or phrases. 