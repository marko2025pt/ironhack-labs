import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

categories = ['reasoning', 'knowledge', 'code', 'instruction_following', 'tool_calling']
model_versions = ['gpt-4', 'gpt-4-turbo', 'gpt-3.5-turbo', 'claude-3-opus']

start_date = datetime.now() - timedelta(days=90)
dates = [start_date + timedelta(days=i) for i in range(90)]

data = []
evaluation_id = 1

for date in dates:
    for category in categories:
        num_evaluations = np.random.randint(5, 16)
        for _ in range(num_evaluations):
            model = np.random.choice(model_versions)
            if category == 'reasoning':
                score = np.random.beta(2, 3) * 100
            elif category == 'knowledge':
                score = np.random.beta(4, 2) * 100
            elif category == 'code':
                score = np.random.beta(3, 3) * 100
            elif category == 'instruction_following':
                score = np.random.beta(5, 2) * 100
            else:
                score = np.random.beta(3, 3) * 100
            score = max(0, min(100, score + np.random.normal(0, 5)))
            data.append({
                'evaluation_id': evaluation_id,
                'category': category,
                'score': round(score, 2),
                'model_version': model,
                'date': date.strftime('%Y-%m-%d')
            })
            evaluation_id += 1

df = pd.DataFrame(data)
df.to_csv('evaluation_data.csv', index=False)
print(f"Generated {len(df)} evaluation records")
print(df.groupby('category')['score'].describe())