# Study on Risk and Randomness

A comprehensive examination of the interplay between risk and randomness in various domains. This study aims to explore the nature of uncertainty, the influence of random events on outcomes, and the strategies for managing risk in different contexts. Through research and analysis, this study investigates the fundamental principles underlying risk and randomness, their impact on decision-making processes, and the implications for individuals. By shedding light on these crucial aspects, the study provides valuable insights into understanding, assessing, and navigating uncertainties, enabling informed decision-making and risk mitigation strategies.

## Our scenario

Lets imagine we have a world where prices are completely random in a market, and that these prices flauctuate between -200 and 200, or x1 and x2. 

Things to Notice in this scenario:

-There is no trading psicology, and this means that, past prices do not influence in any way future prices.

-From one day to another, prices move randomly between -200 and 200.

![Image Alt Text](images/transferir (1).png)


## Our Agent

Our agent can only choose its stoploss, and take profit for the position.

Things to Notice in our agent:

- Agents actions do not have an influence in the price for that day or following days.

- the agent can only buy, and that means that if the price goes up, he earns money when it hits the take profit.

- the agent can only buy, and that means that if the price goes down, he looses money when it hits the stoploss.  
