def analyze_task(text):
    text_lower = text.lower()

    priority = "Low"
    category = "General"
    explanation = "Default classification applied."

    if "exam" in text_lower or "test" in text_lower:
        priority = "High"
        category = "Study"
        explanation = "Exam detected. High priority assigned."

    elif "project" in text_lower or "assignment" in text_lower:
        priority = "Medium"
        category = "Study"
        explanation = "Project or assignment detected."

    elif "meeting" in text_lower:
        priority = "Medium"
        category = "Work"
        explanation = "Work meeting detected."

    elif "gym" in text_lower or "workout" in text_lower:
        priority = "Low"
        category = "Personal"
        explanation = "Health-related task detected."

    if "today" in text_lower or "tomorrow" in text_lower:
        priority = "High"
        explanation += " Time-sensitive keyword increased priority."

    task = {
        "text": text,
        "priority": priority,
        "category": category,
        "explanation": explanation
    }

    return task


def generate_suggestions(tasks):
    if not tasks:
        return "No tasks found. You have free time."

    high = len([t for t in tasks if t["priority"] == "High"])
    medium = len([t for t in tasks if t["priority"] == "Medium"])

    if high > 1:
        return "Multiple high-priority tasks detected. Focus on urgent study tasks first."

    if high == 1 and medium >= 2:
        return "Complete the high-priority task, then schedule medium-priority tasks."

    if high == 0 and medium > 0:
        return "Your workload is balanced. Plan medium tasks efficiently."

    return "Your task list looks well organized."


def generate_summary(tasks):
    summary = {
        "total": len(tasks),
        "high": len([t for t in tasks if t["priority"] == "High"]),
        "medium": len([t for t in tasks if t["priority"] == "Medium"]),
        "low": len([t for t in tasks if t["priority"] == "Low"])
    }
    return summary
