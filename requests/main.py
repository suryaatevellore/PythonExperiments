def count_friends(input):
    request = 0

    candidates = []
    for cidx, centaur in enumerate(input):
        for caidx, candidate in enumerate(input):
            if caidx == cidx:
                continue
            candidates.append((centaur, candidate))
    
    for c in candidates:
        centaur_age = c[0]
        candidate_age = c[1]
        if centaur_age > 100 and candidate_age < 100:
            continue
        if candidate_age > centaur_age:
            continue

        if candidate_age <= (centaur_age//2) + 7:
            continue
            
        request += 1

    return request

print(count_friends([120, 45, 230, 400, 88, 300, 101]))