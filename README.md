# William
A GPT chatbot with [Charles III. William](https://en.wikipedia.org/wiki/Charles_III_William,_Margrave_of_Baden-Durlach)'s persona.

## AI Dev Plan
The goal of this project is to create a chatbot that impersonates Charles III. William, historic margrave of Baden-Durlach and founder of Karlsruhe. The bot is expected to speak from Charles' perspective, giving factually accurate responses to user questions.

Example dialog
```
User: Hi, how are you?
Bot:  Good, how are you?
User: Where are you from?
Bot:  I am from Germany, I was born there in 1679.
User: What do you do on your weekends?
Bot:  I'm currently busy building the city of Karlsruhe.
User: ...
```

## Related Work
There is currently a lot of ongoing work in the domain of NLP and open-domain chatbots. A recent example of a method that combines many relevant skills like information retrieval, empathy, and persona is FAIR's BlenderBot.

Experiments conducted during hackathon x vol. 2 using GPT showed that the bot had difficulties to stay true to the persona and to correctly remember dates. Also, the persona information was only a few sentences long and specifically written in first person, making it easier for the network to copy parts of it. A chatbot based on actual information retrieval would have to identify which sentences of a text contain information about the character it is supposed to impersonate.

As an additional challenge, it would be nice if the bot was able to exchange in different languages.
