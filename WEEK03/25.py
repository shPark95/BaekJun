# 1700 멀티탭 스케줄링

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
uses = list(map(int, input().strip().split()))

plugged_in = []
count = 0

for i in range(K):
    # 이미 꽂혀있으면 넘어감
    if uses[i] in plugged_in:
        continue

    # 멀티탭에 자리가 남아 있으면 그냥 꽂기
    if len(plugged_in) < N:
        plugged_in.append(uses[i])
    else:
        # 나중에 가장 늦게 사용되거나 더 이상 사용되지 않는 기기 뽑기
        last_used = -1
        device_to_remove = -1
        
        for device in plugged_in:
            if device not in uses[i:]:
                device_to_remove = device
                break
            else:
                next_use = uses[i:].index(device)
                if next_use > last_used:
                    last_used = next_use
                    device_to_remove = device
        
        plugged_in.remove(device_to_remove)
        plugged_in.append(uses[i])
        count += 1

print(count)