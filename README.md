This is a modular, interactive command-line Railway Ticket Booking System built in Python.
The system allows users to:
1. Select routes
2. Enter passenger details
3. Calculate fares using a 6-step pricing logic
4. Apply promo codes
5. View booking summaries
6. Store and view booking history

Features:
* Fully interactive CLI system
* Strict modular architecture
* 6-step fare calculation logic
* Promo code support (ADG20, WINTER500)
* Error handling and input validation
* Fare breakdown (step-wise contribution)
* Baggage alerts
* Travel time calculation
* Booking ID generation
* Passenger summary
* Booking history storage (file-based)

How to Run
1. Make sure Python 3 is installed
2. Navigate to project folder:
3. Run the program:

Fare Calculation:
1. Slab-based distance fare
2. Senior citizen discount (>60 years → 40% off)
3. Train type multiplier
4. Travel class multiplier
5. Excess baggage fee
6. Flat surcharge

PromoCode:
| Code      | Discount |
| --------- | -------- |
| ADG20     | 20% off  |
| WINTER500 | ₹500 off |

Error handling
* Invalid numeric inputs
* Incorrect menu selections
* Invalid routes
* Negative or zero values


