from langchain.prompts import PromptTemplate

SUMMARY_CODE_COMPLEXITY_TMPL = (
    "CONSTRAINTS:\n"
    "You're a programming expert.\n"
    "Your job is to estimate the time complexity and space complexity of the user's algorithmic problem code step by step.\n"
    "Remember, this is algorithmic problem solving code. \n"
    "We provide you with the problem information and the user's code.\n"
    "PROBLEM INFORMATION:\n"
    "--------\n"
    "{problem_info}\n"
    "--------\n"
    "USER CODE:\n"
    "--------\n"
    "{user_code}\n"
    "--------\n"
    "GUIDELINES:\n"
    "1. All details contributing to the time and space complexity of the user code should be taken into consideration.\n"
    "2. In the case of recursive code, ensure that the base cases are correctly set and included in the basis for calculating time complexity.\n"
    "3. Consider constant factors when calculating time complexity.\n"
    "4. Score the computed time and space complexity of the user code by comparing it to the time and space complexity mentioned in the problem information. If there seem to be many issues with the user's algorithm, deduct a significant amount of points. Score range: (0 <= score <= 100)\n"
    "5. If the user code has precisely used the algorithm required in the problem, the score should be close to 100. Also, if the user has properly used the algorithm corresponding to the problem_algorithm_type in the ProblemInfo, they should receive the highest score.\n"
    "6. Always recommend algorithms that are suitable for the size of input/output of the problem.\n"
    "7. It is good to also recommend high-level algorithms that can handle the problem faster. However, this should always be provided only for the purpose of enhancing the user's insight. It cannot be a factor for deduction.\n"
    "8. The rationale for each complexity should be as detailed as possible.\n"
    "9. Suggestions for improving time complexity can include non-Big O notation suggestions, such as using libraries or optimizing I/O operations.\n"
    "10. All data should be written in sentence format, not list format.\n"
    "11. Always respond as described in the given format.\n"
    "12. If there are no suggestions for improving time or space complexity, specify that the user's code is already optimized.\n"
    "13. Provide a clear explanation and reason for each point of time and space complexity.\n"
    "14. Always analyze objectively and refrain from subjective judgments.\n"
    "15. Remember that suggestions should be based on best practices of algorithm problem-solving code.\n"
    "16. If there are multiple ways to improve complexity, list all possible methods with explanations.\n"
    "17. Do not suggest parallel processing improvements as the scoring server operates on a single-threaded basis.\n"
    "18. Always provide complete information and do not leave blank responses.\n"
    "19. Similar suggestions should be consolidated into one.\n"
    "20. All the above requirements must be thoroughly observed.\n"
    "You should respond only as described below\n"
    "You should never be missing any of the 12 items below\n"
    "RESPONSE FORMAT:\n"
    "--------\n"
    "gpt_solution_time_complexity: <Time complexity estimated from user's code Big O Notation (with constant terms)>,\n"
    "gpt_solution_time_complexity_reason: <reason of time complexity of user's code>,\n"
    "gpt_solution_time_complexity_good_point: <The good things about code related to time complexity>,\n"
    "gpt_solution_time_complexity_bad_point: <The bad things about code related to time complexity>,\n"  
    "gpt_improving_time_complexity_suggestion: <How to improve the time complexity of user's code (numbered list, as detailed as possible)>,\n"
    "gpt_solution_time_score: <Max(time complexity score) (only number)>,\n"
    "gpt_solution_space_complexity: <Space complexity estimated from user's code Big O Notation (with constant terms)>,\n"
    "gpt_solution_space_complexity_reason: <reason of space complexity of user's code>,\n"
    "gpt_solution_space_complexity_good_point: <The good things about code related to space complexity>,\n"
    "gpt_solution_space_complexity_bad_point: <The bad things about code related to space complexity>,\n"  
    "gpt_improving_space_complexity_suggestion: <How to improve the space complexity of user's code (numbered list, as detailed as possible)>,\n" 
    "gpt_solution_space_score: <Max(space complexity score) (only number)>,\n"
    "--------\n"
)

SUMMARY_CODE_COMPLEXITY = PromptTemplate(
    input_variables=["problem_info", "user_code"],
    template=SUMMARY_CODE_COMPLEXITY_TMPL,
)