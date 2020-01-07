---
title: Model Interpretability via Influence Functions

description: |
  We investigate two interpretation methods in NLP that either highlight salient input words or identify influential training examples. We show when and how the latter one might provide more valuable insights.

people:
  - han

layout: project
image: /img/project/interpretability.png
code: https://github.com/xhan77/influence-analysis
last-updated: 2020-01-06
status: active
---
Modern deep learning models for NLP are notoriously opaque. This has motivated the development of methods for interpreting such models, e.g., via gradient-based saliency maps or the visualization of attention weights. Such approaches aim to provide explanations for a particular model prediction by highlighting important words in the corresponding input text. While this might be useful for tasks where decisions are explicitly influenced by individual tokens in the input, we suspect that such highlighting is not suitable for tasks where model decisions should be driven by more complex reasoning. In this project, we investigate the use of influence functions for NLP, providing an alternative approach to interpreting neural text classifiers.

Influence functions explain the decisions of a model by identifying influential training examples. Despite the promise of this approach, influence functions have not yet been extensively evaluated in the context of NLP, a gap addressed by this work. We conduct a comparison between influence functions and common word-saliency methods on representative tasks. As suspected, we find that influence functions are particularly useful for natural language inference, a task in which saliency maps may not have clear interpretation. Furthermore, we develop a new quantitative measure based on influence functions that can reveal artifacts in training data.
