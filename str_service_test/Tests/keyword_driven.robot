*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
...
...               Creating new tests or editing existing is easy even for
...               people without programming skills.
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.

Resource          ../Resources/connection.robot
Library           ../Libraries/ServerLib.py    ${HOST}    ${PORT}
Library           ../Libraries/ClientLib.py    ${HOST}    ${PORT}

Test Timeout      5

# done for every test
Test Setup        Receive one
# Test Teardown


*** Variables ***



*** Test Cases ***
Reverse a sentence
    [documentation]    This test reverse a sentence
    [tags]    reverse
    Reverse    Hello world
    Result should be    dlrow olleH
    Function called should be    reverse

Lower case a sentence
    [documentation]    This test convert a sentence to lower case
    [tags]    lower
    Lower    HELLO WORLD
    Result should be    hello world
    Function called should be    lower

Capital letter a sentence
    [documentation]    This test capitalize a sentence
    [tags]    upper
    Upper    Hello world
    Result should be    HELLO WORLD
    Function called should be    upper

Multiply a sentence
    [documentation]    This test multiply a sentence
    [tags]    multiply
    Multiply    Hello world    3
    Result should be    Hello worldHello worldHello world
    Function called should be    multiply

