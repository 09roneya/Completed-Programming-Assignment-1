"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    text = text.lower()
    count = 0
    for letter in text: 
        if letter in "aeiou":
            count += 1
    return count

# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    newlist = []
    for pair in items: 
       if len(pair) == 2: 
           newlist.append(pair)
    return newlist


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementatio
    listchanged = []
    for pair in items: 
        if len(pair) != 2: 
            listchanged.append(pair)
        else: 
                if pair[0] >= pair[1]: 
                    neworder = [ pair[1], pair[0]] 
                    listchanged.append(neworder) 
                else:
                    listchanged.append(pair)
    return listchanged

# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    dollars = first.dollars + second.dollars
    cents = first.cents + second.cents 
    while cents >= 100: 
        dollars +=1 
        cents -= 100
    return data.Price(dollars, cents)
    
# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    return width * height




# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    result = []
    for book in books: 
        if author in book.authors: 
            result.append(book)
    return result 

# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    radiussquared = (width*width) + (height*height)
    radius = ( (radiussquared) ** (1/2) ) / 2
    p = data.Point((rectangle.bottom_right.x + rectangle.top_left.x)/2 , (rectangle.top_left.y + rectangle.bottom_right.y)/2 )
    return data.Circle( p, radius)

# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    if employees == []: 
        return []
    below_average = []
    average = 0
    for person in employees:
        average+= person.pay_rate
    average = average/(len(employees))
    for person in employees: 
        if person.pay_rate < average:
            below_average.append(person.name)
    return below_average
