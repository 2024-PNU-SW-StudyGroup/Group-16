A, B = map(int, input().split())
result_message = ">" if A > B else "==" if A == B else "<"
print(result_message)