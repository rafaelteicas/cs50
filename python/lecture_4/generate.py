# In Python we have "modules" that are code written by other people to reuse, and we can use this code with the keyword "import" and the name of module:
import random # in this case the "random" is the module imported
# We can import a function specifically with the keyword "from". You import the function and pass to "from" to choose the module.
# from random import choice

coin = random.choice(["heads", "tails"]) # choice is a function inside this module, this way we use all module.
# coin = choice(["heads", "tails"]) # here we import only the choice function.
print(coin)