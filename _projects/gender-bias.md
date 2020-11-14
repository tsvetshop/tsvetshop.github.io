---
title: Detection of Discrimination, Bias and Microaggressions in Text

description: |
  We are approaching gender bias detection as an unsupervised task, aiming to identify systemic differences in comments addressed towards men and women without relying on explicit annotations.

people:
  - anjalie
  - han
  - chan

paper:
  - title: "Unsupervised Discovery of Implicit Gender Bias"
    url: https://www.aclweb.org/anthology/2020.emnlp-main.44/
  - title: "Fortifying Toxic Speech Detectors Against Veiled Toxicity"
    url: https://www.aclweb.org/anthology/2020.emnlp-main.622/
  - title: "Multilingual Contextual Affective Analysis of LGBT People Portrayals in Wikipedia"
    url: https://arxiv.org/abs/2010.10820
  - title: "A framework for the computational linguistic analysis of dehumanization"
    url: https://www.frontiersin.org/articles/10.3389/frai.2020.00055/full
  - title: "Demoting Racial Bias in Hate Speech Detection"
    url: https://www.aclweb.org/anthology/2020.socialnlp-1.2/
  - title: "Stress and Burnout in Open Source: Toward Finding, Understanding, and Mitigating Unhealthy Interactions"
    url: https://dl.acm.org/doi/10.1145/3377816.3381732
  - title: "Finding Microaggressions in the Wild: A Case for Locating Elusive Phenomena in Social Media Posts"
    url: https://www.aclweb.org/anthology/D19-1176/
  - title: "Contextual Affective Analysis: A Case Study of People Portrayals in Online #MeToo Stories"
    url: https://ojs.aaai.org//index.php/ICWSM/article/view/3358
  - title: "RtGender: A Corpus for Studying Differential Responses to Gender"
    url: https://www.aclweb.org/anthology/L18-1445/

code:
  - https://github.com/xhan77/veiled-toxicity-detection
  - https://nlp.stanford.edu/robvoigt/rtgender/
layout: project
image: /img/project/bias.jpg
last-updated: 2020-11-12
status: active
---

While bias in language has become a prominent social issue, "bias" remains a difficult concept to define and identify, especially for untrained crowd-workers. Unlike prior work in NLP, which relies on crowd-sourced annotations to identify bias, we approach gender bias detection as an unsupervised task, aiming to identify systemic differences in comments addressed towards men and women without relying on explicit annotations. Our primary methodology involves controlling for confounds, features that may be correlated with gender, but are not indicative of bias. To achieve this, we draw frameworks and matching methodology from causality literature, as well as reduce the influence of confounds through an adversarial training objective. Our model is able to surface comments likely to contain bias, even in out-of-domain data.

<br/>
<center>
    <img src="/img/project/veiled-toxicity.png"  width="61.8%" alt="A Framework for Detecting Veiled Toxicity">
</center>
<br/>

Modern toxic speech detectors are incompetent in recognizing disguised offensive language, such as adversarial attacks that deliberately avoid known toxic lexicons, or manifestations of implicit bias. Building a large annotated dataset for such veiled toxicity can be very expensive. In this work, we propose a framework aimed at fortifying existing toxic speech detectors without a large labeled corpus of veiled toxicity. Just a handful of probing examples are used to surface orders of magnitude more disguised offenses. We augment the toxic speech detector's training data with these discovered offensive examples, thereby making it more robust to veiled toxicity while preserving its utility in detecting overt toxicity.
