def convert_mood(list_mood):
    mood_map = {
     "senang" : "😀",
     "biasa" : "😐",
     "sedih" : "😢",
     "semangat" : "💪"
    }

    return list(map(lambda m :mood_map.get(m, "❓"),list_mood))
