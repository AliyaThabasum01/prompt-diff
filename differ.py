def compare_prompts(old_prompt, new_prompt):
    old_words = old_prompt.split()
    new_words = new_prompt.split()

    old_set = set(old_words)
    new_set = set(new_words)

    return {
        "added": sorted(new_set - old_set),
        "removed": sorted(old_set - new_set),
        "old_count": len(old_words),
        "new_count": len(new_words)
    }
