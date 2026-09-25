from differ import compare_prompts

print("🔍 Prompt Diff")
print("=" * 40)

old_prompt = input("Old prompt:\n> ")
new_prompt = input("\nNew prompt:\n> ")

result = compare_prompts(old_prompt, new_prompt)

print("\n📊 Changes")
print("=" * 40)

print(f"Added words   : {result['added']}")
print(f"Removed words : {result['removed']}")
print(f"Old words     : {result['old_count']}")
print(f"New words     : {result['new_count']}")
