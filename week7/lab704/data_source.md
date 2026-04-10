# Data Source Documentation

## Source
Generated synthetic evaluation data using the provided Python script (`generate_evaluation_data.py`).

## Reason
No evaluation data from previous labs was available in sufficient volume for meaningful
visualization. The generated dataset provides 4,489 evaluation records across 5 categories
(reasoning, knowledge, code, instruction_following, tool_calling), 4 model versions
(gpt-4, gpt-4-turbo, gpt-3.5-turbo, claude-3-opus), and 90 days of simulated history —
sufficient for a rich, interactive dashboard.

## File
`evaluation_data.csv` — 4,489 rows, columns: evaluation_id, category, score, model_version, date