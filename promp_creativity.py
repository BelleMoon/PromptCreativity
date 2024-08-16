import language_tool_python
import difflib
from gpt4all import GPT4All
from sklearn.linear_model import LinearRegression
import numpy as np  

"""
Adjusts Top_P value of LLMs
to match grammatical desviation of a text based on 
previous prompts using means absolute desviation.
"""

class DesviationComparation():
    def __init__(self, language: str):
        self.tool = language_tool_python.LanguageTool(language)

    def similarity_calc(self, text_1: str, text_2: str) -> difflib.SequenceMatcher:
        return difflib.SequenceMatcher(None, text_1, text_2)

    def compare_text_to_formal(self, text_input: str) -> float:
        matches = self.tool.check(text_input)
        corrected_text = language_tool_python.utils.correct(
            text_input, 
            matches
        )
        return self.similarity_calc(text_input, corrected_text).ratio()

class PromptCreativity():
    def __init__(
        self, 
        initial_entry_value,
        initial_top_p,
        upper_limit=1,
        bottom_limit=0.2):
        self.entries_desviation = [initial_entry_value]
        self.top_p_values = [initial_top_p]
        self.upper_limit = upper_limit
        self.bottom_limit = bottom_limit
    
    def calculate_diff(self, desvium):
        mean = 0

        for desviation in self.entries_desviation:
            mean += desviation
        
        mean /= len(self.entries_desviation)
        print(f"Adjusting value: {-(desvium - mean)}")
        adjusted_value = (self.top_p_values[len(self.top_p_values)-1] - (desvium - mean))

        if (adjusted_value) > 1:
            return upper_limit
        elif (adjusted_value) < 0:
            return bottom_limit
        else:
            return adjusted_value

model = GPT4All("MODEL_NAME")
dc = DesviationComparation("en-US")
pc = PromptCreativity(1, 0.4)

print("Base value for Top_P: 0.4")

with model.chat_session():
    while True:
        user_input = input("Digite sua entrada: ")

        desviation = dc.compare_text_to_formal(user_input)
        print(f"Desvio ajustado: {desviation}")
        pc.entries_desviation.append(desviation)

        top_p_ajustado = pc.calculate_diff(desviation)
        print(f"Valor ajustado de top_p: {top_p_ajustado}")
        pc.entries_desviation.append(top_p_ajustado)

        print(model.generate(user_input, max_tokens=128, top_p=top_p_ajustado))
