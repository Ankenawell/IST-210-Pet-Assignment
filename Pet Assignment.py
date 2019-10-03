#!/usr/bin/env python
# coding: utf-8

# ## ER Diagram Explanation:
# 
#   In a local pet shop, the manager is implementing a database and is asking for help with the structure of the data.  To begin, We will have all connections leading back to the customer.  This is because all data must be related to one customer when he or she makes a purchase.  Both Fish and Pets are connected to the customer because this is who will be owning the animals after they are purchased.  These connections are one-to-many because one person can purchase many animals, but multiple people cannot own a single pet.  There is also a separate report for when the customer actually makes the purchase.  This is necessary to store because it contains vital information where transactions can be tracked.  With this information, it is possible to see how much money is flowing into and out of the store.  Both the food expense report and the pet expense report are one-to-one because one customer is able to create one expense report at a time. 
# 
#   Additionally, the customer is able to register for a loyalty program.  This contains specific information about transactions a customer has made in order to allow a discount to be added after a certain number of transactions.  It's connectivity to the customer is one-to-one.  One customer can only have one loyalty program, and vice-versa.  There is a foreign key for the customer, "Loyalty Points," which stores the possible discount on any given transaction.  This is foreign because not every customer will have a value for this attribute.
#   
#   Overall, we believe that this entity relation diagram will provide a strong foundation for constructing a database for a local pet shop.

# ## ER Diagram:
# 
# ![Lab%202.png](attachment:Lab%202.png)
