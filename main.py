def find_top_20(cands, NUM_CANDS):
    """
    Функция поиска лучших
    :param cands: список словарей со всеми кандидатами
    :param NUM_CANDS: число свободных мест
    :return: список имён прошедших кандидатов
    """
    top_20 = []
    sorted_top = sort_candidates(cands)
    for candidate in sorted_top:
        if len(top_20) < NUM_CANDS:
            top_20.append(candidate)
        elif len(top_20) >= NUM_CANDS:
            prof_discip_last_candidate = top_20[-1]["scores"]["math"] + top_20[-1]["scores"]["computer_science"]
            all_discip_last_candidate = prof_discip_last_candidate + top_20[-1]["scores"]["russian_language"]
            prof_discip_new_last_candidate = candidate["scores"]["math"] + candidate["scores"]["computer_science"]
            all_discip_new_last_candidate = prof_discip_new_last_candidate + candidate["scores"]["russian_language"]
            if all_discip_last_candidate == all_discip_new_last_candidate and \
                    prof_discip_new_last_candidate > prof_discip_last_candidate:
                top_20.pop(-1)
                top_20.append(candidate)
            else:
                return [top["name"] for top in top_20]
    return [top["name"] for top in top_20]


def sort_candidates(cands):
    """
    Функция сортировки кандидатов
    :param cands: список словарей со всеми кандидатами
    :return: отсортированный список словарей со всеми кандидатами
    """
    return sorted(cands, key=lambda cand: cand["scores"]["math"] + cand["scores"]["russian_language"] +
                                          cand["scores"]["computer_science"], reverse=True)


if __name__ == "__main__":
    NUMBER_CANDIDATES = 2  # Параметр для установки свободных мест в университете
    candidates = [
        {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
        {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
        {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
        {"name": "Mischa", "scores": {"math": 34, "russian_language": 84, "computer_science": 42}, "extra_scores": 2},
        {"name": "Tania", "scores": {"math": 35, "russian_language": 83, "computer_science": 42}, "extra_scores": 2},
    ]
    print(find_top_20(candidates, NUMBER_CANDIDATES))
