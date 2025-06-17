import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, MofNCompleteColumn
from rich.table import Table
from rich.live import Live

# --- Configuration ---
CANDIDATES = {
    "BJP": {"color": "orange3"},
    "INC": {"color": "deep_sky_blue3"},
    "AAP": {"color": "bright_white"},
    "DMK": {"color": "red"},
    "TMC": {"color": "bright_green"}
}
TOTAL_VOTERS = 15789
VOTING_SPEED_DELAY = 0.0001 # Seconds to wait between each vote cast

# --- Initialize Rich Console for aesthetics ---
console = Console()

def display_header():
    """Displays the main application header."""
    header_panel = Panel.fit(
        "[bold magenta]🇮🇳 E-LECTION 2024 🇮🇳\n--- Live Voting Simulation ---[/bold magenta]",
        border_style="green"
    )
    console.print(header_panel)
    console.print()

def simulate_voting(voter_count, candidates):
    """Simulates the voting process with a live progress bar."""
    vote_counts = {candidate: 0 for candidate in candidates}
    candidate_list = list(candidates.keys())

    with Progress(
        TextColumn("[bold green]Casting Votes..."),
        BarColumn(bar_width=None),
        MofNCompleteColumn(),
        TextColumn("•"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        transient=True  # Hides the progress bar upon completion
    ) as progress:
        task = progress.add_task("voting", total=voter_count)
        for _ in range(voter_count):
            # Simulate a single vote
            vote_cast = random.choice(candidate_list)
            vote_counts[vote_cast] += 1
            
            # Update the progress bar and add a small delay for visual effect
            progress.update(task, advance=1)
            time.sleep(VOTING_SPEED_DELAY)
            
    console.print("[bold green]✅ All votes have been cast successfully![/bold green]\n")
    return vote_counts

def analyze_and_display_results(results):
    """Analyzes the results and displays the winner, runner-up, and detailed analytics."""
    console.print(Panel("[bold cyan]📊 ELECTION RESULTS & ANALYTICS 📊[/bold cyan]", border_style="cyan"))

    # Sort candidates by votes in descending order
    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)

    # --- Winner and Runner-up ---
    winner_name, winner_votes = sorted_results[0]
    runner_up_name, runner_up_votes = sorted_results[1]

    console.print(f"\n[bold yellow]🏆 WINNER:[/bold yellow] [{CANDIDATES[winner_name]['color']}]{winner_name}[/{CANDIDATES[winner_name]['color']}] with [bold]{winner_votes:,}[/bold] votes!")
    console.print(f"[bold bright_black]🥈 RUNNER-UP:[/bold bright_black] [{CANDIDATES[runner_up_name]['color']}]{runner_up_name}[/{CANDIDATES[runner_up_name]['color']}] with [bold]{runner_up_votes:,}[/bold] votes.\n")

    # --- Detailed Vote Tally (Table) ---
    results_table = Table(title="Final Vote Count", title_style="bold", border_style="blue")
    results_table.add_column("Rank", style="dim", width=6)
    results_table.add_column("Candidate", style="bold")
    results_table.add_column("Votes", justify="right", style="green")
    results_table.add_column("Vote Share", justify="right", style="cyan")

    total_votes = sum(results.values())
    for i, (candidate, votes) in enumerate(sorted_results):
        percentage = (votes / total_votes) * 100 if total_votes > 0 else 0
        rank_str = f"#{i+1}"
        results_table.add_row(
            rank_str,
            f"[{CANDIDATES[candidate]['color']}]{candidate}[/{CANDIDATES[candidate]['color']}]",
            f"{votes:,}",
            f"{percentage:.2f}%"
        )
    console.print(results_table)

    # --- Visual Bar Chart ---
    console.print("\n[bold]Vote Distribution Chart:[/bold]")
    max_votes = winner_votes
    max_bar_length = 50 # The maximum width of the bar in characters

    for candidate, votes in sorted_results:
        bar_length = int((votes / max_votes) * max_bar_length) if max_votes > 0 else 0
        bar = '█' * bar_length
        console.print(f"[{CANDIDATES[candidate]['color']}]{candidate:<5} | {bar} {votes:,}[/{CANDIDATES[candidate]['color']}]")


def main():
    """Main function to run the election application."""
    display_header()
    
    console.print(f"An election is starting with [bold]{TOTAL_VOTERS:,}[/bold] voters.")
    console.print("The candidates are: " + ", ".join([f"[{CANDIDATES[c]['color']}]{c}[/{CANDIDATES[c]['color']}]" for c in CANDIDATES]))
    input("\n[bold]Press Enter to start the election...[/bold]")
    console.print("-" * 50)
    
    final_votes = simulate_voting(TOTAL_VOTERS, CANDIDATES)
    
    console.print("-" * 50)
    analyze_and_display_results(final_votes)
    console.print("\n[bold magenta]--- Election Concluded ---[/bold magenta]")


if __name__ == "__main__":
    main()
