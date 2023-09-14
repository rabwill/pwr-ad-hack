# Programming with Representation (PwR)

PwR allows you to make changes with just natural language (NL): Describe your change in simple NL and see the LLM make laser sharp edits across the entire stack. Click here for more information [aka.ms/IGotPwR](https://aka.ms/IGotPwR)

## Teams App Stack

We have described our Teams App as a project that has 2 layers:

1. Adaptive Cards UI
2. API 

(note: PwR is generic and can support any number of layers, any number of files and any number of languages)

## Developer notes

1. Pre-requisites
    1. Python3.10
    2. Poetry
    3. Gemfury key to get the `pwr` package. You can get this from a PwR Team member
2. One-time Setup:
    1. Setup Poetry shell
        ```
        $poetry shell
        ```
    2. Add Gemfury key
        ```
        $poetry config http-basic.fury <TOKEN> NOPASS
        ```
    3. Install all the dependencies
        ```
        $poetry install
        $poetry update
        ```
3. Run the PwR agent
    ```
    $poetry run python3 main.py --change <natural language change>
    ```
