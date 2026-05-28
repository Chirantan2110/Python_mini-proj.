"""A local cafe wants a program that suggests a snack.
If a customer asks for cookies or samosa,it confirms the order.Otherwise,it says it"s not available."""
snacks=input("enter your preffered snack:")
snack=snacks.lower()
#print(f"user said: {snack}")
if snack=="cookies" or snack=="samosa":
    print(f"Great Choice! We will serve you tea with {snack}")
else:
    print("Sorry,We only serve cookies or samosa with tea")