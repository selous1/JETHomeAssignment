# JET Coding Assessment <img src="https://d21buns5ku92am.cloudfront.net/69466/images/397955-JET-Logo-Orange-Primary-Hor-RGB-bc348f-large-1627476396.png" alt="JET Logo" width="250" height="42" align="right">

This project is a command-line application that retrieves information about restaurants partnered with [Just Eat Takeaway](https://www.justeattakeaway.com/) within a given UK postcode. It uses [Just Eat Takeaway's API](https://uk.api.just-eat.io/docs) to fetch data such as restaurant name, cuisines, rating, and address, and then displays this information in a table.

Both the number of restaurants to retrieve and postcode can be customized as needed using command-line arguments for better extensibility. Additionally, the cuisines are sorted alphabetically for easier readability.

## Table of Contents

- [General Info](#general-info)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Examples](#examples)
    - [Example 1](#example-1)
    - [Example 2](#example-2)
- [Running Tests](#running-tests)
- [Future Improvements](#future-improvements)
- [Author](#author)

## General Info

- The [API](https://uk.api.just-eat.io/docs)'s responses are assumed to be correct and valid. 
- The program will still function correctly even if the arguments (`limit` and `postcode`) are incorrect or invalid.
- A limit of 0 will be considered invalid, as there must be a positive number of restaurants to retrieve.
- A nonexistent postcode is defined as a postcode for which the API returns 0 restaurants.
- Exceptions are handled in a general manner to ensure overall error handling.

## Requirements

- `Python 3.10+`

**_NOTE:_** The subsequent setup commands and usage instructions are specific to `Linux`, as the application has been tested on Linux only. While it may work on other platforms, compatibility cannot be guaranteed.


## Setup 

To set up the application, follow these steps:

1. Clone the repository to your local machine and switch to its directory:

    ```
    git clone https://github.com/selous1/JETHomeAssignment.git
    cd JETHomeAssignment
    ```

2. Set up a virtual environment and install the required dependencies:
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install -r requirements.txt
    ```

3. Deactivate the virtual environment when finished:
    ```
    deactivate
    ```

## Usage

To run the application, follow these steps:

1. Activate the virtual environment:
    ```
    source .venv/bin/activate
    ```

2. Run the main script from the root folder:
    ```
    python3 main.py
    ```

Additionally, you can customize the number of restaurants to retrieve and the postcode using command-line arguments as such:
- `-l <limit>` or `--limit <limit>:` specify the number of restaurants to retrieve. Default: `10`
- `-p <postcode>` or `--postcode <postcode>:` specify the postcode for restaurant search. Default: `EC4M7RF`
- `-h` or `--help`: display the help message with information about available command-line options.

## Examples

Below are some examples of how to use the application. To run them (and a few others), simply use the command:

```
python3 scripts/run_examples.py
```

#### Example 1

##### Command:
```
python3 main.py
```

##### What it does:
This command will retrieve information of `10` restaurants with the `EC4M7RF` UK postcode.

##### Output:

Data from 10 restaurants from postcode EC4M7RF in London

| N  | Name                                       | Cuisines                                                          | Rating | Address                                                 |
|----|--------------------------------------------|-------------------------------------------------------------------|--------|---------------------------------------------------------|
| 1  | Tops Pizza                                 | Deals, Freebies, Italian, Pizza                                   | 4.4    | Ground Floor 22 Penton Street, N1 9PS                   |
| 2  | Thunderbird Fried Chicken – Charing Cross | Burgers, Chicken, Collect stamps, Deals, Halal, Low Delivery Fee | 4.3    | 29 Villiers Street, WC2N 6ND                            |
| 3  | Choppaluna - Bloomsbury                   | Collect stamps, Deals, Healthy, Low Delivery Fee, Salads          | 4.5    | Marchmont Street 87-89 Marchmont Street, WC1N 1AL       |
| 4  | Chicken Shop - Upper Street               | Burgers, Chicken, Collect stamps, Deals, Halal, Low Delivery Fee | 3.9    | 62 Upper Street, N1 0NY                                 |
| 5  | The Real Greek - Bankside                 | Collect stamps, Deals, Greek, Low Delivery Fee, Mediterranean    | 3.8    | Unit 1 & 2 Riverside House, 2A Southwark Bridge Rd, SE1 9HA |
| 6  | SUBWAY                                     | Low Delivery Fee, Lunch, Sandwiches                               | 2.6    | Bride Street, 107-111 Fleet Street, EC4M 7LD             |
| 7  | JOE & THE JUICE - High Holborn            | Breakfast, Deals, Low Delivery Fee, Sandwiches                    | 4.2    | 335 High Holborn, WC1V 7PX                              |
| 8  | MEATliquor - Shoreditch                   | Burgers, Chicken, Collect stamps, Deals, Low Delivery Fee         | 3.6    | 15 Hoxton Market, N1 6HG                                |
| 9  | Franco Manca - St Paul's                  | Deals, Freebies, Italian, Low Delivery Fee, Pizza                 | 3.6    | 2 St Pauls Churchyard, EC4M 8AP                         |
| 10 | Frozen River                               | Bubble Tea, Chinese, Collect stamps, Deals, Low Delivery Fee      | 4.2    | 29 Lower Marsh, SE1 7RG                                 |


#### Example 2

##### Command:
```
python3 main.py --limit 2 --postcode SW1A1AA
```

##### What it does:
This command will retrieve information of `2` restaurants with the `SW1A1AA` UK postcode.

##### Output:

Data from 2 restaurants from postcode SW1A1AA in London

| N  | Name                | Cuisines                                                          | Rating | Address                                            |
|----|---------------------|-------------------------------------------------------------------|--------|----------------------------------------------------|
| 1  | The Burger Express  | American, Burgers, Collect stamps, Deals, Freebies, Low Delivery Fee | 4.8    | Kitchen 10, 76 Stewart's Road, Nine Elms, SW8 4DE  |
| 2  | Forno Pizza         | Deals, Italian, Low Delivery Fee, Pizza                           | 4.0    | 145-147 Lambeth Walk, SE11 6EE                      |


## Running Tests

To run the unit tests for this project, use the following command:

```
python3 scripts/run_tests.py
```

Alternatively, if you want to run a test class individually, you can do so by running the command:

```
python3 tests/test_<method_name>.py
```


## Future Improvements

- Improve code comments and documentation (sphinx, doxygen, etc.).    
- Implement sorting functionality (names, addresses, ratings, etc) for improved user experience and ease of use.
- Create a possible differentiation between cuisines (e.g., Pizza, Burgers) and tags (e.g., Low Delivery Fee, Deals).
- Simplify postcode insertion process for users.
- Develop a user-friendly web interface to help with the aforementioned points.
- Test the application in other platforms.
- Enhance code coverage and mocking.
- Standardize messaging and exception handling.

## Author
[Diogo Ferreira](https://github.com/selous1)
