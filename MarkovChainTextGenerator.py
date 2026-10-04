# A simple generative text model using a Markov Chain
import random
from string import punctuation
from collections import defaultdict

class MarkovChain:
    def __init__(self):              #Ahhh remember to add two underscores,mistakenly added 1 and was figuring out whats te error
        self.graph=defaultdict(list)

    def _tokenize(self,text):
        return(text.translate(str.maketrans("","",punctuation+"1234567890")).replace("\n"," ").split(" "))

    def train(self,text):
        tokens=self._tokenize(text)
        for i,token in enumerate(tokens):
            if(len(tokens)-1)==i:
                break

            self.graph[token].append(tokens[i+1])      #"I": ["hope"],  "you": ["cry"] ....

    def generate(self, prompt, length=10):
        current = self._tokenize(prompt)[-1]
        output = prompt

        for i in range(length):
            options = self.graph.get(current, [])

            if not options:
                continue

            current = random.choice(options)
            output += f" {current}"

        return output

#Tested on Weekends song "Cry for me" ;)

text = """I hope you cry for me like I cry for you       
Every night for you, take it easy on me, baby
'Cause I tried with you, saw my life with you
End of time with you, now we're strangers
And I hope that you still cry for me like I cry for you
Every night for you, I've been living with this lie
Now I can't hide the truth, I can't hide the truth
Girl, I'll cry for you
Girl, I'll cry for you, ooh, yeah"""

chain = MarkovChain()

chain.train(text)

sample_prompt = "Girl I hope"

result = chain.generate(sample_prompt, length=10)

print(result)