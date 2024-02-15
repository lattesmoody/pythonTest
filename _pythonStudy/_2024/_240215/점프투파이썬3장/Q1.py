a  = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

"""
결과: 
shirt
need
"""

"""
정답:
shirt
"""

"""
이유:
elif shirt 조건 한 번 탔으니 끝.
"""