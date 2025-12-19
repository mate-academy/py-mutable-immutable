# Mutable and Immutable

## 📘 Task Description

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.
- Implement the task described below.

There are **8 variables** of different data types in the main module.

Your task is to create a dictionary named `sorted_variables` with **two keys**:  
`"mutable"` and `"immutable"`.

Each value should be equal to a **list** that contains all variables of the corresponding type.

---

### 🧩 Example

```python
a = 123
b = []
c = "Hi!"
d = [1, 2]

sorted_variables = {
    "mutable": [b, d],
    "immutable": [a, c]
}
