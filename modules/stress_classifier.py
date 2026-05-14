def classify_stress(face_score, text_score, voice_score):

    total = face_score + text_score + voice_score

    if total <= 1:

        level = "Low Stress"

        solution = [
            "Listen to calming music",
            "Practice meditation",
            "Go for a short walk",
            "Do light yoga"
        ]

    elif total <= 3:

        level = "Medium Stress"

        solution = [
            "Take proper rest",
            "Practice breathing exercises",
            "Reduce workload",
            "Talk with friends or family"
        ]

    else:

        level = "High Stress"

        solution = [
            "Consult a physician",
            "Seek professional counseling",
            "Take mental health break",
            "Avoid stressful activities"
        ]

    return level, solution