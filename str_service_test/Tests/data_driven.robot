*** Settings ***
Documentation     Example test cases using the data-driven testing approach.
...
...               The _data-driven_ style works well when you need to repeat
...               the same workflow multiple times.
...
...               Tests use ``Calculate`` keyword created in this file, that in
...               turn uses keywords in ``CalculatorLibrary.py``. An exception
...               is the last test that has a custom _template keyword_.
...
...               Notice that one of these tests fails on purpose to show how
...               failures look like.

Resource          ../Resources/connection.robot
Library           ../Libraries/ServerLib.py    ${HOST}    ${PORT}
Library           ../Libraries/ClientLib.py    ${HOST}    ${PORT}

# this template will be use in every test if no other template is specified
Test Template     ReverseTemplate

Test Timeout      5


*** Test Cases ***      Sentence                Expected

Normal
                        honolulu                ululonoh
                        hello world             dlrow olleh

With punctuation
                        hello, how are you?     ?uoy era woh ,olleh
                        .--.?&%$                $%&?.--.

Palindrome
                        Anna                    annA
                        Hannah                  hannaH
                        Amore Roma              amoR eromA




*** Keywords ***
ReverseTemplate
    [documentation]    This test reverse a sentence and it is performed with different inputs
    [tags]    reverse
    [Arguments]    ${sentence}    ${expected}
    Receive one
    Reverse    ${sentence}
    Result should be    ${expected}
    Function called should be    reverse
