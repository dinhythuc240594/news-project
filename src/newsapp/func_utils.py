import random
import string

#function

def createIdArticle(id_string='article', length=10):
  return id_string + '_' + ''.join(random.sample(string.ascii_lowercase, length))
