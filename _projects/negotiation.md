---
title: Negotiation Dialog in Bargaining Scenarios

description: |
  We study a non-collaborative dialog setting, where a seller negotiates with a buyer over a given product. Specifically, we 1) design a dynamic coach that recommends tactics in real time to the  seller  to  get  a  better  deal, and 2) propose to model tactic history with an FST for better dialog planning and generation.

people:
  - yiheng

layout: project
image: /img/project/negotiation.jpg
last-updated: 2019-09-28
status: active
---
<br> <img src="/img/project/negotiation2.png" alt="negotiation_model" style="display: block;margin-left: auto;margin-right: auto;width: 50%;"><br>

Negotiation  is  a  complex  activity  involving strategic  reasoning,  persuasion,  and  psychology. Our first goal is to assist humans to become better negotiators through a machine-in-the-loop  approach  that  combines machine’s  advantage  at  data-driven  decision-making and human’s language generation ability.  We consider a bargaining scenario where a seller and a buyer negotiate the price of an item for sale through a text-based dialog.  Our negotiation coach recommends tactics in real time to the  seller  to  get  a  better  deal.  Evaluation on human–human dialogs shows that our coach increases the profits of the seller by almost 60%.


Our second goal is to build an automated negotiating system that attempts to sell products. However, due to its non-collaborative nature, it is not effective to model dialog history with a traditional RNN. Therefore, we propose to explicitly model both tactic and semantic history with a finite state transducer (FST). Experimental result shows that FST can model tactic history better than a RNN in non-collaborative settings and modeling both semantic and tactic history achieves the best result.
