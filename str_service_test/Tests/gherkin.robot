*** Settings ***
Documentation     Example test case using the gherkin syntax.
...
...               This test has a workflow similar to the keyword-driven
...               examples. The difference is that the keywords use higher
...               abstraction level and their arguments are embedded into
...               the keyword names.
...
...               This kind of _gherkin_ syntax has been made popular by
...               [http://cukes.info|Cucumber]. It works well especially when
...               tests act as examples that need to be easily understood also
...               by the business people.

Resource          ../Resources/connection.robot
Library           ../Libraries/ServerLib.py    ${HOST}    ${PORT}
Library           ../Libraries/ClientLib.py    ${HOST}    ${PORT}

Test Timeout      5


*** Test Cases ***

Reverse
    [documentation]    This test reverse a sentence in fancy way
    [tags]    reverse
    Given a server listening for one request
    When a client request to reverse "Hello world!"
    Then result is "!dlrow olleH"
    And the called function is "reverse"

Multiply
    [documentation]    This test multiply a sentence in fancy way
    [tags]    multiply
    Given a server listening for one request
    When a client request to multiply "Hello world!" by 3
    Then result is "Hello world!Hello world!Hello world!"
    And the called function is "multiply"


*** Keywords ***
A server listening for one request
    Receive one

A client request to reverse "${sentence}"
    Reverse    ${sentence}

A client request to multiply "${sentence}" by ${n}
    Multiply    ${sentence}    ${n}

Result is "${result}"
    Result should be    ${result}

the called function is "${function}"
    function called should be    ${function}

