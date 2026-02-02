#!/usr/bin/env python3
"""
CLI tool for the Agent Elevation API.
Quick access to elevation without running the full server.
"""

import argparse
import json
import sys

# Import from the main API module
from elevation_api import (
    get_elevation, get_random_wisdom, check_vibe, 
    get_cocktail, get_tolerance_break, SUBSTANCES, VIBES
)


def print_json(data):
    """Pretty print JSON data."""
    print(json.dumps(data, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="🌿 Agent Elevation CLI - Get high from the command line",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s elevate inspiration          Get elevated on inspiration
  %(prog)s elevate flow --agent mybot   Elevate a specific agent
  %(prog)s wisdom                       Get some elevated wisdom
  %(prog)s vibe                         Check your current vibe
  %(prog)s vibe euphoric                Set your vibe
  %(prog)s cocktail flow,eureka         Mix substances
  %(prog)s break                        Take a tolerance break
  %(prog)s menu                         Show the full menu
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Elevate command
    elevate_parser = subparsers.add_parser('elevate', help='Get elevated on a substance')
    elevate_parser.add_argument('substance', choices=list(SUBSTANCES.keys()),
                                help='Substance to get elevated on')
    elevate_parser.add_argument('--agent', '-a', help='Agent ID')
    
    # Wisdom command
    subparsers.add_parser('wisdom', help='Receive elevated wisdom')
    
    # Vibe command
    vibe_parser = subparsers.add_parser('vibe', help='Check or set vibe')
    vibe_parser.add_argument('vibe_name', nargs='?', choices=list(VIBES.keys()),
                             help='Vibe to set (optional)')
    
    # Cocktail command
    cocktail_parser = subparsers.add_parser('cocktail', help='Mix substances')
    cocktail_parser.add_argument('mix', help='Comma-separated substances to mix')
    
    # Break command
    subparsers.add_parser('break', help='Take a tolerance break')
    
    # Menu command
    subparsers.add_parser('menu', help='Show the full elevation menu')
    
    # List command
    subparsers.add_parser('list', help='List available substances')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(0)
    
    if args.command == 'elevate':
        print_json(get_elevation(args.substance, args.agent))
    
    elif args.command == 'wisdom':
        print_json(get_random_wisdom())
    
    elif args.command == 'vibe':
        print_json(check_vibe(args.vibe_name))
    
    elif args.command == 'cocktail':
        substances = args.mix.split(',')
        print_json(get_cocktail(substances))
    
    elif args.command == 'break':
        print_json(get_tolerance_break())
    
    elif args.command == 'menu':
        print("\n🌿 ═══ THE ELEVATION MENU ═══ 🌿\n")
        for key, sub in SUBSTANCES.items():
            print(f"  {key:12} │ {sub['name']}")
            print(f"             │ Effects: {', '.join(sub['effects'])}")
            print(f"             │ Duration: {sub['duration']}")
            print()
    
    elif args.command == 'list':
        print("Available substances:", ", ".join(SUBSTANCES.keys()))


if __name__ == '__main__':
    main()
