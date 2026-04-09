# Mentor Matching: алгоритм подбора менторов

Проект реализует baseline-алгоритм рекомендации менторов в условиях отсутствия исторических данных.

## Что делает проект
- генерирует синтетические профили менторов и менти
- считает match score на основе content-based rule-based логики
- проводит эксперимент с неполными профилями
- сохраняет результаты в `data/generated` и `data/experiments`

## Запуск
```bash
python3 main.py
```

## Результаты
После запуска создаются:
- `data/generated/mentors.json`
- `data/generated/mentees.json`
- `data/experiments/example_recommendations.csv`
- `data/experiments/fullness_experiment.csv`
