{"changed":true,"filter":false,"title":"evens.py","tooltip":"/evens.py","value":"\"\"\"\nSolution to the challenge in the `Test Before` unit found in the `Test Driven\nDevelopment with Python lesson`\nNOTE: The solution found in this file is one of the many potential solutions\nthat can be used to achieve the end result expected by the challenge in the\nlesson.\n\"\"\"\n\n\ndef even_number_of_evens(numbers):\n    \"\"\"\n    Returns the number of even numbers contained in a list of numbers.\n    `numbers` should be a list containing numbers\n    \n    Returns either True or False based on a number of criteria.\n        - if `numbers` is empty, return `False`\n        - if the number of even numbers is odd, return `False`\n        - if the number of even numbers is 0, return `False`\n        - if the number of even numbers is even, return `True`\n    \"\"\"\n\n    # Check to see if the list is empty\n    if numbers == []:\n        return False\n    else:\n        # Set a `number_of_evens` variable that will be incremented each time\n        # an even number is found\n        evens = 0\n        \n    # Iterate of over each item and if it's an even number, increment the\n    # `evens` variable\n    for number in numbers:\n        if number % 2 == 0:\n            evens += 1\n    \n    if evens == 0:\n        return False\n    else:\n        return evens % 2 == 0\n\n# Our set of test cases\nassert even_number_of_evens([]) == False, \"No numbers\"\nassert even_number_of_evens([2]) == False, \"One even number\"\nassert even_number_of_evens([2, 4]) == True, \"Two even numbers\"\nassert even_number_of_evens([2, 3]) == False, \"Two numbers, only one even\"\nassert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, \"Multiple numbers, three even\"\nassert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, \"Multiple numbers, four even\"\nassert even_number_of_evens([1, 3, 9]) == False, \"No even numbers\"\n\n# If all the test cases pass, print some successful info to the console to let\n# the developer know\nprint(\"All tests passed!\")","undoManager":{"mark":-2,"position":12,"stack":[[{"start":{"row":0,"column":0},"end":{"row":51,"column":26},"action":"insert","lines":["\"\"\"","Solution to the challenge in the `Test Before` unit found in the `Test Driven","Development with Python lesson`","NOTE: The solution found in this file is one of the many potential solutions","that can be used to achieve the end result expected by the challenge in the","lesson.","\"\"\"","","","def even_number_of_evens(numbers):","    \"\"\"","    Returns the number of even numbers contained in a list of numbers.","    `numbers` should be a list containing numbers","    ","    Returns either True or False based on a number of criteria.","        - if `numbers` is empty, return `False`","        - if the number of even numbers is odd, return `False`","        - if the number of even numbers is 0, return `False`","        - if the number of even numbers is even, return `True`","    \"\"\"","","    # Check to see if the list is empty","    if numbers == []:","        return False","    else:","        # Set a `number_of_evens` variable that will be incremented each time","        # an even number is found","        evens = 0","        ","    # Iterate of over each item and if it's an even number, increment the","    # `evens` variable","    for number in numbers:","        if number % 2 == 0:","            evens += 1","    ","    if evens == 0:","        return False","    else:","        return evens % 2 == 0","","# Our set of test cases","assert even_number_of_evens([]) == False, \"No numbers\"","assert even_number_of_evens([2]) == False, \"One even number\"","assert even_number_of_evens([2, 4]) == True, \"Two even numbers\"","assert even_number_of_evens([2, 3]) == False, \"Two numbers, only one even\"","assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, \"Multiple numbers, three even\"","assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, \"Multiple numbers, four even\"","assert even_number_of_evens([1, 3, 9]) == False, \"No even numbers\"","","# If all the test cases pass, print some successful info to the console to let","# the developer know","print(\"All tests passed!\")"],"id":1}],[{"start":{"row":42,"column":0},"end":{"row":42,"column":1},"action":"insert","lines":["#"],"id":2}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":1},"action":"insert","lines":["#"],"id":3}],[{"start":{"row":44,"column":0},"end":{"row":44,"column":1},"action":"insert","lines":["#"],"id":4}],[{"start":{"row":45,"column":0},"end":{"row":45,"column":1},"action":"insert","lines":["#"],"id":5}],[{"start":{"row":46,"column":0},"end":{"row":46,"column":1},"action":"insert","lines":["#"],"id":6}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":1},"action":"insert","lines":["#"],"id":7}],[{"start":{"row":42,"column":0},"end":{"row":42,"column":1},"action":"remove","lines":["#"],"id":8}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":1},"action":"remove","lines":["#"],"id":9}],[{"start":{"row":44,"column":0},"end":{"row":44,"column":1},"action":"remove","lines":["#"],"id":10}],[{"start":{"row":45,"column":0},"end":{"row":45,"column":1},"action":"remove","lines":["#"],"id":11}],[{"start":{"row":46,"column":0},"end":{"row":46,"column":1},"action":"remove","lines":["#"],"id":12}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":1},"action":"remove","lines":["#"],"id":13}]]},"ace":{"folds":[],"scrolltop":180,"scrollleft":0,"selection":{"start":{"row":47,"column":0},"end":{"row":47,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":20,"state":"start","mode":"ace/mode/python"}},"timestamp":1560522090674}