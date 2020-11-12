---
title: Detection of Bias and Microaggressions in Text

description: |
  We are approaching gender bias detection as an unsupervised task, aiming to identify systemic differences in comments addressed towards men and women without relying on explicit annotations.

people:
  - anjalie

layout: project
last-updated: 2020-01-08
status: active
---

While bias in language has become a prominent social issue, "bias" remains a difficult concept to define and identify, especially for untrained crowd-workers. Unlike prior work in NLP, which relies on crowd-sourced annotations to identify bias, we approach gender bias detection as an unsupervised task, aiming to identify systemic differences in comments addressed towards men and women without relying on explicit annotations. Our primary methodology involves controlling for confounds, features that may be correlated with gender, but are not indicative of bias. To achieve this, we draw frameworks and matching methodology from causality literature, as well as reduce the influence of confounds through an adversarial training objective. Our model is able to surface comments likely to contain bias, even in out-of-domain data.