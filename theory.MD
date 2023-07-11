# Theory Section

1. Software Development LifeCycle

2. Arithmetic Exception

3. git push

4. The value is missing or not been assigned

5. Host the daily stand-up meetings and removing obstacles to protect their team from distractions

6. Unit testing: test cases are written to make sure blocks of code are working. This would be used for large and complex ongoing projects so a new feature could be tested as it is created. Print statements: Including print statements will show you what the output of the code would be at certain points and this can show you if the code is behaving as intended or not.

7. If a string is passed, instead of an int or float, a TypeError will be thrown. A Try Except block can be used as exception handling. For example:

def can_pay(price, cash_given):
try:
if cash_given >= price:
return True
else:
return False
except TypeError:
return "Enter a numerical value."

8. Git branching allows multiple branches to be created so team members can work on a project at the same time but independently. A branch acts as a pointer to a specific commit in the repository, therefore, allowing developers to create new features, work on bugs or make changes wihtout impacting the main branch until the changes are merged and approved to be included in the main branch.

9. List of key requirements:

- Customers should be able to browse a menu for different dishes
- Customers would order their meals and review they have selected the correct items
- Customers to pay for their items
- Customers to track their order and see how long it would take to come
- Resturant would be notified of new orders
- Resturant would have to accept, or decline, the orders
- Resturant to mark orders as complete
- Resturant would be able to view order history

Main considerations and problems:

- Security to make sure customer data (payment details, address) are encrypted and protected.
- Scalability so if the resturant gets more popular, the company can meet demand via their servers
- Having user roles: a general account or an admin account (which would be controlled by the resturant)
- User interface: Needs to be easy to use for customers and staff
- Performance: response times for user feedback would need to be quick and effecient

Components or tools to be used:

- React for front end development
- React Native to create a multi-platform (iOS and Android) mobile application
- Node.JS or Django for back end development
- Stripe for taking payment
- MySQL for hosting the database
- AWS for hosting cloud services and to be able to scale up or down
- Implementing HTTPS for encryption of user data
