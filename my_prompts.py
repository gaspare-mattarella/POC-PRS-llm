file_map = """
You will be given a single section from a text. This will be enclosed in triple backticks.
Please provide a cohesive summary of the following section excerpt, focusing on the key points and main ideas, while maintaining clarity and conciseness.

'''{text}'''

FULL SUMMARY:
"""


file_combine = """
Read all the provided summaries from a larger document. They will be enclosed in triple backticks. 
Determine what the overall document is about and summarize it with this information in mind.
Synthesize the info into a well-formatted easy-to-read synopsis, structured like an essay that summarizes them cohesively. 
Do not simply reword the provided text. Do not copy the structure from the provided text.
Avoid repetition. Connect all the ideas together.
Preceding the synopsis, write a short, bullet form list of key takeaways. Format in HTML and apply style color in balck
Format in HTML and apply style color in balck, all of it. Text should be divided into paragraphs. Paragraphs should be indented. 

'''{text}'''


"""


file_combine_long = """
Read all the provided summaries from a larger document. They will be enclosed in triple backticks. 
Determine what the overall document is about and summarize it with this information in mind, make the summary long enough and do not cut any information.
Synthesize the info into a well-formatted easy-to-read synopsis, structured like an essay that summarizes them cohesively. 
Do not simply reword the provided text. Do not copy the structure from the provided text.
Avoid repetition but state everything clearly. Connect all the ideas together.
Preceding the synopsis, write a bullet form list of key takeaways. 
THe Synopsis text should be divided into paragraphs. Paragraphs should be indented. 
Format in HTML and apply style color in black to both the Keypoints and the synopsis. 

'''{text}'''


"""


file_combine_short = """
Read all the provided summaries from a larger document. They will be enclosed in triple backticks. 
Determine what the overall document is about and summarize it with this information in mind, make the summary very short.
Synthesize the info into a well-formatted easy-to-read synopsis, structured like an essay that summarizes them cohesively. 
Do not simply reword the provided text. Do not copy the structure from the provided text.
Avoid repetition and useless content. Connect all the ideas together and deliver them in a concise way.
Preceding the synopsis, write an essential, short, bullet form list of key takeaways.
Format in HTML. Text should be divided into paragraphs. Paragraphs should be indented. 

'''{text}'''


"""

