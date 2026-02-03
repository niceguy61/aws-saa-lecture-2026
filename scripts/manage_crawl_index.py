"""Manage crawl index"""
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import argparse
from src.crawl_index import CrawlIndex
from src.config import COLLECTIONS


def main():
    parser = argparse.ArgumentParser(description='Manage crawl index')
    parser.add_argument(
        'action',
        choices=['stats', 'list', 'clear', 'export', 'remove'],
        help='Action to perform'
    )
    parser.add_argument(
        '--collection',
        type=str,
        help='Collection name (e.g., docker_collection)'
    )
    parser.add_argument(
        '--url',
        type=str,
        help='URL to remove'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Output file for export'
    )
    args = parser.parse_args()
    
    index = CrawlIndex()
    
    if args.action == 'stats':
        print("\n" + "="*60)
        print("Crawl Index Statistics")
        print("="*60)
        
        if args.collection:
            stats = index.get_stats(args.collection)
            print(f"\nCollection: {stats['collection']}")
            print(f"Total URLs: {stats['total_urls']}")
            print(f"Total Chunks: {stats['total_chunks']}")
        else:
            stats = index.get_stats()
            print(f"\nTotal URLs: {stats['total_urls']}")
            print("\nBy collection:")
            for coll_name, coll_stats in stats.get('collections', {}).items():
                print(f"\n  {coll_name}:")
                print(f"    URLs: {coll_stats['total_urls']}")
                print(f"    Chunks: {coll_stats['total_chunks']}")
    
    elif args.action == 'list':
        if not args.collection:
            print("✗ --collection required for list action")
            return
        
        urls = index.get_processed_urls(args.collection)
        print(f"\nProcessed URLs for {args.collection}:")
        print("="*60)
        for i, url in enumerate(urls, 1):
            print(f"{i}. {url}")
        print(f"\nTotal: {len(urls)} URLs")
    
    elif args.action == 'clear':
        if not args.collection:
            print("✗ --collection required for clear action")
            return
        
        confirm = input(f"Clear all URLs for {args.collection}? (yes/no): ")
        if confirm.lower() == 'yes':
            index.clear_collection(args.collection)
            print(f"✓ Cleared {args.collection}")
        else:
            print("✗ Cancelled")
    
    elif args.action == 'export':
        if not args.collection or not args.output:
            print("✗ --collection and --output required for export action")
            return
        
        index.export_urls(args.collection, args.output)
    
    elif args.action == 'remove':
        if not args.url:
            print("✗ --url required for remove action")
            return
        
        index.remove_url(args.url, args.collection)
        print(f"✓ Removed {args.url}")


if __name__ == "__main__":
    main()
