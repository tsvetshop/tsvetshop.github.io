---
title: Strategic Non-collaborative Dialog Agents

description: |
  We study a non-collaborative dialog setting, where a seller negotiates with a buyer over a given product. Specifically, we 1) design a dynamic coach that recommends tactics in real time to the  seller  to  get  a  better  deal, 2) propose to model tactic history with an FST for better dialog planning and generation, and 3) propose a novel framework to model negotiations strategies and their dependencies as graph structures, via GNNs.

people:
  - yiheng
  - rishabh
  - vidhisha

layout: project
image: /img/project/negotiation.jpg
code: https://github.com/rishabhjoshi/DialoGraph_ICLR21 ; https://github.com/zhouyiheng11/Negotiation-Coach
paper:
  - joshi2021dialograph
  - zhou2020augmenting
  - zhou2019dynamic
last-updated: 2021-05-29
status: active
---

Negotiation  is  a  complex  activity  involving strategic  reasoning,  persuasion,  and  psychology. Our first goal is to assist humans to become better negotiators through a machine-in-the-loop  approach  that  combines machine’s  advantage  at  data-driven  decision-making and human’s language generation ability.  We consider a bargaining scenario where a seller and a buyer negotiate the price of an item for sale through a text-based dialog.  Our negotiation coach recommends tactics in real time to the  seller  to  get  a  better  deal.  Evaluation on human–human dialogs shows that our coach increases the profits of the seller by almost 60%.


<br> <img src="/img/project/negotiation2.png" alt="negotiation_model" class="project-img"><br>

Our second goal is to build an automated negotiating system that attempts to sell products. However, due to its non-collaborative nature, it is not effective to model dialog history with a traditional RNN. Therefore, we propose to explicitly model both tactic and semantic history with a finite state transducer (FST). Experimental result shows that FST can model tactic history better than a RNN in non-collaborative settings and modeling both semantic and tactic history achieves the best result.

<h1> DialoGraph: Incorporating Interpretable Strategy-Graph Networks into Negotiation Dialogues </h1>

Pragmatic planning of negotiation strategies is essential to successfully negotiate a deal. Modern systems generate fluent sentences but lack pragmatic ground and can't reason strategically. Our system incorporates pragmatic strategies explicitly using graphs. Also, it gives interpretable prediction of future optimal strategies. We incorporate the learned graphs into an end-to-end negotiation dialogue system and demonstrate that it consistently improves future-strategy prediction and downstream dialogue generation, leading to better negotiation deals (sale prices). We also demonstrate how to interpret intermediate structures and learned sequences of strategies, opening-up the black-box of end-to-end strategic dialogue systems. 

<br> <img src="/img/project/dialograph.png" alt="dialograph" class="project-img"><br>

Utterances are encoded using BERT and passed to the Dialogue Context Encoder. It is enriched with explicit strategy and dialogue act sequence encodings from the Structure Encoders. The structure encoder consists of layers of Graph Attention Networks followed by Adaptive Structure Aware Pooling which is used to learn strategy influence and association scores.

<br> <img src="/img/project/dialograph2.png" alt="strategy_sequence_graph" class="project-img"><br>
