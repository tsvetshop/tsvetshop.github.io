---
title: Detection of Discrimination, Bias, and Microaggressions in Text

description: |
  We aim to detect subtle forms of bias and veiled hostility in text, including microaggressions, condescending language, and dehumanization

people:
  - anjalie
  - han
  - chan

paper:
  - field2020unsupervised
  - han2020fortifying
  - park2020multilingual
  - mendelsohn2019
  - xia2020demoting
  - raman2020stress
  - breitfeller2019finding
  - field2019contextual
  - voigt2018rtgender
code:
  - https://github.com/xhan77/veiled-toxicity-detection
  - https://nlp.stanford.edu/robvoigt/rtgender/
  - https://github.com/anjalief/unsupervised_gender_bias
layout: project
image: /img/project/bias.jpg
last-updated: 2020-11-12
status: active
---

While much work in NLP has focused on detecting toxic language like hate speech, veiled offensive language remains difficult to identify. This includes comments that deliberately avoid known toxic lexicons and manifestations of implicit bias, such as microaggressions, condescending language, and dehumanization. Our lab has developed and continues to build data sets and methods for detecting this type of veiled hostility in domains like newspaper articles and social media comments.

Voigt et al. (2018) presents our data set of 2nd-person social media comments, and Breitfeller et al. (2019) describes our methodology for collecting annotated microaggressions. Given the difficulty of collecting direct annotations for subtle and implicit biases, we have additionally worked to develop an unsupervised approach to surfacing implicit gender bias (Field and Tsvetkov, 2020). In this project, we aim to identify systemic differences in comments addressed towards men and women without relying on explicit annotations. Our primary methodology involves controlling for confounds: features that may be correlated with gender, but are not indicative of bias. To achieve this, we draw frameworks and matching methodology from causality literature, as well as reduce the influence of confounds through an adversarial training objective. Our model is able to surface comments likely to contain bias, even in out-of-domain data.

<br/>
<center>
    <img src="/img/project/veiled-toxicity.png"  width="61.8%" alt="A Framework for Detecting Veiled Toxicity">
</center>
<br/>

In Han and Tsvetkov (2020), we additionally aim to improve the ability of existing toxic speech detectors to uncover veiled toxicity without requiring large labeled corpora, which are difficult and expensive to collect. Our framework uses a handful of probing examples to surface orders of magnitude more disguised offenses. We augment a toxic speech detector’s training data with these discovered offensive examples, thereby making it more robust to veiled toxicity while preserving its utility in detecting overt toxicity.