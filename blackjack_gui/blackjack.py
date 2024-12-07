import argparse
import logging

from blackjack_gui import cli, gui


def main():
    parser = argparse.ArgumentParser(description="Blackjack")
    parser.add_argument(
        "--stack", type=int, default=1000, help="Stack size. Default is 1000."
    )
    parser.add_argument(
        "--n_games",
        type=int,
        default=10,
        help="Number of rounds to be played. Default is 10.",
    )
    parser.add_argument("--bet", type=int, default=1, help="Bet size. Default is 1.")
    parser.add_argument("--gui", type=str, default="True", help="Open GUI version.")
    parser.add_argument(
        "--ai", type=str, default="False", help="Computer play. Default is False."
    )
    parser.add_argument(
        "--count",
        type=str,
        default="False",
        help="Count cards. Default is False. Can be used with --ai=True.",
    )
    parser.add_argument(
        "--loglevel",
        type=str,
        default="DEBUG",
        help="Log level. Can be DEBUG or INFO. Default is DEBUG.",
    )
    parser.add_argument(
        "--cards",
        type=lambda s: s.split(","),
        default=None,
        help="Determine first player cards. E.g. --cards=A,7 to simulate soft 18.",
    )
    parser.add_argument(
        "--dealer_cards",
        type=lambda s: s.split(","),
        default=None,
        help="Determine first dealer cards. Useful for tests.",
    )
    parser.add_argument(
        "--subset",
        type=str,
        choices=["hard", "soft", "pairs"],
        default=None,
    )

    args = parser.parse_args()
    if args.gui.lower() == "true":
        logging.basicConfig(level="WARNING")
        gui.main(args)
    else:
        args.count = args.count.lower() == "true"
        args.ai = args.ai.lower() == "true"
        logging.basicConfig(level=args.loglevel)
        cli.play(args)


if __name__ == "__main__":
    main()
