from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """ 

The greatest burritos I have ever had. They are very filling. Kind of hard to hear over the counter and you have to be loud for the workers to hear what you want on your food. Only outside seats as of 2023.
My roommate introduced me to this place and omg amazing. Food is so good service ok and ambience ok.
I love the chicken burrito I get the regular size I like it with the beans I love how you can select all your own toppings personally add barbecue sauce to my chicken burrito and it's insanely good. service is always 5 star places always totally clean. everybody that works there is great park lot can be tricky but it's iv.
Food is always bomb. I got the chicken nachos they were $16 so that was pretty steep. When I was in college here the nachos were bigger and cheaper but now they are smaller and more expensive. But it hits every time. Make sure to get the fried onions. I came on a Monday and service was super quick, nobody was in line (ucsb on spring break). Will be back once my wallet heals from the price lol

"""

print("5 STARS: ")
print(summarizer(ARTICLE, max_length=75, min_length=50, do_sample=False))

ARTICLE = """ 

Food wasn't very good. $20 for a burrito is not worth it. The location was crowded with people. There is no seating. Employees were not wearing gloves. 1st and last visit.
Stay away, they advertise a .49 delivery fee and add 6.00 for other fees.
Too expensive. $20 for a boring burrito. Better off going to chipotle or making it at home
We need a chipotle, this is not the move whatsoever. I cannot be spending $18 on nachos in this economy. Also the chicken is bland and that's coming from me. Tastes like nutrition cubes. Do not get the chicken.


"""

print("1 STARS: ")
print(summarizer(ARTICLE, max_length=75, min_length=50, do_sample=True))


#TESTS COMMIT