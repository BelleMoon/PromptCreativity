# PromptCreativity


### Adjusts Top_P value of LLMs to match grammatical desviation of a text based on previous prompts using absolute desviation to mean.

"Top_p", along with other parameters, are used in LLMs to adjust determinism and randomness of token generation. Lower values increase determism and higher values increase randomness and creativity of a LLM model response.

A notorious subject is that in many LLM uses, Top_p is adjusted per session of conversation, which can be limitating for different scenarios, such a conversation that starts as more formal and tends to informality or vice versa. 

## The concept behind

Therefore, the intention of this project is to adjust the parameter based on grammatical desviations of an user input by it's desviation to the mean of previous desviations and adjusting "top_p" parameter to every input. Also, it's possible to establish a upper and bottom limit to "top_p" variation.

## Implementation

- This solution is a proof of concept python using GPT4All for modeling.

### Prerequisites

Requirements for the software and other tools to build and test

`` pip3 install -R requirements.txt ``

## Authors

  - **Labelle Moon** - Hugo Cardoso (hugo.card@usp.br) -
    [LabelleMoon](https://github.com/BelleMoon)

## License

This project is licensed under the [MIT](LICENSE.md)
MIT License - see the [LICENSE.md](LICENSE.md) file for
details.