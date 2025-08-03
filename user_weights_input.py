def get_weight_preferences():
    print("\nNow rank the following factors based on your travel priority.")
    print("You'll assign a rank 1 (most important), 2, and 3 (least important). Each rank must be used only once.\n")

    ranking_options = ["budget", "group_type", "purpose"]
    weights = {}
    used_ranks = set()

    for factor in ranking_options:
        while True:
            try:
                rank = int(input(f"Rank the importance of {factor.replace('_', ' ').title()} (1 / 2 / 3): ").strip())
                if rank in [1, 2, 3] and rank not in used_ranks:
                    weights[factor] = 4 - rank  # So rank 1 → weight 3, etc.
                    used_ranks.add(rank)
                    break
                else:
                    print("Invalid rank or already used. Please choose 1, 2, or 3 without repeating.")
            except ValueError:
                print("Invalid input. Please enter a number (1/2/3).")

    return weights
