sentence = "what is the airspeed velocity of an unladen swallow?"

result = {word:len(word) for word in sentence.split()}

print(result)
