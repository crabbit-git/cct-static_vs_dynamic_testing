### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # "=" in Python is assigment, not a check for equality
      return True
    else # There needs to be a colon after "else" otherwise it's broken syntax
      return False
   

  dif highest_card(self, card1 card2): # "dif" rather than "def", needs to be a comma separating "card1" and "card2" parameters
  # The indentation below this line is incorrect; it needs to be one step further in
  if card1.value > card2.value:
    return card # Which card? There has been no "card" variable defined; should be "card1"
  else:
    return card2
  '''
  The trouble with this is that it only accounts for two possibilities: either card1 has higher value than card2, or card2 does.
  What if they're the same, though? It'll just return card2, implying card2's value is higher than card1, which isn't the case.
  It should probably be an "else if" such that it only returns either card if its value exceeds that of the other.
  If the values are equal instead, then it should either return None, or some other result as desired.
  '''
  


def cards_total(self, cards):
  total # This should declare "total" as a variable and assign it the value 0 (because of what's done in the next 3 lines)
  for card in cards:
    total += card.value
    return "You have a total of" + total # The return statement needs to be outside the "for" loop to return the correct total
    '''
    The indentation on this entire function is wrong: it needs to be indented one step further in to run.
    Additionally, you can't concatenate an integer into a string without changing its type to a string or wrapping the whole thing
    in a formatted string instead.
    '''

```
