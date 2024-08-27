
"""
Scenario: BNK Cafe
For every 1 cup of green tea, a customer will get a coaster with a random image of a BNK member.
Since BNK has 48 members, how many cups on average can the company expect to sell to an individual
supporter who aims to collect all coasters with all BNK photos?
"""
def coupon_collector(n):
  """
  Calculate the expected number of draws needed to collect all unique items
  (in this case, coasters with images of BNK members).

  Parameters:
  n (int): The total number of unique coasters to collect (e.g., 48).
  If it isn't an int, the function will catch the error and provide a message.

  Returns:
  int: The expected number of cups a customer needs to buy.
  """

  if not isinstance(n,int):
    raise ValueError("The number of coasters (n) must be an integer.")

  sum_of_Hn = 0
  for i in range (1,n+1):
    sum_of_Hn += 1/i
  En = round(n * sum_of_Hn,0)

  print(f"On average, a customer would need to buy about {En} cups of green tea to collect all 48 coasters.")

# Test the function with 48 of BNK members
coupon_collector(48)
