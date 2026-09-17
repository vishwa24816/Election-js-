"""E-LECTION 2024 — streamlined CLI: nominate -> vote (1 per voter ID) -> end -> results. Stdlib only."""
from collections import Counter

# ponytail: in-memory demo, no persistence/auth; add sqlite + OTP for real elections
def main():
    print("IN E-LECTION 2024 IN\nNomination -> Voting -> Results")
    candidates, votes, voted = [], Counter(), set()

    print("\n--- Step 1: Nomination (blank line to finish, min 2) ---")
    while True:
        name = input("Nominate: ").strip().upper()
        if not name:
            if len(candidates) >= 2:
                break
            print("Nominate at least 2 candidates first.")
        elif name in candidates:
            print("Already nominated.")
        else:
            candidates.append(name)
            print(f"OK: {name} nominated ({', '.join(candidates)})")

    input("\nNominees: " + ", ".join(candidates) + "\nPress Enter to START VOTING...")
    print("\n--- Step 2: Voting (blank Voter ID ends election) ---")
    while True:
        vid = input("Voter ID: ").strip()
        if not vid:
            break
        if vid in voted:
            print(f"REJECTED: {vid} already voted.")
            continue
        print("Candidates: " + ", ".join(f"{i+1}={c}" for i, c in enumerate(candidates)))
        try:
            pick = candidates[int(input("Pick number: ")) - 1]
        except (ValueError, IndexError):
            print("Invalid pick, vote skipped.")
            continue
        voted.add(vid)
        votes[pick] += 1
        print("Vote recorded. Thank you!")

    total = sum(votes.values())
    print(f"\n--- Election Concluded: {total} votes ---")
    for i, c in enumerate(sorted(candidates, key=lambda c: votes[c], reverse=True), 1):
        v = votes[c]
        print(f"#{i} {c}: {v:,} ({v/total:.1%})" if total else f"#{i} {c}: 0")
    if total:
        print(f"WINNER: {max(candidates, key=lambda c: votes[c])}")

if __name__ == "__main__":
    main()
