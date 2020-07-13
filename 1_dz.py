from sys import argv

script_name, bid_hour, hours, reward = argv

print((int(bid_hour) * int(hours)) + int(reward))