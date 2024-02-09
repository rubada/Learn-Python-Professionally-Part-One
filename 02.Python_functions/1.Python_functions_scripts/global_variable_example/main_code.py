import config

print("x and y before calling the function", config.x, config.y)
config.check_x(True)
print("x and y after calling the function", config.x, config.y)
